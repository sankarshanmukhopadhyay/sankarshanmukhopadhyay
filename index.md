---
layout: default
title: Trust Infrastructure Portfolio
permalink: /
---

# Trust Infrastructure Portfolio

A governed portfolio of interoperable projects spanning executable governance, trust-system architecture, machine-readable contracts, agent assurance, trust-registry conformance, reference implementations, and applied systems.

## Start here

| Problem | Recommended entry point |
|---|---|
| Model authority, evidence, and policy-governed decisions | [Trust Systems Meta Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) |
| Express reusable trust contracts | [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) |
| Turn governance into implementation patterns | [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) |
| Establish software-agent naming assurance | [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline) |
| Test trust-registry behavior | [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) |
| Produce trust-registry assurance evidence | [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) |

## Architecture

The portfolio follows a layered model:

```text
Canonical semantics
      ↓
Portable schemas
      ↓
Governance and assurance patterns
      ↓
Domain-specific profiles and protocols
      ↓
Reference implementations and tests
      ↓
Evidence bundles and assurance conclusions
```

Read the [portfolio architecture](docs/portfolio-architecture.md) for authority boundaries, dependencies, and adoption paths.

## Governance and evidence

- [Portfolio governance](GOVERNANCE.md)
- [Human-readable portfolio status](docs/portfolio-status.md)
- [Adoption readiness checklist](portfolio/adoption-checklist.md)
- [Portfolio drift review](portfolio/drift-review.md)
- [Release-impact evidence ledger](portfolio/release-impact/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## Machine-verifiable controls

The authoritative registries are maintained as YAML and validated in CI:

- [`data/repository-status.yaml`](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/blob/main/data/repository-status.yaml)
- [`data/portfolio-relationships.yaml`](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/blob/main/data/portfolio-relationships.yaml)

Run locally:

```bash
python -m pip install PyYAML
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
```
