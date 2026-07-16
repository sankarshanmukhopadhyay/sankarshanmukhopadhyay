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
VALID_PROVENANCE = {"original", "fork", "mirror", "archived-import", "collaborative-host"}
VALID_GOVERNANCE = {"controlled", "shared", "fork-only", "none"}
VALID_ADOPTION = {"not-applicable", "not-proposed", "proposed", "partially-accepted", "accepted", "rejected", "not-asserted"}


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
        provenance = repo.get("provenance")
        if provenance not in VALID_PROVENANCE:
            errors.append(f"{name}: invalid provenance {provenance!r}")
        if repo.get("portfolio_governance") not in VALID_GOVERNANCE:
            errors.append(f"{name}: invalid portfolio_governance {repo.get('portfolio_governance')!r}")
        if repo.get("upstream_adoption_status") not in VALID_ADOPTION:
            errors.append(f"{name}: invalid upstream_adoption_status {repo.get('upstream_adoption_status')!r}")
        if not repo.get("maturity"):
            errors.append(f"{name}: missing maturity")
        if provenance == "fork":
            if not repo.get("upstream"):
                errors.append(f"{name}: fork must declare upstream")
            if repo.get("portfolio_governance") != "fork-only":
                errors.append(f"{name}: fork must use portfolio_governance 'fork-only'")
        elif repo.get("upstream"):
            errors.append(f"{name}: non-fork repository must not declare upstream")
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

    external = {item.get("name") for item in relationships.get("external_repositories", []) if isinstance(item, dict)}
    valid_relationship_types = set(relationships.get("relationship_types", []))
    fork_relationships: set[tuple[str, str]] = set()

    for item in relationships.get("relationships", []):
        if not isinstance(item, dict):
            errors.append("relationship entries must be mappings")
            continue
        source, target = item.get("from"), item.get("to")
        if source not in names:
            errors.append(f"relationship from references unknown repository {source!r}")
        if target not in names and target not in external:
            errors.append(f"relationship to references unknown repository {target!r}")
        rel_type = item.get("type")
        if not rel_type or not item.get("constraint"):
            errors.append(f"relationship {item!r} requires type and constraint")
        elif valid_relationship_types and rel_type not in valid_relationship_types:
            errors.append(f"relationship uses ungoverned type {rel_type!r}")
        if rel_type == "fork-of":
            fork_relationships.add((source, target))

    for repo in repos:
        if isinstance(repo, dict) and repo.get("provenance") == "fork":
            pair = (repo.get("name"), repo.get("upstream"))
            if pair not in fork_relationships:
                errors.append(f"{repo.get('name')}: missing matching fork-of relationship to {repo.get('upstream')}")

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
