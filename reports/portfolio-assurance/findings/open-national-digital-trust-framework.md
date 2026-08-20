---
layout: default
title: Remediation dossier — open-national-digital-trust-framework
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `open-national-digital-trust-framework`

**Generated:** 2026-08-20T10:54:49Z  
**Open findings:** 2  
**Repository snapshot:** `8ed4f45621cba23539a99f4336bf5f6b1a8d9702`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/open-national-digital-trust-framework.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/open-national-digital-trust-framework.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 2 |
| Governance | `evaluated` | 0 |
| Assurance | `not-evaluated` | 0 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-ADCE64569869 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-BEB5B50F9786` at `2026-08-20T10:54:49Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-08-20T10:54:49Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "completed_examined": 12,
  "lookback_days": 7,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-08-20T10:33:58Z",
      "head_sha": "8ed4f45621cba23539a99f4336bf5f6b1a8d9702",
      "html_url": "https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework/actions/runs/32359554330",
      "name": "Build and deploy GitHub Pages",
      "path": ".github/workflows/pages.yml",
      "updated_at": "2026-08-20T10:34:13Z",
      "workflow_id": 317410093
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 2
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.

## PF-DCC0C9AA3F10 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-FB81693ED37C` at `2026-08-20T10:54:49Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/quality.yml`
- Lifecycle: `open`; first observed `2026-08-20T10:54:49Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "completed_examined": 12,
  "lookback_days": 7,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-08-20T10:33:58Z",
      "head_sha": "8ed4f45621cba23539a99f4336bf5f6b1a8d9702",
      "html_url": "https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework/actions/runs/32359554360",
      "name": "Documentation quality",
      "path": ".github/workflows/quality.yml",
      "updated_at": "2026-08-20T10:34:12Z",
      "workflow_id": 317410095
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 2
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
