from __future__ import annotations
import datetime as dt
import hashlib
from typing import Any

FAILURE_CONCLUSIONS = {"failure", "timed_out", "cancelled", "action_required", "startup_failure"}
SEVERITY_RANK = {"info": 0, "low": 1, "medium": 2, "high": 3, "critical": 4}


def iso(value: dt.datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def parse_github_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def finding_fingerprint(repository: str, rule_id: str, subject: str = "repository") -> str:
    digest = hashlib.sha256(f"{repository}|{rule_id}|{subject}".encode()).hexdigest()[:12].upper()
    return f"PF-{digest}"


def make_finding(repository: str, rule_id: str, severity: str, observed_at: str, claim: str,
                 evidence: dict[str, Any], action: str, *, subject: str = "repository",
                 routing: dict[str, Any] | None = None) -> dict[str, Any]:
    fingerprint = finding_fingerprint(repository, rule_id, subject)
    observation_digest = hashlib.sha256(f"{fingerprint}|{observed_at[:10]}".encode()).hexdigest()[:12].upper()
    return {
        "finding_id": f"PAM-{observation_digest}",
        "finding_fingerprint": fingerprint,
        "repository": repository,
        "rule_id": rule_id,
        "subject": subject,
        "severity": severity,
        "observed_at": observed_at,
        "claim": claim,
        "evidence": evidence,
        "recommended_action": action,
        "dimension": "unclassified",
        "remediation": {
            "objective": action,
            "acceptance_criteria": [],
            "verification": [],
        },
        "automatic_effect": "none",
        "routing": routing or {"eligible": False, "target": "central-review"},
    }


def latest_workflow_states(workflow_runs: list[dict[str, Any]], now: dt.datetime, lookback_days: int) -> dict[str, Any]:
    """Return latest completed state per workflow inside the governed lookback window."""
    cutoff = now - dt.timedelta(days=lookback_days)
    in_window: list[dict[str, Any]] = []
    for run in workflow_runs:
        if run.get("status") != "completed":
            continue
        created = parse_github_time(run.get("run_started_at") or run.get("created_at"))
        if created is None or created < cutoff:
            continue
        in_window.append(run)
    in_window.sort(key=lambda r: parse_github_time(r.get("run_started_at") or r.get("created_at")) or cutoff, reverse=True)
    latest: dict[str, dict[str, Any]] = {}
    for run in in_window:
        key = str(run.get("workflow_id") or run.get("path") or run.get("name") or "unknown-workflow")
        if key not in latest:
            latest[key] = run
    unresolved = [r for r in latest.values() if r.get("conclusion") in FAILURE_CONCLUSIONS]
    unresolved.sort(key=lambda r: str(r.get("name") or r.get("path") or r.get("workflow_id")))
    return {
        "lookback_days": lookback_days,
        "completed_examined": len(in_window),
        "workflows_examined": len(latest),
        "unresolved_failures": len(unresolved),
        "unresolved": [
            {
                "workflow_id": r.get("workflow_id"),
                "name": r.get("name"),
                "path": r.get("path"),
                "conclusion": r.get("conclusion"),
                "created_at": r.get("created_at"),
                "updated_at": r.get("updated_at"),
                "html_url": r.get("html_url"),
                "head_sha": r.get("head_sha"),
            }
            for r in unresolved
        ],
    }
