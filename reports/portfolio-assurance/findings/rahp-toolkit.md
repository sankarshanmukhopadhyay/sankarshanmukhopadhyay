---
layout: default
title: Remediation dossier — rahp-toolkit
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `rahp-toolkit`

**Generated:** 2026-11-14T06:19:37Z  
**Open findings:** 1  
**Repository snapshot:** `b574290285ef7d960186ebd14ce9cb928407b6b3`  
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

## PF-4E123844FBF6 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-B2D17E59452E` at `2026-11-14T06:19:37Z`
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
        "created_at": "2026-11-13T03:07:48Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859780",
        "name": "Corpus source status",
        "path": ".github/workflows/corpus-status.yml",
        "run_number": 343,
        "run_started_at": "2026-11-13T03:07:48Z",
        "status": "completed",
        "updated_at": "2026-11-13T03:08:14Z",
        "workflow_id": 333347627
      }
    },
    ".github/workflows/cross-spec-pressure-test.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-13T20:26:57Z",
        "event": "workflow_dispatch",
        "head_branch": "main",
        "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43501647008",
        "name": "Run cross-specification pressure test",
        "path": ".github/workflows/cross-spec-pressure-test.yml",
        "run_number": 207,
        "run_started_at": "2026-11-13T20:26:57Z",
        "status": "completed",
        "updated_at": "2026-11-13T20:27:24Z",
        "workflow_id": 337404001
      }
    },
    ".github/workflows/pages.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-13T03:07:48Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859761",
        "name": "Build and deploy RAHP documentation",
        "path": ".github/workflows/pages.yml",
        "run_number": 1513,
        "run_started_at": "2026-11-13T03:07:48Z",
        "status": "completed",
        "updated_at": "2026-11-13T03:09:01Z",
        "workflow_id": 333196290
      }
    },
    ".github/workflows/validate.yml": {
      "available": true,
      "run": {
        "conclusion": "success",
        "created_at": "2026-11-13T03:07:48Z",
        "event": "push",
        "head_branch": "main",
        "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
        "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859791",
        "name": "validate",
        "path": ".github/workflows/validate.yml",
        "run_number": 1535,
        "run_started_at": "2026-11-13T03:07:48Z",
        "status": "completed",
        "updated_at": "2026-11-13T03:09:39Z",
        "workflow_id": 331522431
      }
    }
  },
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-11-13T03:07:48Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859780",
      "name": "Corpus source status",
      "path": ".github/workflows/corpus-status.yml",
      "run_number": 343,
      "run_started_at": "2026-11-13T03:07:48Z",
      "status": "completed",
      "updated_at": "2026-11-13T03:08:14Z",
      "workflow_id": 333347627
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-13T20:26:57Z",
      "event": "workflow_dispatch",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43501647008",
      "name": "Run cross-specification pressure test",
      "path": ".github/workflows/cross-spec-pressure-test.yml",
      "run_number": 207,
      "run_started_at": "2026-11-13T20:26:57Z",
      "status": "completed",
      "updated_at": "2026-11-13T20:27:24Z",
      "workflow_id": 337404001
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-14T01:48:33Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43542767983",
      "name": "Reconcile RAHP-DPIP lifecycle and returns",
      "path": ".github/workflows/dpip-lifecycle.yml",
      "run_number": 1798,
      "run_started_at": "2026-11-14T01:48:33Z",
      "status": "completed",
      "updated_at": "2026-11-14T01:49:24Z",
      "workflow_id": 343401275
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-14T00:01:09Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43531277447",
      "name": "Reconcile DTG end-to-end assurance",
      "path": ".github/workflows/dtg-assurance-reconcile.yml",
      "run_number": 3057,
      "run_started_at": "2026-11-14T00:01:09Z",
      "status": "completed",
      "updated_at": "2026-11-14T00:01:18Z",
      "workflow_id": 343549711
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-13T20:26:13Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43501535636",
      "name": "Consume DTG Portfolio Monitor assurance signals",
      "path": ".github/workflows/dtg-portfolio-materiality-handoff.yml",
      "run_number": 203,
      "run_started_at": "2026-11-13T20:26:13Z",
      "status": "completed",
      "updated_at": "2026-11-13T20:27:02Z",
      "workflow_id": 343470013
    },
    {
      "conclusion": "failure",
      "created_at": "2026-11-13T11:28:00Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43417278464",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 79,
      "run_started_at": "2026-11-13T11:28:00Z",
      "status": "completed",
      "updated_at": "2026-11-13T11:30:25Z",
      "workflow_id": 334033746
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-13T03:07:48Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859761",
      "name": "Build and deploy RAHP documentation",
      "path": ".github/workflows/pages.yml",
      "run_number": 1513,
      "run_started_at": "2026-11-13T03:07:48Z",
      "status": "completed",
      "updated_at": "2026-11-13T03:09:01Z",
      "workflow_id": 333196290
    },
    {
      "conclusion": "skipped",
      "created_at": "2026-11-14T00:01:09Z",
      "event": "issues",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43531277389",
      "name": "Advance bounded RAHP review workers",
      "path": ".github/workflows/review-workers.yml",
      "run_number": 369,
      "run_started_at": "2026-11-14T00:01:09Z",
      "status": "completed",
      "updated_at": "2026-11-14T00:01:10Z",
      "workflow_id": 396124313
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-13T03:07:48Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43356859791",
      "name": "validate",
      "path": ".github/workflows/validate.yml",
      "run_number": 1535,
      "run_started_at": "2026-11-13T03:07:48Z",
      "status": "completed",
      "updated_at": "2026-11-13T03:09:39Z",
      "workflow_id": 331522431
    },
    {
      "conclusion": "success",
      "created_at": "2026-11-13T22:43:38Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43521612999",
      "name": "Workflow governance",
      "path": ".github/workflows/workflow-governance.yml",
      "run_number": 376,
      "run_started_at": "2026-11-13T22:43:38Z",
      "status": "completed",
      "updated_at": "2026-11-13T22:43:55Z",
      "workflow_id": 345766991
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-11-13T11:28:00Z",
      "event": "schedule",
      "head_branch": "main",
      "head_sha": "b574290285ef7d960186ebd14ce9cb928407b6b3",
      "html_url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/actions/runs/43417278464",
      "name": "Incremental DTG/CAWG monitor \u00b7 schedule \u00b7",
      "path": ".github/workflows/instance-watch.yml",
      "run_number": 79,
      "run_started_at": "2026-11-13T11:28:00Z",
      "status": "completed",
      "updated_at": "2026-11-13T11:30:25Z",
      "workflow_id": 334033746
    }
  ],
  "unresolved_failures": 1,
  "workflows_examined": 10
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
