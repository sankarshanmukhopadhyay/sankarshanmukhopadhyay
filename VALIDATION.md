# Validation Evidence

Validation date: 2026-07-21

## Commands

```bash
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
```

## Results

- Portfolio validation passed: 32 classified repositories, 25 authority scopes, 25 relationships.
- Internal link validation passed: 26 Markdown files checked.
- Python syntax validation passed for `scripts/validate_portfolio.py`.

## Build environment limitation

A local Jekyll build was not executed because Bundler is not installed in the packaging environment. The existing GitHub Actions Pages workflow remains the authoritative rendered-site build check.

## Public portfolio discoverability

`validate_portfolio.py` also enforces a portfolio discoverability invariant: every repository whose canonical disposition makes it a `portfolio_member: true` must be named on at least one designated public portfolio surface (`README.md`, `docs/portfolio-status.md`, or `portfolio/architecture.md`). This prevents a governed member from silently disappearing from public navigation while preserving the curated boundary.

This local invariant is distinct from future GitHub account discovery. Account discovery may report repositories that have no disposition, but it must never auto-enrol or auto-classify them.
