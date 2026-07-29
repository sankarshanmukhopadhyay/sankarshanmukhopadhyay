---
layout: default
title: Operations
parent: Portfolio Assurance Monitor
nav_order: 3
---

# Monitor operations

## Scheduled execution

`.github/workflows/portfolio-assurance-monitor.yml` runs every Monday and may also be started manually. The workflow validates the portfolio, executes the monitor, runs tests, publishes the generated evidence as a workflow artefact, and commits changed assurance reports to the repository.

## Local validation

```bash
pip install pyyaml
python scripts/validate_portfolio.py
python scripts/portfolio_assurance_monitor.py --offline --check
python -m unittest discover -s tests -p 'test_*.py'
```

## Live execution

```bash
GITHUB_TOKEN="..." python scripts/portfolio_assurance_monitor.py
```

The standard GitHub Actions token is sufficient for the initial public-evidence profile. Broader permissions must not be added unless a documented evidence requirement justifies them.

## Generated outputs

- `reports/portfolio-assurance/latest.md`: latest human-readable assessment;
- `reports/portfolio-assurance/latest-findings.json`: current observations and findings;
- `reports/portfolio-assurance/history/YYYY-MM-DD.md`: dated report history;
- `docs/portfolio-assurance/dashboard.md`: GitHub Pages dashboard.

## Failure behaviour

A repository collection failure becomes evidence and normally produces a `REPOSITORY_UNAVAILABLE` finding. The workflow should fail only for defects in monitor execution, validation, tests, or report generation. A portfolio finding is not itself a CI failure because it requires governed disposition.

## Revocation and enforcement

The monitor has no authority to change portfolio tier, maturity, lifecycle, disposition, or authority scope. Any future automatic effect must be introduced through an explicit policy change, test coverage, documentation, and reviewed commit.
