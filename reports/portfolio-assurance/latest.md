---
layout: default
title: Portfolio Assurance Report — 2026-08-03
nav_exclude: true
search_exclude: true
---

# Portfolio Assurance Report — 2026-08-03

**Observed:** 2026-08-03T05:53:40Z  
**Scope:** 10 flagship original repositories  
**Open findings:** 10

> This is first-party, evidence-based portfolio monitoring. Findings do not automatically modify portfolio status, maturity, lifecycle, authority, or disposition.

## Current observations

| Repository | Availability | Status declaration | Workflow evidence | Findings |
|---|---:|---:|---:|---:|
| [open-national-digital-trust-framework](https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework) | available | valid | 0 failed | 0 |
| [governance-authority-assurance-metamodel](https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel) | available | attention | 0 failed | 1 |
| [agent-registry-protocol](https://github.com/sankarshanmukhopadhyay/agent-registry-protocol) | available | attention | 6 failed | 2 |
| [trust-systems-meta-model](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) | available | valid | 3 failed | 1 |
| [trust-infrastructure-schemas](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) | available | valid | 11 failed | 1 |
| [trust-graph-artifacts](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) | available | valid | 0 failed | 0 |
| [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | available | valid | 10 failed | 1 |
| [cawg-trqp-verifier-refimpl](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | available | attention | 2 failed | 2 |
| [trqp-conformance-suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | available | valid | 10 failed | 1 |
| [trqp-assurance-hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | available | valid | 15 failed | 1 |

## Findings

### PAM-0CA992CCB05A: agent-registry-protocol

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-8D48750AC52A: cawg-trqp-verifier-refimpl

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-BB862543025D: governance-authority-assurance-metamodel

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-61B45868517E: TRQP-TSPP

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-0140F504F5F7: agent-registry-protocol

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-AD724FA4AB50: cawg-trqp-verifier-refimpl

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-7F9A7897462A: trqp-assurance-hub

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-60498A1F4DDF: trqp-conformance-suite

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-927DEE718AC8: trust-infrastructure-schemas

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-E8D214D4CF21: trust-systems-meta-model

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

## Governance boundary

The monitor observes public evidence and evaluates configured rules. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.
