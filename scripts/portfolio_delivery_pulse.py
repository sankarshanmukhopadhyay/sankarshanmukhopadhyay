#!/usr/bin/env python3
"""Add an evidence-backed delivery pulse to the Portfolio Work Queue.

The pulse is observational portfolio evidence. It does not assert project health,
assurance, maturity, release authority, or causal impact.
"""
from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/repository-status.yaml"
CONFIG = ROOT / "config/portfolio-work-queue.yaml"
OWNER = "sankarshanmukhopadhyay"
DEFAULT_JSON = ROOT / "data/portfolio-delivery-pulse.json"
DEFAULT_MD = ROOT / "docs/portfolio-work/index.md"

AUTOMATION_MESSAGE_PREFIXES = (
    "chore(monitor):",
    "chore(assurance): advance monitored",
    "rebuild generated",
)
MAINTENANCE_MESSAGE_PREFIXES = (
    "chore(deps):",
    "build(deps):",
    "chore(maintenance):",
)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def eligible_repositories() -> list[str]:
    registry = load_yaml(REGISTRY)
    config = load_yaml(CONFIG)
    rules = config["eligible"]
    dispositions = set(rules["dispositions"])
    lifecycles = set(rules["lifecycles"])
    operational = set(rules["operational_statuses"])
    return sorted(
        repo["name"]
        for repo in registry.get("repositories", [])
        if repo.get("portfolio_disposition") in dispositions
        and repo.get("lifecycle") in lifecycles
        and repo.get("operational_status") in operational
    )


def github_page(url: str, token: str | None) -> list[dict[str, Any]]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "portfolio-delivery-pulse/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.load(response)
    if not isinstance(payload, list):
        raise ValueError(f"Expected list response from {url}")
    return payload


