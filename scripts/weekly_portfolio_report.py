#!/usr/bin/env python3
"""Weekly contribution events; observational, never an assertion of upstream authority."""
import argparse
import json
import re
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
FIRST_OPERATIONAL_WEEK = date(2026, 10, 26)  # October 1-25 is curated backfill.
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
    # GitHub issue search shares its endpoint with PRs. Specify a positive
    # issue type and an explicit PR exclusion; never infer zero issue events
    # from a PR-only response to an issue query.
    kind_filter = "type:issue -is:pr" if kind == "issue" else "is:pr"
    q = f"author:{AUTHOR} {kind_filter} {event}:{start}..{end - timedelta(days=1)}"
    results = []
    for page in range(1, 12):
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
            {"q": q, "sort": "created" if event == "created" else "updated",
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
        # GitHub's issue-search endpoint returns PRs and issues in one wire
        # format. An empty but present pull_request object is still a PR.
        # Validate against the canonical browser path before classification.
        url = item.get("html_url", "")
        path = urllib.parse.urlparse(url).path.split("/")
        if len(path) != 5 or path[3] not in ("pull", "issues") or not path[4].isdigit():
            raise RuntimeError(f"Unrecognized GitHub search result URL: {url!r}")
        url_kind = "pull-request" if path[3] == "pull" else "issue"
        actual_kind = "pull-request" if item.get("pull_request") is not None else "issue"
        if actual_kind != url_kind:
            raise RuntimeError(f"Contradictory kind metadata for GitHub result: {url}")
        if actual_kind != kind:
            # This indicates that the type-filtered source query cannot
            # establish completeness. Do not publish a zero-filled report.
            raise RuntimeError(
                f"Cross-kind GitHub search response for {kind}/{event}: "
                f"returned {actual_kind} at {url}"
            )
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


def missing_completed_weeks(today):
    """Return fully absent weeks; never silently overwrite partial evidence."""
    _, end = last_week(today)
    weeks = []
    start = FIRST_OPERATIONAL_WEEK
    while start < end:
        md, ledger = output_paths(start)
        if md.exists() != ledger.exists():
            raise RuntimeError(f"Partial weekly archive for {start}: Markdown/JSON disagree")
        if not md.exists():
            weeks.append(start)
        start += timedelta(days=7)
    return weeks


def update_archive_index():
    """Synchronize visible navigation from existing report artifacts."""
    index = ROOT / "docs/weekly-reports/index.md"
    text = index.read_text(encoding="utf-8")
    begin = "<!-- BEGIN GENERATED WEEKLY REPORT INDEX -->"
    finish = "<!-- END GENERATED WEEKLY REPORT INDEX -->"
    files = sorted((ROOT / "docs/weekly-reports").glob("[0-9][0-9][0-9][0-9]/week-*.md"), reverse=True)
    operational = []
    for file in files:
        match = re.fullmatch(r"week-(\d{2})\.md", file.name)
        if not match:
            continue
        year = int(file.parent.name)
        week = int(match.group(1))
        start = date.fromisocalendar(year, week, 1)
        if start < FIRST_OPERATIONAL_WEEK:
            continue
        ledger = ROOT / "reports/weekly" / str(year) / f"week-{week:02d}.json"
        if not ledger.exists():
            raise RuntimeError(f"Report missing evidence ledger: {file}")
        end = start + timedelta(days=6)
        operational.append(f"- [{start.day} {start:%B}–{end.day} {end:%B %Y}]({year}/week-{week:02d}.html)")
    block = begin + "\n\n## Operational weekly reports\n\n" + (
        "\n".join(operational) if operational else "No operational reports have been published yet."
    ) + "\n\n" + finish
    if begin in text or finish in text:
        if text.count(begin) != 1 or text.count(finish) != 1:
            raise RuntimeError("Malformed generated weekly index markers")
        text = text[:text.index(begin)] + block + text[text.index(finish) + len(finish):]
    else:
        marker = "[Reporting methodology](methodology.md)"
        if text.count(marker) != 1:
            raise RuntimeError("Weekly archive has no unique insertion marker")
        text = text.replace(marker, block + "\n\n" + marker)
    index.write_text(text, encoding="utf-8")


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
              f"Evidence ledger: `reports/weekly/{y}/week-{w:02d}.json`.", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", help="UTC Monday of a completed week")
    parser.add_argument("--catch-up", action="store_true", help="Generate all missing completed operational weeks")
    parser.add_argument("--out-json", help="Explicit evidence output path for validation")
    parser.add_argument("--out-md", help="Explicit Markdown output path")
    args = parser.parse_args()
    today = datetime.now(timezone.utc).date()
    if args.catch_up and (args.start or args.out_json or args.out_md):
        parser.error("--catch-up cannot be combined with --start or explicit outputs")
    if args.catch_up:
        starts = missing_completed_weeks(today)
    elif args.start:
        start = date.fromisoformat(args.start)
        if start.weekday() or start + timedelta(days=7) > today:
            parser.error("Window must be a completed Monday-to-Monday UTC week")
        starts = [start]
    else:
        starts = [last_week(today)[0]]
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or ""
    if not token:
        raise RuntimeError("GitHub API token required; cannot claim complete evidence")
    for start in starts:
        end = start + timedelta(days=7)
        doc, ledger = output_paths(start)
        if not args.catch_up:
            if args.out_json:
                ledger = Path(args.out_json)
            if args.out_md:
                doc = Path(args.out_md)
        if doc.exists() != ledger.exists():
            raise RuntimeError(f"Partial weekly archive for {start}; refusing overwrite")
        if doc.exists():
            print("Existing archive not overwritten:", doc)
            continue
        evidence = collect(start, end, token)
        doc.parent.mkdir(parents=True, exist_ok=True)
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        doc.write_text(render(evidence), encoding="utf-8")
        print(f"Generated completed week: {start} to {end}")
    if not args.out_md and not args.out_json:
        update_archive_index()



if __name__ == "__main__":
    main()
