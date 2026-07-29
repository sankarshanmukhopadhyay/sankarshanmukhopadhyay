---
layout: default
title: Portfolio Assurance Dashboard
nav_order: 6
---

# Portfolio Assurance Dashboard

**Observed:** 2026-07-29T14:07:40Z  
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

### PAM-B1F7373560E2: agent-registry-protocol

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-DE85CB93134C: cawg-trqp-verifier-refimpl

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-A8ABDDF3E722: governance-authority-assurance-metamodel

- **Rule:** `STATUS_DECLARATION_MISSING`
- **Severity:** `high`
- **Claim:** A required repository-local status declaration must exist.
- **Recommended action:** Add the required status declaration or revise the governed status-source contract.
- **Automatic effect:** `none`

### PAM-874BFE44561D: TRQP-TSPP

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-74CC1BDDC034: agent-registry-protocol

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-1256024271CE: cawg-trqp-verifier-refimpl

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-F10ABA79DED5: trqp-assurance-hub

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-346A8771A4FA: trqp-conformance-suite

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-FE485BABB33C: trust-infrastructure-schemas

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

### PAM-E6030F233BB4: trust-systems-meta-model

- **Rule:** `DEFAULT_BRANCH_WORKFLOW_FAILURE`
- **Severity:** `medium`
- **Claim:** Recent completed default-branch workflows should not contain unresolved failures.
- **Recommended action:** Review the failed workflow and record remediation or accepted risk.
- **Automatic effect:** `none`

## Governance boundary

The monitor observes public evidence and evaluates configured rules. Portfolio classifications change only through reviewed governance updates. Repository-local evidence remains authoritative for implementation and release claims.