def github_paginated(url: str, token: str | None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    separator = "&" if "?" in url else "?"
    for page in range(1, 51):
        batch = github_page(f"{url}{separator}per_page=100&page={page}", token)
        records.extend(batch)
        if len(batch) < 100:
            break
    else:
        raise RuntimeError(f"Pagination safety bound exceeded for {url}")
    return records


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def commit_kind(item: dict[str, Any]) -> str:
    message = ((item.get("commit") or {}).get("message") or "").splitlines()[0].lower()
    actors = [item.get("author") or {}, item.get("committer") or {}]
    if any(
        actor.get("type") == "Bot" or str(actor.get("login", "")).endswith("[bot]")
        for actor in actors
    ) or message.startswith(AUTOMATION_MESSAGE_PREFIXES):
        return "automated"
    if message.startswith(MAINTENANCE_MESSAGE_PREFIXES) or "dependabot" in message:
        return "maintenance"
    return "substantive"


def collect_repository(name: str, since: datetime, token: str | None) -> dict[str, Any]:
    base = f"https://api.github.com/repos/{OWNER}/{urllib.parse.quote(name)}"
    since_iso = since.isoformat().replace("+00:00", "Z")
    commits = github_paginated(f"{base}/commits?since={urllib.parse.quote(since_iso)}", token)
    pulls = github_paginated(f"{base}/pulls?state=closed&sort=updated&direction=desc", token)
    issues = github_paginated(f"{base}/issues?state=closed&since={urllib.parse.quote(since_iso)}", token)
    releases = github_paginated(f"{base}/releases", token)

    return {
        "commits": [
            {
                "sha": c.get("sha"),
                "url": c.get("html_url"),
                "timestamp": ((c.get("commit") or {}).get("committer") or {}).get("date")
                or ((c.get("commit") or {}).get("author") or {}).get("date"),
                "kind": commit_kind(c),
            }
            for c in commits
        ],
        "merged_prs": [
            {"number": p.get("number"), "url": p.get("html_url"), "timestamp": p.get("merged_at")}
            for p in pulls
            if p.get("merged_at") and parse_time(p.get("merged_at")) >= since
        ],
        "closed_issues": [
            {"number": i.get("number"), "url": i.get("html_url"), "timestamp": i.get("closed_at")}
            for i in issues
            if "pull_request" not in i
            and i.get("closed_at")
            and parse_time(i.get("closed_at")) >= since
        ],
        "releases": [
            {"id": r.get("id"), "url": r.get("html_url"), "timestamp": r.get("published_at")}
            for r in releases
            if r.get("published_at") and parse_time(r.get("published_at")) >= since
        ],
    }


def summarize(repositories: dict[str, Any], generated_at: datetime, days: int) -> dict[str, int]:
    cutoff = generated_at - timedelta(days=days)
    totals = {
        "commits": 0,
        "substantive_commits": 0,
        "maintenance_commits": 0,
        "automated_commits": 0,
        "merged_prs": 0,
        "closed_issues": 0,
        "releases": 0,
        "active_repositories": 0,
    }
    for evidence in repositories.values():
        active = False
        for commit in evidence.get("commits", []):
            if (parse_time(commit.get("timestamp")) or datetime.min.replace(tzinfo=timezone.utc)) < cutoff:
                continue
            totals["commits"] += 1
            kind = commit.get("kind", "substantive")
            totals[f"{kind}_commits"] += 1
            if kind == "substantive":
                active = True
        for key in ("merged_prs", "closed_issues", "releases"):
            count = sum(
                1
                for item in evidence.get(key, [])
                if (parse_time(item.get("timestamp")) or datetime.min.replace(tzinfo=timezone.utc)) >= cutoff
            )
            totals[key] += count
            active = active or count > 0
        if active:
            totals["active_repositories"] += 1
    return totals


def build_pulse(now: datetime, token: str | None) -> dict[str, Any]:
    since = now - timedelta(days=30)
    repositories = {
        name: collect_repository(name, since, token) for name in eligible_repositories()
    }
    return {
        "schema_version": "1.0",
        "generated_at": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "scope": {
            "owner": OWNER,
            "repository_source": "data/repository-status.yaml + config/portfolio-work-queue.yaml eligible scope",
            "commit_scope": "default-branch commits returned by GitHub commits API",
            "statement": "Observational throughput evidence only; not assurance, maturity, health, or project authority.",
        },
        "classification": {
            "automated": "GitHub bot actor or known generated/monitor commit prefix",
            "maintenance": "dependency or explicit maintenance commit prefix",
            "substantive": "remaining default-branch commits; still not a claim of impact or quality",
        },
        "windows": {"7d": summarize(repositories, now, 7), "30d": summarize(repositories, now, 30)},
        "repositories": repositories,
    }


def render_markdown(pulse: dict[str, Any]) -> str:
    seven, thirty = pulse["windows"]["7d"], pulse["windows"]["30d"]
    return "\n".join(
        [
            "## Portfolio delivery pulse",
            "",
            "Rolling throughput across the same governed repository scope as this planner. Raw commit volume is decomposed so automation and maintenance cannot masquerade as delivery progress.",
            "",
            "| Window | Commits | Substantive | Maintenance | Automated | PRs merged | Issues closed | Releases | Active repos |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
            f"| 7 days | {seven['commits']} | {seven['substantive_commits']} | {seven['maintenance_commits']} | {seven['automated_commits']} | {seven['merged_prs']} | {seven['closed_issues']} | {seven['releases']} | {seven['active_repositories']} |",
            f"| 30 days | {thirty['commits']} | {thirty['substantive_commits']} | {thirty['maintenance_commits']} | {thirty['automated_commits']} | {thirty['merged_prs']} | {thirty['closed_issues']} | {thirty['releases']} | {thirty['active_repositories']} |",
            "",
            "> **Interpretation boundary:** this is delivery-throughput evidence, not a project-health, assurance, maturity, certification, or impact score. `Substantive` means only that the commit was not classified as automation or routine maintenance.",
            "",
            "Machine-readable evidence: [`data/portfolio-delivery-pulse.json`](../../data/portfolio-delivery-pulse.json).",
            "",
        ]
    )


def inject(page: str, pulse_md: str) -> str:
    marker = "## Work now"
    if marker not in page:
        raise ValueError(f"Portfolio page is missing insertion marker: {marker}")
    return page.replace(marker, pulse_md + "\n" + marker, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--page", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    pulse = build_pulse(now, os.getenv("GITHUB_TOKEN"))
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(pulse, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.page.write_text(inject(args.page.read_text(encoding="utf-8"), render_markdown(pulse)), encoding="utf-8")
    print(f"Wrote portfolio delivery pulse for {len(pulse['repositories'])} repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
