---
layout: default
title: Portfolio Status
---

# Portfolio status

The authoritative state is maintained in [`data/repository-status.yaml`](../data/repository-status.yaml). This page is a public discoverability surface for governed portfolio members; validation fails if a member cannot be discovered from at least one designated public portfolio surface.

## Core original portfolio

| Repository | Tier | Maturity | Operational status |
|---|---|---|---|
| `sankarshanmukhopadhyay` | Flagship | Stable | Stable maintenance |
| `open-national-digital-trust-framework` | Flagship | Candidate | Active validation |
| `governance-authority-assurance-metamodel` | Flagship | Candidate | Active validation |
| `agent-registry-protocol` | Flagship | Pilot ready | Active validation |
| `trust-systems-meta-model` | Flagship | Candidate | Active validation |
| `trust-infrastructure-schemas` | Flagship | Candidate | Active validation |
| `trust-graph-artifacts` | Flagship | Implementation draft | Active development |
| `rahp-toolkit` | Flagship | Stable | Stable maintenance |
| `TRQP-TSPP` | Flagship | Implementation draft | Active validation |
| `cawg-trqp-verifier-refimpl` | Flagship | Pilot ready | Active validation |
| `trqp-conformance-suite` | Flagship | Implementation draft | Active validation |
| `trqp-assurance-hub` | Flagship | Candidate | Active validation |

## Supporting original work

| Repository | Tier | Maturity | Role |
|---|---|---|---|
| `PolicyMesh` | Supporting | Implementation draft | Policy authority evaluation and enforcement |
| `trust-protocol-interop-lab` | Supporting | Implementation draft | Cross-protocol interoperability assurance lab |
| `dtg-portfolio-monitor` | Supporting | Implementation draft | DTG ecosystem situational awareness |
| `trust-ecosystem-monitor` | Supporting | Implementation draft | Reusable cross-ecosystem monitoring and evidence infrastructure |
| `dtg-privacy-implementation-profile` | Supporting | Implementation draft | Composed-interaction privacy assurance for DTG |
| `agent-name-assurance-baseline` | Supporting | Implementation draft | Agent name assurance |
| `dtg-conformance-assurance` | Supporting | Implementation draft | General conformance and assurance |
| `trust-infrastructure-glossary` | Supporting | Stable | Independent trust-infrastructure terminology |
| `ERC-8004-CSP` | Supporting | Implementation draft | Ecosystem-specific agent profile |

## Adjacent work

| Repository | Tier | Maturity | Role |
|---|---|---|---|
| `kiranaos` | Featured | Implementation draft | Applied product |
| `digital-governance-paper-notes` | Featured | Stable | Research analysis |
| `dpi-ai-governance-lab` | Supporting | Implementation draft | Applied governance lab |
| `dpi-ai-governance-artifacts` | Supporting | Implementation draft | Applied governance artefacts |
| `arf-onramp-pack` | Supporting | Implementation draft | Implementation onramp |
| `atal-enterprise-assurance-profile` | Supporting | Working draft | Enterprise assurance profile |
| `uncefact-portfolio-monitor` | Incubating | Implementation draft | UN/CEFACT ecosystem monitoring deployment and portability proof |

## Adapted upstream work

| Repository | Tier | Fork-local maturity | Upstream authority | Portfolio-local role |
|---|---|---|---|---|
| `dtgwg-zkp-tf` | Featured | Implementation draft | `trustoverip/dtgwg-zkp-tf` | Adapted ZKP implementation, risk, deployment, and learning guidance |

`adapted-upstream-work` recognizes substantive fork-local capability while preserving upstream authorship, governance, release, and adoption boundaries. The former `dtgwg-rahp-tf` fork is retained in the canonical register as **historical/superseded lineage**; the portable assurance capability is now governed as the original `rahp-toolkit` project.

## Upstream references

The governed upstream-reference set currently includes `agtp`, `dtgwg-cred-tf`, `tswg-trust-registry-protocol`, `conformance-test-suite`, `awesome-8004`, and `TokenTaxonomyFramework`. The former CTWG glossary fork has transitioned into the independently governed `trust-infrastructure-glossary`; its earlier upstream lineage is historical provenance rather than current portfolio authority. Reference forks use `upstream-tracking` maturity and identify the canonical upstream. Portfolio inclusion covers fork-local collaboration or reference use only and conveys no upstream governance, release, or adoption authority.

## Other governed dispositions

Repositories such as `decentralized-directory-protocol`, `A2A`, and `route-story-studio` may remain `pending-review`; `DHP-Specs` is retained as historical portfolio material. Older public repositories that do not need full portfolio metadata are recorded in the lightweight `account_dispositions` section of the canonical registry as `historical` or `unrelated`. This prevents known legacy repositories from being repeatedly rediscovered while keeping the detailed `repositories[]` register focused on governed portfolio and review candidates.

## Curated boundary

The registry is not a claim that every public repository belongs to the portfolio. Repositories outside the curated portfolio receive an account-level disposition rather than full portfolio membership. The Portfolio Assurance Monitor compares the live public account against both detailed repository records and lightweight account dispositions. Only genuinely unclassified public repositories are nominated for review; discovery itself never auto-enrols a repository.