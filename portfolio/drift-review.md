# Portfolio Drift Review

## Objective

Detect divergence between declared architecture, repository provenance, and repository behaviour before incompatible or misleading claims become embedded in releases or profile presentation.

## Review triggers

- a repository changes a canonical concept or schema;
- a dependency, evidence path, or adoption sequence changes;
- a repository is promoted, demoted, archived, superseded, or converted to a fork classification;
- a fork changes upstream source, disposition, adaptation scope, or makes an upstream-adoption claim;
- a coordinated capability is released;
- a quarterly portfolio review becomes due.

## Procedure

1. Run `python scripts/validate_portfolio.py` and `python scripts/check_internal_links.py`.
2. Compare authority claims against member-repository governance files.
3. Confirm each fork's canonical upstream and matching `fork-of` relationship; for `adapted-upstream-work`, verify the fork-local authority scope and evidence-backed maturity.
4. Verify that fork-local descriptions do not imply upstream authorship, governance authority, release authority, endorsement, or adoption.
5. Confirm dependency references, evidence paths, documentation URLs, and review dates.
6. Compare the live public repository set against explicit portfolio dispositions and record newly detected repositories for review.
7. Record cross-repository impact in `portfolio/release-impact/`.
8. Update both registries in the same commit when provenance, authority, or relationships change.

## Findings classification

| Severity | Meaning |
|---|---|
| Critical | Conflicting canonical authority, false provenance, or misleading assurance or upstream-adoption claim |
| High | Broken adoption path, unresolved compatibility, missing fork upstream, or expired flagship control |
| Medium | Stale documentation, unreviewed scope, or incomplete relationship evidence |
| Low | Presentation or metadata inconsistency |
