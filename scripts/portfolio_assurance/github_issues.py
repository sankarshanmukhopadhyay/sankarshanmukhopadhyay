from __future__ import annotations
import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

USER_AGENT = "portfolio-assurance-monitor/2.0"


def _request(url: str, token: str, method: str = "GET", payload: dict[str, Any] | None = None) -> Any:
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def issue_marker(fingerprint: str) -> str:
    return f"<!-- portfolio-assurance:fingerprint={fingerprint} -->"


def render_issue_body(finding: dict[str, Any], report_url: str | None = None) -> str:
    ev = finding.get("evidence", {})
    evidence_lines = []
    unresolved = ev.get("unresolved", []) if isinstance(ev, dict) else []
    for item in unresolved:
        label = item.get("name") or item.get("path") or item.get("workflow_id") or "workflow"
        url = item.get("html_url")
        evidence_lines.append(f"- {label}: {url}" if url else f"- {label}: `{item.get('conclusion', 'unknown')}`")
    if not evidence_lines:
        evidence_lines.append(f"- Monitor evidence: `{json.dumps(ev, sort_keys=True)[:1500]}`")
    if report_url:
        evidence_lines.append(f"- Portfolio assurance report: {report_url}")
    return "\n".join([
        "## Portfolio assurance finding",
        "",
        "The Portfolio Assurance Monitor detected an actionable condition that remains unresolved in the current governed observation window.",
        "",
        "### Finding",
        "",
        f"- Finding fingerprint: `{finding['finding_fingerprint']}`",
        f"- Rule: `{finding['rule_id']}`",
        f"- Severity: `{finding['severity']}`",
        f"- Subject: `{finding.get('subject', 'repository')}`",
        f"- First/last observation represented by this issue: `{finding['observed_at']}`",
        "",
        "### Why this was raised",
        "",
        finding["claim"],
        "",
        "### Evidence",
        "",
        *evidence_lines,
        "",
        "### Expected remediation",
        "",
        finding["recommended_action"],
        "",
        "### Closure evidence",
        "",
        "A later machine-verifiable observation should demonstrate recovery, or a human reviewer should record an explicit governed disposition or accepted risk. Automated recovery detection does not by itself change repository status, maturity, lifecycle, authority, or release state.",
        "",
        "### Governance boundary",
        "",
        "This issue is generated as assurance evidence. It does not automatically modify normative content, portfolio classification, repository maturity, release authority, or upstream governance.",
        "",
        issue_marker(finding["finding_fingerprint"]),
    ])


def find_open_issue(owner: str, repository: str, fingerprint: str, token: str) -> dict[str, Any] | None:
    marker = issue_marker(fingerprint)
    issues = _request(f"https://api.github.com/repos/{owner}/{repository}/issues?state=open&per_page=100", token)
    for item in issues if isinstance(issues, list) else []:
        if item.get("pull_request"):
            continue
        if marker in (item.get("body") or ""):
            return item
    return None


def create_issue(owner: str, repository: str, finding: dict[str, Any], token: str, report_url: str | None = None) -> dict[str, Any]:
    title = f"[Portfolio assurance] {finding['rule_id']}: {finding.get('subject', 'repository')}"
    return _request(
        f"https://api.github.com/repos/{owner}/{repository}/issues",
        token,
        method="POST",
        payload={"title": title, "body": render_issue_body(finding, report_url), "labels": []},
    )


def comment_issue(owner: str, repository: str, issue_number: int, finding: dict[str, Any], token: str) -> dict[str, Any]:
    body = "\n".join([
        "### Portfolio assurance observation update",
        "",
        f"The condition represented by `{finding['finding_fingerprint']}` remains unresolved as of `{finding['observed_at']}`.",
        "",
        f"Current evidence: `{json.dumps(finding.get('evidence', {}), sort_keys=True)[:1800]}`",
        "",
        "No portfolio status or repository authority change is implied by this update.",
    ])
    return _request(f"https://api.github.com/repos/{owner}/{repository}/issues/{issue_number}/comments", token, method="POST", payload={"body": body})


def publish_findings(owner: str, findings: list[dict[str, Any]], token: str, policy: dict[str, Any], report_url: str | None = None) -> list[dict[str, Any]]:
    cfg = policy.get("issue_routing", {})
    limit = int(cfg.get("max_new_issues_per_run", 2))
    comment_existing = bool(cfg.get("comment_on_repeat", False))
    created = 0
    records: list[dict[str, Any]] = []
    for finding in findings:
        if not finding.get("routing", {}).get("eligible"):
            continue
        repo = finding["repository"]
        try:
            existing = find_open_issue(owner, repo, finding["finding_fingerprint"], token)
            if existing:
                if comment_existing:
                    comment_issue(owner, repo, int(existing["number"]), finding, token)
                records.append({"fingerprint": finding["finding_fingerprint"], "repository": repo, "action": "deduplicated", "issue_url": existing.get("html_url")})
                continue
            if created >= limit:
                records.append({"fingerprint": finding["finding_fingerprint"], "repository": repo, "action": "suppressed-run-cap"})
                continue
            issue = create_issue(owner, repo, finding, token, report_url)
            created += 1
            records.append({"fingerprint": finding["finding_fingerprint"], "repository": repo, "action": "created", "issue_url": issue.get("html_url")})
        except (urllib.error.HTTPError, urllib.error.URLError, ValueError) as error:
            records.append({"fingerprint": finding["finding_fingerprint"], "repository": repo, "action": "publication-error", "error": str(error)})
    return records
