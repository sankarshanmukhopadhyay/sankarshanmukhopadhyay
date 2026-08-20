---
layout: default
title: Portfolio Assurance Monitor
nav_order: 5
has_children: true
---

# Portfolio Assurance Monitor

The Portfolio Assurance Monitor is the executable evidence and drift-detection layer for the curated trust-infrastructure portfolio. It derives its scope from `data/repository-status.yaml`, collects public GitHub evidence, evaluates deterministic rules, and publishes findings without changing governed portfolio state.

Repository-local governance is additionally enforced through the **Member Status Contract Assurance** workflow. Every repository whose central status record requires a `member-declaration` is fetched independently, validated against `schemas/project-status.schema.json`, and reconciled against the portfolio registry for project state and normative authority scope. This prevents a repository from satisfying governance merely by exposing parseable YAML.

## Operating model

1. The portfolio register declares membership, tier, maturity, lifecycle, authority, provenance, and review dates.
2. The monitor selects flagship original repositories according to the monitoring policy for operational observation and finding lifecycle management.
3. The member-status contract validator selects every repository whose `status_source` is a required `member-declaration`, independent of portfolio tier.
4. Required repository-local declarations are fetched from the repository default branch and validated against the canonical project-status schema.
5. Declared project identity, maturity, lifecycle, operational status, specification status, and normative authority scope are reconciled against central portfolio governance.
6. Public GitHub evidence and default-branch workflow state are collected for the monitor's operational scope.
7. Deterministic rules produce machine-readable findings with stable cross-run fingerprints, remediation objectives, acceptance criteria, and verification guidance.
8. Findings are consolidated into repository remediation dossiers that can travel with repository source into implementation work.
9. Account discovery nominates genuinely unclassified public repositories for central review without auto-enrolment.
10. Eligible repository-local findings may be deduplicated and routed to the affected repository when scoped issue publication is enabled.
11. Later runs retain finding lifecycle evidence while repository governance retains authority over implementation and issue closure.

## Member status contract assurance

The federated contract validator produces `reports/portfolio-assurance/member-status-contracts.json` as machine-readable evidence. A required declaration is clear only when all of the following are true:

- the configured declaration is observable on the repository default branch;
- the YAML parses to a mapping;
- the declaration satisfies the canonical JSON Schema;
- project identity and governed status fields match `data/repository-status.yaml`; and
- `authority.normative_scope` exactly matches the authority scope assigned by portfolio governance.

A failure blocks the Member Status Contract Assurance workflow but does not automatically alter portfolio maturity, lifecycle, authority, or repository-local content. Disposition remains a governed human decision.

## Start here

- [Assurance dashboard](dashboard.md)
- [Remediation dossiers](findings.md)
- [Methodology](methodology.md)
- [Operations](operations.md)
- [Portfolio classification policy](../portfolio-classification-policy.md)
- [Portfolio drift review](../portfolio-drift-review.md)

## Assurance boundary

This is first-party assurance. It improves repeatability, evidence retention, and review discipline, but does not represent independent certification. Repository-local tests, release artefacts, and normative content remain authoritative within their respective scopes.

A clear member-status contract means the declared governance state is observable, schema-valid, and aligned with the central portfolio authority record. It does **not** mean substantive conformance, security, harms, interoperability, or independent assurance has been established unless those dimensions are separately evidenced.
