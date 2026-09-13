---
layout: default
title: Remediation dossier — trust-graph-artifacts
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `trust-graph-artifacts`

**Generated:** 2026-09-13T04:46:05Z  
**Open findings:** 2  
**Repository snapshot:** `3694d63c677f02a4e4984f665cf8d60fc447993c`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trust-graph-artifacts.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trust-graph-artifacts.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 2 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-2B6A1AD853DF — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-B31E3A5E20B1` at `2026-09-13T04:46:05Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-09-10T02:21:16Z`
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

## PF-820B3E478EBA — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-8130B047B25A` at `2026-09-13T04:46:05Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/validate-tsmm-native.yml`
- Lifecycle: `open`; first observed `2026-09-10T02:21:16Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "native_model_validation",
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
