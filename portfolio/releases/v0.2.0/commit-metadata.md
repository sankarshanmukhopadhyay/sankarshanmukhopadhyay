# GitHub commit metadata

## Commit title

```text
governance: integrate portfolio control surface and automated validation
```

## Commit message

```text
Integrate Repository Portfolio Change Management v0.2.0 into the GitHub
profile repository as a dedicated, maintainable governance control surface.

Consolidate portfolio architecture, drift review, adoption gates, release
impact records, version history, validation evidence, release notes, and
commit metadata under portfolio/. Retain data/portfolio-relationships.yaml
as the stable machine-readable source of truth and replace former docs/
copies with compatibility pointers to prevent duplicate maintenance and
broken inbound links.

Add Trust Graph Artifacts to the ecosystem and relationship model as the
portfolio's governance-research-to-executable-artifact incubation layer.
Record its influence and drift-sensitive relationships with TSMM and TIS,
and include the coordinated delegation-lineage release-impact evidence.

Add scripts/validate_portfolio.py and a scoped GitHub Actions workflow to
verify registry integrity, repository identifiers, relationship endpoints,
relationship types, release-impact metadata, required governance files,
and local documentation links.

Refresh the profile README with an executable-governance adoption path and
a clear maintainer entry point while preserving the independent release
authority of every portfolio repository.
```
