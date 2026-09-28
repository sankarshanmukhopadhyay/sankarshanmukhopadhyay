---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-09-28T13:52:39Z  
**Open findings:** 5  
**Repository snapshot:** `916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 3 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 2 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-E8B1B5CFA71B — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-BE426C057634` at `2026-09-28T13:52:39Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-09-01T21:01:37Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": null,
  "freshness_policy": "current-head",
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

## PF-40A9B6AD0B44 — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-3B104AEA80E2` at `2026-09-28T13:52:39Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/validate.yml`
- Lifecycle: `open`; first observed `2026-09-01T21:01:37Z`
- Claim: Required assurance evidence was not observed inside the governed evidence window.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "toolkit_validation",
  "evidence_head_sha": null,
  "freshness_policy": "current-head",
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

## PF-D6A19F4EBA45 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-3399C66DCF61` at `2026-09-28T13:52:39Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/combined-review-worker.yml`
- Lifecycle: `open`; first observed `2026-09-11T16:27:45Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/clean-room-assessment.yml",
    ".github/workflows/combined-review-worker.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/current-portfolio-clean-room.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-handoff.yml",
    ".github/workflows/dpip-lifecycle.yml",
    ".github/workflows/dtg-assurance-reconcile.yml",
    ".github/workflows/dtg-portfolio-materiality-handoff.yml",
    ".github/workflows/dtg-repository-review-worker.yml",
    ".github/workflows/dtg-vtc-full-clean-room.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/human-power-reconciliation.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/materiality-journal-canary.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/regen-authority-at-commitment.yml",
    ".github/workflows/release-codename-policy.yml",
    ".github/workflows/release.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/vti-assessment-profile.yml",
    ".github/workflows/vti-composition-wave.yml",
    ".github/workflows/vti-semantic-completion.yml",
    ".github/workflows/workflow-governance.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "latest": [
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609241",
      "name": "Execute bounded combined RAHP reviews",
      "path": ".github/workflows/combined-review-worker.yml",
      "run_number": 1473,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343490806
    },
    {
      "conclusion": "success",
      "created_at": "2026-09-28T09:49:55Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36405973014",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 161,
      "run_started_at": "2026-09-28T09:49:55Z",
      "status": "completed",
      "updated_at": "2026-09-28T09:50:16Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609365",
      "name": "Promote qualified RAHP referrals to DPIP",
      "path": ".github/workflows/dpip-handoff.yml",
      "run_number": 1211,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:54Z",
      "workflow_id": 342518526
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:27:59Z",
      "event": "issue_comment",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391791073",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 819,
      "run_started_at": "2026-09-28T07:27:59Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:28:00Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:26:57Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391702404",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 1825,
      "run_started_at": "2026-09-28T07:26:57Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:26:58Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609296",
      "name": "Advance DTG gatherer repository reviews",
      "path": ".github/workflows/dtg-repository-review-worker.yml",
      "run_number": 1463,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343549712
    },
    {
      "conclusion": "failure",
      "created_at": "2026-09-28T10:07:25Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36407772440",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 45,
      "run_started_at": "2026-09-28T10:07:25Z",
      "status": "completed",
      "updated_at": "2026-09-28T10:09:44Z",
      "workflow_id": 334033746
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609241",
      "name": "Execute bounded combined RAHP reviews",
      "path": ".github/workflows/combined-review-worker.yml",
      "run_number": 1473,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343490806
    }
  ],
  "unresolved_failures": 3,
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

## PF-40DA3BA7712C — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-535683400EEE` at `2026-09-28T13:52:39Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/dtg-repository-review-worker.yml`
- Lifecycle: `open`; first observed `2026-08-27T09:46:58Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/clean-room-assessment.yml",
    ".github/workflows/combined-review-worker.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/current-portfolio-clean-room.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-handoff.yml",
    ".github/workflows/dpip-lifecycle.yml",
    ".github/workflows/dtg-assurance-reconcile.yml",
    ".github/workflows/dtg-portfolio-materiality-handoff.yml",
    ".github/workflows/dtg-repository-review-worker.yml",
    ".github/workflows/dtg-vtc-full-clean-room.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/human-power-reconciliation.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/materiality-journal-canary.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/regen-authority-at-commitment.yml",
    ".github/workflows/release-codename-policy.yml",
    ".github/workflows/release.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/vti-assessment-profile.yml",
    ".github/workflows/vti-composition-wave.yml",
    ".github/workflows/vti-semantic-completion.yml",
    ".github/workflows/workflow-governance.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "latest": [
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609241",
      "name": "Execute bounded combined RAHP reviews",
      "path": ".github/workflows/combined-review-worker.yml",
      "run_number": 1473,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343490806
    },
    {
      "conclusion": "success",
      "created_at": "2026-09-28T09:49:55Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36405973014",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 161,
      "run_started_at": "2026-09-28T09:49:55Z",
      "status": "completed",
      "updated_at": "2026-09-28T09:50:16Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609365",
      "name": "Promote qualified RAHP referrals to DPIP",
      "path": ".github/workflows/dpip-handoff.yml",
      "run_number": 1211,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:54Z",
      "workflow_id": 342518526
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:27:59Z",
      "event": "issue_comment",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391791073",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 819,
      "run_started_at": "2026-09-28T07:27:59Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:28:00Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:26:57Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391702404",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 1825,
      "run_started_at": "2026-09-28T07:26:57Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:26:58Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609296",
      "name": "Advance DTG gatherer repository reviews",
      "path": ".github/workflows/dtg-repository-review-worker.yml",
      "run_number": 1463,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343549712
    },
    {
      "conclusion": "failure",
      "created_at": "2026-09-28T10:07:25Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36407772440",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 45,
      "run_started_at": "2026-09-28T10:07:25Z",
      "status": "completed",
      "updated_at": "2026-09-28T10:09:44Z",
      "workflow_id": 334033746
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609296",
      "name": "Advance DTG gatherer repository reviews",
      "path": ".github/workflows/dtg-repository-review-worker.yml",
      "run_number": 1463,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343549712
    }
  ],
  "unresolved_failures": 3,
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

## PF-4E123844FBF6 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-B1A6EACB3C58` at `2026-09-28T13:52:39Z`
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
    ".github/workflows/clean-room-assessment.yml",
    ".github/workflows/combined-review-worker.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/current-portfolio-clean-room.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-handoff.yml",
    ".github/workflows/dpip-lifecycle.yml",
    ".github/workflows/dtg-assurance-reconcile.yml",
    ".github/workflows/dtg-portfolio-materiality-handoff.yml",
    ".github/workflows/dtg-repository-review-worker.yml",
    ".github/workflows/dtg-vtc-full-clean-room.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/human-power-reconciliation.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/materiality-journal-canary.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/regen-authority-at-commitment.yml",
    ".github/workflows/release-codename-policy.yml",
    ".github/workflows/release.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/vti-assessment-profile.yml",
    ".github/workflows/vti-composition-wave.yml",
    ".github/workflows/vti-semantic-completion.yml",
    ".github/workflows/workflow-governance.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "latest": [
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609241",
      "name": "Execute bounded combined RAHP reviews",
      "path": ".github/workflows/combined-review-worker.yml",
      "run_number": 1473,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343490806
    },
    {
      "conclusion": "success",
      "created_at": "2026-09-28T09:49:55Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36405973014",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 161,
      "run_started_at": "2026-09-28T09:49:55Z",
      "status": "completed",
      "updated_at": "2026-09-28T09:50:16Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609365",
      "name": "Promote qualified RAHP referrals to DPIP",
      "path": ".github/workflows/dpip-handoff.yml",
      "run_number": 1211,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:54Z",
      "workflow_id": 342518526
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:27:59Z",
      "event": "issue_comment",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391791073",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 819,
      "run_started_at": "2026-09-28T07:27:59Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:28:00Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-09-28T07:26:57Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391702404",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 1825,
      "run_started_at": "2026-09-28T07:26:57Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:26:58Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "cancelled",
      "created_at": "2026-09-28T07:25:54Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36391609296",
      "name": "Advance DTG gatherer repository reviews",
      "path": ".github/workflows/dtg-repository-review-worker.yml",
      "run_number": 1463,
      "run_started_at": "2026-09-28T07:25:54Z",
      "status": "completed",
      "updated_at": "2026-09-28T07:25:55Z",
      "workflow_id": 343549712
    },
    {
      "conclusion": "failure",
      "created_at": "2026-09-28T10:07:25Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36407772440",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 45,
      "run_started_at": "2026-09-28T10:07:25Z",
      "status": "completed",
      "updated_at": "2026-09-28T10:09:44Z",
      "workflow_id": 334033746
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-09-28T10:07:25Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "916acbf3f34a1fda1e6e75e5f2c70e87f53ec9ba",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/36407772440",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 45,
      "run_started_at": "2026-09-28T10:07:25Z",
      "status": "completed",
      "updated_at": "2026-09-28T10:09:44Z",
      "workflow_id": 334033746
    }
  ],
  "unresolved_failures": 3,
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
