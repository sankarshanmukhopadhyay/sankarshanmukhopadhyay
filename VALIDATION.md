# Validation Evidence

Validation date: 2026-08-19

## Commands

```bash
python -m unittest discover -s tests -p 'test_*.py'
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
```

## Results

- Monitor and validation test suite passed: 23 tests.
- Portfolio validation passed: 37 classified repositories, 40 lightweight account dispositions, 33 authority scopes, 34 relationships.
- Internal link validation passed: 80 Markdown files checked.
- Site navigation validation passed: 8 unique visible titles checked.

## GitHub Pages link validation contract

The internal-link validator distinguishes repository source paths from GitHub Pages build outputs. A relative link to `page.html` is valid when either `page.html` exists directly or a corresponding `page.md` source exists for Jekyll to render. A `.html` link with neither a rendered file nor a Markdown source remains a validation failure.

This preserves publication-facing `.html` URLs in generated portfolio assurance reports without requiring generated Jekyll output to be committed to the repository.

## Build environment limitation

A local Jekyll build was not executed because Bundler is not installed in the packaging environment. The existing GitHub Actions Pages workflow remains the authoritative rendered-site build check.

## Public portfolio discoverability

`validate_portfolio.py` also enforces a portfolio discoverability invariant: every repository whose canonical disposition makes it a `portfolio_member: true` must be named on at least one designated public portfolio surface (`README.md`, `docs/portfolio-status.md`, or `portfolio/architecture.md`). This prevents a governed member from silently disappearing from public navigation while preserving the curated boundary.

This local invariant is distinct from GitHub account discovery. Account discovery may report repositories that have no disposition, but it must never auto-enrol or auto-classify them.
