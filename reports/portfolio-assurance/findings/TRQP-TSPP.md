---
layout: default
title: Remediation dossier — TRQP-TSPP
nav_exclude: true
search_exclude: true
---

# Repository remediation dossier — `TRQP-TSPP`

**Generated:** 2026-09-10T02:21:16Z  
**Open findings:** 2  
**Repository snapshot:** `6f1772bb6d304401cfb700c480d54965b6526fdb`  
**Download:** [Markdown](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/TRQP-TSPP.md) · [JSON](https://raw.githubusercontent.com/sankarshanmukhopadhyay/sankarshanmukhopadhyay/main/reports/portfolio-assurance/findings/TRQP-TSPP.json)

> **Remediation handoff.** Download this dossier and provide it with the affected repository source. The monitor owns the observation and finding; the target repository retains authority over implementation, risk disposition, release, and closure evidence.

## Assessment boundary

| Dimension | State | Open findings |
|---|---|---:|
| Operational | `evaluated` | 1 |
| Governance | `evaluated` | 0 |
| Assurance | `evaluated` | 1 |
| Cross Specification | `not-evaluated` | 0 |

## Open findings

## PF-25F4E070337B — ASSURANCE_CONTROL_FAILED

- Observation: `PAM-58EEAB14C150` at `2026-09-10T02:21:16Z`
- Severity: `high`
- Dimension: `assurance`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-09-10T02:21:16Z`
- Claim: The repository-native control bound to this assurance claim is currently failing.
- Automatic effect: `none`

### Evidence

```json
{
  "claim": "publication_integrity",
  "evidence_head_sha": null,
  "freshness_policy": "latest-success",
  "reason": "latest completed workflow conclusion is failure",
  "repository_head_sha": null,
  "state": "degraded",
  "workflow": {
    "conclusion": "failure",
    "created_at": "2026-09-10T01:21:28Z",
    "event": "push",
    "head_branch": "main",
    "head_sha": "6f1772bb6d304401cfb700c480d54965b6526fdb",
    "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/34425140373",
    "name": "Deploy documentation to GitHub Pages",
    "path": ".github/workflows/pages.yml",
    "run_number": 28,
    "run_started_at": "2026-09-10T01:21:28Z",
    "status": "completed",
    "updated_at": "2026-09-10T01:21:57Z",
    "workflow_id": 316453200
  }
}
```

### Remediation objective

Resolve the failing repository-native assurance control or record an explicit governed disposition.

### Acceptance criteria

- [ ] The configured assurance control completes successfully.
- [ ] The resulting evidence remains attributable to the configured repository revision.

### Verification

- Execute the control and rerun the portfolio monitor.

## PF-DE34E30A16D3 — DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE

- Observation: `PAM-418991CDA7F4` at `2026-09-10T02:21:16Z`
- Severity: `medium`
- Dimension: `operational`
- Subject: `.github/workflows/pages.yml`
- Lifecycle: `open`; first observed `2026-09-10T02:21:16Z`
- Claim: The latest completed default-branch run for this workflow is failing within the governed observation window.
- Automatic effect: `none`

### Evidence

```json
{
  "active_inventory_available": true,
  "active_workflow_paths": [
    ".github/workflows/ci.yml",
    ".github/workflows/one-shot-tag-v0.16.0.yml",
    ".github/workflows/one-shot-tag-v0.16.1.yml",
    ".github/workflows/pages.yml",
    ".github/workflows/portfolio-contract.yml",
    ".github/workflows/wp8-evidence.yml",
    "dynamic/dependabot/dependabot-updates",
    "dynamic/dependabot/update-graph",
    "dynamic/pages/pages-build-deployment"
  ],
  "available": true,
  "completed_examined": 14,
  "latest": [
    {
      "conclusion": "success",
      "created_at": "2026-09-10T01:21:28Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "6f1772bb6d304401cfb700c480d54965b6526fdb",
      "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/34425140338",
      "name": "TSPP CI",
      "path": ".github/workflows/ci.yml",
      "run_number": 184,
      "run_started_at": "2026-09-10T01:21:28Z",
      "status": "completed",
      "updated_at": "2026-09-10T01:22:14Z",
      "workflow_id": 236888247
    },
    {
      "conclusion": "failure",
      "created_at": "2026-09-10T01:21:28Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "6f1772bb6d304401cfb700c480d54965b6526fdb",
      "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/34425140373",
      "name": "Deploy documentation to GitHub Pages",
      "path": ".github/workflows/pages.yml",
      "run_number": 28,
      "run_started_at": "2026-09-10T01:21:28Z",
      "status": "completed",
      "updated_at": "2026-09-10T01:21:57Z",
      "workflow_id": 316453200
    },
    {
      "conclusion": "success",
      "created_at": "2026-09-10T01:21:28Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "6f1772bb6d304401cfb700c480d54965b6526fdb",
      "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/34425140289",
      "name": "Portfolio Integration Contract",
      "path": ".github/workflows/portfolio-contract.yml",
      "run_number": 44,
      "run_started_at": "2026-09-10T01:21:28Z",
      "status": "completed",
      "updated_at": "2026-09-10T01:21:38Z",
      "workflow_id": 338452297
    },
    {
      "conclusion": "success",
      "created_at": "2026-09-03T04:18:01Z",
      "event": "dynamic",
      "head_branch": "main",
      "head_sha": "cd90305519746e563632c53c6bae6698ed609db8",
      "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/33714535616",
      "name": "pip in /harness - Update #1554001854",
      "path": "dynamic/dependabot/dependabot-updates",
      "run_number": 105,
      "run_started_at": "2026-09-03T04:18:01Z",
      "status": "completed",
      "updated_at": "2026-09-03T04:19:06Z",
      "workflow_id": 240284144
    }
  ],
  "lookback_days": 7,
  "retired": [],
  "retired_workflows_examined": 0,
  "unresolved": [
    {
      "conclusion": "failure",
      "created_at": "2026-09-10T01:21:28Z",
      "event": "push",
      "head_branch": "main",
      "head_sha": "6f1772bb6d304401cfb700c480d54965b6526fdb",
      "html_url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/actions/runs/34425140373",
      "name": "Deploy documentation to GitHub Pages",
      "path": ".github/workflows/pages.yml",
      "run_number": 28,
      "run_started_at": "2026-09-10T01:21:28Z",
      "status": "completed",
      "updated_at": "2026-09-10T01:21:57Z",
      "workflow_id": 316453200
    }
  ],
  "unresolved_failures": 1,
  "workflows_examined": 4
}
```

### Remediation objective

Restore a successful latest completed default-branch run for the affected workflow or record an explicit repository-governed risk disposition.

### Acceptance criteria

- [ ] The affected workflow's latest completed default-branch run succeeds, or an explicit governed disposition supersedes the operational expectation.

### Verification

- Run the affected workflow on the default branch.
- Rerun the portfolio monitor and confirm the stable finding fingerprint is no longer open.
