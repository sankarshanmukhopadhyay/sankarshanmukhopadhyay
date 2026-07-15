# Sankarshan Mukhopadhyay

### Building executable governance, trust infrastructure, and assurance systems

I work at the intersection of **digital trust**, **agentic systems**, **verifiable data**, **registries**, and **conformance engineering**. My repositories translate governance claims into specifications, schemas, tests, evidence flows, and reference implementations that can be inspected and challenged in operation.

> **Core premise:** trust becomes infrastructure only when authority, constraints, revocation, evidence, and redress can be made operational and independently verified.

[![Portfolio validation](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml)
[![Portfolio documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0969da)](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

## Featured work

| Repository | What it delivers | Portfolio role |
|---|---|---|
| [**Trust Graph Artifacts**](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) | Practical governance patterns, implementation guidance, and negative-assurance tests | Executable-governance incubation |
| [**Trust Systems Meta Model**](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Canonical concepts for authority, evidence, policy-governed decisions, and effects | Semantic foundation |
| [**Trust Infrastructure Schemas**](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Portable machine-readable contracts for trust actors, claims, bindings, and relationships | Schema authority |
| [**Agent Name Assurance Baseline**](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline) | Assurance requirements for identifying and relying on software-agent names | Agent assurance baseline |
| [**TRQP Assurance Hub**](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Evidence-oriented assurance workflows for trust-registry deployments | Operational assurance |
| [**DTG Conformance & Assurance**](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance) | Reusable conformance and assurance methods for digital-trust systems | General assurance framework |

## Portfolio lanes

### Executable governance and delegated authority

Governance is treated as an execution problem: who holds authority, what may be delegated, how scope is constrained, how authority is revoked, and what evidence proves the resulting action was legitimate.

**Start with:** [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) → [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) → [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline)

### Trust registries, conformance, and assurance

This lane moves trust-registry implementations beyond protocol compliance toward repeatable testing, portable evidence, security profiling, and reviewable assurance conclusions.

**Adoption path:** [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) → [Reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) → [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) → [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub)

### Agentic systems and machine-readable trust

Identity alone is insufficient for software agents. The portfolio examines intelligible names, bounded mandates, delegation chains, operational constraints, revocation, and evidence that a relying party can verify.

**Related work:** [AGTP](https://github.com/sankarshanmukhopadhyay/agtp) · [ERC-8004 CSP](https://github.com/sankarshanmukhopadhyay/ERC-8004-CSP) · [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas)

### Applied systems and research

- [**KiranaOS**](https://github.com/sankarshanmukhopadhyay/kiranaos): an applied operations platform developed through staged, testable releases.
- [**Digital Governance Paper Notes**](https://github.com/sankarshanmukhopadhyay/digital-governance-paper-notes): structured governance-first reviews of research and policy papers.
- [**DTG ZKP Task Force**](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf): implementation and interoperability guidance for zero-knowledge proofs.

## How the repositories fit together

```text
Governance problem
        ↓
Canonical concepts            Trust Systems Meta Model
        ↓
Portable contracts            Trust Infrastructure Schemas
        ↓
Governance patterns           Trust Graph Artifacts
        ↓
Domain profiles               Agent / TRQP / ZKP projects
        ↓
Tests and reference systems   Conformance suites and implementations
        ↓
Portable evidence             Assurance conclusions and audit records
```

The profile repository maintains the portfolio’s classification and relationship metadata. It does **not** override the governance, normative authority, or release decisions of individual projects.

- [Explore the portfolio documentation](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
- [Review portfolio architecture](docs/portfolio-architecture.md)
- [Inspect the repository-status registry](data/repository-status.yaml)
- [Inspect cross-repository relationships](data/portfolio-relationships.yaml)
- [Review governance](GOVERNANCE.md)

## Verification

The portfolio control plane is machine-verifiable:

```bash
git clone https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay.git
cd sankarshanmukhopadhyay
python -m pip install PyYAML
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
```

These checks verify portfolio structure, authority uniqueness, adoption-path resolution, relationship integrity, review dates, and internal documentation links. Project-level conformance evidence remains the responsibility of each member repository.

## Writing and ecosystem work

I publish **The Trust Graph**, a long-form exploration of digital trust infrastructure, delegated authority, agentic systems, and governance-by-design.

[The Trust Graph](https://thetrustgraph.substack.com) · [LinkedIn](https://www.linkedin.com/in/sankarshan) · [About](https://about.me/sankarshan.mukhopadhyay/)

My work engages with Trust Over IP, LF Decentralized Trust, UN/CEFACT, and adjacent standards and implementation communities. The recurring objective is to connect policy intent to deployable controls and verifiable outcomes.

## Collaboration

Useful collaboration begins with a concrete deployment or assurance problem. Open an issue describing the operating context, authority model, constraints, expected evidence, and a testable definition of done.
