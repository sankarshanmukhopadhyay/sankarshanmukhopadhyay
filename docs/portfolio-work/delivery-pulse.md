---
layout: default
title: Portfolio Delivery Pulse
parent: Portfolio Work Queue
nav_order: 3
---

# Portfolio Delivery Pulse

The Portfolio Delivery Pulse is a compact observational surface embedded in the Portfolio Work Queue. It answers a different question from the ranked queue: **what delivery activity has actually become visible across the governed repository scope during the last 7 and 30 days?**

It does not create project authority and must not be interpreted as assurance, maturity, certification, health, quality, impact, or roadmap completion.

## Scope

The pulse uses the same eligible repository scope derived from `data/repository-status.yaml` and `config/portfolio-work-queue.yaml`. Repository-local evidence remains authoritative.

Commit counts are bounded to default-branch commits returned by the GitHub commits API. Pull-request, issue, and release counts are derived from GitHub repository evidence within the rolling observation window.

## Commit classification

Raw commit volume is deliberately decomposed:

- **automated** — a GitHub bot actor or a known generated/monitor commit prefix;
- **maintenance** — dependency or explicitly routine maintenance commit prefixes;
- **substantive** — remaining default-branch commits.

`Substantive` is only a classification residual. It does **not** mean that a commit is important, correct, assured, user-visible, or strategically valuable.

A repository counts as active when the window contains at least one substantive commit, merged pull request, closed issue, or published release. Automation-only or maintenance-only churn does not make a repository substantively active.

## Evidence and auditability

The Pages build and scheduled work-queue workflow regenerate the pulse from live GitHub evidence. Machine-readable evidence is emitted to `data/portfolio-delivery-pulse.json` on the published Pages build and alongside the scheduled Portfolio Work Queue artifact.

The JSON retains per-repository event evidence and the classification rules used for aggregation so that displayed totals can be independently recomputed.

## Interpretation boundary

The pulse should be used as a delivery-throughput signal alongside, not instead of, repository-local assurance evidence and the planner's ranked work state. In particular:

- high commit volume cannot substitute for merged outcomes, closed work, releases, or assurance evidence;
- automated and maintenance activity must remain separately visible;
- a release count records publication, not release quality or downstream adoption;
- closed issues and merged PRs record repository events, not proof that the underlying problem is fully resolved;
- the pulse never changes lifecycle, maturity, assurance, or authority state in member repositories.
