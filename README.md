# Sankarshan Mukhopadhyay

## Building executable governance, authority-control planes, and assurance infrastructure

I design specifications, protocols, schemas, conformance systems, and reference implementations for digital trust and agentic systems. The work focuses on making authority, delegation, constraints, revocation, evidence, accountability, and redress explicit enough to be implemented, tested, audited, and independently challenged.

> **Core premise:** trust becomes infrastructure only when authority, constraints, revocation, evidence, and redress are operational, enforceable, and independently verifiable.

[![Portfolio validation](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml)
[![Portfolio documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0969da)](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
[![Code license: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Content license: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE-CONTENT)

This is a **curated body-of-work portfolio**, not an ownership inventory. Institutionally stewarded open-source and open-knowledge work is maintained through [QBF Consulting](https://github.com/qbf-consulting); this personal profile remains the body-of-work and relationship front door. Repository ownership identifies current stewardship, while authority over normative content remains repository-local.

**Terminology:** [Trust Infrastructure Glossary](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-glossary) · **Writing:** [The Trust Graph](https://thetrustgraph.substack.com/) · **Full portfolio status:** [Portfolio Status](docs/portfolio-status.md)

## Start here

Maturity below is derived from the canonical [data/repository-status.yaml](data/repository-status.yaml) registry and is validated in CI.

| If you are trying to… | Start with | Maturity |
|---|---|---|
| Design or assess a national or multi-sector digital trust framework | [Open National Digital Trust Framework](https://github.com/qbf-consulting/open-national-digital-trust-framework) | Stable |
| Model authority, delegation, revocation, accountability, appeal, or remedy | [Governance, Authority and Assurance Metamodel](https://github.com/qbf-consulting/governance-authority-assurance-metamodel) | Candidate |
| Analyse the semantics of a trust system | [Trust Systems Meta Model](https://github.com/qbf-consulting/trust-systems-meta-model) | Candidate |
| Implement portable trust records or evidence contracts | [Trust Infrastructure Schemas](https://github.com/qbf-consulting/trust-infrastructure-schemas) | Candidate |
| Deploy or evaluate an agent registry | [Agent Registry Protocol](https://github.com/qbf-consulting/agent-registry-protocol) | Pilot Ready |
| Determine whether an actor is permitted to act under mandate, evidence, policy, and time | [PolicyMesh](https://github.com/sankarshanmukhopadhyay/PolicyMesh) | Implementation Draft |
| Pressure-test a specification for harms, security weaknesses, and governance failure modes | [Risk, Harms and Privacy (RAHP) Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) | Stable |
| Reuse concrete digital-trust failure propositions and falsification criteria | [Digital Trust Failure Corpus](https://github.com/qbf-consulting/digital-trust-failure-corpus) | Implementation Draft |
| Evaluate whether a composed Digital Trust Graph (DTG) interaction preserves an asserted privacy property | [DTG Privacy Implementation Profile](https://github.com/sankarshanmukhopadhyay/dtg-privacy-implementation-profile) | Implementation Draft |
| Apply the Trust Registry Query Protocol security/privacy profile | [TRQP Trust Service Provider Profile (TRQP-TSPP)](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | Implementation Draft |
| Run the TRQP reference verifier | [TRQP reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | Pilot Ready |
| Produce executable TRQP conformance evidence | [TRQP conformance suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | Implementation Draft |
| Compose TRQP assurance evidence | [TRQP assurance hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Candidate |

The **Trust Systems Modelling Stack (TSMS)** composes the [Trust Systems Meta Model (TSMM)](https://github.com/qbf-consulting/trust-systems-meta-model), [Trust Infrastructure Schemas (TIS)](https://github.com/qbf-consulting/trust-infrastructure-schemas), and [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts). Each layer retains its own authority and stewardship.

The TRQP implementation path similarly separates security/profile semantics, implementation, conformance and assurance: [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) → [reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) → [conformance suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) → [assurance hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub). Runnable validation commands remain authoritative in the component repositories; this profile does not duplicate commands it cannot independently exercise.

## How the portfolio fits together

The portfolio treats trust infrastructure as separable but composable layers. Authority remains bounded: semantic models do not acquire protocol authority, interoperability experiments do not create adoption claims, monitoring does not create ecosystem authority, and assurance findings do not modify normative content automatically.

~~~mermaid
flowchart LR
    A[Frameworks and adoption] --> B[Governance and semantics]
    B --> C[Protocols and policy]
    C --> D[Implementations]
    D --> E[Conformance and assurance]
    E -. evidence and feedback .-> B
    T[Terminology] -. shared language .-> B
    M[Ecosystem monitoring] -. nominates review .-> I[Interop Lab]
    I -. evidence .-> E
    R[RAHP] -. risk and harm review .-> P[DPIP]
    P -. composed privacy evidence .-> E
~~~

See **[Portfolio Architecture](portfolio/architecture.md)** for the full system view and **[Portfolio Status](docs/portfolio-status.md)** for the governed catalogue, lifecycle, stewardship and maturity state.

## Standards, community work, and writing

The portfolio includes work developed through or contributed into external standards and technical communities. Representative public evidence includes the [Agent Registry Protocol IETF Internet-Draft](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/), [Trust over IP Trust Registry Query Protocol](https://trustoverip.github.io/tswg-trust-registry-protocol/), and portfolio work connected to [UN/CEFACT](https://unece.org/trade/uncefact). These links identify contribution contexts; they do not imply authority over the external organisations or their specifications.

[The Trust Graph](https://thetrustgraph.substack.com/) is the long-form writing programme associated with this body of work. [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) carries selected propositions into executable governance patterns, implementation guidance and negative assurance tests; publication does not itself make a proposition normative.

## Portfolio assurance

This repository runs an evidence-producing portfolio assurance monitor over governed repositories, including projects stewarded outside this personal GitHub account. A finding is evidence for review, not an instruction; disposition, remediation and closure remain with the repository or authority that owns the affected scope.

- **[Assurance dashboard](docs/portfolio-assurance/dashboard.md)**
- **[Methodology](docs/portfolio-assurance/methodology.md)**

## Governance and provenance

The profile repository owns **portfolio membership, strategic presentation, relationship metadata, stewardship metadata and portfolio-level assurance evidence**. Individual repositories retain authority over normative content, releases, maturity declarations, validation commands and project-local evidence. A repository may therefore be a portfolio member without being owned by the sankarshanmukhopadhyay GitHub account.

Forks and adapted upstream work are identified explicitly. Inclusion in this portfolio does not imply upstream authorship, governance authority, release authority, endorsement or adoption. See [LICENSES.md](LICENSES.md) for the profile repository's code/content licensing boundary; linked repositories retain their own licence terms.

## For maintainers and contributors

- **[Portfolio Work Queue](docs/portfolio-work/index.md)** — choose the next bounded work item.
- **[Portfolio Assurance](docs/portfolio-assurance/index.md)** — review evidence and findings.
- **[Portfolio Architecture](portfolio/architecture.md)** — review composition and authority boundaries.
- **[GOVERNANCE.md](GOVERNANCE.md)** — portfolio governance.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — contribution guidance.
- **[SECURITY.md](SECURITY.md)** — security reporting.
- **[LICENSES.md](LICENSES.md)** — licensing boundaries.

Portfolio validation, maturity consistency, tests, internal links and site navigation are automated. This README is intentionally a **front door**, not the portfolio database.
