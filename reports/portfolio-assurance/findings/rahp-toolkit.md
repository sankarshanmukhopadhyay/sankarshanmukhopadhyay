---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-10-28T12:52:31Z  
**Open findings:** 2  
**Repository snapshot:** `7fb34a0400ea27c20f0149825a481f2bc90b2912`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 2 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 0 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-175F07FC3EA4 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-F9D2E42F124C` at `2026-10-28T12:52:31Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/dtg-portfolio-materiality-handoff.yml`
- Lifecycle: `open`; first observed `2026-10-24T10:57:47Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/cawg-vlei-verifier-probe.yml",
    ".github/workflows/clean-room-assessment.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/current-portfolio-clean-room.yml",
    ".github/workflows/dco.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-lifecycle.yml",
    ".github/workflows/dtg-assurance-reconcile.yml",
    ".github/workflows/dtg-portfolio-materiality-handoff.yml",
    ".github/workflows/dtg-vtc-full-clean-room.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/generate-portable-catalogue-artifacts.yml",
    ".github/workflows/glossary-branch-regenerate.yml",
    ".github/workflows/human-power-reconciliation.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/materiality-journal-canary.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/performance-profile.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/regen-authority-at-commitment.yml",
    ".github/workflows/regen-credential-renewal.yml",
    ".github/workflows/release-codename-policy.yml",
    ".github/workflows/release.yml",
    ".github/workflows/review-workers.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/tsp-source-evidence.yml",
    ".github/workflows/upstream-source-compat.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/vti-assessment-profile.yml",
    ".github/workflows/workflow-governance.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "contract_evidence": {
    ".github/workflows/corpus-status.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628566",
        "name": "Corpus source status",
        "path": ".github/workflows/corpus-status.yml",
        "run_number": 325,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:25:30Z",
        "workflow_id": 333347627
      }
    },
    ".github/workflows/cross-spec-pressure-test.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628272",
        "name": "Build and deploy RAHP documentation",
        "path": ".github/workflows/pages.yml",
        "run_number": 1463,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:26:24Z",
        "workflow_id": 333196290
      }
    },
    ".github/workflows/validate.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628510",
        "name": "validate",
        "path": ".github/workflows/validate.yml",
        "run_number": 1483,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:26:53Z",
        "workflow_id": 331522431
      }
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628566",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 325,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:30Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T12:25:23Z",
      "event": "issue_comment",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687668952",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 1440,
      "run_started_at": "2026-10-28T12:25:23Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:30Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T11:51:11Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40683147575",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 2759,
      "run_started_at": "2026-10-28T11:51:11Z",
      "status": "completed",
      "updated_at": "2026-10-28T11:51:12Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T06:46:39Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40645920258",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 170,
      "run_started_at": "2026-10-28T06:46:39Z",
      "status": "completed",
      "updated_at": "2026-10-28T06:46:51Z",
      "workflow_id": 343470013
    },
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T09:58:31Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40668416739",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 67,
      "run_started_at": "2026-10-28T09:58:31Z",
      "status": "completed",
      "updated_at": "2026-10-28T10:01:25Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628272",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 1463,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:26:24Z",
      "workflow_id": 333196290
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T11:51:11Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40683146783",
      "name": "Advance bounded RAHP review workers",
      "path": ".github/workflows/review-workers.yml",
      "run_number": 62,
      "run_started_at": "2026-10-28T11:51:11Z",
      "status": "completed",
      "updated_at": "2026-10-28T11:51:12Z",
      "workflow_id": 396124313
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628510",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 1483,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:26:53Z",
      "workflow_id": 331522431
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:07Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687629193",
      "name": "Workflow governance",
      "path": ".github/workflows/workflow-governance.yml",
      "run_number": 360,
      "run_started_at": "2026-10-28T12:25:07Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:20Z",
      "workflow_id": 345766991
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T06:46:39Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40645920258",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 170,
      "run_started_at": "2026-10-28T06:46:39Z",
      "status": "completed",
      "updated_at": "2026-10-28T06:46:51Z",
      "workflow_id": 343470013
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 9
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

