# Portfolio Drift Review

## Objective

Detect divergence between declared architecture and repository behavior before incompatible assumptions become embedded in releases.

## Review triggers

- a repository changes a canonical concept or schema;
- a dependency or adoption sequence changes;
- a repository is promoted, demoted, archived, or superseded;
- a coordinated capability is released;
- a quarterly portfolio review becomes due.

## Procedure

1. Run `python scripts/validate_portfolio.py`.
2. Compare authority claims against member repository governance files.
3. Confirm dependency references and documentation URLs.
4. Review overdue `next_review` dates.
5. Record cross-repository impact in `portfolio/release-impact/`.
6. Update both registries in the same commit when a relationship changes.

## Findings classification

| Severity | Meaning |
|---|---|
| Critical | Conflicting canonical authority or misleading assurance claim |
| High | Broken adoption path, unresolved compatibility, or expired flagship control |
| Medium | Stale documentation or unreviewed incubating scope |
| Low | Presentation or metadata inconsistency |
