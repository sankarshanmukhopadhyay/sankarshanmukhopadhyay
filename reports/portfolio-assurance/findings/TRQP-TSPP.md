---
layout: default
title: Remediation dossier — TRQP-TSPP
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `TRQP-TSPP`

**Generated:** 2026-08-20T11:13:29Z  
**Open findings:** 1  
**Repository snapshot:** `b1d592ee0b58e47e6741ab4f583c824cd4c833d4`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/TRQP-TSPP.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/TRQP-TSPP.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-54FF6F2FAF55 — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-ED22FC52DC48` at `2026-08-20T11:13:29Z`
- Severity: `medium`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-08-20T11:13:29Z`
- Claim: Required assurance evidence is successful but does not cover the current governed repository state.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": "4baefbd17369940b5e261bb62a0b3d7930d0177a",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "b1d592ee0b58e47e6741ab4f583c824cd4c833d4",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-20T09:47:57Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "4baefbd17369940b5e261bb62a0b3d7930d0177a",
    "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/32355712824",
    "name": "Deploy documentation to GitHub Pages",
    "path": ".github/workflows/pages.yml",
    "run_number": 13,
    "run_started_at": "2026-08-20T09:47:57Z",
    "status": "completed",
    "updated_at": "2026-08-20T09:48:34Z",
    "workflow_id": 316453200
  }
}
```

### Remediation objective

Regenerate assurance evidence against the current governed repository revision.

### Acceptance criteria

- [ ] The evidence-producing workflow succeeds against the current default-branch HEAD.
- [ ] The evidence HEAD SHA matches the governed repository HEAD SHA.

### Verification

- Execute the configured control on the current default branch and rerun the monitor.
