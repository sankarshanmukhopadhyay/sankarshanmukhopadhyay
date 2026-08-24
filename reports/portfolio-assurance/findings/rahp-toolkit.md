---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-08-24T01:57:24Z  
**Open findings:** 2  
**Repository snapshot:** `1ff01b44bb11f6f0d72b98a8bcbc8793960fd829`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 1 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-9769E5EB9C48 — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-9B1F9EEF070C` at `2026-08-24T01:57:24Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/corpus-status.yml`
- Lifecycle: `open`; first observed `2026-08-22T01:49:53Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "corpus_integrity",
  "evidence_head_sha": null,
  "freshness_policy": "latest-success",
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

## PF-954D1C442655 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-E2C995567FB3` at `2026-08-24T01:57:24Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/release-v1.5.0.yml`
- Lifecycle: `open`; first observed `2026-08-23T18:48:01Z`
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
      "created_at": "2026-08-24T01:04:50Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "1ff01b44bb11f6f0d72b98a8bcbc8793960fd829",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32678636830",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 177,
      "run_started_at": "2026-08-24T01:04:50Z",
      "status": "completed",
      "updated_at": "2026-08-24T01:05:47Z",
      "workflow_id": 333196290
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-23T15:25:54Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "1bf27bccd22de06fd7cd1272f4f79c5c99555415",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32648524664",
      "name": "publish qualified RAHP release",
      "path": ".github/workflows/publish-qualified-release.yml",
      "run_number": 1,
      "run_started_at": "2026-08-23T15:25:54Z",
      "status": "completed",
      "updated_at": "2026-08-23T15:26:29Z",
      "workflow_id": 340627964
    },
    {
      "conclusion": "failure",
      "created_at": "2026-08-23T15:25:54Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "1bf27bccd22de06fd7cd1272f4f79c5c99555415",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32648524629",
      "name": "Publish RAHP v1.5.0",
      "path": ".github/workflows/release-v1.5.0.yml",
      "run_number": 2,
      "run_started_at": "2026-08-23T15:25:54Z",
      "status": "completed",
      "updated_at": "2026-08-23T15:26:06Z",
      "workflow_id": 339785962
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-24T00:40:56Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "feda195e211eaa2cf3b61defce8e913f33d69d0d",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32677426239",
      "name": "Publish qualified RAHP release",
      "path": ".github/workflows/release.yml",
      "run_number": 1,
      "run_started_at": "2026-08-24T00:40:56Z",
      "status": "completed",
      "updated_at": "2026-08-24T00:41:16Z",
      "workflow_id": 340849453
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-24T01:04:50Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "1ff01b44bb11f6f0d72b98a8bcbc8793960fd829",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32678636860",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 188,
      "run_started_at": "2026-08-24T01:04:50Z",
      "status": "completed",
      "updated_at": "2026-08-24T01:05:28Z",
      "workflow_id": 331522431
    }
  ],
  "lookback_days": 7,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-08-23T15:25:54Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "1bf27bccd22de06fd7cd1272f4f79c5c99555415",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32648524629",
      "name": "Publish RAHP v1.5.0",
      "path": ".github/workflows/release-v1.5.0.yml",
      "run_number": 2,
      "run_started_at": "2026-08-23T15:25:54Z",
      "status": "completed",
      "updated_at": "2026-08-23T15:26:06Z",
      "workflow_id": 339785962
    }
  ],
  "unresolved_failures": 1,
  "workflows_examined": 5
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
