---
layout: default
title: Remediation dossier — cawg-trqp-verifier-refimpl
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `cawg-trqp-verifier-refimpl`

**Generated:** 2026-10-27T05:02:19Z  
**Open findings:** 1  
**Repository snapshot:** `ada8927d17f0d5007b83416d412c1f656e01da6d`  
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

- Observation: `PAM-43B6A440EF09` at `2026-10-27T05:02:19Z`
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
  "completed_examined": 38,
  "contract_evidence": {
    ".github/workflows/ci.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-26T01:31:59Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40254676124",
        "name": "CI",
        "path": ".github/workflows/ci.yml",
        "run_number": 434,
        "run_started_at": "2026-10-26T01:31:59Z",
        "status": "completed",
        "updated_at": "2026-10-26T01:32:26Z",
        "workflow_id": 248717477
      }
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-26T01:31:59Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
        "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40254676085",
        "name": "Deploy Documentation (Just the Docs)",
        "path": ".github/workflows/pages.yml",
        "run_number": 44,
        "run_started_at": "2026-10-26T01:31:59Z",
        "status": "completed",
        "updated_at": "2026-10-26T01:33:12Z",
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
      "created_at": "2026-10-23T20:35:47Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "47e08a7eb8cadb95b6aae06b3835661a48d915ed",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40020438906",
      "name": "Weekly merged-branch housekeeping",
      "path": ".github/workflows/branch-housekeeping.yml",
      "run_number": 2,
      "run_started_at": "2026-10-23T20:35:47Z",
      "status": "completed",
      "updated_at": "2026-10-23T20:36:06Z",
      "workflow_id": 381758282
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-26T01:31:59Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40254676124",
      "name": "CI",
      "path": ".github/workflows/ci.yml",
      "run_number": 434,
      "run_started_at": "2026-10-26T01:31:59Z",
      "status": "completed",
      "updated_at": "2026-10-26T01:32:26Z",
      "workflow_id": 248717477
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-26T01:31:59Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40254676085",
      "name": "Deploy Documentation (Just the Docs)",
      "path": ".github/workflows/pages.yml",
      "run_number": 44,
      "run_started_at": "2026-10-26T01:31:59Z",
      "status": "completed",
      "updated_at": "2026-10-26T01:33:12Z",
      "workflow_id": 315515884
    },
    {
      "conclusion": "failure",
      "created_at": "2026-10-26T08:49:05Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40294912258",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 1,
      "run_started_at": "2026-10-26T08:49:05Z",
      "status": "completed",
      "updated_at": "2026-10-26T08:49:30Z",
      "workflow_id": 396546945
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-26T01:31:59Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40254676103",
      "name": "Release",
      "path": ".github/workflows/release.yml",
      "run_number": 16,
      "run_started_at": "2026-10-26T01:31:59Z",
      "status": "completed",
      "updated_at": "2026-10-26T01:32:07Z",
      "workflow_id": 347445405
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-23T11:23:01Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "47e08a7eb8cadb95b6aae06b3835661a48d915ed",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/39945681613",
      "name": "bundler in / for jekyll-seo-tag, jekyll-relative-links - Update #1647638685",
      "path": "dynamic/dependabot/dependabot-updates",
      "run_number": 107,
      "run_started_at": "2026-10-23T11:23:01Z",
      "status": "completed",
      "updated_at": "2026-10-23T11:23:50Z",
      "workflow_id": 261742867
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-26T00:14:16Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "ed553ab0ae476d1e5c7fb20466db2b1a584bf694",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40248365960",
      "name": "Configured Graph Update: pip in /. #1652259640",
      "path": "dynamic/dependabot/update-graph",
      "run_number": 24,
      "run_started_at": "2026-10-26T00:14:16Z",
      "status": "completed",
      "updated_at": "2026-10-26T00:15:09Z",
      "workflow_id": 303797171
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-10-26T08:49:05Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "ada8927d17f0d5007b83416d412c1f656e01da6d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/cawg-trqp-verifier-refimpl/actions/runs/40294912258",
      "name": "Public Documentation Link Audit",
      "path": ".github/workflows/publication-link-audit.yml",
      "run_number": 1,
      "run_started_at": "2026-10-26T08:49:05Z",
      "status": "completed",
      "updated_at": "2026-10-26T08:49:30Z",
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
