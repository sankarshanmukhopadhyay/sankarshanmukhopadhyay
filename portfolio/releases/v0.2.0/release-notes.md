# Profile Portfolio Governance v0.2.0

## Why this release matters

The GitHub profile repository already acted as the narrative index for a federated trust-infrastructure portfolio, while its portfolio-governance files were spread across the repository and difficult to release, validate, or maintain as one controlled unit.

This release integrates the Repository Portfolio Change Management v0.2.0 increment into the profile repository as a dedicated governance control surface. It also registers Trust Graph Artifacts and records the coordinated delegation-lineage changes across TGA, TSMM, and TIS.

## What changed

### Manageable governance structure

- Added `portfolio/README.md` as the maintainer entry point.
- Consolidated architecture, drift review, adoption gates, release-impact records, version history, release notes, validation evidence, and commit metadata under `portfolio/`.
- Retained `data/portfolio-relationships.yaml` as the stable machine-readable source of truth.
- Replaced former `docs/` copies with compatibility pointers so existing links continue to resolve without creating duplicate sources of truth.

### Automated release gate

- Added `scripts/validate_portfolio.py`.
- Added `.github/workflows/validate-portfolio.yml`.
- Validation now checks registry integrity, declared relationship types, registered relationship endpoints, release-impact metadata, required governance documents, and local Markdown links.

### Portfolio model update

- Registered Trust Graph Artifacts as the governance-research-to-executable-artifact incubation layer.
- Added explicit TGA influence and drift-review relationships with TSMM and TIS.
- Added a completed release-impact record for the delegation-lineage increment.

### Profile adoption improvements

- Added TGA to the visible ecosystem map and portfolio map.
- Added a dedicated executable-governance adoption path.
- Added a “Managing the portfolio” section with the canonical workflow and validation command.

## Authority and scope

This repository coordinates cross-repository review. It does not become a monorepo and does not supersede the release authority of individual repositories.

- TSMM remains authoritative for canonical semantic models.
- TIS remains authoritative for portable schema contracts.
- TGA incubates executable governance patterns and assurance cases.
- Operational repositories retain ownership of implementations, conformance behavior, and release decisions.

## Compatibility

This release is additive. Existing links to:

- `docs/portfolio-architecture.md`
- `docs/portfolio-drift-review.md`
- `docs/release-impact-template.md`
- `data/portfolio-relationships.yaml`

continue to work. The three legacy Markdown paths now direct maintainers to their canonical files under `portfolio/`.

## Validation

```bash
python scripts/validate_portfolio.py
```

Expected result:

```text
Portfolio governance validation passed.
```

## Maintainer outcome

A coordinated portfolio increment can now be managed through one repeatable path:

1. identify the initiating repository;
2. inspect declared dependencies and drift triggers;
3. record release impact;
4. preserve repository authority boundaries;
5. run automated validation;
6. publish release and assurance evidence;
7. close downstream review outcomes explicitly.
