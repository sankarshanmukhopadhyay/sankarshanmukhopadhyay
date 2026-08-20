#!/usr/bin/env python3
"""Validate Jekyll navigation ownership and generated evidence isolation."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if ":" not in raw_line or raw_line.startswith((" ", "\t")):
            continue
        key, value = raw_line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def markdown_pages() -> list[Path]:
    excluded_roots = {"vendor", "node_modules", ".git"}
    return [
        path for path in ROOT.rglob("*.md")
        if not excluded_roots.intersection(path.relative_to(ROOT).parts)
    ]


def main() -> int:
    errors: list[str] = []
    visible_titles: dict[str, list[Path]] = defaultdict(list)

    for path in markdown_pages():
        metadata = parse_front_matter(path)
        title = metadata.get("title")
        if title and metadata.get("nav_exclude", "false").lower() != "true":
            visible_titles[title].append(path.relative_to(ROOT))

    for title, paths in sorted(visible_titles.items()):
        if len(paths) > 1:
            errors.append(f"Duplicate visible navigation title {title!r}: {', '.join(map(str, paths))}")

    canonical_home = parse_front_matter(ROOT / "index.md")
    if canonical_home.get("permalink") != "/" or canonical_home.get("nav_exclude") != "true":
        errors.append("index.md must be the canonical / page and excluded from duplicate sidebar navigation")

    dashboard = parse_front_matter(ROOT / "docs/portfolio-assurance/dashboard.md")
    if dashboard.get("parent") != "Portfolio Assurance Monitor" or dashboard.get("nav_order") != "1":
        errors.append("The canonical dashboard must be the first child of Portfolio Assurance Monitor")

    evidence_paths = [ROOT / "reports/portfolio-assurance/latest.md", *sorted((ROOT / "reports/portfolio-assurance/history").glob("*.md"))]
    for path in evidence_paths:
        metadata = parse_front_matter(path)
        if metadata.get("nav_exclude") != "true" or metadata.get("search_exclude") != "true":
            errors.append(f"Generated evidence must be excluded from navigation and search: {path.relative_to(ROOT)}")
        if metadata.get("title") == "Portfolio Assurance Dashboard":
            errors.append(f"Generated evidence must use a dated report title: {path.relative_to(ROOT)}")

    if errors:
        print("Site navigation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Site navigation validation passed: {len(visible_titles)} unique visible titles checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
