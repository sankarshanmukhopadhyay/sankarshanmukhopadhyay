---
layout: default
title: Portfolio Assurance Dashboard
parent: Portfolio Assurance Monitor
nav_order: 1
---

# Portfolio Assurance Dashboard

**Observed:** 2026-08-12T04:12:05Z  
**Scope:** 10 flagship original repositories  
**Open findings:** 7

> This is first-party, evidence-based portfolio monitoring. Findings do not automatically modify portfolio status, maturity, lifecycle, authority, or disposition.

## Current observations

| Repository | Availability | Status declaration | Workflow evidence | Findings |
|---|---:|---:|---:|---:|
| [open-national-digital-trust-framework](https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework) | available | valid | 0 failed | 0 |
| [governance-authority-assurance-metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | available | valid | 3 failed | 1 |
| [agent-registry-protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | available | valid | 7 failed | 1 |
| [trust-systems-meta-model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | available | valid | 3 failed | 1 |
| [trust-infrastructure-schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | available | valid | 11 failed | 1 |
| [trust-graph-artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) | available | valid | 0 failed | 0 |
| [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | available | valid | 10 failed | 1 |
| [cawg-trqp-verifier-refimpl](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | available | valid | 0 failed | 0 |
| [trqp-conformance-suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | available | valid | 11 failed | 1 |
| [trqp-assurance-hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | available | valid | 14 failed | 1 |

## Findings

### PAM-1859777085AF: TRQP-TSPP

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-A0B485BEAEAD: agent-registry-protocol

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-53E0745899E3: governance-authority-assurance-metamodel

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-5E55077BA582: trqp-assurance-hub

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-3917673E35FF: trqp-conformance-suite

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-3638CC58C9D0: trust-infrastructure-schemas

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-C2F279CF8608: trust-systems-meta-model

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

## Governance boundary

The monitor observes public evidence and evaluates configured rules. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.
