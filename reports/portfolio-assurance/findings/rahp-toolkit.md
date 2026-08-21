---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-08-21T01:57:07Z  
**Open findings:** 1  
**Repository snapshot:** `d66dc86bc8229cda340bac181ae73c80860e6180`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 1 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 0 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-85368F53178F — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-F72E4B659F49` at `2026-08-21T01:57:07Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/cross-spec-pressure-test.yml`
- Lifecycle: `open`; first observed `2026-08-19T03:07:01Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "available": true,
  "completed_examined": 50,
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-08-19T00:54:25Z",
      "event": "workflow_dispatch",
      "head_branch": "main",
      "head_sha": "f561c7541b8c31365efff36a2cb8d7872b547906",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32202996271",
      "name": "Run CAWG/C2PA cross-specification pressure test",
      "path": ".github/workflows/cawg-cross-spec-pressure-test.yml",
      "run_number": 1,
      "run_started_at": "2026-08-19T00:54:25Z",
      "status": "completed",
      "updated_at": "2026-08-19T00:54:47Z",
      "workflow_id": 337419009
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-17T04:04:12Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ec068f0077305d15e9e6ae3e1854fd7d39920592",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/31993181629",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 6,
      "run_started_at": "2026-08-17T04:04:12Z",
      "status": "completed",
      "updated_at": "2026-08-17T04:04:26Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "failure",
      "created_at": "2026-08-19T00:44:33Z",
      "event": "workflow_dispatch",
      "head_branch": "main",
      "head_sha": "420aae6b5d8fab2f242018b8038b38159d0fdfa0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32202382447",
      "name": "Run cross-specification pressure test",
      "path": ".github/workflows/cross-spec-pressure-test.yml",
      "run_number": 2,
      "run_started_at": "2026-08-19T00:44:33Z",
      "status": "completed",
      "updated_at": "2026-08-19T00:44:49Z",
      "workflow_id": 337404001
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-19T04:38:26Z",
      "event": "workflow_dispatch",
      "head_branch": "main",
      "head_sha": "6969731623a09d862c51e7fda641551190b3424d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32216489952",
      "name": "Run DTG cross-specification pressure test",
      "path": ".github/workflows/dtg-cross-spec-pressure-test.yml",
      "run_number": 3,
      "run_started_at": "2026-08-19T04:38:26Z",
      "status": "completed",
      "updated_at": "2026-08-19T04:38:47Z",
      "workflow_id": 337419010
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-20T04:17:52Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "e13a0d2e9640ec35ef0daa2b58fa2860a97703f6",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32331362664",
      "name": "RAHP instance change watch",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 9,
      "run_started_at": "2026-08-20T04:17:52Z",
      "status": "completed",
      "updated_at": "2026-08-20T04:18:54Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-20T06:19:14Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "d66dc86bc8229cda340bac181ae73c80860e6180",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32339100389",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 62,
      "run_started_at": "2026-08-20T06:19:14Z",
      "status": "completed",
      "updated_at": "2026-08-20T06:21:00Z",
      "workflow_id": 333196290
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-20T06:19:14Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "d66dc86bc8229cda340bac181ae73c80860e6180",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32339100508",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 73,
      "run_started_at": "2026-08-20T06:19:14Z",
      "status": "completed",
      "updated_at": "2026-08-20T06:20:19Z",
      "workflow_id": 331522431
    }
  ],
  "lookback_days": 7,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-08-19T00:44:33Z",
      "event": "workflow_dispatch",
      "head_branch": "main",
      "head_sha": "420aae6b5d8fab2f242018b8038b38159d0fdfa0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32202382447",
      "name": "Run cross-specification pressure test",
      "path": ".github/workflows/cross-spec-pressure-test.yml",
      "run_number": 2,
      "run_started_at": "2026-08-19T00:44:33Z",
      "status": "completed",
      "updated_at": "2026-08-19T00:44:49Z",
      "workflow_id": 337404001
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
