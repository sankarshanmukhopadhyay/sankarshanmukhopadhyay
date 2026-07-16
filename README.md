# Sankarshan Mukhopadhyay

### Building executable governance, authority-control planes, and assurance infrastructure

I design specifications, protocols, schemas, conformance systems, and reference implementations for digital trust and agentic systems. The work focuses on making authority, delegation, constraints, revocation, evidence, accountability, and redress explicit enough to be implemented, tested, audited, and independently challenged.

> **Core premise:** trust becomes infrastructure only when authority, constraints, revocation, evidence, and redress are operational, enforceable, and independently verifiable.

[![Portfolio validation](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml)
[![Portfolio documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0969da)](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

## Start here

| You are trying to… | Begin with | Provenance |
|---|---|---|
| Model authority, delegation, revocation, accountability, or remedy | [Governance, Authority and Assurance Metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | Original portfolio work |
| Analyse the semantics of a trust system | [Trust Systems Meta Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Original portfolio work |
| Implement portable trust records or evidence contracts | [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Original portfolio work |
| Deploy or evaluate an agent registry | [Agent Registry Protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | Original portfolio work |
| Test or assure a trust-registry deployment | [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Original multi-repository work |
| Examine ZKP implementation and interoperability boundaries | [DTG ZKP Task Force fork](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) | Upstream-derived collaborative work |
| Review governed digital-trust terminology | [CTWG Main Glossary fork](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary) | Upstream-derived collaborative work |
| Examine agent-transfer protocol implementation and hardening | [AGTP fork](https://github.com/sankarshanmukhopadhyay/agtp) | Upstream-derived collaborative work |

## Flagship original work

| Repository | What it delivers | Portfolio role | Maturity |
|---|---|---|---|
| [**Governance, Authority and Assurance Metamodel**](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | A normative model for authority, delegation, revocation, evidence, assurance, accountability, appeal, and remedy | Executable-governance foundation | Candidate specification |
| [**Agent Registry Protocol**](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | A modular protocol, schemas, APIs, conformance system, and reference implementation for agent authority-control planes | Agent registry architecture | Community draft |
| [**Trust Systems Meta Model**](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Canonical concepts for analysing actors, authority, policy, evidence, decisions, and effects | Semantic foundation | Evolving specification |
| [**Trust Infrastructure Schemas**](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Portable machine-readable contracts for trust actors, claims, bindings, relationships, and governance evidence | Schema foundation | Implementable artefacts |
| [**Trust Graph Artifacts**](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) | Applied governance patterns, implementation guidance, failure models, and negative-assurance tests | Applied governance laboratory | Active |
| [**TRQP Assurance Stack**](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | A coordinated security-profile, verifier, conformance, and evidence workflow for trust-registry deployments | Registry assurance system | Multi-repository stack |

## Featured upstream and collaborative work

The following repositories are forks of upstream projects. They are included because the portfolio forks contain implementation guidance, assurance artefacts, documentation refinements, tests, or other contribution-oriented work.

Fork inclusion does not imply authorship of the upstream project, control over its governance or releases, upstream endorsement, or adoption of fork-specific material.

| Repository fork | Upstream | Work represented in this portfolio |
|---|---|---|
| [**DTG ZKP Task Force**](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) | [Trust Over IP upstream](https://github.com/trustoverip/dtgwg-zkp-tf) | Implementation-guide development, assurance and disclosure boundaries, deployment guidance, conformance artefacts, and interoperability analysis |
| [**CTWG Main Glossary**](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary) | [Trust Over IP upstream](https://github.com/trustoverip/ctwg-main-glossary) | Terminology harmonisation, glossary extensions, cross-repository vocabulary analysis, documentation quality, and publication hardening |
| [**AGTP — Agent Transfer Protocol**](https://github.com/sankarshanmukhopadhyay/agtp) | [Nomotic AI upstream](https://github.com/nomoticai/agtp) | Security hardening, implementation refinement, deferred-work completion, validation, and release-oriented engineering performed in the fork |

## Portfolio lanes

### Governance, authority, and semantic foundations

[GAAM](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) defines normative authority and assurance structures. [TSMM](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) provides semantic analysis, [TIS](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) supplies portable contracts, and [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) develops applied patterns and failure tests. Informative alignment does not create a normative dependency.

### Agent infrastructure, delegation, and protocol enforcement

[Agent Registry Protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) addresses discovery, attribution, bounded authority, status, evidence, governance, and redress. Supporting work includes [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline), [ERC-8004 CSP](https://github.com/sankarshanmukhopadhyay/ERC-8004-CSP), and the upstream-derived [AGTP fork](https://github.com/sankarshanmukhopadhyay/agtp).

### Trust registries, conformance, and assurance

**Evidence path:** [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) → [reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) → [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) → [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub)

This path connects security requirements to executable tests, verifier output, retained provenance, and reviewable assurance conclusions. [DTG Conformance & Assurance](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance) supplies reusable assurance methods.

### Privacy-preserving proofs and interoperability

The [DTG ZKP Task Force fork](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) contains contribution-oriented implementation and interoperability work, including predicate, disclosure, and assurance-boundary analysis. The upstream project retains governance and release authority.

### Applied systems and research

- [**KiranaOS**](https://github.com/sankarshanmukhopadhyay/kiranaos): an applied operations platform developed through staged, testable releases.
- [**Digital Governance Paper Notes**](https://github.com/sankarshanmukhopadhyay/digital-governance-paper-notes): structured governance-first reviews of research and policy papers.
- [**DPI AI Governance Lab**](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab): applied exploration of governance controls for AI-enabled public infrastructure.

## How the repositories fit together

```text
                         GOVERNANCE AND AUTHORITY
                Governance, Authority and Assurance Metamodel
                                      │
                    normative rules, profiles, and controls
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
 SEMANTIC FOUNDATION          MACHINE CONTRACTS             APPLIED PATTERNS
 Trust Systems Meta Model     Trust Infrastructure Schemas  Trust Graph Artifacts
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      │
                         DOMAIN AND PROTOCOL SYSTEMS
                Agent Registry Protocol · TRQP · ZKP · AGTP
                                      │
                     tests, implementations, and validators
                                      │
                       CONFORMANCE AND ASSURANCE
          suites · reference verifiers · evidence · review conclusions
```

Portfolio inclusion does not create normative dependency. Relationships are classified as normative dependency, profile adoption, informative alignment, evidence production, reference implementation, incubation, or fork provenance.

## Repository provenance and authority

An **original portfolio repository** is governed and released within this portfolio unless its own governance documentation states otherwise.

A **fork** retains the provenance, licence, and upstream governance of its source project. Changes made in a fork apply only to that fork unless accepted through the upstream project’s contribution and decision process. A fork’s inclusion here does not imply upstream endorsement, maintainership, normative authority, or adoption.

The profile repository maintains portfolio classification and relationship metadata. It does **not** override the governance, normative authority, or release decisions of individual projects or upstream repositories.

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

A successful run verifies declared provenance, upstream references for forks, governed maturity and relationship values, authority uniqueness, adoption-path resolution, review dates, and internal documentation links. It does not certify member repositories, upstream projects, interoperability, or independent assurance.

## Research and writing

I publish **[The Trust Graph](https://thetrustgraph.substack.com)**, where architectural and governance questions are developed in long form before, alongside, or after their expression as specifications and executable artefacts.

Essays develop arguments, failure models, and institutional implications. Specifications establish governed terminology and requirements. Schemas encode portable contracts. Tests and reference implementations expose whether claims survive execution.

[LinkedIn](https://www.linkedin.com/in/sankarshan) · [About](https://about.me/sankarshan.mukhopadhyay/)

## Collaboration

Useful collaboration begins with a concrete deployment, interoperability, or assurance problem. Open an issue describing the operating context, authority model, constraints, expected evidence, provenance boundary, and a testable definition of done.
