#!/usr/bin/env python3
"""Build the evidence-backed Portfolio Work Queue.

The queue is derived evidence. It does not mutate member repositories or create project authority.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/repository-status.yaml"
CONFIG = ROOT / "config/portfolio-work-queue.yaml"
DEFAULT_JSON = ROOT / "data/portfolio-work-queue.json"
DEFAULT_MD = ROOT / "docs/portfolio-work/index.md"
OWNER = "sankarshanmukhopadhyay"

LEVELS = ["none", "low", "medium", "high", "very-high"]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def norm_labels(item: dict[str, Any]) -> list[str]:
    labels = item.get("labels", [])
    out: list[str] = []
    for value in labels:
        if isinstance(value, dict):
            value = value.get("name", "")
        if value:
            out.append(str(value).strip().lower())
    return sorted(set(out))


def eligible_repositories(registry: dict[str, Any], config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    rules = config["eligible"]
    allowed_dispositions = set(rules["dispositions"])
    allowed_lifecycles = set(rules["lifecycles"])
    allowed_ops = set(rules["operational_statuses"])
    return {
        repo["name"]: repo
        for repo in registry.get("repositories", [])
        if repo.get("portfolio_disposition") in allowed_dispositions
        and repo.get("lifecycle") in allowed_lifecycles
        and repo.get("operational_status") in allowed_ops
    }


def github_json(url: str, token: str | None) -> Any:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "portfolio-work-queue/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def collect_live(repositories: dict[str, dict[str, Any]], token: str | None) -> dict[str, Any]:
    evidence: dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "repositories": {},
    }
    for name in sorted(repositories):
        base = f"https://api.github.com/repos/{OWNER}/{urllib.parse.quote(name)}"
        issues = github_json(f"{base}/issues?state=open&per_page=100", token)
        pure_issues, prs = [], []
        for item in issues:
            record = {
                "number": item["number"],
                "title": item.get("title", ""),
                "url": item.get("html_url", ""),
                "labels": [x.get("name", "") for x in item.get("labels", [])],
                "body": item.get("body") or "",
                "updated_at": item.get("updated_at"),
            }
            if "pull_request" in item:
                prs.append(record)
            else:
                pure_issues.append(record)
        evidence["repositories"][name] = {"issues": pure_issues, "pull_requests": prs}
    return evidence


def text_blob(item: dict[str, Any]) -> str:
    return " ".join([item.get("title", ""), item.get("body", ""), " ".join(norm_labels(item))]).lower()


def has_any(text: str, values: list[str]) -> bool:
    return any(value.lower() in text for value in values)


def effort_for(item: dict[str, Any], config: dict[str, Any]) -> tuple[str, int, str]:
    labels = norm_labels(item)
    quick = config["heuristics"].get("quick_labels", {})
    for label, bucket in quick.items():
        if label.lower() in labels:
            match = next(x for x in config["effort_buckets"] if x["id"] == bucket)
            return bucket, int(match["minutes"]), "medium"

    text = text_blob(item)
    if has_any(text, ["typo", "link", "docs only", "documentation"]) and not has_any(text, ["architecture", "normative", "security"]):
        bucket = "30-60m"
    elif has_any(text, ["end-to-end", "cross-repository", "migration", "implementation", "harness", "conformance"]):
        bucket = "2-4h"
    elif has_any(text, ["release", "schema", "workflow", "validation", "test"]):
        bucket = "1-2h"
    else:
        bucket = "1-2h"
    match = next(x for x in config["effort_buckets"] if x["id"] == bucket)
    confidence = "medium" if item.get("body") else "low"
    return bucket, int(match["minutes"]), confidence


def classify_state(item: dict[str, Any], config: dict[str, Any]) -> tuple[str, str]:
    labels = norm_labels(item)
    text = text_blob(item)
    h = config["heuristics"]
    if any(x in labels for x in h["blocked_labels"]):
        if has_any(text, ["upstream", "external", "ratification", "third party", "independent implementation"]):
            return "waiting-external", "Explicit blocker depends on external/upstream evidence."
        return "blocked", "Explicit blocker label is present."
    if any(x in labels for x in h["consequential_labels"]):
        return "needs-judgment", "Label indicates consequential architecture/governance/security/release judgment."
    if any(x in labels for x in h["maintenance_labels"]) or has_any(text, ["dependabot", "build(deps)", "bump dependency"]):
        return "maintenance", "Dependency/chore evidence is separated from strategic execution."
    return "ready", "No explicit blocking, judgment, or maintenance signal observed."


def impact_for(repo: str, item: dict[str, Any], config: dict[str, Any]) -> tuple[str, list[str]]:
    goal = config.get("project_goals", {}).get(repo)
    if not goal:
        return "medium", ["No explicit current-goal declaration; portfolio activity provides only medium-confidence impact."]
    text = text_blob(item)
    matches = [signal for signal in goal.get("signals", []) if signal.lower() in text]
    if len(matches) >= 3:
        level = "very-high"
    elif len(matches) == 2:
        level = "high"
    elif len(matches) == 1:
        level = "medium"
    else:
        level = "low"
    return level, [f"Matches current project goal signal: {m}" for m in matches] or ["No current-goal signal matched."]


def score(repo_meta: dict[str, Any], item: dict[str, Any], state: str, impact: str, confidence: str, config: dict[str, Any]) -> tuple[float, list[str]]:
    weights = config["scoring"]["weights"]
    penalties = config["scoring"]["penalties"]
    values = config["scoring"]["impact_values"]
    text = text_blob(item)
    title_signals = config["heuristics"]["title_signals"]
    rationale: list[str] = []

    components = {
        "project_goal_impact": values[impact],
        "portfolio_impact": 1.0 if repo_meta.get("tier") == "flagship" else 0.6,
        "unblock_value": 1.0 if has_any(text, title_signals["unblock"]) else 0.25,
        "release_proximity": 1.0 if has_any(text, title_signals["release"]) else 0.2,
        "assurance_value": 1.0 if has_any(text, title_signals["assurance"]) else 0.2,
        "adoption_value": 1.0 if has_any(text, title_signals["adoption"]) else 0.2,
        "staleness_pressure": 0.25,
    }
    total = sum(weights[k] * v for k, v in components.items())
    if state == "blocked":
        total -= penalties["blocked"]
    elif state == "waiting-external":
        total -= penalties["waiting_external"]
    elif state == "maintenance":
        total -= penalties["maintenance_noise"]
    if confidence == "low":
        total -= penalties["low_confidence"]

    for key, value in components.items():
        if value >= 0.75:
            rationale.append(key.replace("_", " "))
    return round(max(total, 0.0), 2), rationale


def complexity_for(item: dict[str, Any], state: str) -> str:
    text = text_blob(item)
    if state == "needs-judgment":
        return "consequential"
    if has_any(text, ["cross-repository", "end-to-end", "migration", "protocol", "schema", "security"]):
        return "high"
    if has_any(text, ["implementation", "workflow", "conformance", "validation", "test", "release"]):
        return "medium"
    return "low"


def build_queue(registry: dict[str, Any], config: dict[str, Any], evidence: dict[str, Any]) -> dict[str, Any]:
    eligible = eligible_repositories(registry, config)
    candidates: list[dict[str, Any]] = []
    for repo in sorted(eligible):
        observed = evidence.get("repositories", {}).get(repo, {})
        for source_key, source_type in (("issues", "issue"), ("pull_requests", "pull-request")):
            for item in observed.get(source_key, []):
                state, state_reason = classify_state(item, config)
                bucket, minutes, confidence = effort_for(item, config)
                impact, impact_reasons = impact_for(repo, item, config)
                complexity = complexity_for(item, state)
                priority, score_reasons = score(eligible[repo], item, state, impact, confidence, config)
                leverage = round(priority / max(minutes / 60.0, 0.25), 2)
                candidates.append({
                    "id": f"{repo}:{source_type}:{item['number']}",
                    "repository": repo,
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "source_type": source_type,
                    "state": state,
                    "effort": {"bucket": bucket, "minutes": minutes},
                    "complexity": complexity,
                    "confidence": confidence,
                    "project_goal_impact": impact,
                    "priority": priority,
                    "leverage": leverage,
                    "labels": norm_labels(item),
                    "rationale": [state_reason, *impact_reasons, *score_reasons],
                })
    candidates.sort(key=lambda x: (-x["priority"], -x["leverage"], x["repository"], x["id"]))
    return {
        "schema_version": "1.0",
        "generated_at": evidence.get("generated_at") or datetime.now(timezone.utc).isoformat(),
        "authority": {
            "scope_source": str(REGISTRY.relative_to(ROOT)),
            "statement": config["authority"]["statement"],
        },
        "candidates": candidates,
    }


def render_markdown(queue: dict[str, Any], config: dict[str, Any]) -> str:
    candidates = queue["candidates"]
    ready = [c for c in candidates if c["state"] == "ready"]
    blocked = [c for c in candidates if c["state"] in {"blocked", "waiting-external"}]
    judgment = [c for c in candidates if c["state"] == "needs-judgment"]
    maintenance = [c for c in candidates if c["state"] == "maintenance"]

    def table(items: list[dict[str, Any]], limit: int | None = None) -> str:
        rows = items[:limit] if limit else items
        if not rows:
            return "_No candidates in this view._\n"
        out = ["| Priority | Repository | Work | Effort | Complexity | Impact | Confidence |", "|---:|---|---|---|---|---|---|"]
        for c in rows:
            out.append(f"| {c['priority']:.1f} | `{c['repository']}` | [{c['title']}]({c['url']}) | {c['effort']['bucket']} | {c['complexity']} | {c['project_goal_impact']} | {c['confidence']} |")
        return "\n".join(out) + "\n"

    by_leverage = sorted(ready, key=lambda x: (-x["leverage"], -x["priority"], x["repository"]))
    lines = [
        "---",
        "layout: default",
        "title: Portfolio Work Queue",
        "nav_order: 2",
        "---",
        "",
        "# Portfolio Work Queue",
        "",
        f"**Evidence snapshot:** {queue['generated_at']}  ",
        f"**Candidates:** {len(candidates)} · **Ready:** {len(ready)} · **Blocked/waiting:** {len(blocked)} · **Needs judgment:** {len(judgment)}",
        "",
        "> This is derived planning evidence, not project authority. Source repositories retain authority over goals, implementation and releases.",
        "",
        "## Work now",
        "",
        "Highest strategic-priority candidates that are currently classified as executable.",
        "",
        table(ready, 15),
        "## Highest leverage",
        "",
        "Ready candidates ranked by strategic priority per estimated effort.",
        "",
        table(by_leverage, 15),
        "## By available time",
        "",
    ]
    for bucket in config["effort_buckets"][:-1]:
        matching = [c for c in by_leverage if c["effort"]["minutes"] <= bucket["minutes"]]
        lines += [f"### {bucket['label']}", "", table(matching, 8)]
    lines += [
        "## Needs judgment",
        "",
        table(judgment),
        "## Blocked or waiting",
        "",
        table(blocked),
        "## Maintenance lane",
        "",
        table(maintenance),
        "## How ranking works",
        "",
        "Priority and effort are deliberately separate. See the [methodology](methodology.md) for authority boundaries, scoring, falsification rules and limitations.",
        "",
        "Machine-readable output: [`data/portfolio-work-queue.json`](../../data/portfolio-work-queue.json).",
        "",
    ]
    return "\n".join(lines)


def validate_queue(queue: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    last = float("inf")
    for c in queue.get("candidates", []):
        if c["id"] in ids:
            errors.append(f"duplicate candidate id: {c['id']}")
        ids.add(c["id"])
        if c["priority"] > last:
            errors.append("candidate ordering is not deterministic descending priority")
        last = c["priority"]
        if c["state"] == "ready" and c["complexity"] == "consequential":
            errors.append(f"consequential candidate cannot be ready: {c['id']}")
        if c["state"] in {"blocked", "waiting-external"} and c["priority"] >= 80:
            errors.append(f"blocked candidate retained implausibly high priority: {c['id']}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", type=Path, help="Read GitHub evidence from a JSON fixture/snapshot.")
    parser.add_argument("--check", action="store_true", help="Validate generation without writing output.")
    parser.add_argument("--output-json", type=Path, default=DEFAULT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_MD)
    args = parser.parse_args()

    registry, config = load_yaml(REGISTRY), load_yaml(CONFIG)
    eligible = eligible_repositories(registry, config)
    if args.offline:
        evidence = json.loads(args.offline.read_text(encoding="utf-8"))
    else:
        try:
            evidence = collect_live(eligible, os.getenv("GITHUB_TOKEN"))
        except (urllib.error.URLError, TimeoutError) as exc:
            print(f"live evidence collection failed: {exc}", file=sys.stderr)
            return 2

    queue = build_queue(registry, config, evidence)
    errors = validate_queue(queue)
    if errors:
        print("Portfolio Work Queue validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if args.check:
        print(f"Portfolio Work Queue validation passed: {len(queue['candidates'])} candidates")
        return 0

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(queue, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    args.output_md.write_text(render_markdown(queue, config), encoding="utf-8")
    print(f"Wrote {len(queue['candidates'])} candidates to {args.output_json} and {args.output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
