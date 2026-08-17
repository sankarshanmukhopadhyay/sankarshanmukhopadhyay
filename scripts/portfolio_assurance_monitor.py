#!/usr/bin/env python3
"""Collect portfolio evidence, evaluate deterministic rules, and publish assurance reports."""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from portfolio_assurance.core import iso, latest_workflow_states, make_finding as _make_finding
from portfolio_assurance.discovery import discover_public_repositories, discovery_findings, registered_repository_churn_findings
from portfolio_assurance.github_issues import publish_findings
from portfolio_assurance.routing import routing_decision

STATUS_PATH = ROOT / "data/repository-status.yaml"
POLICY_PATH = ROOT / "config/portfolio-monitor/policy.yaml"
USER_AGENT = "portfolio-assurance-monitor/2.0"


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


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
            runs = request_json(
                f"https://api.github.com/repos/{owner}/{name}/actions/runs?branch={branch}&per_page={int(policy['collection']['workflow_runs_per_repository'])}",
                token, timeout,
            )
            workflow_runs = runs.get("workflow_runs", []) if isinstance(runs, dict) else []
            observation["evidence"]["workflow_runs"] = latest_workflow_states(
                workflow_runs, now, int(policy["collection"]["lookback_days"])
            )
        except Exception as error:
            observation["evidence"]["workflow_runs"] = {"available": False, "error": str(error)}
    except Exception as error:
        observation["collection_error"] = str(error)
    return observation


def make_finding(repository: str, rule_id: str, severity: str, observed_at: str, claim: str,
                 evidence: dict[str, Any], action: str, *, subject: str = "repository",
                 repo: dict[str, Any] | None = None, policy: dict[str, Any] | None = None) -> dict[str, Any]:
    finding = _make_finding(repository, rule_id, severity, observed_at, claim, evidence, action, subject=subject)
    if repo is not None and policy is not None:
        finding["routing"] = routing_decision(repo, finding, policy)
    return finding


def evaluate(repo: dict[str, Any], observation: dict[str, Any], policy: dict[str, Any], now: dt.datetime) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    rules = policy["rules"]
    name, observed_at = repo["name"], observation["observed_at"]
    if not observation["available"] and rules["repository_unavailable"]["enabled"]:
        findings.append(make_finding(name, "REPOSITORY_UNAVAILABLE", rules["repository_unavailable"]["severity"], observed_at,
            "A monitored flagship repository must remain publicly observable.", {"collection_error": observation.get("collection_error")},
            "Verify repository availability, visibility, rename state, and monitor permissions.", repo=repo, policy=policy))
        return findings
    try:
        next_review = dt.date.fromisoformat(str(repo["next_review"]))
        if next_review < now.date() and rules["review_overdue"]["enabled"]:
            findings.append(make_finding(name, "REVIEW_OVERDUE", rules["review_overdue"]["severity"], observed_at,
                "The portfolio review date must not be expired.", {"next_review": str(next_review)},
                "Conduct and record a portfolio status review.", repo=repo, policy=policy))
    except Exception:
        pass
    declaration = observation["evidence"].get("status_declaration")
    if repo.get("status_source", {}).get("required") and declaration:
        if not declaration.get("present") and rules["status_declaration_missing"]["enabled"]:
            findings.append(make_finding(name, "STATUS_DECLARATION_MISSING", rules["status_declaration_missing"]["severity"], observed_at,
                "A required repository-local status declaration must exist.", declaration,
                "Add the required status declaration or revise the governed status-source contract.", repo=repo, policy=policy))
        elif not declaration.get("readable") and rules["status_declaration_unreadable"]["enabled"]:
            findings.append(make_finding(name, "STATUS_DECLARATION_UNREADABLE", rules["status_declaration_unreadable"]["severity"], observed_at,
                "A required repository-local status declaration must be readable YAML.", declaration,
                "Correct the declaration syntax and validate it against the portfolio schema.", repo=repo, policy=policy))
    workflows = observation["evidence"].get("workflow_runs", {})
    if workflows.get("unresolved_failures", 0) > 0 and rules["default_branch_workflow_unresolved_failure"]["enabled"]:
        for unresolved in workflows.get("unresolved", []):
            subject = str(unresolved.get("path") or unresolved.get("name") or unresolved.get("workflow_id") or "workflow")
            findings.append(make_finding(name, "DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE",
                rules["default_branch_workflow_unresolved_failure"]["severity"], observed_at,
                "The latest completed default-branch run for this workflow is failing within the governed observation window.",
                {**workflows, "unresolved": [unresolved]},
                "Review the failed workflow, restore a successful default-branch run, or record an explicit accepted-risk disposition.",
                subject=subject, repo=repo, policy=policy))
    pushed_at = observation["evidence"].get("repository", {}).get("pushed_at")
    if pushed_at and rules["no_recent_activity"]["enabled"]:
        pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        threshold = int(rules["no_recent_activity"]["threshold_days"])
        if (now - pushed).days > threshold and repo.get("lifecycle") == "active":
            findings.append(make_finding(name, "NO_RECENT_ACTIVITY", rules["no_recent_activity"]["severity"], observed_at,
                "An active flagship repository has exceeded the configured activity-review threshold.",
                {"pushed_at": pushed_at, "threshold_days": threshold},
                "Review whether the declared lifecycle and operational status remain accurate. Activity alone does not determine health.",
                repo=repo, policy=policy))
    return findings


