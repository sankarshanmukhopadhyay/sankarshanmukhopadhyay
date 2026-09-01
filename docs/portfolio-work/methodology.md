---
layout: default
title: Portfolio Work Queue Methodology
parent: Portfolio Work Queue
nav_order: 2
---

# Portfolio Work Queue methodology

The Portfolio Work Queue is a **derived execution-planning surface**, not a source of project authority. It ranks observable work signals from governed repositories so a maintainer can choose a bounded next action without reconstructing the entire portfolio manually.

## Authority

The portfolio registry (`data/repository-status.yaml`) decides which repositories are in scope. Member repositories retain authority over project goals, normative content, releases, implementation state and repository-local evidence. The queue owns only discovery, classification, prioritisation and presentation.

An inferred candidate therefore means **"this evidence suggests useful work"**, not **"the portfolio has ordered this repository to change."**

## Evidence sources

The live builder reads:

1. the governed portfolio registry;
2. `config/portfolio-work-queue.yaml`;
3. open GitHub Issues and pull requests for eligible repositories.

Repository-local `PROJECT-STATUS.yaml`, roadmaps and assurance evidence remain authoritative inputs for future enrichment, but the first stable contract deliberately limits automated inference to structured portfolio metadata plus issue/PR evidence. This keeps the ranking falsifiable and avoids pretending that free-form prose has deterministic semantics.

## Candidate states

| State | Meaning |
|---|---|
| `ready` | bounded work with no observed blocker |
| `blocked` | repository evidence explicitly marks the work blocked |
| `waiting-external` | progress depends on an upstream/external decision |
| `needs-judgment` | consequential architecture, governance, security, normative or release judgment |
| `maintenance` | dependency/chore work that should not outrank strategic execution by default |

Only `ready` items appear in the default "work now" view.

## Effort

Effort is bucketed: ≤15m, 15–30m, 30–60m, 1–2h, 2–4h, half-day, one-day, or **decompose**. The queue never claims minute-level precision. Estimates are heuristic and always carry confidence.

Work estimated beyond a day is intentionally surfaced as a decomposition candidate rather than a normal quick-choice item.

## Complexity

Complexity is independent from effort:

- `low` — routine bounded change;
- `medium` — multiple files/interfaces or non-trivial validation;
- `high` — cross-repository or substantial implementation;
- `consequential` — changes authority, normative semantics, security, compatibility or release qualification.

Consequential work is routed to `needs-judgment` even when its mechanical implementation appears small.

## Priority and leverage

Priority is computed from project-goal impact, portfolio impact, unblock value, release proximity, assurance value, adoption value and staleness pressure, minus explicit penalties for blockers, external waiting, low-confidence inference and maintenance noise.

Effort is **not** part of strategic priority. A separate leverage score divides positive priority by estimated effort. This preserves two distinct questions:

- **Priority:** what matters most?
- **Leverage:** what produces the most advancement within the time available?

## Falsification rules

The model is wrong and should be corrected if dependency noise routinely outranks release-critical work, blocked work appears executable, consequential work appears as a quick win, an ungoverned repository enters scope, estimates lack evidence/confidence, or a ranking cannot explain itself.

Repository-local overrides should be preferred over adding increasingly clever global heuristics when the evidence demonstrates a stable project-specific boundary.
