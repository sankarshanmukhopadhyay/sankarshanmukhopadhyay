# Portfolio Governance Control Surface

This directory contains the human-readable controls used to govern the portfolio as a federation of original repositories and explicitly identified upstream forks.

## Control set

| Control | Purpose | Evidence |
|---|---|---|
| Repository status registry | Records tier, lifecycle, role, maturity, provenance, upstream, governance scope, and review dates | `data/repository-status.yaml` |
| Relationship registry | Records authority, dependencies, evidence paths, adoption sequence, and `fork-of` provenance | `data/portfolio-relationships.yaml` |
| Adoption checklist | Defines flagship admission and review gates | `portfolio/adoption-checklist.md` |
| Drift review | Detects contradictory authority, stale relationships, or ambiguous provenance | `portfolio/drift-review.md` |
| Release-impact ledger | Records cross-repository consequences | `portfolio/release-impact/` |
| Validator | Enforces minimum machine-verifiable controls | `scripts/validate_portfolio.py` |

## Validation

```bash
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
```

A passing result confirms structural consistency of this repository. It does not prove project-level conformance, certify an upstream project, or establish that fork-local work has been proposed or accepted upstream.
