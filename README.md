# Sankarshan Mukhopadhyay

## Building executable governance, authority-control planes, and assurance infrastructure

I design specifications, protocols, schemas, conformance systems, and reference implementations for digital trust and agentic systems. The work focuses on making authority, delegation, constraints, revocation, evidence, accountability, and redress explicit enough to be implemented, tested, audited, and independently challenged.

> **Core premise:** trust becomes infrastructure only when authority, constraints, revocation, evidence, and redress are operational, enforceable, and independently verifiable.

[![Portfolio validation](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/actions/workflows/validate.yml)
[![Portfolio documentation](https://img.shields.io/badge/docs-GitHub%20Pages-0969da)](https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/)
[![Code license: Apache-2.0](https://img.shields.io/badge/code-Apache--2.0-blue.svg)](LICENSE-CODE)
[![Content license: CC BY-NC-SA 4.0](https://img.shields.io/badge/content-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE-CONTENT)

## Portfolio Assurance Monitor

The repository includes a weekly, evidence-producing assurance monitor for flagship original repositories. It derives scope from the governed portfolio register, checks public operational evidence and repository-local status declarations, and publishes findings without automatically modifying portfolio classifications. The monitor now evaluates unresolved latest workflow state within a governed lookback window, detects public repositories that lack an account-level disposition, and can route deduplicated evidence-rich findings to affected repositories when explicitly enabled with a scoped GitHub App.

- [Monitor overview](docs/portfolio-assurance/index.md)
- [Methodology](docs/portfolio-assurance/methodology.md)
- [Operations](docs/portfolio-assurance/operations.md)
- [Dashboard](docs/portfolio-assurance/dashboard.md)

## Portfolio scope

This profile presents a **curated trust-infrastructure portfolio**. It is not an exhaustive inventory of every public repository on this GitHub account. Older infrastructure projects, personal utilities, conference material, upstream mirrors, and unrelated historical work may remain publicly accessible without being portfolio members.

Every repository reviewed by this programme receives an account-level disposition. Only included, adjacent, upstream-reference, and historical portfolio repositories receive detailed portfolio governance records.

## How status is communicated

Repository significance and readiness are separate claims.

| Dimension | Question answered |
|---|---|
| Portfolio disposition | Is the repository part of, adjacent to, or outside the curated portfolio? |
| Tier | How strategically prominent is it within the portfolio? |
| Maturity | How ready is its declared output for use? |
| Lifecycle | Is it active, maintained, superseded, or archived? |
| Operational status | What work is currently occurring? |
| Specification status | What formal status does its specification claim? |
| Provenance | Is it original, forked, mirrored, or collaboratively hosted? |
| Authority | What does the repository govern, and what remains elsewhere? |

The authoritative vocabulary and current classifications are maintained in [`data/repository-status.yaml`](data/repository-status.yaml). Featured original repositories are expected to publish a repository-local `PROJECT-STATUS.yaml` conforming to [`schemas/project-status.schema.json`](schemas/project-status.schema.json).

## Start here

| You are trying to… | Begin with | Current positioning |
|---|---|---|
| Design or assess a national or multi-sector digital trust framework | [Open National Digital Trust Framework](https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework) | Flagship · Working draft · Original |
| Model authority, delegation, revocation, accountability, or remedy | [Governance, Authority and Assurance Metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | Flagship · Candidate · Original |
| Analyse the semantics of a trust system | [Trust Systems Meta Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Flagship · Candidate · Original |
| Implement portable trust records or evidence contracts | [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Flagship · Candidate · Original |
| Deploy or evaluate an agent registry | [Agent Registry Protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | Flagship · Pilot ready · Original |
| Determine whether an actor is permitted to act under mandate, evidence, policy, and time | [PolicyMesh](https://github.com/sankarshanmukhopadhyay/PolicyMesh) | Supporting · Implementation draft · Original |
| Test whether independently governed trust and agent protocols compose correctly | [Trust Protocol Interop Lab](https://github.com/sankarshanmukhopadhyay/trust-protocol-interop-lab) | Supporting · Implementation draft · Original |
| Pressure-test specifications for risks, harms, security weaknesses, and governance failure modes | [RAHP Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) | Flagship · Stable · Original |
| Observe change, convergence, and alignment across the wider DTG landscape | [DTG Portfolio Monitor](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor) | Supporting · Implementation draft · Original |
| Test or assure a trust-registry deployment | [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Flagship · Pilot ready · Original |
| Apply ZKP implementation, threat, risk, and deployment guidance | [DTG ZKP Task Force fork](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) | Featured · Implementation draft · Adapted upstream work |
| Review governed digital-trust terminology | [CTWG Main Glossary fork](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary) | Upstream collaboration · Upstream tracking |
| Examine agent-transfer protocol implementation and hardening | [AGTP fork](https://github.com/sankarshanmukhopadhyay/agtp) | Upstream collaboration · Upstream tracking |

## Flagship original work

| Repository | Operational contribution | Maturity | Operational status |
|---|---|---|---|
| [Governance, Authority and Assurance Metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | Normative model for executable governance, delegation, revocation, assurance, accountability, appeal, and remedy | Candidate | Active validation |
| [Agent Registry Protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | Protocol, schemas, APIs, conformance tests, and reference artefacts for deployable agent registries | Pilot ready | Active validation |
| [Trust Systems Meta Model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | Semantic metamodel for actors, authority, policy, evidence, decisions, effects, and accountability | Candidate | Active validation |
| [Trust Infrastructure Schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | Portable machine-readable contracts for trust actors, claims, bindings, relationships, and evidence | Candidate | Active validation |
| [Trust Graph Artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) | Applied governance patterns, threat models, implementation guidance, and negative-assurance artefacts | Implementation draft | Active development |
| [RAHP Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) | Portable RAHP, security, and combined specification assurance with evidence retention and change monitoring | Stable | Stable maintenance |
| [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | Security and trust-service-provider profile for TRQP | Candidate | Active validation |
| [TRQP reference verifier](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | Deterministic verifier producing provenance-preserving conclusions | Pilot ready | Active validation |
| [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | Executable tests producing lifecycle-aware interoperability evidence | Pilot ready | Active validation |
| [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | Coordinated implementation, conformance, evidence, and assurance entry point | Pilot ready | Active validation |

## Supporting and adjacent work

Supporting repositories provide domain profiles, policy execution, reusable assurance methods, applied laboratories, implementation guidance, ecosystem observation, and research. Inclusion here does not imply the same strategic tier or adoption maturity as flagship work.

### Policy execution and authority

- [PolicyMesh](https://github.com/sankarshanmukhopadhyay/PolicyMesh)
- [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline)

### Interoperability and experimentation

- [Trust Protocol Interop Lab](https://github.com/sankarshanmukhopadhyay/trust-protocol-interop-lab)

### Assurance and pressure testing

- [DTG Conformance and Assurance](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance)
- [RAHP Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) — portable risk, harms, security, and specification-assurance infrastructure

### Ecosystem observation

- [DTG Portfolio Monitor](https://github.com/sankarshanmukhopadhyay/dtg-portfolio-monitor)

### Applied implementation and adoption

- [ERC-8004 CSP](https://github.com/sankarshanmukhopadhyay/ERC-8004-CSP)
- [KiranaOS](https://github.com/sankarshanmukhopadhyay/kiranaos)
- [DPI AI Governance Lab](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab)
- [DPI AI Governance Artifacts](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts)
- [ARF Onramp Pack](https://github.com/sankarshanmukhopadhyay/arf-onramp-pack)
- [Atal Enterprise Assurance Profile](https://github.com/sankarshanmukhopadhyay/atal-enterprise-assurance-profile)

### Research and exploratory work

- [Digital Governance Paper Notes](https://github.com/sankarshanmukhopadhyay/digital-governance-paper-notes)

## Adapted and reference upstream work

Fork inclusion represents bounded fork-local implementation, assurance, documentation, validation, or contribution-oriented work. `adapted-upstream-work` identifies a substantive portfolio-local capability, while `upstream-reference` identifies primarily tracking or collaboration use. Neither disposition implies upstream authorship, governance authority, release authority, endorsement, or adoption.

| Portfolio fork | Canonical upstream | Portfolio-local role |
|---|---|---|
| [DTG ZKP Task Force](https://github.com/sankarshanmukhopadhyay/dtgwg-zkp-tf) | `trustoverip/dtgwg-zkp-tf` | Adapted implementation, threat, risk, deployment, and learning guidance |
| `dtgwg-rahp-tf` (superseded lineage) | `trustoverip/dtgwg-rahp-tf` | Historical fork lineage retained for provenance; reusable assurance capability now lives in the original [RAHP Toolkit](https://github.com/sankarshanmukhopadhyay/rahp-toolkit) |
| [CTWG Main Glossary](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary) | `trustoverip/ctwg-main-glossary` | Terminology harmonisation and publication refinement |
| [AGTP](https://github.com/sankarshanmukhopadhyay/agtp) | `nomoticai/agtp` | Security hardening and implementation refinement |
| [DTG Credential Task Force](https://github.com/sankarshanmukhopadhyay/dtgwg-cred-tf) | `trustoverip/dtgwg-cred-tf` | Standards-facing collaboration |
| [Trust Registry Protocol](https://github.com/sankarshanmukhopadhyay/tswg-trust-registry-protocol) | `trustoverip/tswg-trust-registry-protocol` | Protocol reference and contribution surface |

### Account-level disposition coverage

The canonical registry also carries a lightweight `account_dispositions` section for known public repositories that are historical or unrelated to the active trust-infrastructure portfolio. This keeps live account discovery high-signal without forcing full governance metadata onto legacy repositories. Newly observed public repositories remain unclassified until a human assigns a governed disposition.

## Portfolio architecture

The five functional planes remain the portfolio backbone. Three cross-cutting capabilities now make the operating model explicit: **PolicyMesh** evaluates bounded policy and mandate context, the **Trust Protocol Interop Lab** tests composition seams without acquiring protocol authority, and the **DTG Portfolio Monitor** observes external ecosystem movement and nominates questions for human review. The standalone **RAHP Toolkit** adds portable risk, harm, guardrail, security, and combined specification pressure testing alongside conformance; its DTG origin is retained as provenance rather than as the toolkit identity.

```mermaid
flowchart TB
    subgraph P0["1. Frameworks and adoption"]
        ONDTF["Open National Digital Trust Framework"]
    end
    subgraph P1["2. Governance and semantic authority"]
        GAAM["GAAM"]
        TSMM["TSMM"]
        TIS["TIS"]
        TGA["Trust Graph Artifacts"]
    end
    subgraph P2["3. Protocols and profiles"]
        ARPA["Agent Registry Protocol"]
        ANAB["Agent Name Assurance Baseline"]
        TSPP["TRQP-TSPP"]
    end
    subgraph P3["4. Implementations and operational systems"]
        PM["PolicyMesh"]
        VERIFIER["TRQP Reference Verifier"]
        ZKP["Adapted DTG ZKP guidance"]
        DPI["DPI AI Governance Lab"]
    end
    subgraph P4["5. Conformance, evidence and assurance"]
        TRQPCS["TRQP Conformance Suite"]
        HUB["TRQP Assurance Hub"]
        DTGCA["DTG Conformance and Assurance"]
        RAHP["RAHP Toolkit\nportable specification assurance"]
        EVIDENCE["Evidence packages"]
    end
    INTEROP["Trust Protocol Interop Lab
composition and seam testing"]
    MONITOR["DTG Portfolio Monitor
ecosystem situational awareness"]
    subgraph UP["External upstream authority"]
        ZKPUP["trustoverip/dtgwg-zkp-tf"]
        RAHPUP["historical DTG RAHP lineage"]
    end

    ONDTF -.-> GAAM
    ONDTF -.-> TSMM
    ONDTF -.-> TIS
    TSMM -.-> TIS
    GAAM -.-> ARPA
    GAAM -. "bounded concepts" .-> PM
    TSMM -. "bounded semantics" .-> PM
    PM --> INTEROP
    TSPP --> TRQPCS
    VERIFIER --> TRQPCS
    TRQPCS --> HUB
    HUB --> EVIDENCE
    DTGCA --> EVIDENCE
    RAHP --> EVIDENCE
    INTEROP --> EVIDENCE
    MONITOR -. "nominates review questions" .-> INTEROP
    INTEROP -. "pressure-tested by" .-> RAHP
    EVIDENCE -. "assurance feedback" .-> GAAM
    ZKP -. "fork of" .-> ZKPUP
    RAHP -. "historical provenance" .-> RAHPUP
```

Solid edges represent operational, implementation, testing, or evidence flows. Dashed edges represent bounded semantic alignment, observation signals, assurance feedback, provenance, or contribution-oriented learning. Observation never creates interoperability claims; interoperability experiments never acquire upstream authority; assurance findings never modify normative content automatically.

See [Portfolio Architecture](portfolio/architecture.md), [Portfolio Status](docs/portfolio-status.md), and the [Classification Policy](docs/portfolio-classification-policy.md).

## Governance and evidence

The profile repository owns portfolio membership, strategic tier, presentation, and relationship metadata. Each original member repository retains authority over its normative content, releases, maturity declaration, validation commands, and evidence outputs. The portfolio may record a finding or reduce public prominence when a member claim lacks sufficient evidence; it does not silently rewrite the member repository’s declaration.

Validation:

```bash
python scripts/validate_portfolio.py
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
```

## Writing and research

Long-form analysis is published through [The Trust Graph](https://thetrustgraph.substack.com/), focused on executable trust, registries, governance, agentic systems, digital public infrastructure, assurance, and redress.

## Licensing

Unless otherwise stated in an individual file or repository:

- source code, scripts, schemas, workflows, and test software in this profile repository are licensed under [Apache-2.0](LICENSE-CODE);
- documentation, diagrams, governance material, and other written portfolio content are licensed under [CC BY-NC-SA 4.0](LICENSE-CONTENT).

See [LICENSES.md](LICENSES.md) for the licence boundary. Individual repositories retain their own licences and governance terms.