def render_report(repos: list[dict[str, Any]], observations: list[dict[str, Any]], findings: list[dict[str, Any]], now: dt.datetime, *, publication_role: str = "dashboard") -> str:
    if publication_role not in {"dashboard", "evidence"}:
        raise ValueError(f"Unsupported publication role: {publication_role}")
    by_repo = {o["repository"]: o for o in observations}
    f_by_repo: dict[str, list[dict[str, Any]]] = {}
    for finding in findings:
        f_by_repo.setdefault(finding["repository"], []).append(finding)
    if publication_role == "dashboard":
        front_matter = ["---", "layout: default", "title: Portfolio Assurance Dashboard", "parent: Portfolio Assurance Monitor", "nav_order: 1", "---"]
        heading = "Portfolio Assurance Dashboard"
    else:
        front_matter = ["---", "layout: default", f"title: Portfolio Assurance Report — {now.date().isoformat()}", "nav_exclude: true", "search_exclude: true", "---"]
        heading = f"Portfolio Assurance Report — {now.date().isoformat()}"
    monitored_findings = [f for f in findings if f["repository"] in by_repo]
    discovery_count = len([f for f in findings if f["rule_id"] == "PUBLIC_REPOSITORY_WITHOUT_DISPOSITION"])
    lines = front_matter + ["", f"# {heading}", "", f"**Observed:** {iso(now)}  ", f"**Scope:** {len(repos)} flagship original repositories  ", f"**Open findings:** {len(findings)}  ", f"**Unclassified public repositories:** {discovery_count}", "", "> This is first-party, evidence-based portfolio monitoring. Findings do not automatically modify portfolio status, maturity, lifecycle, authority, or disposition.", "", "## Current observations", "", "| Repository | Availability | Status declaration | Workflow evidence | Findings |", "|---|---:|---:|---:|---:|"]
    for repo in repos:
        obs = by_repo[repo["name"]]
        ev = obs.get("evidence", {})
        declaration = ev.get("status_declaration")
        decl = "n/a" if declaration is None else ("valid" if declaration.get("readable") else "attention")
        workflows = ev.get("workflow_runs", {})
        wf = "unavailable" if workflows.get("available") is False else f"{workflows.get('unresolved_failures', 0)} unresolved"
        lines.append(f"| [{repo['name']}](https://github.com/sankarshanmukhopadhyay/{repo['name']}) | {'available' if obs['available'] else 'unavailable'} | {decl} | {wf} | [{len(f_by_repo.get(repo['name'], []))}](../../reports/portfolio-assurance/findings/{repo['name']}.html) |")
    lines += ["", "## Findings", "", "Per-repository development feeds are published as downloadable JSON and Markdown under `reports/portfolio-assurance/findings/`. These feeds are intended to be supplied to the affected repository during release planning and implementation.", ""]
    if not findings:
        lines.append("No findings were produced by the enabled rules.")
    for finding in sorted(findings, key=lambda x: (x["severity"], x["repository"], x["rule_id"], x.get("subject", ""))):
        lines += [f"### {finding['finding_id']}: {finding['repository']}", "", f"- **Fingerprint:** `{finding['finding_fingerprint']}`", f"- **Rule:** `{finding['rule_id']}`", f"- **Subject:** `{finding.get('subject', 'repository')}`", f"- **Severity:** `{finding['severity']}`", f"- **Claim:** {finding['claim']}", f"- **Recommended action:** {finding['recommended_action']}", f"- **Issue routing:** `{finding.get('routing', {}).get('target', 'central-review')}`", f"- **Automatic effect:** `{finding['automatic_effect']}`", ""]
    lines += ["## Governance boundary", "", "The monitor observes public evidence and evaluates configured rules. Account discovery can nominate unclassified repositories, and issue publication can route eligible actionable findings, but neither capability changes portfolio membership or repository authority. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.", ""]
    return "\n".join(lines)



