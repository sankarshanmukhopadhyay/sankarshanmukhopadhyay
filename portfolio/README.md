# Portfolio Governance Control Surface

This directory is the operational control surface for managing the repositories described by this GitHub profile.

It does **not** turn the portfolio into a monorepo. Each project retains its own release authority, versioning, schemas, tests, and maintainership. This directory records cross-repository relationships, release impact, drift obligations, and the evidence needed to justify coordinated changes.

## Source of truth

| Concern | Canonical location |
|---|---|
| Repository and relationship graph | [`../data/portfolio-relationships.yaml`](../data/portfolio-relationships.yaml) |
| Portfolio architecture | [`architecture.md`](architecture.md) |
| Drift review procedure | [`drift-review.md`](drift-review.md) |
| Adoption readiness gate | [`adoption-checklist.md`](adoption-checklist.md) |
| Release-impact template | [`release-impact-template.md`](release-impact-template.md) |
| Release-impact records | [`release-impact/`](release-impact/) |
| Version and change history | [`VERSION`](VERSION) and [`CHANGELOG.md`](CHANGELOG.md) |
| Release evidence | [`releases/`](releases/) |
| Path migration guidance | [`MIGRATION.md`](MIGRATION.md) |

## Operating workflow

1. **Identify the initiating repository.** Record which repository owns the proposed semantic, schema, assurance, conformance, or adoption change.
2. **Inspect declared relationships.** Use `data/portfolio-relationships.yaml` to identify affected repositories and review triggers.
3. **Create a release-impact record.** Copy `release-impact-template.md` or add a machine-readable YAML record under `release-impact/`.
4. **Preserve authority boundaries.** A research or artifact repository may inform TSMM or TIS, but it does not silently redefine their canonical semantics or contracts.
5. **Run validation.** Execute `python scripts/validate_portfolio.py` locally. The same gate runs in GitHub Actions.
6. **Publish evidence.** Add release notes, validation evidence, and commit metadata under `releases/<version>/`.
7. **Review downstream drift.** Close the coordinated release only after every triggered repository records an explicit outcome: changed, reviewed with no change, or deferred with rationale.

## Release directory convention

```text
portfolio/
├── README.md
├── VERSION
├── CHANGELOG.md
├── architecture.md
├── drift-review.md
├── adoption-checklist.md
├── release-impact-template.md
├── release-impact/
│   └── <version>-<initiative>.yaml
└── releases/
    └── <version>/
        ├── release-notes.md
        ├── validation-evidence.md
        └── commit-metadata.md
```

## Validation

```bash
python scripts/validate_portfolio.py
```

The validator checks that:

- the portfolio relationship YAML parses;
- repository identifiers are unique;
- relationship endpoints resolve to registered repositories;
- relationship types are declared;
- release-impact records parse and contain required release metadata;
- required governance documents exist;
- local Markdown links resolve.

## Change classification

| Change | Expected handling |
|---|---|
| Editorial profile update | Root README only; no portfolio release required |
| Repository description or link update | Update relationship registry when identity or role changes |
| New repository | Register it, classify its authority, and add relevant relationships |
| Semantic-model change | Review TSMM dependants and drift-sensitive repositories |
| Schema-contract change | Review TIS consumers, fixtures, and conformance tooling |
| Coordinated portfolio increment | Add release-impact record and versioned release evidence |

## Current release

The current portfolio-governance release is **v0.2.0**, which registers Trust Graph Artifacts and records the coordinated delegation-lineage increment across TGA, TSMM, and TIS.
