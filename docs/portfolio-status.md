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
| `open-national-digital-trust-framework` | Flagship | Working draft | Active development |
| `governance-authority-assurance-metamodel` | Flagship | Candidate | Active validation |
| `agent-registry-protocol` | Flagship | Pilot ready | Active validation |
| `trust-systems-meta-model` | Flagship | Candidate | Active validation |
| `trust-infrastructure-schemas` | Flagship | Candidate | Active validation |
| `trust-graph-artifacts` | Flagship | Implementation draft | Active development |
| `TRQP-TSPP` | Flagship | Candidate | Active validation |
| `cawg-trqp-verifier-refimpl` | Flagship | Pilot ready | Active validation |
| `trqp-conformance-suite` | Flagship | Pilot ready | Active validation |
| `trqp-assurance-hub` | Flagship | Pilot ready | Active validation |

## Supporting original work

| Repository | Tier | Maturity | Role |
|---|---|---|---|
| `PolicyMesh` | Supporting | Implementation draft | Policy authority evaluation and enforcement |
| `trust-protocol-interop-lab` | Supporting | Implementation draft | Cross-protocol interoperability assurance lab |
| `dtg-portfolio-monitor` | Supporting | Implementation draft | DTG ecosystem situational awareness |
| `agent-name-assurance-baseline` | Supporting | Implementation draft | Agent name assurance |
| `dtg-conformance-assurance` | Supporting | Implementation draft | General conformance and assurance |
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

## Adapted upstream work

| Repository | Tier | Fork-local maturity | Upstream authority | Portfolio-local role |
|---|---|---|---|---|
| `dtgwg-zkp-tf` | Featured | Implementation draft | `trustoverip/dtgwg-zkp-tf` | Adapted ZKP implementation, risk, deployment, and learning guidance |
| `dtgwg-rahp-tf` | Featured | Implementation draft | `trustoverip/dtgwg-rahp-tf` | Adapted risk/harm pressure testing, security hardening, assurance evidence, and adoption tooling |

`adapted-upstream-work` recognizes substantive fork-local capability while preserving upstream authorship, governance, release, and adoption boundaries.

## Upstream references

The governed upstream-reference set currently includes `agtp`, `ctwg-main-glossary`, `dtgwg-cred-tf`, `tswg-trust-registry-protocol`, `conformance-test-suite`, `awesome-8004`, and `TokenTaxonomyFramework`. Reference forks use `upstream-tracking` maturity and identify the canonical upstream. Portfolio inclusion covers fork-local collaboration or reference use only and conveys no upstream governance, release, or adoption authority.

## Other governed dispositions

Repositories such as `decentralized-directory-protocol` and `A2A` may remain `pending-review`; `DHP-Specs` is retained as historical portfolio material. Other repositories may be historical or otherwise outside active portfolio membership. Their account-level disposition is still recorded in the canonical registry.

## Curated boundary

The registry is not a claim that every public repository belongs to the portfolio. Repositories outside the curated portfolio receive an account-level disposition rather than full portfolio membership. A separate external-discovery check can identify public repositories that have not yet received any disposition; discovery itself never auto-enrols a repository.
