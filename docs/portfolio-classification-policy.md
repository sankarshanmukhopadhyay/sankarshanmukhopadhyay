---
layout: default
title: Portfolio Classification Policy
---

# Portfolio Classification Policy

## Scope

The portfolio is curated. Public availability on the account does not automatically create portfolio membership.

## Decision sequence

1. Assign an account-level `portfolio_disposition`.
2. For included or adjacent work, assign strategic `tier`.
3. Record `maturity`, `lifecycle`, `operational_status`, `specification_status`, and `provenance` separately.
4. Declare authority scope and explicit non-authority boundaries.
5. Identify validation commands, evidence outputs, and known limitations.
6. Set a review date and define promotion, demotion, suspension, supersession, or archival conditions.

## Portfolio dispositions

| Value | Meaning |
|---|---|
| `included` | Governed member of the curated portfolio |
| `adjacent` | Relevant work presented with explicit separation from the core portfolio |
| `upstream-reference` | Fork or mirror used primarily for collaboration, reference, tracking, or contribution |
| `adapted-upstream-work` | Fork with substantive portfolio-local implementation, risk, deployment, assurance, documentation, or learning artefacts; upstream authority remains external |
| `historical` | Retained portfolio evidence without a current adoption claim |
| `unrelated` | Public account repository outside portfolio scope |
| `pending-review` | Awaiting a time-bounded inclusion or exclusion decision |

## Maturity vocabulary

| Value | Evidence expectation |
|---|---|
| `exploratory` | Problem framing and scope exist; no implementation dependency is asserted |
| `working-draft` | Structured artefacts exist but may change materially |
| `implementation-draft` | Prototype implementation is possible and validation guidance exists |
| `candidate` | Near feature-complete and undergoing systematic validation |
| `pilot-ready` | Documented deployment path, tests, and pilot artefacts exist |
| `stable` | Versioned, governed, documented, and suitable for declared stable use |
| `maintenance` | Stable scope receiving corrections and compatibility updates |
| `historical` | Retained for provenance or reference without current adoption claims |
| `upstream-tracking` | Local fork tracks or contributes to an upstream authority |

## Federated status authority

Featured original repositories and adapted upstream work should publish `PROJECT-STATUS.yaml` using the shared schema. The member repository owns maturity, lifecycle, specification status, intended use, validation, and evidence declarations. The profile repository owns membership, strategic tier, presentation, and cross-repository relationship metadata.

When evidence is insufficient or declarations conflict, the profile records a finding and may downgrade presentation. It does not silently alter member-owned status.

## Review and revocation

A repository may be demoted, suspended, marked historical, superseded, or removed from the curated portfolio when:

- required evidence is missing or irreproducible;
- status declarations become stale;
- authority claims overlap without resolution;
- an upstream fork is presented as original authority or its fork-local adaptations are not clearly bounded;
- a review deadline expires without disposition;
- maintenance or security obligations are not met;
- another repository supersedes its function.
