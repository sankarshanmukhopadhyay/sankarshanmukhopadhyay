---
layout: default
title: Remediation dossier — trust-infrastructure-schemas
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `trust-infrastructure-schemas`

**Generated:** 2026-08-28T11:22:17Z  
**Open findings:** 2  
**Repository snapshot:** `bc6fb1a339fd8e8c3469f9e0bd999efdd6726412`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trust-infrastructure-schemas.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trust-infrastructure-schemas.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 2 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-67C44D44EC73 — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-EF4EF1F007AE` at `2026-08-28T11:22:17Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-08-27T22:15:16Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": null,
  "freshness_policy": "current-head",
  "reason": "no completed workflow execution was observed inside the governed lookback window",
  "repository_head_sha": null,
  "state": "missing",
  "workflow": null
}
```

### Remediation objective

Restore or execute the repository-native control required by the governed assurance contract.

### Acceptance criteria

- [ ] The required evidence is observable inside the governed lookback window.
- [ ] The evidence is attributable to the configured repository-native control.

### Verification

- Execute the required repository-native control and rerun the portfolio monitor.

## PF-38863D0F6C2C — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-BA1525B0B5A1` at `2026-08-28T11:22:17Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/validate-schemas.yml`
- Lifecycle: `open`; first observed `2026-08-27T22:15:16Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "schema_validation",
  "evidence_head_sha": null,
  "freshness_policy": "current-head",
  "reason": "no completed workflow execution was observed inside the governed lookback window",
  "repository_head_sha": null,
  "state": "missing",
  "workflow": null
}
```

### Remediation objective

Restore or execute the repository-native control required by the governed assurance contract.

### Acceptance criteria

- [ ] The required evidence is observable inside the governed lookback window.
- [ ] The evidence is attributable to the configured repository-native control.

### Verification

- Execute the required repository-native control and rerun the portfolio monitor.