- Observation: `PAM-7C256736190B` at `2026-10-28T12:52:31Z`
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
    ".github/workflows/cawg-vlei-verifier-probe.yml",
    ".github/workflows/clean-room-assessment.yml",
    ".github/workflows/corpus-review.yml",
    ".github/workflows/corpus-status.yml",
    ".github/workflows/cross-spec-pressure-test.yml",
    ".github/workflows/current-portfolio-clean-room.yml",
    ".github/workflows/dco.yml",
    ".github/workflows/debug-guardianship-render.yml",
    ".github/workflows/distributed-resilience-assessment.yml",
    ".github/workflows/dpip-lifecycle.yml",
    ".github/workflows/dtg-assurance-reconcile.yml",
    ".github/workflows/dtg-portfolio-materiality-handoff.yml",
    ".github/workflows/dtg-vtc-full-clean-room.yml",
    ".github/workflows/execution-benchmark.yml",
    ".github/workflows/generate-portable-catalogue-artifacts.yml",
    ".github/workflows/glossary-branch-regenerate.yml",
    ".github/workflows/human-power-reconciliation.yml",
    ".github/workflows/instance-watch.yml",
    ".github/workflows/materiality-journal-canary.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/performance-profile.yml",
    ".github/workflows/recompose-tt-credspec-corpus.yml",
    ".github/workflows/regen-authority-at-commitment.yml",
    ".github/workflows/regen-credential-renewal.yml",
    ".github/workflows/release-codename-policy.yml",
    ".github/workflows/release.yml",
    ".github/workflows/review-workers.yml",
    ".github/workflows/sync-corpus-generated-views.yml",
    ".github/workflows/tsp-source-evidence.yml",
    ".github/workflows/upstream-source-compat.yml",
    ".github/workflows/validate.yml",
    ".github/workflows/vti-assessment-profile.yml",
    ".github/workflows/workflow-governance.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph"
  ],
  "available": true,
  "completed_examined": 50,
  "contract_evidence": {
    ".github/workflows/corpus-status.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628566",
        "name": "Corpus source status",
        "path": ".github/workflows/corpus-status.yml",
        "run_number": 325,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:25:30Z",
        "workflow_id": 333347627
      }
    },
    ".github/workflows/cross-spec-pressure-test.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628272",
        "name": "Build and deploy RAHP documentation",
        "path": ".github/workflows/pages.yml",
        "run_number": 1463,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:26:24Z",
        "workflow_id": 333196290
      }
    },
    ".github/workflows/validate.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-10-28T12:25:06Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628510",
        "name": "validate",
        "path": ".github/workflows/validate.yml",
        "run_number": 1483,
        "run_started_at": "2026-10-28T12:25:06Z",
        "status": "completed",
        "updated_at": "2026-10-28T12:26:53Z",
        "workflow_id": 331522431
      }
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628566",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 325,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:30Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T12:25:23Z",
      "event": "issue_comment",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687668952",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 1440,
      "run_started_at": "2026-10-28T12:25:23Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:30Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T11:51:11Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40683147575",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 2759,
      "run_started_at": "2026-10-28T11:51:11Z",
      "status": "completed",
      "updated_at": "2026-10-28T11:51:12Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T06:46:39Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40645920258",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 170,
      "run_started_at": "2026-10-28T06:46:39Z",
      "status": "completed",
      "updated_at": "2026-10-28T06:46:51Z",
      "workflow_id": 343470013
    },
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T09:58:31Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40668416739",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 67,
      "run_started_at": "2026-10-28T09:58:31Z",
      "status": "completed",
      "updated_at": "2026-10-28T10:01:25Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628272",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 1463,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:26:24Z",
      "workflow_id": 333196290
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-10-28T11:51:11Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40683146783",
      "name": "Advance bounded RAHP review workers",
      "path": ".github/workflows/review-workers.yml",
      "run_number": 62,
      "run_started_at": "2026-10-28T11:51:11Z",
      "status": "completed",
      "updated_at": "2026-10-28T11:51:12Z",
      "workflow_id": 396124313
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:06Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687628510",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 1483,
      "run_started_at": "2026-10-28T12:25:06Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:26:53Z",
      "workflow_id": 331522431
    },
    {
      "conclusion": "success",
      "created_at": "2026-10-28T12:25:07Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "7fb34a0400ea27c20f0149825a481f2bc90b2912",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40687629193",
      "name": "Workflow governance",
      "path": ".github/workflows/workflow-governance.yml",
      "run_number": 360,
      "run_started_at": "2026-10-28T12:25:07Z",
      "status": "completed",
      "updated_at": "2026-10-28T12:25:20Z",
      "workflow_id": 345766991
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-10-28T09:58:31Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "c84d88dfdd7adad43962ce6981283d15c61dc6c0",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/40668416739",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 67,
      "run_started_at": "2026-10-28T09:58:31Z",
      "status": "completed",
      "updated_at": "2026-10-28T10:01:25Z",
      "workflow_id": 334033746
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 9
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
