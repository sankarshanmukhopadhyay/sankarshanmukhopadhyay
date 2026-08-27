---
layout: default
title: Remediation dossier — open-national-digital-trust-framework
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `open-national-digital-trust-framework`

**Generated:** 2026-08-27T22:15:16Z  
**Open findings:** 2  
**Repository snapshot:** `9dcd9af8fe5d1818fa7da94b55dc3b22a7fe5661`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/open-national-digital-trust-framework.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/open-national-digital-trust-framework.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 2 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-7AB5F3D457EE — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-97AB7F8855B0` at `2026-08-27T22:15:16Z`
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

## PF-EE7FADD90617 — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-EAE99E5C2075` at `2026-08-27T22:15:16Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/quality.yml`
- Lifecycle: `open`; first observed `2026-08-27T22:15:16Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "specification_quality",
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
