#!/usr/bin/env python3
"""Generate a review-only weekly GitHub portfolio activity report."""
import argparse
import json
import os
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNERS = ("sankarshanmukhopadhyay", "qbf-consulting")


def last_week(today):
    end = today - timedelta(days=today.weekday())
    return end - timedelta(days=7), end


def collect(owner, start, end, token):
    query = f"{'user' if owner == OWNERS[0] else 'org'}:{owner} author:sankarshanmukhopadhyay is:pull-request merged:{start}..{end - timedelta(days=1)}"
    items = []
    for page in range(1, 12):
        url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": query, "per_page": 100, "page": page})
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "weekly-portfolio-report"}
        if token:
            headers["Authorization"] = "Bearer " + token
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40) as response:
            payload = json.load(response)
        if payload.get("incomplete_results") or payload["total_count"] > 1000:
            raise RuntimeError("Incomplete GitHub search; refusing report")
        items += payload["items"]
        if len(items) >= payload["total_count"]:
            break
    else:
        raise RuntimeError("GitHub pagination limit reached")
    if len(items) != payload["total_count"]:
        raise RuntimeError("Incomplete pagination")
    records = []
    for p in items:
        stamp = (p.get("pull_request") or {}).get("merged_at")
        if not stamp:
            raise RuntimeError("Missing merge timestamp")
        observed = datetime.fromisoformat(stamp.replace("Z", "+00:00")).date()
        if start <= observed < end:
            records.append({"repository": p["repository_url"].split("/repos/")[1],
                            "number": p["number"], "title": p["title"], "url": p["html_url"],
                            "merged_at": stamp})
    return records


def produce(start, end, evidence):
    year, week, _ = start.isocalendar()
    base = ROOT / "docs/weekly-reports" / str(year) / f"week-{week:02d}.md"
    audit = ROOT / "reports/weekly" / str(year) / f"week-{week:02d}.json"
    if base.exists() or audit.exists():
        print("Existing week not overwritten:", base.relative_to(ROOT))
        return False
    records = evidence["records"]
    counts = Counter(x["repository"] for x in records)
    lines = ["---", "layout: default", f"title: Week {week:02d} ({start})",
             "parent: Weekly Portfolio Reports", "---", "",
             f"# Week {week:02d} — Portfolio activity and evidence review", "",
             f"**{start} to {end - timedelta(days=1)} (UTC)**", "",
             f"**{len(records)} author-attributed merged PRs** across {len(counts)} repositories.", "",
             "> **Deterministic draft:** human review must add bounded outcome analysis before merge.",
             "", "## Repository activity", "", "| Repository | Merged PRs |", "|---|---:|"]
    for repo, count in sorted(counts.items(), key=lambda p: (-p[1], p[0])):
        lines.append(f"| [{repo}](https://github.com/{repo}) | {count} |")
    if not records:
        lines.append("| No observed PR merges in scanned scope | 0 |")
    lines += ["", "## Representative merged changes", ""]
    for repo, _ in sorted(counts.items(), key=lambda p: (-p[1], p[0]))[:10]:
        lines.append(f"### {repo}")
        for p in [x for x in records if x["repository"] == repo][-5:]:
            title = p["title"].replace("[", r"\[").replace("]", r"\]")
            lines.append(f"- [#{p['number']}: {title}]({p['url']})")
        lines.append("")
    lines += ["## Interpretation and limitations", "",
              "Observed merge events are not independent assurance, interoperability, test execution or production readiness. This report excludes upstream-owned repositories, private activity, collaborator-authored PRs and direct pushes. Missing evidence must not imply success.",
              "", "[Methodology](../methodology.md).", "",
              f"Evidence: \`reports/weekly/{year}/week-{week:02d}.json\`.", ""]
    base.parent.mkdir(parents=True, exist_ok=True)
    audit.parent.mkdir(parents=True, exist_ok=True)
    base.write_text("\n".join(lines), encoding="utf-8")
    audit.write_text(json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", help="Completed UTC week start, Monday YYYY-MM-DD")
    args = parser.parse_args()
    today = datetime.now(timezone.utc).date()
    if args.start:
        start = date.fromisoformat(args.start)
        end = start + timedelta(days=7)
        if start.weekday() != 0 or end > today:
            parser.error("Week must start on Monday and be complete")
    else:
        start, end = last_week(today)
    token = os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or ""
    records = sorted([x for owner in OWNERS for x in collect(owner, start, end, token)],
                     key=lambda x: (x["merged_at"], x["repository"], x["number"]))
    ids = [(p["repository"], p["number"]) for p in records]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Duplicate PR identities")
    evidence = {"schema_version": "1.0", "kind": "derived-activity",
                "start_inclusive_utc": str(start), "end_exclusive_utc": str(end),
                "owners": OWNERS, "author": "sankarshanmukhopadhyay",
                "count": len(records), "records": records,
                "assurance_claim": "none"}
    produce(start, end, evidence)


if __name__ == "__main__":
    main()
