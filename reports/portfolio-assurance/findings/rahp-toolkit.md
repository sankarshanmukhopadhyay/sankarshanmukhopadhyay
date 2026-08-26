---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-08-26T20:03:28Z  
**Open findings:** 3  
**Repository snapshot:** `2beebe0f2e19e2862e11d676cdd2baa32b6ec5b5`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 1 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 2 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-237AE4A6472D — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-92FC55EFB386` at `2026-08-26T20:03:28Z`
- Severity: `medium`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-08-21T07:07:22Z`
- Claim: Required assurance evidence is successful but does not cover the current governed repository state.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "2beebe0f2e19e2862e11d676cdd2baa32b6ec5b5",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-26T00:13:11Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
    "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32914160311",
    "name": "Build and deploy RAHP documentation",
    "path": ".github/workflows/pages.yml",
    "run_number": 183,
    "run_started_at": "2026-08-26T00:13:11Z",
    "status": "completed",
    "updated_at": "2026-08-26T00:14:11Z",
    "workflow_id": 333196290
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

## PF-8A31AAA852D1 — ASSURANCE_EVIDENCE_STALE

- Observation: `PAM-1509B2F77EC6` at `2026-08-26T20:03:28Z`
- Severity: `medium`
- Dimension: `assurance`
- Subject: `.github/workflows/validate.yml`
- Lifecycle: `open`; first observed `2026-08-21T07:07:22Z`
- Claim: Required assurance evidence is successful but does not cover the current governed repository state.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "toolkit_validation",
  "evidence_head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
  "freshness_policy": "current-head",
  "reason": "successful evidence does not cover the current default-branch HEAD",
  "repository_head_sha": "2beebe0f2e19e2862e11d676cdd2baa32b6ec5b5",
  "state": "stale",
  "workflow": {
    "conclusion": "success",
    "created_at": "2026-08-26T00:13:11Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
    "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32914160322",
    "name": "validate",
    "path": ".github/workflows/validate.yml",
    "run_number": 194,
    "run_started_at": "2026-08-26T00:13:11Z",
    "status": "completed",
    "updated_at": "2026-08-26T00:13:48Z",
    "workflow_id": 331522431
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

## PF-4E123844FBF6 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-BDD5049CC645` at `2026-08-26T20:03:28Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/instance-watch.yml`
- Lifecycle: `open`; first observed `2026-08-25T07:08:19Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/cawg-cross-spec-pressure-test.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-handoff.yml",
    ".github/workflows/dtg-cross-spec-pressure-test.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/release.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/validate.yml",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-08-24T04:06:38Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "1ff01b44bb11f6f0d72b98a8bcbc8793960fd829",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32688788144",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 7,
      "run_started_at": "2026-08-24T04:06:38Z",
      "status": "completed",
      "updated_at": "2026-08-24T04:06:56Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "failure",
      "created_at": "2026-08-26T04:19:34Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32929791994",
      "name": "RAHP instance change watch",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 13,
      "run_started_at": "2026-08-26T04:19:34Z",
      "status": "completed",
      "updated_at": "2026-08-26T04:20:33Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "success",
      "created_at": "2026-08-26T00:13:11Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32914160311",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 183,
      "run_started_at": "2026-08-26T00:13:11Z",
      "status": "completed",
      "updated_at": "2026-08-26T00:14:11Z",
      "workflow_id": 333196290
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
      "created_at": "2026-08-26T00:13:11Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32914160322",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 194,
      "run_started_at": "2026-08-26T00:13:11Z",
      "status": "completed",
      "updated_at": "2026-08-26T00:13:48Z",
      "workflow_id": 331522431
    }
  ],
  "lookback_days": 7,
  "retired": [
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
    }
  ],
  "retired_workflows_examined": 2,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-08-26T04:19:34Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "be0dd48f0cde8a8d19dd791c8ed52d7b679f50d8",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/32929791994",
      "name": "RAHP instance change watch",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 13,
      "run_started_at": "2026-08-26T04:19:34Z",
      "status": "completed",
      "updated_at": "2026-08-26T04:20:33Z",
      "workflow_id": 334033746
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
