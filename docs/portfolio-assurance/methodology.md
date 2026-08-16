---
layout: default
title: Methodology
parent: Portfolio Assurance Monitor
nav_order: 3
---

# Portfolio assurance methodology

The monitor evaluates the curated portfolio as executable governance. Its authority is intentionally narrower than the repositories it observes.

## Scope derivation

The default monitoring scope is derived from `data/repository-status.yaml` and currently selects repositories with:

- `portfolio_disposition: included`;
- `tier: flagship`; and
- `provenance: original`.

The profile/control-plane repository is excluded from repository-health collection and remains the central destination for portfolio-governance findings such as account-discovery drift.

## Evidence model

For each monitored repository the collector attempts to observe:

- public repository availability and default branch;
- repository-local `PROJECT-STATUS.yaml` where required;
- recent default-branch GitHub Actions runs; and
- repository activity timestamps.

Workflow evidence uses a governed lookback window and resolves the **latest completed state per workflow**. A prior failure superseded by a later success is not an unresolved failure.

## Finding identity

Findings have two identities:

- `finding_id`: observation-scoped and date-sensitive;
- `finding_fingerprint`: stable for the same repository, rule, and subject.

Stable fingerprints provide a machine-verifiable deduplication key for target-repository issues and future disposition records.

## Deterministic rules

The current rules cover:

- repository unavailability;
- overdue portfolio review;
- missing required status declarations;
- unreadable required status declarations;
- unresolved latest default-branch workflow failure; and
- inactivity thresholds for repositories declared active.

Account discovery adds a central `PUBLIC_REPOSITORY_WITHOUT_DISPOSITION` finding when a public repository has not yet received a governed account-level disposition.

## Routing boundary

A finding is not automatically an issue. The routing layer separately evaluates rule eligibility, severity, policy opt-in, deduplication state, and per-run publication caps. Only actionable repository-local findings may be routed to the repository where the evidence was observed.

Portfolio-governance findings remain central. In particular, account discovery and inactivity do not create target-repository issues by default.

## Assurance boundary

The monitor may produce evidence that a claim requires review. It cannot automatically:

- change portfolio membership or tier;
- change repository maturity or lifecycle;
- change normative specification content;
- accept risk;
- confer upstream authority; or
- close a repository-local governance decision.

The machine produces observations and findings. Human governance produces disposition.
