#!/usr/bin/env python3
"""Weekly contribution events; observational, never an assertion of upstream authority."""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "sankarshanmukhopadhyay"
OWNERS = ("sankarshanmukhopadhyay", "qbf-consulting")
KINDS = ("pull-request", "issue")
EVENTS = {"pull-request": ("created", "merged", "closed"), "issue": ("created", "closed")}


def last_week(today):
    end = today - timedelta(days=today.weekday())
    return end - timedelta(days=7), end


def source_fetch(url, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "portfolio-weekly-report/2",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40) as response:
        return json.load(response)


def search(kind, event, start, end, token, fetch=source_fetch):
    if kind not in EVENTS or event not in EVENTS[kind]:
        raise ValueError("Unknown type/event pair")
    # Search all GitHub organizations, including upstream; avoid owner restrictions.
    q = f"author:{AUTHOR} is:{kind} {event}:{start}..{end - timedelta(days=1)}"
    results = []
    for page in range(1, 12):
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "sort": event if event != "merged" else "updated",
             "per_page": 100, "page": page})
        payload = fetch(url, token)
        if payload.get("incomplete_results") or payload.get("total_count", 0) > 1000:
            raise RuntimeError(f"Incomplete GitHub {kind}/{event} search; cannot publish")
        batch = payload.get("items", [])
        results.extend(batch)
        if len(results) >= payload["total_count"]:
            break
        if not batch:
            raise RuntimeError("Search pagination ended before total_count")
    else:
        raise RuntimeError("Search result exceeded pagination limit")
    if len(results) != payload["total_count"]:
        raise RuntimeError("Search results truncated")

    start_utc = datetime.combine(start, datetime.min.time(), timezone.utc)
    end_utc = datetime.combine(end, datetime.min.time(), timezone.utc)
    events = []
    for item in results:
        actual_kind = "pull-request" if item.get("pull_request") else "issue"
        if actual_kind != kind:
            raise RuntimeError("Search returned mismatched record kind")
        if kind == "pull-request" and event == "merged":
            timestamp = item["pull_request"].get("merged_at")
        else:
            timestamp = item.get({"created": "created_at", "closed": "closed_at"}[event])
        if not timestamp:
            raise RuntimeError("Missing timestamp for reported event")
        when = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        if not (start_utc <= when < end_utc):
            continue
        full_repo = item["repository_url"].split("/repos/", 1)[1]
        owner = full_repo.split("/", 1)[0]
        # Closed-but-merged PR is represented solely by merged event.
        if kind == "pull-request" and event == "closed" and item["pull_request"].get("merged_at"):
            continue
        events.append({"key": f"github:{kind}:{full_repo}#{item['number']}:{event}",
                       "kind": kind, "event": event, "repository": full_repo,
                       "scope": "portfolio" if owner.lower() in OWNERS else "external",
                       "number": item["number"], "title": item["title"],
                       "url": item["html_url"], "occurred_at": timestamp})
    return events


def collect(start, end, token, fetch=source_fetch):
    events = [item for kind in KINDS for event in EVENTS[kind]
              for item in search(kind, event, start, end, token, fetch)]
    events.sort(key=lambda x: (x["occurred_at"], x["key"]))
    keys = [x["key"] for x in events]
    if len(keys) != len(set(keys)):
        raise RuntimeError("Duplicate GitHub lifecycle events")
    counts = Counter((x["scope"], x["kind"], x["event"]) for x in events)
    return {"schema_version": "2.0", "kind": "derived-weekly-contribution-events",
            "window": {"start_inclusive_utc": str(start), "end_exclusive_utc": str(end)},
            "author": AUTHOR, "collection_status": "complete",
            "source": "GitHub public issue search; event timestamps rechecked in UTC",
            "counts": {"|".join(k): v for k, v in sorted(counts.items())},
            "events": events, "limitations": [
                "Author-attributed PRs/issues only; comments, reviews, discussions, private content, direct pushes and GitLab excluded",
                "GitHub event occurrence does not imply upstream acceptance or independent assurance",
                "Creation, merge and closure of one item count as distinct lifecycle events",
                "External contributions are not portfolio-governed outputs",
                "Historical report content remains unchanged; new events are a separately derived view"]}


