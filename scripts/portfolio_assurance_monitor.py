#!/usr/bin/env python3
"""Collect portfolio evidence, evaluate deterministic rules, and publish assurance reports."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, sys, urllib.error, urllib.request
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "data/repository-status.yaml"
POLICY_PATH = ROOT / "config/portfolio-monitor/policy.yaml"
REL_PATH = ROOT / "data/portfolio-relationships.yaml"
USER_AGENT = "portfolio-assurance-monitor/1.0"


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso(value: dt.datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def selected_repositories(status: dict[str, Any], policy: dict[str, Any]) -> list[dict[str, Any]]:
    scope = policy["scope"]
    excluded = set(scope.get("exclude_repositories", []))
    selected = []
    for repo in status.get("repositories", []):
        if repo.get("name") in excluded:
            continue
        if repo.get("portfolio_disposition") not in set(scope["portfolio_dispositions"]):
            continue
        if repo.get("tier") not in set(scope["tiers"]):
            continue
        if repo.get("provenance") not in set(scope["provenance"]):
            continue
        selected.append(repo)
    return selected


def request_json(url: str, token: str | None, timeout: int) -> Any:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT, "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url: str, token: str | None, timeout: int) -> str:
    headers = {"Accept": "application/vnd.github.raw+json", "User-Agent": USER_AGENT, "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8")


def collect_repository(owner: str, repo: dict[str, Any], policy: dict[str, Any], token: str | None, now: dt.datetime) -> dict[str, Any]:
    name = repo["name"]
    timeout = int(policy["collection"]["request_timeout_seconds"])
    observation: dict[str, Any] = {"repository": name, "observed_at": iso(now), "available": False, "evidence": {}, "collection_error": None}
    try:
        metadata = request_json(f"https://api.github.com/repos/{owner}/{name}", token, timeout)
        observation["available"] = True
        observation["evidence"]["repository"] = {
            "html_url": metadata.get("html_url"), "default_branch": metadata.get("default_branch"),
            "archived": metadata.get("archived"), "pushed_at": metadata.get("pushed_at"),
            "updated_at": metadata.get("updated_at"), "open_issues_count": metadata.get("open_issues_count")
        }
        branch = metadata.get("default_branch", "main")
        status_source = repo.get("status_source", {})
        if status_source.get("type") == "member-declaration":
            path = status_source.get("path", "PROJECT-STATUS.yaml")
            try:
                raw = request_text(f"https://api.github.com/repos/{owner}/{name}/contents/{path}?ref={branch}", token, timeout)
                parsed = yaml.safe_load(raw)
                observation["evidence"]["status_declaration"] = {"path": path, "present": True, "readable": isinstance(parsed, dict)}
            except urllib.error.HTTPError as error:
                observation["evidence"]["status_declaration"] = {"path": path, "present": error.code != 404, "readable": False, "http_status": error.code}
            except Exception as error:
                observation["evidence"]["status_declaration"] = {"path": path, "present": True, "readable": False, "error": str(error)}
        try:
            runs = request_json(f"https://api.github.com/repos/{owner}/{name}/actions/runs?branch={branch}&per_page={int(policy['collection']['workflow_runs_per_repository'])}", token, timeout)
            workflow_runs = runs.get("workflow_runs", []) if isinstance(runs, dict) else []
            completed = [r for r in workflow_runs if r.get("status") == "completed"]
            failed = [r for r in completed if r.get("conclusion") in {"failure", "timed_out", "cancelled", "action_required", "startup_failure"}]
            observation["evidence"]["workflow_runs"] = {"completed_examined": len(completed), "failed": len(failed), "latest_failed_url": failed[0].get("html_url") if failed else None}
        except Exception as error:
            observation["evidence"]["workflow_runs"] = {"available": False, "error": str(error)}
    except Exception as error:
        observation["collection_error"] = str(error)
    return observation


def make_finding(repository: str, rule_id: str, severity: str, observed_at: str, claim: str, evidence: dict[str, Any], action: str) -> dict[str, Any]:
    digest = hashlib.sha256(f"{repository}|{rule_id}|{observed_at[:10]}".encode()).hexdigest()[:12].upper()
    return {"finding_id": f"PAM-{digest}", "repository": repository, "rule_id": rule_id, "severity": severity, "observed_at": observed_at, "claim": claim, "evidence": evidence, "recommended_action": action, "automatic_effect": "none"}


def evaluate(repo: dict[str, Any], observation: dict[str, Any], policy: dict[str, Any], now: dt.datetime) -> list[dict[str, Any]]:
    findings = []
    rules = policy["rules"]
    name, observed_at = repo["name"], observation["observed_at"]
    if not observation["available"] and rules["repository_unavailable"]["enabled"]:
        findings.append(make_finding(name, "REPOSITORY_UNAVAILABLE", rules["repository_unavailable"]["severity"], observed_at, "A monitored flagship repository must remain publicly observable.", {"collection_error": observation.get("collection_error")}, "Verify repository availability, visibility, rename state, and monitor permissions."))
        return findings
    try:
        next_review = dt.date.fromisoformat(str(repo["next_review"]))
        if next_review < now.date() and rules["review_overdue"]["enabled"]:
            findings.append(make_finding(name, "REVIEW_OVERDUE", rules["review_overdue"]["severity"], observed_at, "The portfolio review date must not be expired.", {"next_review": str(next_review)}, "Conduct and record a portfolio status review."))
    except Exception:
        pass
    declaration = observation["evidence"].get("status_declaration")
    if repo.get("status_source", {}).get("required") and declaration:
        if not declaration.get("present") and rules["status_declaration_missing"]["enabled"]:
            findings.append(make_finding(name, "STATUS_DECLARATION_MISSING", rules["status_declaration_missing"]["severity"], observed_at, "A required repository-local status declaration must exist.", declaration, "Add the required status declaration or revise the governed status-source contract."))
        elif not declaration.get("readable") and rules["status_declaration_unreadable"]["enabled"]:
            findings.append(make_finding(name, "STATUS_DECLARATION_UNREADABLE", rules["status_declaration_unreadable"]["severity"], observed_at, "A required repository-local status declaration must be readable YAML.", declaration, "Correct the declaration syntax and validate it against the portfolio schema."))
    workflows = observation["evidence"].get("workflow_runs", {})
    if workflows.get("failed", 0) > 0 and rules["default_branch_workflow_failure"]["enabled"]:
        findings.append(make_finding(name, "DEFAULT_BRANCH_WORKFLOW_FAILURE", rules["default_branch_workflow_failure"]["severity"], observed_at, "Recent completed default-branch workflows should not contain unresolved failures.", workflows, "Review the failed workflow and record remediation or accepted risk."))
    pushed_at = observation["evidence"].get("repository", {}).get("pushed_at")
    if pushed_at and rules["no_recent_activity"]["enabled"]:
        pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        threshold = int(rules["no_recent_activity"]["threshold_days"])
        if (now - pushed).days > threshold and repo.get("lifecycle") == "active":
            findings.append(make_finding(name, "NO_RECENT_ACTIVITY", rules["no_recent_activity"]["severity"], observed_at, "An active flagship repository has exceeded the configured activity-review threshold.", {"pushed_at": pushed_at, "threshold_days": threshold}, "Review whether the declared lifecycle and operational status remain accurate. Activity alone does not determine health."))
    return findings


def render_report(repos: list[dict[str, Any]], observations: list[dict[str, Any]], findings: list[dict[str, Any]], now: dt.datetime) -> str:
    by_repo = {o["repository"]: o for o in observations}
    f_by_repo: dict[str, list[dict[str, Any]]] = {}
    for finding in findings: f_by_repo.setdefault(finding["repository"], []).append(finding)
    lines = ["---", "layout: default", "title: Portfolio Assurance Dashboard", "nav_order: 6", "---", "", "# Portfolio Assurance Dashboard", "", f"**Observed:** {iso(now)}  ", f"**Scope:** {len(repos)} flagship original repositories  ", f"**Open findings:** {len(findings)}", "", "> This is first-party, evidence-based portfolio monitoring. Findings do not automatically modify portfolio status, maturity, lifecycle, authority, or disposition.", "", "## Current observations", "", "| Repository | Availability | Status declaration | Workflow evidence | Findings |", "|---|---:|---:|---:|---:|"]
    for repo in repos:
        obs = by_repo[repo["name"]]; ev = obs.get("evidence", {}); declaration = ev.get("status_declaration")
        decl = "n/a" if declaration is None else ("valid" if declaration.get("readable") else "attention")
        workflows = ev.get("workflow_runs", {}); wf = "unavailable" if workflows.get("available") is False else f"{workflows.get('failed', 0)} failed"
        lines.append(f"| [{repo['name']}](https://github.com/sankarshanmukhopadhyay/{repo['name']}) | {'available' if obs['available'] else 'unavailable'} | {decl} | {wf} | {len(f_by_repo.get(repo['name'], []))} |")
    lines += ["", "## Findings", ""]
    if not findings: lines.append("No findings were produced by the enabled rules.")
    for finding in sorted(findings, key=lambda x: (x["severity"], x["repository"], x["rule_id"])):
        lines += [f"### {finding['finding_id']}: {finding['repository']}", "", f"- **Rule:** `{finding['rule_id']}`", f"- **Severity:** `{finding['severity']}`", f"- **Claim:** {finding['claim']}", f"- **Recommended action:** {finding['recommended_action']}", f"- **Automatic effect:** `{finding['automatic_effect']}`", ""]
    lines += ["## Governance boundary", "", "The monitor observes public evidence and evaluates configured rules. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.", ""]
    return "\n".join(lines)


def write_outputs(report: str, findings: list[dict[str, Any]], observations: list[dict[str, Any]], policy: dict[str, Any], now: dt.datetime) -> None:
    publication = policy["publication"]
    latest = ROOT / publication["latest_report"]
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(report, encoding="utf-8")
    (ROOT / publication["documentation_page"]).write_text(report, encoding="utf-8")
    (ROOT / publication["latest_findings"]).write_text(json.dumps({"generated_at": iso(now), "findings": findings, "observations": observations}, indent=2) + "\n", encoding="utf-8")
    history = ROOT / publication["history_directory"]
    history.mkdir(parents=True, exist_ok=True)
    (history / f"{now.date().isoformat()}.md").write_text(report, encoding="utf-8")


def offline_observation(repo: dict[str, Any], now: dt.datetime) -> dict[str, Any]:
    declaration = repo.get("status_source", {})
    evidence: dict[str, Any] = {"repository": {"pushed_at": iso(now), "default_branch": "main"}, "workflow_runs": {"completed_examined": 0, "failed": 0}}
    if declaration.get("type") == "member-declaration": evidence["status_declaration"] = {"path": declaration.get("path"), "present": True, "readable": True, "mode": "offline-validation"}
    return {"repository": repo["name"], "observed_at": iso(now), "available": True, "evidence": evidence, "collection_error": None}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Validate generation without GitHub network calls")
    parser.add_argument("--check", action="store_true", help="Evaluate and print summary without writing files")
    args = parser.parse_args()
    status, policy = load_yaml(STATUS_PATH), load_yaml(POLICY_PATH)
    repos = selected_repositories(status, policy)
    if not repos: raise SystemExit("No repositories selected by portfolio monitor policy")
    now = utc_now(); token = os.getenv("GITHUB_TOKEN")
    observations = [offline_observation(repo, now) if args.offline else collect_repository(policy["owner"], repo, policy, token, now) for repo in repos]
    findings = [finding for repo, observation in zip(repos, observations) for finding in evaluate(repo, observation, policy, now)]
    report = render_report(repos, observations, findings, now)
    if not args.check: write_outputs(report, findings, observations, policy, now)
    print(f"Portfolio assurance monitor: {len(repos)} repositories, {len(findings)} findings, mode={'offline' if args.offline else 'live'}")
    return 0

if __name__ == "__main__": raise SystemExit(main())
