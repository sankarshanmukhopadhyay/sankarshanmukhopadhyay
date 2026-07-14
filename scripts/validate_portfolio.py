#!/usr/bin/env python3
"""Validate the profile repository's portfolio-governance control surface."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RELATIONSHIPS = ROOT / "data" / "portfolio-relationships.yaml"
PORTFOLIO = ROOT / "portfolio"
REQUIRED = [
    PORTFOLIO / "README.md",
    PORTFOLIO / "VERSION",
    PORTFOLIO / "CHANGELOG.md",
    PORTFOLIO / "architecture.md",
    PORTFOLIO / "drift-review.md",
    PORTFOLIO / "adoption-checklist.md",
    PORTFOLIO / "release-impact-template.md",
]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - defensive CLI path
        fail(f"cannot parse {path.relative_to(ROOT)}: {exc}")


def validate_registry() -> None:
    data = load_yaml(RELATIONSHIPS)
    if not isinstance(data, dict):
        fail("portfolio relationship registry must be a mapping")
    repositories = data.get("repositories", [])
    relationships = data.get("relationships", [])
    relationship_types = data.get("relationship_types", {})
    ids = [item.get("id") for item in repositories if isinstance(item, dict)]
    if not ids or any(not item for item in ids):
        fail("every repository requires a non-empty id")
    if len(ids) != len(set(ids)):
        fail("repository ids must be unique")
    known = set(ids)
    for index, relationship in enumerate(relationships):
        if not isinstance(relationship, dict):
            fail(f"relationship {index} must be a mapping")
        source = relationship.get("source")
        target = relationship.get("target")
        kind = relationship.get("type")
        if source not in known or target not in known:
            fail(f"relationship {index} references an unregistered endpoint")
        if kind not in relationship_types:
            fail(f"relationship {index} uses undeclared type: {kind}")


def validate_release_impacts() -> None:
    for path in sorted((PORTFOLIO / "release-impact").glob("*.yaml")):
        data = load_yaml(path)
        if not isinstance(data, dict):
            fail(f"{path.relative_to(ROOT)} must be a mapping")
        serialized = path.read_text(encoding="utf-8")
        if "release" not in serialized.lower() or "version" not in serialized.lower():
            fail(f"{path.relative_to(ROOT)} lacks release/version metadata")


def validate_links() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository in {path.relative_to(ROOT)}: {target}")
            if not resolved.exists():
                fail(f"broken local link in {path.relative_to(ROOT)}: {target}")


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    validate_registry()
    validate_release_impacts()
    validate_links()
    print("Portfolio governance validation passed.")


if __name__ == "__main__":
    main()
