---
layout: default
title: Remediation dossier — cawg-trqp-verifier-refimpl
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `cawg-trqp-verifier-refimpl`

**Generated:** 2026-11-03T23:21:51Z  
**Open findings:** 1  
**Repository snapshot:** `f007b9316350145138f4169aaf65273843e41080`  
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

- Observation: `PAM-F33D971A0C96` at `2026-11-03T23:21:51Z`
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
  "completed_examined": 23,
  "contract_evidence": {
    ".github/workflows/ci.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-03T03:55:26Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "f007b9316350145138f4169aaf65273843e41080",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41575054440",
        "name": "CI",
        "path": ".github/workflows/ci.yml",
        "run_number": 510,
        "run_started_at": "2026-11-03T03:55:26Z",
        "status": "completed",
        "updated_at": "2026-11-03T03:56:05Z",
        "workflow_id": 248717477
      }
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-03T03:55:26Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "f007b9316350145138f4169aaf65273843e41080",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41575054319",
        "name": "Deploy Documentation (Just the Docs)",
        "path": ".github/workflows/pages.yml",
        "run_number": 48,
        "run_started_at": "2026-11-03T03:55:26Z",
        "status": "completed",
        "updated_at": "2026-11-03T03:56:01Z",
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
      "created_at": "2026-10-30T21:39:44Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41132681639",
      "name": "Weekly merged-branch housekeeping",
      "path": ".github/workflows/branch-housekeeping.yml",
      "run_number": 3,
      "run_started_at": "2026-10-30T21:39:44Z",
      "status": "completed",
      "updated_at": "2026-10-30T21:39:56Z",
      "workflow_id": 381758282
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-03T03:55:26Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41575054440",
      "name": "CI",
      "path": ".github/workflows/ci.yml",
      "run_number": 510,
      "run_started_at": "2026-11-03T03:55:26Z",
      "status": "completed",
      "updated_at": "2026-11-03T03:56:05Z",
      "workflow_id": 248717477
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-03T03:55:26Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41575054319",
      "name": "Deploy Documentation (Just the Docs)",
      "path": ".github/workflows/pages.yml",
      "run_number": 48,
      "run_started_at": "2026-11-03T03:55:26Z",
      "status": "completed",
      "updated_at": "2026-11-03T03:56:01Z",
      "workflow_id": 315515884
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-02T10:56:08Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41432727239",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 2,
      "run_started_at": "2026-11-02T10:56:08Z",
      "status": "completed",
      "updated_at": "2026-11-02T10:56:55Z",
      "workflow_id": 396546945
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-03T03:55:26Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "f007b9316350145138f4169aaf65273843e41080",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41575054380",
      "name": "Release",
      "path": ".github/workflows/release.yml",
      "run_number": 21,
      "run_started_at": "2026-11-03T03:55:26Z",
      "status": "completed",
      "updated_at": "2026-11-03T03:55:43Z",
      "workflow_id": 347445405
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-03T02:05:19Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "858901fc68a419b77fb154bf5c3797d91636c764",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41563893240",
      "name": "github_actions in / for actions/upload-artifact - Update #1676206538",
      "path": "dynamic/dependabot/dependabot-updates",
      "run_number": 112,
      "run_started_at": "2026-11-03T02:05:19Z",
      "status": "completed",
      "updated_at": "2026-11-03T02:06:30Z",
      "workflow_id": 261742867
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-03T03:07:41Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "dc6e36558a998b0310098232af5550e0c6cc78f2",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41570306152",
      "name": "Configured Graph Update: pip in /. #1676334349",
      "path": "dynamic/dependabot/update-graph",
      "run_number": 25,
      "run_started_at": "2026-11-03T03:07:41Z",
      "status": "completed",
      "updated_at": "2026-11-03T03:08:39Z",
      "workflow_id": 303797171
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-11-02T10:56:08Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/41432727239",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 2,
      "run_started_at": "2026-11-02T10:56:08Z",
      "status": "completed",
      "updated_at": "2026-11-02T10:56:55Z",
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
