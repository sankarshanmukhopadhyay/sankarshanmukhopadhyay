# Portfolio Governance Control Surface

This directory contains the human-readable controls used to govern the portfolio as a federated system.

## Control set

| Control | Purpose | Evidence |
|---|---|---|
| Repository status registry | Records tier, lifecycle, role, and review dates | `data/repository-status.yaml` |
| Relationship registry | Records authority, dependencies, and adoption sequence | `data/portfolio-relationships.yaml` |
| Adoption checklist | Defines flagship admission and review gates | `portfolio/adoption-checklist.md` |
| Drift review | Detects contradictory authority or stale relationships | `portfolio/drift-review.md` |
| Release-impact ledger | Records cross-repository consequences | `portfolio/release-impact/` |
| Validator | Enforces minimum machine-verifiable controls | `scripts/validate_portfolio.py` |

## Validation

```bash
python scripts/validate_portfolio.py
```

A passing result confirms structural consistency of this repository. It does not prove that every member repository currently satisfies its declared adoption or assurance level; that requires repository-level evidence and scheduled review.
