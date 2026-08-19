---
layout: default
title: Remediation Dossiers
parent: Portfolio Assurance Monitor
nav_order: 2
---

# Repository remediation dossiers

The Portfolio Assurance Monitor publishes a **consolidated remediation dossier** for each governed repository. The dossier is the portable handoff artifact between portfolio-level observation and repository-local remediation.

The intended workflow is deliberately simple:

```text
portfolio observation
        ↓
deterministic finding
        ↓
repository remediation dossier
        ↓
download Markdown / JSON
        ↓
provide dossier + repository source
        ↓
repository-local remediation
        ↓
validation and implementation evidence
        ↓
later monitor run
        ↓
open finding or recorded resolution
```

## What to download

For a repository named `example-repository`, the monitor publishes:

```text
reports/portfolio-assurance/findings/example-repository.md
reports/portfolio-assurance/findings/example-repository.json
```

The dashboard exposes a rendered dossier plus direct raw Markdown and JSON download links. The Markdown dossier is designed to be supplied alongside a repository archive during development or release work. JSON is the canonical machine-readable equivalent for automation and future cross-repository tooling.

## What a dossier contains

A dossier records:

- the affected repository;
- the observation time;
- the default-branch commit SHA when it was observable;
- the assessment dimensions that were evaluated and those explicitly not evaluated;
- every currently open finding for that repository;
- stable finding fingerprints;
- evidence supporting each finding;
- remediation objectives;
- acceptance criteria;
- verification guidance; and
- finding lifecycle state.

This allows a remediation task to begin from the evidence package rather than reconstructing the monitor's reasoning from a dashboard entry.

## Snapshot provenance

When live collection can observe the repository default branch, the dossier records its current commit SHA. This binds the finding set to the repository state against which it was evaluated.

If the SHA cannot be observed, the dossier says so explicitly. Missing provenance must not be replaced with a guessed repository state.

## Finding lifecycle

`reports/portfolio-assurance/finding-lifecycle.json` tracks stable finding fingerprints across monitor runs.

A finding has a stable identity based on repository, rule, and subject. Repeated observations update `last_observed`. When a later monitor run no longer observes an open fingerprint, the lifecycle registry records it as resolved with a resolution time.

Disappearance is therefore not silently discarded; the monitor retains evidence that the condition was previously open and later ceased to be observed.

## Empty dossiers do not mean assured

Dossiers are generated even when a repository has zero findings. An empty dossier means only:

> no findings were produced by the rules in dimensions currently marked `evaluated`.

It does **not** mean substantive assurance, conformance, RAHP, or cross-specification review has passed when those dimensions are marked `not-evaluated`.

## Authority boundary

The portfolio monitor owns observation, rule evaluation, finding identity, and finding lifecycle evidence. It does not own the affected repository's implementation decision.

The target repository retains authority over:

- source and specification changes;
- risk acceptance;
- release decisions;
- normative interpretation; and
- remediation implementation.

A dossier is therefore an evidence-bearing development input, not a command channel.
