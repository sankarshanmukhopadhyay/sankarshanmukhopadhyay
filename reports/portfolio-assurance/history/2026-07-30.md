---
layout: default
title: Portfolio Assurance Dashboard
nav_order: 6
---

# Portfolio Assurance Dashboard

**Observed:** 2026-07-30T02:36:25Z  
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
| [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP) | available | valid | 4 failed | 1 |
| [cawg-trqp-verifier-refimpl](https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl) | available | attention | 8 failed | 2 |
| [trqp-conformance-suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite) | available | valid | 11 failed | 1 |
| [trqp-assurance-hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub) | available | valid | 16 failed | 1 |

## Findings

### PAM-73F19805853F: agent-registry-protocol

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-01A0953B91D9: cawg-trqp-verifier-refimpl

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-7A3E87A0193A: governance-authority-assurance-metamodel

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-13A88DFC6454: TRQP-TSPP

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-67C1287E784B: agent-registry-protocol

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-A4EFEC7D61C0: cawg-trqp-verifier-refimpl

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-E14CA0EFDB89: trqp-assurance-hub

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-6A38FF4DFF26: trqp-conformance-suite

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-1B84D7CE0D5F: trust-infrastructure-schemas

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-C2173C6BCB40: trust-systems-meta-model

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

## Governance boundary

The monitor observes public evidence and evaluates configured rules. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.
