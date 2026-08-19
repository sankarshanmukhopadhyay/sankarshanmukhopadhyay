---
layout: default
title: Portfolio Assurance Monitor
nav_order: 5
has_children: true
---

# Portfolio Assurance Monitor

The Portfolio Assurance Monitor is the executable evidence and drift-detection layer for the curated trust-infrastructure portfolio. It derives its scope from `data/repository-status.yaml`, collects public GitHub evidence, evaluates deterministic rules, and publishes findings without changing governed portfolio state.

## Operating model

1. The portfolio register declares membership, tier, maturity, lifecycle, authority, provenance, and review dates.
2. The monitor selects flagship original repositories according to the monitoring policy.
3. Public evidence is collected from GitHub and required repository-local status declarations.
4. Deterministic rules produce machine-readable findings with stable cross-run fingerprints, remediation objectives, acceptance criteria, and verification guidance.
5. Findings are consolidated into repository remediation dossiers that can travel with repository source into implementation work.
6. Account discovery nominates genuinely unclassified public repositories for central review without auto-enrolment.
7. Eligible repository-local findings may be deduplicated and routed to the affected repository when scoped issue publication is enabled.
8. Later runs retain finding lifecycle evidence while repository governance retains authority over implementation and issue closure.

## Start here

- [Assurance dashboard](dashboard.md)
- [Remediation dossiers](findings.md)
- [Methodology](methodology.md)
- [Operations](operations.md)
- [Portfolio classification policy](../portfolio-classification-policy.md)
- [Portfolio drift review](../portfolio-drift-review.md)

## Assurance boundary

This is first-party assurance. It improves repeatability, evidence retention, and review discipline, but does not represent independent certification. Repository-local tests, release artefacts, and normative content remain authoritative within their respective scopes.
