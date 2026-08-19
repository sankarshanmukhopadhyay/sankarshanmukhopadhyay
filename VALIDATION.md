# Validation Evidence

Validation date: 2026-08-19

## Commands

```bash
python -m unittest discover -s tests -p 'test_*.py'
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
# JSON Schema validation of generated remediation dossiers
```

## Results

- Monitor and validation test suite passed: 27 tests.
- Portfolio validation passed: 37 classified repositories, 40 lightweight account dispositions, 33 authority scopes, 34 relationships.
- Internal link validation passed: 80 Markdown files checked.
- Site navigation validation passed: 8 unique visible titles checked.
- 37 generated repository remediation dossier JSON files validated against `portfolio-finding-feed.schema.json`.

## Remediation handoff validation

The test suite verifies that repository remediation dossiers contain explicit assessment dimensions, remediation objectives, acceptance criteria, verification guidance, and repository snapshot provenance fields. It also verifies fail-closed handling when required status or workflow evidence cannot be observed, and lifecycle transition from an open stable fingerprint to a recorded resolved state when a later run no longer observes the condition.

Generated dashboard and dossier pages in this commit were refreshed from the last stored **live** observation snapshot (`2026-08-17T03:14:24Z`), not from offline synthetic evidence. The next live workflow run will populate the newly collected default-branch commit SHA.

## GitHub Pages link validation contract

The internal-link validator distinguishes repository source paths from GitHub Pages build outputs. A relative link to `page.html` is valid when either `page.html` exists directly or a corresponding `page.md` source exists for Jekyll to render. A `.html` link with neither a rendered file nor a Markdown source remains a validation failure.

This preserves publication-facing `.html` URLs in generated portfolio assurance reports without requiring generated Jekyll output to be committed to the repository.

## Build environment limitation

A local Jekyll build was not executed because Bundler is not installed in the packaging environment. The existing GitHub Actions Pages workflow remains the authoritative rendered-site build check.

## Public portfolio discoverability

`validate_portfolio.py` also enforces a portfolio discoverability invariant: every repository whose canonical disposition makes it a `portfolio_member: true` must be named on at least one designated public portfolio surface (`README.md`, `docs/portfolio-status.md`, or `portfolio/architecture.md`). This prevents a governed member from silently disappearing from public navigation while preserving the curated boundary.

This local invariant is distinct from GitHub account discovery. Account discovery may report repositories that have no disposition, but it must never auto-enrol or auto-classify them.
