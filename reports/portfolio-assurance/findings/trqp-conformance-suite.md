---
layout: default
title: Remediation dossier — trqp-conformance-suite
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `trqp-conformance-suite`

**Generated:** 2026-08-20T11:13:29Z  
**Open findings:** 1  
**Repository snapshot:** `294bf81ffce8eb091a904f859adde0549041003f`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trqp-conformance-suite.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/trqp-conformance-suite.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-828DF4A3DE49 — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-61C37E873800` at `2026-08-20T11:13:29Z`
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
  "evidence_head_sha": "452483a29e3901eba82a36dc27721bbc53f023ce",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "294bf81ffce8eb091a904f859adde0549041003f",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-20T09:48:03Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "452483a29e3901eba82a36dc27721bbc53f023ce",
    "html_url": "https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite/actions/runs/32355721574",
    "name": "Deploy documentation to GitHub Pages",
    "path": ".github/workflows/pages.yml",
    "run_number": 14,
    "run_started_at": "2026-08-20T09:48:03Z",
    "status": "completed",
    "updated_at": "2026-08-20T09:48:35Z",
    "workflow_id": 316454130
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
