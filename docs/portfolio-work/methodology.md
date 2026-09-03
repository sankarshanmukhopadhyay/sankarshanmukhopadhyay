---
layout: default
title: Portfolio Work Queue Methodology
parent: Portfolio Work Queue
nav_order: 2
---

# Portfolio Work Queue methodology

The Portfolio Work Queue is a **derived execution-planning and reconciliation surface**, not a source of project authority. It ranks observable work signals from governed repositories so a maintainer can choose a bounded next action without reconstructing the entire portfolio manually.

## Authority

The portfolio registry (`data/repository-status.yaml`) decides which repositories are in scope. Member repositories retain authority over project goals, normative content, releases, implementation state and repository-local evidence. The queue owns only discovery, classification, reconciliation, prioritisation and presentation.

An inferred candidate therefore means **"current evidence supports this planning proposition"**, not **"the portfolio has ordered this repository to change."**

## Evidence sources

The live builder reads the governed portfolio registry, `config/portfolio-work-queue.yaml`, and current GitHub Issues/pull requests for eligible repositories. Each candidate retains the evidence observation time and the source artifact's update time.

Repository-local issues, pull requests, releases, rulesets, `PROJECT-STATUS.yaml`, roadmaps and assurance artifacts remain authoritative for the claims they make. The planner must not turn absence of a parsed blocker into evidence that no blocker exists.

## Change convention

Issue and pull-request titles should use:

```text
<type>(<scope>): <imperative summary>
```

Supported portfolio types are `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `ci`, `perf`, `security`, and `governance`. A `!` before `:` declares a consumer-visible breaking change, for example `feat(schema)!: replace lifecycle contract`.

The planner records whether classification came from a typed title or inference. Untyped legacy work remains visible but receives lower classification confidence. `security`, `governance`, and breaking changes are consequential signals and must not silently become quick executable work.

## Lifecycle state is not priority

| State | Meaning |
|---|---|
| `ready` | current evidence positively supports execution |
| `in_progress` | repository evidence says execution has begun |
| `waiting_internal` | unresolved dependency is controlled within the portfolio/repository |
| `waiting_external` | progress depends on an upstream/external authority or event |
| `needs_judgment` | consequential architecture, governance, security, normative, compatibility or release decision |
| `evidence_required` | additional evidence is explicitly required before execution or closure |
| `superseded` | newer/current work has displaced this candidate |
| `stale_candidate` | the planning evidence is too old to support a current execution claim |
| `completed` | authoritative source is completed/closed |

Priority and impact remain orthogonal. A very-high-impact issue can correctly remain `waiting_external`.

## Lanes

Lifecycle state is separate from work lane. `strategic` is the default execution lane; `maintenance` contains dependency/chore work; `planning` contains roadmap-only work. A maintenance item can be ready without being allowed to dominate the strategic work-now view.

## Evidence state

The machine-readable queue exposes `unverified`, `partially_verified`, `verified`, `execution_evidence_pending`, or `complete`. Missing evidence is never PASS. `ready` is therefore a positive claim backed by reconciled evidence, not a synonym for `open`.

## Effort and complexity

Effort remains bucketed: ≤15m, 15–30m, 30–60m, 1–2h, 2–4h, half-day, one-day, or **decompose**. Complexity remains independent: `low`, `medium`, `high`, or `consequential`.

Consequential work is routed away from `ready` even when its mechanical implementation appears small.

## Priority and leverage

Priority is computed from project-goal impact, portfolio impact, unblock value, release proximity, assurance value, adoption value and staleness pressure, minus explicit penalties for waiting, low-confidence inference, maintenance/planning noise and untyped change intent.

Effort is not part of strategic priority. Leverage divides positive priority by estimated effort.

## Trustworthiness invariants

The planner is wrong if any of these occur:

- a candidate is `ready` while carrying an unresolved dependency;
- consequential work is emitted as `ready`;
- an external wait lacks external dependency evidence;
- superseded/completed work retains executable priority;
- dependency or roadmap noise dominates the strategic work-now view;
- an ungoverned repository enters scope;
- a ranking cannot explain its evidence and classification provenance.

Regression fixtures should deliberately falsify these rules. RAHP #88 is a canonical example: high importance does not make the issue executable while the authoritative issue says to wait for upstream WD02.

## Schema v2 migration

`data/portfolio-work-queue.json` schema v2 adds `change`, `lane`, `dependency`, and `evidence`, and replaces the earlier mixed state/maintenance vocabulary with explicit lifecycle states. Machine consumers must migrate before relying on v2 output.
