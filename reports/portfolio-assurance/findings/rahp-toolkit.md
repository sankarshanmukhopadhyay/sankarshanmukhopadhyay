---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-11-10T19:42:27Z  
**Open findings:** 3  
**Repository snapshot:** `db09379ffcc80f3fa2f071acb510d633e2ab3e2c`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/rahp-toolkit.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 2 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-E8B1B5CFA71B — ASSURANCE_EVIDENCE_MISSING

- Observation: `PAM-CA88AC9666C2` at `2026-11-10T19:42:27Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-09-01T21:01:37Z`
- Claim: Required assurance evidence satisfying the configured evidence contract was not observed.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": null,
  "freshness_policy": "current-head",
  "reason": "no completed workflow execution satisfying the configured evidence contract was observed",
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

## PF-175F07FC3EA4 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-7792100725DA` at `2026-11-10T19:42:27Z`
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
        "created_at": "2026-11-09T11:36:31Z",
        "event": "schedule",
        "head_branch": "main",
        "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42610392951",
        "name": "Corpus source status",
        "path": ".github/workflows/corpus-status.yml",
        "run_number": 336,
        "run_started_at": "2026-11-09T11:36:31Z",
        "status": "completed",
        "updated_at": "2026-11-09T11:36:52Z",
        "workflow_id": 333347627
      }
    },
    ".github/workflows/cross-spec-pressure-test.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/validate.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-08T10:27:38Z",
        "event": "schedule",
        "head_branch": "main",
        "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42471512486",
        "name": "validate",
        "path": ".github/workflows/validate.yml",
        "run_number": 1508,
        "run_started_at": "2026-11-08T10:27:38Z",
        "status": "completed",
        "updated_at": "2026-11-08T10:28:15Z",
        "workflow_id": 331522431
      }
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-11-09T11:36:31Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42610392951",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 336,
      "run_started_at": "2026-11-09T11:36:31Z",
      "status": "completed",
      "updated_at": "2026-11-09T11:36:52Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-10T17:17:21Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42863394681",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 1686,
      "run_started_at": "2026-11-10T17:17:21Z",
      "status": "completed",
      "updated_at": "2026-11-10T17:18:32Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-10T13:07:14Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42821611910",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 2966,
      "run_started_at": "2026-11-10T13:07:14Z",
      "status": "completed",
      "updated_at": "2026-11-10T13:07:15Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T08:15:00Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42781143778",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 196,
      "run_started_at": "2026-11-10T08:15:00Z",
      "status": "completed",
      "updated_at": "2026-11-10T08:15:13Z",
      "workflow_id": 343470013
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T11:40:49Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42809433646",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 76,
      "run_started_at": "2026-11-10T11:40:49Z",
      "status": "completed",
      "updated_at": "2026-11-10T11:43:03Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-10T13:07:14Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42821611914",
      "name": "Advance bounded RAHP review workers",
      "path": ".github/workflows/review-workers.yml",
      "run_number": 267,
      "run_started_at": "2026-11-10T13:07:14Z",
      "status": "completed",
      "updated_at": "2026-11-10T13:07:15Z",
      "workflow_id": 396124313
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T08:15:00Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42781143778",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 196,
      "run_started_at": "2026-11-10T08:15:00Z",
      "status": "completed",
      "updated_at": "2026-11-10T08:15:13Z",
      "workflow_id": 343470013
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 6
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

- Observation: `PAM-AAA250B4A6B2` at `2026-11-10T19:42:27Z`
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
        "created_at": "2026-11-09T11:36:31Z",
        "event": "schedule",
        "head_branch": "main",
        "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42610392951",
        "name": "Corpus source status",
        "path": ".github/workflows/corpus-status.yml",
        "run_number": 336,
        "run_started_at": "2026-11-09T11:36:31Z",
        "status": "completed",
        "updated_at": "2026-11-09T11:36:52Z",
        "workflow_id": 333347627
      }
    },
    ".github/workflows/cross-spec-pressure-test.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": null
    },
    ".github/workflows/validate.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-08T10:27:38Z",
        "event": "schedule",
        "head_branch": "main",
        "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42471512486",
        "name": "validate",
        "path": ".github/workflows/validate.yml",
        "run_number": 1508,
        "run_started_at": "2026-11-08T10:27:38Z",
        "status": "completed",
        "updated_at": "2026-11-08T10:28:15Z",
        "workflow_id": 331522431
      }
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-11-09T11:36:31Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42610392951",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 336,
      "run_started_at": "2026-11-09T11:36:31Z",
      "status": "completed",
      "updated_at": "2026-11-09T11:36:52Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-10T17:17:21Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42863394681",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 1686,
      "run_started_at": "2026-11-10T17:17:21Z",
      "status": "completed",
      "updated_at": "2026-11-10T17:18:32Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-10T13:07:14Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42821611910",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 2966,
      "run_started_at": "2026-11-10T13:07:14Z",
      "status": "completed",
      "updated_at": "2026-11-10T13:07:15Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T08:15:00Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42781143778",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 196,
      "run_started_at": "2026-11-10T08:15:00Z",
      "status": "completed",
      "updated_at": "2026-11-10T08:15:13Z",
      "workflow_id": 343470013
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T11:40:49Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42809433646",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 76,
      "run_started_at": "2026-11-10T11:40:49Z",
      "status": "completed",
      "updated_at": "2026-11-10T11:43:03Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-10T13:07:14Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42821611914",
      "name": "Advance bounded RAHP review workers",
      "path": ".github/workflows/review-workers.yml",
      "run_number": 267,
      "run_started_at": "2026-11-10T13:07:14Z",
      "status": "completed",
      "updated_at": "2026-11-10T13:07:15Z",
      "workflow_id": 396124313
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-11-10T11:40:49Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "db09379ffcc80f3fa2f071acb510d633e2ab3e2c",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/42809433646",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 76,
      "run_started_at": "2026-11-10T11:40:49Z",
      "status": "completed",
      "updated_at": "2026-11-10T11:43:03Z",
      "workflow_id": 334033746
    }
  ],
  "unresolved_failures": 2,
  "workflows_examined": 6
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
