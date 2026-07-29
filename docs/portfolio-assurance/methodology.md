---
layout: default
title: Methodology
parent: Portfolio Assurance Monitor
nav_order: 2
---

# Monitoring methodology

## Scope derivation

The monitor does not maintain a second repository inventory. It reads `data/repository-status.yaml` and applies the selectors in `config/portfolio-monitor/policy.yaml`. The initial profile includes repositories that are simultaneously:

- `portfolio_disposition: included`;
- `tier: flagship`;
- `provenance: original`.

The portfolio control-plane repository is excluded from member-repository evaluation because it owns the classification and reporting process.

## Evidence collected

The initial implementation collects public evidence only:

| Evidence | Purpose | Limitation |
|---|---|---|
| Repository metadata | Availability, default branch, archive state, recent push | Activity is not a maturity proxy |
| Required `PROJECT-STATUS.yaml` | Presence and YAML readability | Semantic consistency remains a governed review task |
| Recent default-branch workflow runs | Surface unresolved execution failures | A failed run may be superseded or intentionally accepted |
| Portfolio review dates | Detect overdue governance review | Review quality requires human evidence |

## Finding rules

The initial rule set produces findings for repository unavailability, overdue reviews, missing or unreadable required status declarations, recent default-branch workflow failures, and prolonged inactivity requiring status review.

Findings are observations against declared policy. They are not automatic decisions. Every finding contains `automatic_effect: none`.

## Evidence and assurance level

The monitor provides first-party, repeatable, machine-produced evidence. It does not claim independent assessment. A stronger assurance profile could later add signed evidence bundles, schema-level declaration comparison, release-to-status reconciliation, cross-repository version compatibility, and independent reruns.
