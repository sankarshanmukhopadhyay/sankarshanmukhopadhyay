---
layout: default
title: Development Finding Feeds
parent: Portfolio Assurance Monitor
nav_order: 4
---

# Development finding feeds

The Portfolio Assurance Monitor publishes each current finding in two forms: a human-readable Markdown feed and a machine-readable JSON feed scoped to the affected repository. The purpose is to make assurance findings portable into the repository's next development or release cycle without turning the portfolio monitor into a source of implementation authority.

## Intended workflow

```text
portfolio observation
        ↓
stable finding fingerprint
        ↓
per-repository JSON / Markdown feed
        ↓
release planning or development context
        ↓
human disposition in target repository
        ↓
implementation + validation evidence
        ↓
subsequent monitor run verifies recovery
```

A development team can download the repository feed and provide it alongside the repository source when planning a release. The feed contains the stable finding fingerprint, observation identifier, rule, severity, claim, evidence, and recommended action. A finding is therefore traceable across repeated observations even when the date-scoped observation ID changes.

## Download convention

For a repository named `example-repository`:

```text
https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/reports/portfolio-assurance/findings/example-repository.json
https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/reports/portfolio-assurance/findings/example-repository.md
```

The machine-readable index is published at:

```text
https://sankarshanmukhopadhyay.github.io/sankarshanmukhopadhyay/reports/portfolio-assurance/findings/index.json
```

Feeds are generated for governed repositories even when they contain zero findings. This is intentional: an empty feed is machine-verifiable evidence that the current monitor run has no open portfolio-assurance findings for that repository.

## Governance boundary

The feed is an input to development, not a command channel. It cannot change repository authority, normative content, maturity, lifecycle, release status, or issue state. Findings must be reviewed and dispositioned by the repository's own governance process. Closure should be supported by implementation and validation evidence, after which a later monitor run can verify that the condition is no longer observed.
