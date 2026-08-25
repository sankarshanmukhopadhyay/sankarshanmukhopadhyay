#!/usr/bin/env python3
"""Portfolio assurance monitor v3: evidence-contract evaluation over v2 collection."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import portfolio_assurance_monitor as legacy
from portfolio_assurance.assurance import evaluate_portfolio_assurance, render_assurance_section

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS_PATH = ROOT / "config/portfolio-monitor/assurance-contracts.yaml"
ASSURANCE_STATE_PATH = ROOT / "reports/portfolio-assurance/assurance-state.json"


def bind_assurance_findings(
    repos: list[dict[str, Any]],
    findings: list[dict[str, Any]],
    policy: dict[str, Any],
) -> list[dict[str, Any]]:
    by_repo = {str(repo["name"]): repo for repo in repos}
    result: list[dict[str, Any]] = []
    for finding in findings:
        repo = by_repo.get(str(finding.get("repository")))
        if repo is not None:
            finding["routing"] = legacy.routing_decision(repo, finding, policy)
        finding = legacy.enrich_finding(finding, policy)
        result.append(finding)
    return result


def bind_current_workflow_inventory(
    owner: str,
    repo: dict[str, Any],
    observation: dict[str, Any],
    policy: dict[str, Any],
    token: str | None,
) -> None:
    """Reconcile recent workflow evidence with workflows present at current HEAD.

    A removed workflow can retain recent GitHub Actions runs inside the governed
    lookback window. Those runs remain useful historical evidence, but they no
    longer represent an active control and therefore must not create an open
    operational failure or satisfy a current assurance claim.

    Inventory collection fails closed: if the active workflow set cannot be
    observed, the pre-existing conservative workflow evaluation is preserved.
    """
    if not observation.get("available"):
        return
    workflow_state = observation.get("evidence", {}).get("workflow_runs")
    if not isinstance(workflow_state, dict) or workflow_state.get("available") is False:
        return

    timeout = int(policy["collection"]["request_timeout_seconds"])
    name = str(repo["name"])
    try:
        inventory = legacy.request_json(
            f"https://api.github.com/repos/{owner}/{name}/actions/workflows?per_page=100",
            token,
            timeout,
        )
    except Exception as error:
        workflow_state["active_inventory_available"] = False
        workflow_state["active_inventory_error"] = str(error)
        return

    workflows = inventory.get("workflows", []) if isinstance(inventory, dict) else []
    active_paths = {
        str(item.get("path"))
        for item in workflows
        if isinstance(item, dict) and item.get("path") and item.get("state") != "deleted"
    }
    workflow_state["active_inventory_available"] = True
    workflow_state["active_workflow_paths"] = sorted(active_paths)

    latest = list(workflow_state.get("latest", []))
    retired = list(workflow_state.get("retired", []))
    active_latest: list[dict[str, Any]] = []
    for record in latest:
        path = record.get("path") if isinstance(record, dict) else None
        if path and str(path) not in active_paths:
            retired.append(record)
        else:
            active_latest.append(record)

    active_unresolved = [
        record
        for record in workflow_state.get("unresolved", [])
        if not record.get("path") or str(record.get("path")) in active_paths
    ]
    workflow_state["latest"] = active_latest
    workflow_state["retired"] = retired
    workflow_state["workflows_examined"] = len(active_latest)
    workflow_state["retired_workflows_examined"] = len(retired)
    workflow_state["unresolved"] = active_unresolved
    workflow_state["unresolved_failures"] = len(active_unresolved)


def inject_assurance_section(report: str, section: str) -> str:
    marker = "## Governance boundary"
    if marker in report:
        return report.replace(marker, f"{section}\n\n{marker}", 1)
    return f"{report}\n\n{section}\n"


def write_assurance_state(states: dict[str, dict[str, Any]], generated_at: str) -> None:
    ASSURANCE_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": "1.0",
        "generated_at": generated_at,
        "authority": "evidence-coverage-observation",
        "states": states,
    }
    ASSURANCE_STATE_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Validate generation without GitHub network calls")
    parser.add_argument("--check", action="store_true", help="Evaluate and print summary without writing files")
    parser.add_argument("--publish-issues", action="store_true", help="Publish eligible findings when issue routing and credentials are enabled")
    args = parser.parse_args()

    status = legacy.load_yaml(legacy.STATUS_PATH)
    policy = legacy.load_yaml(legacy.POLICY_PATH)
    contracts = legacy.load_yaml(CONTRACTS_PATH)
    repos = legacy.selected_repositories(status, policy)
    if not repos:
        raise SystemExit("No repositories selected by portfolio monitor policy")

    configured = set(contracts.get("repositories", {}))
    selected = {str(repo["name"]) for repo in repos}
    missing_contracts = sorted(selected - configured)
    if missing_contracts:
        raise SystemExit(f"Missing assurance contracts for monitored repositories: {', '.join(missing_contracts)}")

    now = legacy.utc_now()
    token = os.getenv("GITHUB_TOKEN")
    observations = [
        legacy.offline_observation(repo, now)
        if args.offline
        else legacy.collect_repository(policy["owner"], repo, policy, token, now)
        for repo in repos
    ]

    if not args.offline:
        for repo, observation in zip(repos, observations):
            bind_current_workflow_inventory(policy["owner"], repo, observation, policy, token)

    findings = [
        finding
        for repo, observation in zip(repos, observations)
        for finding in legacy.evaluate(repo, observation, policy, now)
    ]

    assurance_states, assurance_findings = evaluate_portfolio_assurance(repos, observations, contracts)
    findings.extend(bind_assurance_findings(repos, assurance_findings, policy))

    if not args.offline and policy.get("discovery", {}).get("enabled", False):
        try:
            public_repos = legacy.discover_public_repositories(
                policy["owner"], legacy.request_json, token, int(policy["collection"]["request_timeout_seconds"])
            )
            findings.extend([
                legacy.enrich_finding(f, policy)
                for f in legacy.discovery_findings(
                    status, public_repos, legacy.iso(now), str(policy["discovery"].get("severity", "info"))
                )
            ])
            if policy.get("rules", {}).get("registered_repository_not_publicly_discovered", {}).get("enabled", True):
                churn_rule = policy["rules"]["registered_repository_not_publicly_discovered"]
                findings.extend([
                    legacy.enrich_finding(f, policy)
                    for f in legacy.registered_repository_churn_findings(
                        status, public_repos, legacy.iso(now), str(churn_rule.get("severity", "medium"))
                    )
                ])
        except Exception as error:
            findings.append(legacy.enrich_finding(legacy._make_finding(
                policy["owner"],
                "ACCOUNT_DISCOVERY_UNAVAILABLE",
                "low",
                legacy.iso(now),
                "Public account discovery could not be completed.",
                {"error": str(error)},
                "Review GitHub API availability and monitor permissions; do not infer portfolio completeness from this run.",
                subject="public-account-discovery",
            ), policy))

    publication_records: list[dict[str, Any]] = []
    issue_cfg = policy.get("issue_routing", {})
    issue_token = os.getenv("PORTFOLIO_ISSUE_TOKEN")
    if args.publish_issues and issue_cfg.get("enabled", False):
        if not issue_token:
            publication_records.append({"action": "skipped", "reason": "PORTFOLIO_ISSUE_TOKEN not configured"})
        else:
            report_url = f"https://{policy['owner']}.github.io/{policy['owner']}/docs/portfolio-assurance/dashboard.html"
            publication_records = legacy.publish_findings(policy["owner"], findings, issue_token, policy, report_url)

    assurance_section = render_assurance_section(repos, assurance_states)
    dashboard_report = inject_assurance_section(
        legacy.render_report(repos, observations, findings, now, publication_role="dashboard"), assurance_section
    )
    evidence_report = inject_assurance_section(
        legacy.render_report(repos, observations, findings, now, publication_role="evidence"), assurance_section
    )

    if not args.check:
        legacy.write_outputs(
            dashboard_report,
            evidence_report,
            findings,
            observations,
            policy,
            now,
            publication_records,
        )
        write_assurance_state(assurance_states, legacy.iso(now))

    counts: dict[str, int] = {}
    for state in assurance_states.values():
        key = str(state.get("state", "not-evaluated"))
        counts[key] = counts.get(key, 0) + 1
    summary = ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    print(
        f"Portfolio assurance monitor v3: {len(repos)} repositories, {len(findings)} findings, "
        f"assurance[{summary}], {len(publication_records)} issue actions, "
        f"mode={'offline' if args.offline else 'live'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
