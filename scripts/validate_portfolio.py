#!/usr/bin/env python3
"""Validate the machine-readable portfolio governance control surface."""
from __future__ import annotations

from datetime import date
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required: pip install PyYAML", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "data" / "repository-status.yaml"
REL = ROOT / "data" / "portfolio-relationships.yaml"
REQUIRED_FILES = [
    "README.md", "LICENSE", "GOVERNANCE.md", "CONTRIBUTING.md",
    "CHANGELOG.md", "ROADMAP.md", "portfolio/README.md",
    "portfolio/architecture.md", "portfolio/adoption-checklist.md",
    "portfolio/drift-review.md", "data/repository-status.yaml",
    "data/portfolio-relationships.yaml",
]
VALID_TIERS = {"flagship", "incubating", "historical", "upstream-fork", "unrelated"}
VALID_LIFECYCLES = {"active", "maintenance", "archived", "superseded"}


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = yaml.safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a mapping")
    return value


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    try:
        status = load(STATUS)
        relationships = load(REL)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    repos = status.get("repositories", [])
    if not isinstance(repos, list) or not repos:
        errors.append("repository-status.yaml must contain a non-empty repositories list")
        repos = []

    names: set[str] = set()
    scope_owners: dict[str, str] = {}
    today = date.today()
    for index, repo in enumerate(repos):
        label = f"repositories[{index}]"
        if not isinstance(repo, dict):
            errors.append(f"{label} must be a mapping")
            continue
        name = repo.get("name")
        if not name:
            errors.append(f"{label} missing name")
            continue
        if name in names:
            errors.append(f"duplicate repository: {name}")
        names.add(name)
        if repo.get("tier") not in VALID_TIERS:
            errors.append(f"{name}: invalid tier {repo.get('tier')!r}")
        if repo.get("lifecycle") not in VALID_LIFECYCLES:
            errors.append(f"{name}: invalid lifecycle {repo.get('lifecycle')!r}")
        if not repo.get("role"):
            errors.append(f"{name}: missing role")
        for field in ("last_portfolio_review", "next_review"):
            try:
                date.fromisoformat(str(repo[field]))
            except (KeyError, ValueError):
                errors.append(f"{name}: {field} must be an ISO date")
        try:
            next_review = date.fromisoformat(str(repo["next_review"]))
            if next_review < today and repo.get("lifecycle") == "active":
                errors.append(f"{name}: portfolio review overdue since {next_review}")
        except (KeyError, ValueError):
            pass
        for scope in repo.get("authority_scope", []):
            if scope in scope_owners:
                errors.append(f"authority scope {scope!r} claimed by both {scope_owners[scope]} and {name}")
            scope_owners[scope] = name

    authorities = relationships.get("authorities", {})
    for authority, owner in authorities.items():
        if owner not in names:
            errors.append(f"authority {authority!r} references unknown repository {owner!r}")

    for item in relationships.get("relationships", []):
        if not isinstance(item, dict):
            errors.append("relationship entries must be mappings")
            continue
        for endpoint in ("from", "to"):
            if item.get(endpoint) not in names:
                errors.append(f"relationship {endpoint} references unknown repository {item.get(endpoint)!r}")
        if not item.get("type") or not item.get("constraint"):
            errors.append(f"relationship {item!r} requires type and constraint")

    for path_name, path in relationships.get("adoption_paths", {}).items():
        if not isinstance(path, list) or len(path) < 2:
            errors.append(f"adoption path {path_name!r} must contain at least two repositories")
            continue
        unknown = [name for name in path if name not in names]
        if unknown:
            errors.append(f"adoption path {path_name!r} references unknown repositories: {unknown}")

    if errors:
        print("Portfolio validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Portfolio validation passed: {len(names)} repositories, {len(authorities)} authorities, "
          f"{len(relationships.get('relationships', []))} relationships.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
