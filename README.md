# Sankarshan Mukhopadhyay

## Research and implementation of verifiable authority in digital systems

I work on making authority verifiable in distributed digital systems: how identity, delegation, policy and evidence support enforceable decisions; how permissions change or end; and how failures can be detected, challenged and remedied. The work spans digital trust infrastructure and agentic systems through specifications, protocols, reference implementations, conformance tools and research artifacts.

The central engineering question is whether a consequential action remains authorized in its actual scope and context, and what evidence permits an independent party to verify or dispute that conclusion.

[![Portfolio validation](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml)
[![Portfolio documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0969da)](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
[![Code license: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Content license: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE-CONTENT)

This is a **curated body-of-work portfolio**, not an ownership inventory. Institutionally stewarded open-source and open-knowledge work is maintained through [QBF Consulting](https://github.com/qbf-consulting); this personal profile remains the body-of-work and relationship front door. Repository ownership identifies current stewardship, while authority over normative content remains repository-local.

**Terminology:** [Trust Infrastructure Glossary](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-glossary) · **Writing:** [The Trust Graph](https://thetrustgraph.substack.com/) · **Full portfolio status:** [Portfolio Status](docs/portfolio-status.md)

## Areas of work

These are **reader navigation groups**, not additional normative layers or shared release authorities. Each linked repository retains its declared governance and maturity.

| Area | Question explored | Representative entry points |
|---|---|---|
| Governance and authority | Who may act, on whose authority, and under what scope, time, and redress conditions? | [GAAM](https://github.com/qbf-consulting/governance-authority-assurance-metamodel) · [ARPA](https://github.com/qbf-consulting/agent-registry-protocol) · [PolicyMesh](https://github.com/sankarshanmukhopadhyay/PolicyMesh) |
| Trust infrastructure and interoperability | How can independently governed systems express and exchange compatible trust semantics? | [ONDTF](https://github.com/qbf-consulting/open-national-digital-trust-framework) · [TSMM](https://github.com/qbf-consulting/trust-systems-meta-model) · [TIS](https://github.com/qbf-consulting/trust-infrastructure-schemas) |
| Conformance and assurance | What tests and evidence justify a bounded claim, and which gaps remain unresolved? | [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) · [RAHP Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) · [DPIP](https://github.com/sankarshanmukhopadhyay/dtg-privacy-implementation-profile) · [Interop Lab](https://github.com/sankarshanmukhopadhyay/trust-protocol-interop-lab) · [DTFC](https://github.com/qbf-consulting/digital-trust-failure-corpus) |
| Research and knowledge | What can published research establish, and how does its evidence inform implementation and governance? | [Digital Governance Paper Notes](https://github.com/sankarshanmukhopadhyay/digital-governance-paper-notes) · [The Trust Graph](https://thetrustgraph.substack.com/) |

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
| Pressure-test a specification for harms, security weaknesses, and governance failure modes | [Risk Assessment & Harms Prevention (RAHP) Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) | Stable |
| Reuse concrete digital-trust failure propositions and falsification criteria | [Digital Trust Failure Corpus](https://github.com/qbf-consulting/digital-trust-failure-corpus) | Implementation Draft |
| Evaluate whether a composed Digital Trust Graph (DTG) interaction preserves an asserted privacy property | [DTG Privacy Implementation Profile](https://github.com/sankarshanmukhopadhyay/dtg-privacy-implementation-profile) | Implementation Draft |
| Apply the Trust Registry Query Protocol security/privacy profile | [TRQP Trust Service Provider Profile (TRQP-TSPP)](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | Implementation Draft |
| Run the TRQP reference verifier | [TRQP reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | Pilot Ready |
| Produce executable TRQP conformance evidence | [TRQP conformance suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | Implementation Draft |
| Compose TRQP assurance evidence | [TRQP assurance hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Candidate |

The **Trust Systems Modelling Stack (TSMS)** composes the [Trust Systems Meta Model (TSMM)](https://github.com/qbf-consulting/trust-systems-meta-model), [Trust Infrastructure Schemas (TIS)](https://github.com/qbf-consulting/trust-infrastructure-schemas), and [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts). Each layer retains its own authority and stewardship.

The TRQP implementation path similarly separates security/profile semantics, implementation, conformance and assurance: [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) → [reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) → [conformance suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) → [assurance hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub). Runnable validation commands remain authoritative in the component repositories; this profile does not duplicate commands it cannot independently exercise.

## What can be evaluated today

These are practical entry points, not claims of external certification or universal interoperability. Follow the owning repository's documented validation steps and inspect the stated evidence limitations.

| Evaluation | Reproducible entry point | Evidence boundary |
|---|---|---|
| Reproduce a coordinated TRQP assurance stack | [Stack quickstart](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/blob/main/docs/adoption/stack-quickstart.md) and [Lotus release record](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/releases/tag/trqp-stack-2026.4) | The pinned tuple demonstrates bounded component compatibility, not certification of a live deployment. |
| Run a bounded risk and harms assessment | [RAHP adoption guide](https://github.com/sankarshanmukhopadhyay/rahp-toolkit/blob/main/docs/adoption-guide.md) and [Hello RAHP](https://github.com/sankarshanmukhopadhyay/rahp-toolkit/tree/main/examples/hello-rahp) | A completed workflow is not an assurance PASS when evidence is missing. |
| Examine agent registry authority contracts | [ARPA start-here guidance](https://qbfconsulting.digital/agent-registry-protocol/docs/start-here/) | Protocol examples and local tests do not prove external runtime authorization or independent interoperability. |
| Validate digital-trust failure cases | [DTFC consumption guidance](https://github.com/qbf-consulting/digital-trust-failure-corpus/blob/main/docs/consuming-the-corpus.md) | Corpus cases are falsification inputs, not normative authority or proof of an implementation's conformance. |

The [RAHP Assessment Registry](https://github.com/sankarshanmukhopadhyay/rahp-assessment-registry) is a **working pilot** for durable assessment-case ownership and operational coordination. Its [migration tracker](https://github.com/sankarshanmukhopadhyay/rahp-assessment-registry/issues/11) records the remaining live cutover gates. Registry execution must continue to use the canonical Toolkit engine; a source-pinned pilot is not a completed operational handoff.

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

## Using and contributing to this work

For an implementation question, reproducibility problem, interoperability experiment, or proposed change, start with the owning repository's issues, discussions, adoption guide, or contribution process. For research and standards questions, use the relevant project or upstream community rather than assuming this profile has authority over it. For consulting or implementation engagement, see [QBF Consulting](https://qbfconsulting.digital/). The [portfolio work queue](docs/portfolio-work/index.md) is a derived planning aid, not a transfer of approval authority.

## Portfolio assurance

This repository runs an evidence-producing portfolio assurance monitor over governed repositories, including projects stewarded outside this personal GitHub account. A finding is evidence for review, not an instruction; disposition, remediation and closure remain with the repository or authority that owns the affected scope.

- **[Assurance dashboard](docs/portfolio-assurance/dashboard.md)**
- **[Methodology](docs/portfolio-assurance/methodology.md)**

## Governance and provenance

GitHub's repository tab is an account activity view, not a portfolio lifecycle model. Historical forks, unrelated earlier work, upstream copies and maintenance commits can appear alongside current projects. For lifecycle, provenance and maturity, use [Portfolio Status](docs/portfolio-status.md) and the governed [repository status registry](data/repository-status.yaml); recent activity alone does not establish resumed product development.

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
