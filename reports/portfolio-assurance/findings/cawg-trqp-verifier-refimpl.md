---
layout: default
title: Remediation dossier — cawg-trqp-verifier-refimpl
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `cawg-trqp-verifier-refimpl`

**Generated:** 2026-11-12T15:12:39Z  
**Open findings:** 1  
**Repository snapshot:** `e2121e7b5166abef46227f029ee072ea0d4e9afe`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/cawg-trqp-verifier-refimpl.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/cawg-trqp-verifier-refimpl.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 1 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 0 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-398FA7C456CF — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-EAED307E065C` at `2026-11-12T15:12:39Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/publication-link-audit.yml`
- Lifecycle: `open`; first observed `2026-10-26T13:00:04Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/branch-housekeeping.yml",
    ".github/workflows/ci.yml",
    ".github/workflows/dco.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/publication-link-audit.yml",
    ".github/workflows/pypi-publish.yml",
    ".github/workflows/release.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 20,
  "contract_evidence": {
    ".github/workflows/ci.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-11T10:31:16Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004299807",
        "name": "CI",
        "path": ".github/workflows/ci.yml",
        "run_number": 532,
        "run_started_at": "2026-11-11T10:31:16Z",
        "status": "completed",
        "updated_at": "2026-11-11T10:31:45Z",
        "workflow_id": 248717477
      }
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-11T10:31:16Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004299597",
        "name": "Deploy Documentation (Just the Docs)",
        "path": ".github/workflows/pages.yml",
        "run_number": 50,
        "run_started_at": "2026-11-11T10:31:16Z",
        "status": "completed",
        "updated_at": "2026-11-11T10:31:49Z",
        "workflow_id": 315515884
      }
    },
    ".github/workflows/pypi-publish.yml": {
      "available": true,
      "run": null
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-11-06T22:16:01Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/42303367119",
      "name": "Weekly merged-branch housekeeping",
      "path": ".github/workflows/branch-housekeeping.yml",
      "run_number": 4,
      "run_started_at": "2026-11-06T22:16:01Z",
      "status": "completed",
      "updated_at": "2026-11-06T22:16:10Z",
      "workflow_id": 381758282
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-11T10:31:16Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004299807",
      "name": "CI",
      "path": ".github/workflows/ci.yml",
      "run_number": 532,
      "run_started_at": "2026-11-11T10:31:16Z",
      "status": "completed",
      "updated_at": "2026-11-11T10:31:45Z",
      "workflow_id": 248717477
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-11T10:31:16Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004299597",
      "name": "Deploy Documentation (Just the Docs)",
      "path": ".github/workflows/pages.yml",
      "run_number": 50,
      "run_started_at": "2026-11-11T10:31:16Z",
      "status": "completed",
      "updated_at": "2026-11-11T10:31:49Z",
      "workflow_id": 315515884
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-09T11:24:08Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/42608753583",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 3,
      "run_started_at": "2026-11-09T11:24:08Z",
      "status": "completed",
      "updated_at": "2026-11-09T11:24:49Z",
      "workflow_id": 396546945
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-11T10:31:16Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004299550",
      "name": "Release",
      "path": ".github/workflows/release.yml",
      "run_number": 26,
      "run_started_at": "2026-11-11T10:31:16Z",
      "status": "completed",
      "updated_at": "2026-11-11T10:31:54Z",
      "workflow_id": 347445405
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-11T10:32:38Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004491596",
      "name": "pip in / for pytest - Update #1695584426",
      "path": "dynamic/dependabot/dependabot-updates",
      "run_number": 117,
      "run_started_at": "2026-11-11T10:32:38Z",
      "status": "completed",
      "updated_at": "2026-11-11T10:34:27Z",
      "workflow_id": 261742867
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-11T10:31:23Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "e2121e7b5166abef46227f029ee072ea0d4e9afe",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/43004314852",
      "name": "Configured Graph Update: pip in /. #1695580550",
      "path": "dynamic/dependabot/update-graph",
      "run_number": 26,
      "run_started_at": "2026-11-11T10:31:23Z",
      "status": "completed",
      "updated_at": "2026-11-11T10:32:08Z",
      "workflow_id": 303797171
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-11-09T11:24:08Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/42608753583",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 3,
      "run_started_at": "2026-11-09T11:24:08Z",
      "status": "completed",
      "updated_at": "2026-11-09T11:24:49Z",
      "workflow_id": 396546945
    }
  ],
  "unresolved_failures": 1,
  "workflows_examined": 7
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
