---
layout: default
title: Remediation dossier — trqp-assurance-hub
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `trqp-assurance-hub`

**Generated:** 2026-08-20T11:13:29Z  
**Open findings:** 1  
**Repository snapshot:** `ee5e767e9134bb78dd8ee81772b75cc525d80a9b`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trqp-assurance-hub.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trqp-assurance-hub.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-5FA38CA6ACF4 — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-75FF505A7FD5` at `2026-08-20T11:13:29Z`
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
  "evidence_head_sha": "da64e3b8032eff0efa5ab04302c964ee648c1618",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "ee5e767e9134bb78dd8ee81772b75cc525d80a9b",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-20T09:48:11Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "da64e3b8032eff0efa5ab04302c964ee648c1618",
    "html_url": "https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/actions/runs/32355733023",
    "name": "Deploy documentation to GitHub Pages",
    "path": ".github/workflows/pages.yml",
    "run_number": 15,
    "run_started_at": "2026-08-20T09:48:11Z",
    "status": "completed",
    "updated_at": "2026-08-20T09:48:51Z",
    "workflow_id": 316454965
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
