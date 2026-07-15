#!/usr/bin/env python3
"""Validate relative Markdown links that should resolve inside the repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def normalize_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split(" ", 1)[0].strip("<>")
    if not target or target.startswith(SKIP_PREFIXES):
        return None
    target = unquote(target.split("#", 1)[0])
    if not target:
        return None
    return (source.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    markdown_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = normalize_target(source, match.group(1))
            if target is None:
                continue
            try:
                target.relative_to(ROOT)
            except ValueError:
                failures.append(f"{source.relative_to(ROOT)}: escapes repository: {match.group(1)}")
                continue
            if not target.exists():
                failures.append(f"{source.relative_to(ROOT)}: missing target: {match.group(1)}")

    if failures:
        print("Internal link validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Internal link validation passed: {len(markdown_files)} Markdown files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
