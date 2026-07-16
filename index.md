---
layout: default
title: Trust Infrastructure Portfolio
permalink: /
---

# Trust Infrastructure Portfolio

A governed portfolio of original specifications, protocols, schemas, assurance systems, applied artefacts, and explicitly identified upstream forks.

## Start here

| Problem | Recommended entry point | Provenance |
|---|---|---|
| Model authority, delegation, revocation, and remedy | [Governance, Authority and Assurance Metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | Original |
| Analyse trust-system semantics | [Trust Systems Meta Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Original |
| Express reusable trust contracts | [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Original |
| Deploy an agent authority-control plane | [Agent Registry Protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | Original |
| Produce trust-registry assurance evidence | [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Original stack |
| Review ZKP implementation guidance | [DTG ZKP Task Force fork](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) | Upstream-derived |

## Architecture

```text
Governance and authority
        ↓
Semantics · machine contracts · applied patterns
        ↓
Domain protocols and profiles
        ↓
Implementations, tests, and validators
        ↓
Evidence and assurance conclusions
```

Forked repositories are governed only within the fork. Their upstream projects retain authorship, governance, and release authority.

Read the [portfolio architecture](docs/portfolio-architecture.md) and [human-readable status](docs/portfolio-status.md) for authority, provenance, dependencies, and adoption paths.

## Governance and evidence

- [Portfolio governance](GOVERNANCE.md)
- [Repository status registry](data/repository-status.yaml)
- [Relationship registry](data/portfolio-relationships.yaml)
- [Adoption readiness checklist](portfolio/adoption-checklist.md)
- [Portfolio drift review](portfolio/drift-review.md)
- [Release-impact evidence ledger](portfolio/release-impact/README.md)

## Machine-verifiable controls

```bash
python -m pip install PyYAML
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
```

A passing result confirms structural consistency, declared provenance, fork-to-upstream relationships, authority uniqueness, adoption-path integrity, review dates, and internal links. It does not certify member repositories or assert upstream adoption.