def finding_export_paths(repository: str, policy: dict[str, Any]) -> tuple[Path, Path]:
    directory = ROOT / policy["publication"].get("development_findings_directory", "reports/portfolio-assurance/findings")
    return directory / f"{repository}.json", directory / f"{repository}.md"


def finding_export_urls(owner: str, repository: str) -> dict[str, str]:
    base = f"https://{owner}.github.io/{owner}/reports/portfolio-assurance/findings/{repository}"
    return {"json": f"{base}.json", "markdown": f"{base}.md"}


def write_finding_exports(findings: list[dict[str, Any]], policy: dict[str, Any], now: dt.datetime) -> None:
    owner = policy["owner"]
    repositories = sorted({f["repository"] for f in findings})
    configured = {r["name"] for r in load_yaml(STATUS_PATH).get("repositories", [])}
    repositories = sorted(set(repositories) | configured)
    directory = ROOT / policy["publication"].get("development_findings_directory", "reports/portfolio-assurance/findings")
    directory.mkdir(parents=True, exist_ok=True)
    expected: set[Path] = set()
    index: list[dict[str, Any]] = []
    for repository in repositories:
        repo_findings = sorted(
            [f for f in findings if f["repository"] == repository],
            key=lambda x: (x["severity"], x["rule_id"], x.get("subject", "")),
        )
        json_path, md_path = finding_export_paths(repository, policy)
        expected.update({json_path, md_path})
        urls = finding_export_urls(owner, repository)
        payload = {
            "$schema": f"https://{owner}.github.io/{owner}/schemas/portfolio-finding-feed.schema.json",
            "schema_version": "1.0",
            "generated_at": iso(now),
            "repository": repository,
            "source": {
                "monitor": f"https://github.com/{owner}/{owner}",
                "dashboard": f"https://{owner}.github.io/{owner}/docs/portfolio-assurance/dashboard.html",
                "latest_report": f"https://{owner}.github.io/{owner}/reports/portfolio-assurance/latest.html",
            },
            "finding_count": len(repo_findings),
            "findings": repo_findings,
        }
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        lines = [
            "---", "layout: default", f"title: Development findings — {repository}", "nav_exclude: true", "search_exclude: true", "---", "",
            f"# Development findings — `{repository}`", "",
            f"**Generated:** {iso(now)}  ",
            f"**Open findings:** {len(repo_findings)}  ",
            f"**Machine-readable feed:** [JSON]({urls['json']})", "",
            "> This feed is a development input, not an automatic instruction or status change. Each finding must be reviewed, dispositioned, and closed using repository authority and release governance.", "",
        ]
        if not repo_findings:
            lines += ["No current findings are open for this repository.", ""]
        for finding in repo_findings:
            lines += [
                f"## {finding['finding_fingerprint']} — {finding['rule_id']}", "",
                f"- Observation: `{finding['finding_id']}` at `{finding['observed_at']}`",
                f"- Severity: `{finding['severity']}`",
                f"- Subject: `{finding.get('subject', 'repository')}`",
                f"- Claim: {finding['claim']}",
                f"- Recommended action: {finding['recommended_action']}",
                f"- Automatic effect: `{finding['automatic_effect']}`", "",
            ]
        md_path.write_text("\n".join(lines), encoding="utf-8")
        index.append({"repository": repository, "finding_count": len(repo_findings), "json": urls["json"], "markdown": urls["markdown"]})
    # Remove stale per-repository exports after repository churn.
    for path in directory.glob("*.json"):
        if path not in expected and path.name != "index.json":
            path.unlink()
    for path in directory.glob("*.md"):
        if path not in expected:
            path.unlink()
    (directory / "index.json").write_text(json.dumps({"generated_at": iso(now), "repositories": index}, indent=2) + "\n", encoding="utf-8")

