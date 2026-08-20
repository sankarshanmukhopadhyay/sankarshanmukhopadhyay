---
layout: default
title: Remediation dossier — cawg-trqp-verifier-refimpl
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `cawg-trqp-verifier-refimpl`

**Generated:** 2026-08-20T11:13:29Z  
**Open findings:** 1  
**Repository snapshot:** `2870653c12748fc54ed05822f079ccac7424a7ec`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/cawg-trqp-verifier-refimpl.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/cawg-trqp-verifier-refimpl.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 0 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-2B2778E887E9 — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-EA2FD15868CF` at `2026-08-20T11:13:29Z`
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
  "evidence_head_sha": "39484f72b8cb01935d1303b0dd4f6fce0ad02ab7",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "2870653c12748fc54ed05822f079ccac7424a7ec",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-20T09:39:31Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "39484f72b8cb01935d1303b0dd4f6fce0ad02ab7",
    "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/32354999523",
    "name": "Deploy Documentation (Just the Docs)",
    "path": ".github/workflows/pages.yml",
    "run_number": 29,
    "run_started_at": "2026-08-20T09:39:31Z",
    "status": "completed",
    "updated_at": "2026-08-20T09:40:05Z",
    "workflow_id": 315515884
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