def output_paths(start):
    y, w, _ = start.isocalendar()
    return ROOT / "docs/weekly-reports" / str(y) / f"week-{w:02d}.md", ROOT / "reports/weekly" / str(y) / f"week-{w:02d}.json"


def render(result):
    start = date.fromisoformat(result["window"]["start_inclusive_utc"])
    end = date.fromisoformat(result["window"]["end_exclusive_utc"])
    y, w, _ = start.isocalendar()
    ev = result["events"]
    lines = ["---", "layout: default", f"title: Week {w:02d} ({start})",
             "parent: Weekly Portfolio Reports", "---", "",
             f"# Week {w:02d} — Portfolio and external contribution activity", "",
             f"**{start} to {end - timedelta(days=1)} (UTC)**", "",
             "> **Deterministic draft.** Events establish activity, not impact or upstream acceptance. Add sourced editorial interpretation during review.", "",
             "## Lifecycle activity", "", "| Scope | PRs opened | PRs merged | PRs closed without merge | Issues opened | Issues closed |",
             "|---|---:|---:|---:|---:|---:|"]
    for scope in ("portfolio", "external"):
        values = [sum(x["scope"] == scope and x["kind"] == kind and x["event"] == event for x in ev)
                  for kind, event in (("pull-request", "created"), ("pull-request", "merged"),
                                      ("pull-request", "closed"), ("issue", "created"), ("issue", "closed"))]
        lines.append("| " + scope.capitalize() + " | " + " | ".join(map(str, values)) + " |")
    for scope in ("portfolio", "external"):
        lines += ["", f"## {'Maintained portfolio' if scope == 'portfolio' else 'External and upstream'} events", ""]
        grouped = {}
        for x in ev:
            if x["scope"] == scope:
                grouped.setdefault(x["repository"], []).append(x)
        if not grouped:
            lines.append("No authored lifecycle events observed in this scope.")
        for repo, items in sorted(grouped.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            lines += ["", f"### {repo}"]
            for x in items[:20]:
                lines.append(f"- **{x['kind']} {x['event']}**: [#{x['number']}]({x['url']}) — {x['title']}")
            if len(items) > 20:
                lines.append(f"- {len(items)-20} more events in the machine-readable ledger.")
    lines += ["", "## Evidence and interpretation limits", "",
              "These are events from GitHub Search, not independent implementation evidence. Reviews, comments, discussions, GitLab, private work and collaborator-authored activity are not covered. Upstream owners retain all governance and acceptance authority.",
              "", "[Reporting methodology](../methodology.md).",
              f"Evidence ledger: \`reports/weekly/{y}/week-{w:02d}.json\`.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", help="UTC Monday of a completed week")
    parser.add_argument("--out-json", help="Explicit evidence output path for validation")
    parser.add_argument("--out-md", help="Explicit Markdown output path")
    args = parser.parse_args()
    today = datetime.now(timezone.utc).date()
    if args.start:
        start = date.fromisoformat(args.start)
        end = start + timedelta(days=7)
        if start.weekday() or end > today:
            parser.error("Window must be a completed Monday-to-Monday UTC week")
    else:
        start, end = last_week(today)
    doc, ledger = output_paths(start)
    if args.out_json:
        ledger = Path(args.out_json)
    if args.out_md:
        doc = Path(args.out_md)
    if doc.exists() or ledger.exists():
        print("Existing archive not overwritten:", doc)
        return
    evidence = collect(start, end, os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or "")
    doc.parent.mkdir(parents=True, exist_ok=True)
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ledger.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    doc.write_text(render(evidence), encoding="utf-8")


if __name__ == "__main__":
    main()
