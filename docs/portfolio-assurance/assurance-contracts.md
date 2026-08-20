---
layout: default
title: Assurance Evidence Contracts
parent: Portfolio Assurance Monitor
nav_order: 4
---

# Assurance Evidence Contracts

The portfolio monitor evaluates whether evidence exists for a repository's governed assurance claims. It does **not** appoint a universal assurance provider and it does not replace repository-local authority over conformance, risk, release, or normative claims.

## Contract model

Each monitored flagship repository is assigned an assurance profile and one or more claims in `config/portfolio-monitor/assurance-contracts.yaml`.

A claim identifies:

- whether the evidence is required or optional;
- the evidence producer or repository-native control;
- the exact workflow or artifact used as evidence; and
- the freshness policy applied to that evidence.

The initial implementation uses GitHub Actions as the first evidence adapter because all current flagship repositories already expose native validation through observable workflows. Additional adapters can be added without changing the authority model.

## Evidence states

| State | Meaning |
|---|---|
| `satisfied` | Required evidence exists, succeeded, and meets its configured freshness policy. |
| `degraded` | The required evidence-producing control completed unsuccessfully. |
| `stale` | Successful evidence exists but does not cover the current governed repository revision. |
| `missing` | No completed evidence was observed in the governed evidence window. |
| `unobservable` | The evidence source should be observable but could not be collected. |
| `not-applicable` | No required claims apply to the evaluated scope. |
| `not-evaluated` | No governed contract or supported evidence adapter exists. |

These states are evidence-coverage states. `satisfied` does not mean that the monitor independently proves the underlying substantive claim.

## Current-HEAD binding

For claims configured with `freshness: current-head`, the monitor compares the workflow run's `head_sha` with the repository's observed default-branch HEAD SHA. A successful run against an earlier commit is reported as `stale`, not `satisfied`.

This prevents a repository from appearing assured merely because a validator succeeded at some earlier point in its history.

## Required and optional evidence

Required claims contribute to the repository assurance state and produce findings when missing, failed, stale, or unobservable.

Optional claims are still displayed as evidence observations but do not degrade the repository's aggregate assurance state. This is important for specialized assessment mechanisms. For example, RAHP cross-specification pressure testing may provide useful evidence without becoming a mandatory assurance provider for every repository or even every RAHP execution mode.

## Findings

The initial evidence-contract rules are:

- `ASSURANCE_EVIDENCE_MISSING`;
- `ASSURANCE_EVIDENCE_UNOBSERVABLE`;
- `ASSURANCE_CONTROL_FAILED`; and
- `ASSURANCE_EVIDENCE_STALE`.

Findings retain the existing monitor lifecycle model: a stable fingerprint identifies the same condition over time, and closure occurs only when a later observation no longer detects the condition.

## Authority boundary

The monitor can state that a configured control executed successfully against a specific repository revision. It must not silently transform that observation into a stronger substantive claim.

For example, the monitor may state that a repository's configured conformance workflow succeeded against the current HEAD. The authority to define what that workflow tests, what conformance means, and whether an exception is acceptable remains with the evidence-producing repository and its governance process.

## Extension model

Future evidence adapters may include conformance-result artifacts, release provenance, schema-validation records, signed attestations, external assurance feeds, and cross-repository dependency evidence. Each adapter must preserve:

1. subject identity;
2. producer identity;
3. revision or version coverage;
4. observation time;
5. result semantics; and
6. authority/provenance boundaries.
