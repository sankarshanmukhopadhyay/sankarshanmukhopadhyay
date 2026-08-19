---
layout: default
title: Methodology
parent: Portfolio Assurance Monitor
nav_order: 3
---

# Portfolio assurance methodology

The monitor treats portfolio governance as executable evidence processing: observe, evaluate, package, remediate, and verify. Its authority is intentionally narrower than the repositories it observes.

## Scope derivation

The default monitoring scope is derived from `data/repository-status.yaml` and selects repositories with:

- `portfolio_disposition: included`;
- `tier: flagship`; and
- `provenance: original`.

The profile/control-plane repository is excluded from repository-health collection and remains the central destination for portfolio-governance findings such as account-discovery drift.

## Assessment dimensions

The monitor reports assessment dimensions independently instead of collapsing them into a single green/red portfolio state.

Current dimensions are:

| Dimension | Current monitor state | Meaning |
|---|---|---|
| Operational | `evaluated` | repository availability and observable default-branch workflow evidence |
| Governance | `evaluated` | review state, status declaration, lifecycle and governed repository identity |
| Assurance | `not-evaluated` | substantive conformance, risk, controls and assurance evidence are not yet ingested |
| Cross-specification | `not-evaluated` | cross-specification pressure-test evidence is not yet ingested |

`evaluated` means the configured rules ran against observable evidence. It does not mean the repository is universally assured. `not-evaluated` is an explicit epistemic state and must never render as green.

## Evidence model

For each monitored repository the collector attempts to observe:

- public repository availability and default branch;
- the default-branch commit SHA;
- repository-local `PROJECT-STATUS.yaml` where required;
- recent default-branch GitHub Actions runs; and
- repository activity timestamps.

Workflow evidence uses a governed lookback window and resolves the **latest completed state per workflow**. A prior failure superseded by a later success is not an unresolved failure.

Required evidence is fail-closed. If a required status declaration or workflow evidence cannot be observed, the monitor produces an evidence-availability finding rather than interpreting absence of evidence as evidence of health.

## Finding identity and remediation contract

Findings have two identities:

- `finding_id`: observation-scoped and date-sensitive;
- `finding_fingerprint`: stable for the same repository, rule, and subject.

Each finding also carries:

- an assessment dimension;
- evidence;
- a remediation objective;
- acceptance criteria; and
- verification guidance.

This makes each finding suitable for a machine-verifiable remediation handoff while preserving target-repository authority over implementation.

## Repository remediation dossier

All current findings for a repository are consolidated into one Markdown dossier and one JSON dossier. The dashboard links directly to the rendered dossier and downloadable raw artifacts.

The Markdown dossier is intentionally optimized for this development flow:

```text
repository archive + remediation dossier → implementation work → validation → monitor re-evaluation
```

Individual findings remain independently identifiable by their stable fingerprint even though the handoff artifact is consolidated per repository.

## Finding lifecycle and closure

The monitor maintains `reports/portfolio-assurance/finding-lifecycle.json`.

For each stable fingerprint it records:

- first observed;
- last observed;
- current state;
- latest observation identifier; and
- resolution time when a later run no longer observes the condition.

The monitor can verify that an observed condition disappeared, but it does not claim that every semantic or normative concern is resolved merely because a rule stopped firing. Repository-level implementation and validation evidence remain authoritative for the remediation itself.

## Deterministic rules

The current evaluated rules cover:

- repository unavailability;
- unavailable workflow evidence;
- overdue portfolio review;
- unobservable required status declarations;
- missing required status declarations;
- unreadable required status declarations;
- unresolved latest default-branch workflow failure;
- inactivity review thresholds for repositories declared active; and
- governed/public repository identity drift.

Account discovery can also produce a central finding when a public repository has not received a governed account-level disposition.

## Routing boundary

A finding is not automatically an issue. The routing layer separately evaluates rule eligibility, severity, policy opt-in, deduplication state, and per-run publication caps. Only actionable repository-local findings may be routed to the repository where the evidence was observed.

Portfolio-governance findings remain central. Discovery never auto-enrols a repository and repository identity churn never automatically infers a rename or transfer target.

## Assurance boundary

The monitor may produce evidence that a claim requires review. It cannot automatically:

- change portfolio membership or tier;
- change repository maturity or lifecycle;
- change normative specification content;
- accept risk;
- confer upstream authority;
- choose an implementation remediation; or
- close a repository-local governance decision.

The monitor produces observations, findings, handoff artifacts, and lifecycle evidence. Repository governance produces implementation and disposition.