def write_outputs(dashboard_report: str, evidence_report: str, findings: list[dict[str, Any]], observations: list[dict[str, Any]], policy: dict[str, Any], now: dt.datetime, publication_records: list[dict[str, Any]] | None = None) -> None:
    publication = policy["publication"]
    latest = ROOT / publication["latest_report"]
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(evidence_report, encoding="utf-8")
    (ROOT / publication["documentation_page"]).write_text(dashboard_report, encoding="utf-8")
    payload = {"generated_at": iso(now), "findings": findings, "observations": observations, "issue_publication": publication_records or []}
    (ROOT / publication["latest_findings"]).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    history = ROOT / publication["history_directory"]
    history.mkdir(parents=True, exist_ok=True)
    (history / f"{now.date().isoformat()}.md").write_text(evidence_report, encoding="utf-8")
    write_finding_exports(findings, policy, now)


def offline_observation(repo: dict[str, Any], now: dt.datetime) -> dict[str, Any]:
    declaration = repo.get("status_source", {})
    evidence: dict[str, Any] = {"repository": {"pushed_at": iso(now), "default_branch": "main"}, "workflow_runs": {"lookback_days": 7, "completed_examined": 0, "workflows_examined": 0, "unresolved_failures": 0, "unresolved": []}}
    if declaration.get("type") == "member-declaration":
        evidence["status_declaration"] = {"path": declaration.get("path"), "present": True, "readable": True, "mode": "offline-validation"}
    return {"repository": repo["name"], "observed_at": iso(now), "available": True, "evidence": evidence, "collection_error": None}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="Validate generation without GitHub network calls")
    parser.add_argument("--check", action="store_true", help="Evaluate and print summary without writing files")
    parser.add_argument("--publish-issues", action="store_true", help="Publish eligible findings when issue routing and credentials are enabled")
    args = parser.parse_args()
    status, policy = load_yaml(STATUS_PATH), load_yaml(POLICY_PATH)
    repos = selected_repositories(status, policy)
    if not repos:
        raise SystemExit("No repositories selected by portfolio monitor policy")
    now = utc_now()
    token = os.getenv("GITHUB_TOKEN")
    observations = [offline_observation(repo, now) if args.offline else collect_repository(policy["owner"], repo, policy, token, now) for repo in repos]
    findings = [finding for repo, observation in zip(repos, observations) for finding in evaluate(repo, observation, policy, now)]
    if not args.offline and policy.get("discovery", {}).get("enabled", False):
        try:
            public_repos = discover_public_repositories(policy["owner"], request_json, token, int(policy["collection"]["request_timeout_seconds"]))
            findings.extend(discovery_findings(status, public_repos, iso(now), str(policy["discovery"].get("severity", "info"))))
            if policy.get("rules", {}).get("registered_repository_not_publicly_discovered", {}).get("enabled", True):
                churn_rule = policy["rules"]["registered_repository_not_publicly_discovered"]
                findings.extend(registered_repository_churn_findings(status, public_repos, iso(now), str(churn_rule.get("severity", "medium"))))
        except Exception as error:
            findings.append(_make_finding(policy["owner"], "ACCOUNT_DISCOVERY_UNAVAILABLE", "low", iso(now),
                "Public account discovery could not be completed.", {"error": str(error)},
                "Review GitHub API availability and monitor permissions; do not infer portfolio completeness from this run.", subject="public-account-discovery"))
    publication_records: list[dict[str, Any]] = []
    issue_cfg = policy.get("issue_routing", {})
    issue_token = os.getenv("PORTFOLIO_ISSUE_TOKEN")
    if args.publish_issues and issue_cfg.get("enabled", False):
        if not issue_token:
            publication_records.append({"action": "skipped", "reason": "PORTFOLIO_ISSUE_TOKEN not configured"})
        else:
            report_url = f"https://{policy['owner']}.github.io/{policy['owner']}/docs/portfolio-assurance/dashboard.html"
            publication_records = publish_findings(policy["owner"], findings, issue_token, policy, report_url)
    dashboard_report = render_report(repos, observations, findings, now, publication_role="dashboard")
    evidence_report = render_report(repos, observations, findings, now, publication_role="evidence")
    if not args.check:
        write_outputs(dashboard_report, evidence_report, findings, observations, policy, now, publication_records)
    print(f"Portfolio assurance monitor: {len(repos)} repositories, {len(findings)} findings, {len(publication_records)} issue actions, mode={'offline' if args.offline else 'live'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
