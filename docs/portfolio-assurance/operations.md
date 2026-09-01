---
layout: default
title: Operations
parent: Portfolio Assurance Monitor
nav_order: 4
---

# Portfolio assurance operations

The Portfolio Assurance Monitor is an evidence-producing governance control. It observes governed repositories, evaluates deterministic operational, governance, and assurance-evidence rules, detects account-level classification drift, and can route narrowly scoped actionable findings to affected repositories. Observation and publication do not transfer repository, release, specification, risk-acceptance, or portfolio authority.

## Scheduled execution

The monitor reevaluates portfolio evidence every six hours and may also be invoked manually. It also runs when governed monitor configuration, repository status data, monitor implementation, monitor workflows, or the core assurance-operations documentation changes. Generated evidence-only merges do not retrigger the monitor because generated output paths are not monitor push triggers.

Its normal sequence is:

1. validate portfolio governance data;
2. execute the monitor tests;
3. collect repository metadata, default-branch HEAD, status declarations, and workflow evidence;
4. evaluate deterministic operational and governance findings;
5. evaluate repository-specific assurance evidence contracts;
6. discover public repositories that lack an account-level disposition;
7. optionally route eligible findings to affected repositories;
8. render the dashboard, assurance-state artifact, remediation dossiers, and finding lifecycle evidence;
9. validate documentation links;
10. publish changed evidence to `automation/portfolio-assurance-evidence` using the repository-scoped Portfolio Assurance GitHub App token; and
11. create or update one evidence PR against `main`.

The evidence PR is then evaluated by the same protected-main required checks as any other change. A separate merge controller merges it only when both `validate` and `build` are successful and the PR still contains only governed evidence paths.

The six-hour cadence is an operational responsiveness control rather than an assurance claim. Repository-local evidence remains authoritative for the meaning of the underlying validation or conformance result.

## Protected-main publication contract

`main` has no automation bypass. Generated evidence reaches the default branch only through a pull request.

The publication workflow is allowed to commit only:

- `docs/portfolio-assurance/dashboard.md`;
- `reports/portfolio-assurance/**`.

Both the publisher and the merge controller independently reject out-of-scope paths. The publisher never pushes directly to `main`; it updates the deterministic `automation/portfolio-assurance-evidence` branch and creates or updates an evidence PR. The merge controller does not bypass the ruleset: it merges the PR only after the required checks succeed.

This produces the control chain:

```text
monitor
  -> generated evidence
  -> governed evidence branch
  -> pull request
  -> validate + build
  -> scope re-check
  -> normal PR merge
  -> protected main
```

A ruleset bypass for the Portfolio Assurance App is neither required nor permitted by this operating model.

## GitHub App permissions and setup

Configure repository secrets:

- `PORTFOLIO_ASSURANCE_APP_ID`
- `PORTFOLIO_ASSURANCE_APP_PRIVATE_KEY`

Recommended repository permissions for the installed Portfolio Assurance GitHub App:

| Permission | Access |
|---|---|
| Metadata | Read |
| Actions | Read |
| Contents | Read and write |
| Pull requests | Read and write |
| Issues | Read and write |

The workflow mints separate installation tokens for cross-repository issue routing and repository-local evidence publication. The publication token is explicitly scoped to `sankarshanmukhopadhyay/sankarshanmukhopadhyay`.

If App credentials are absent, evidence collection and evaluation may proceed, but PR-native evidence publication fails closed and no cross-repository issue writes occur.

## Assurance evidence contracts

Repository-specific contracts are defined in `config/portfolio-monitor/assurance-contracts.yaml`. A contract binds an explicit repository-native control to an assurance claim and states whether that evidence is required or optional and whether it must cover the current default-branch HEAD or may rely on the latest successful publication-specific execution.

The evidence states are:

- `satisfied`: required evidence exists, succeeded, and meets the configured freshness policy;
- `degraded`: the required evidence-producing control completed unsuccessfully;
- `stale`: successful evidence exists but does not cover the governed revision required by policy;
- `missing`: required evidence was not observed inside the governed evidence window;
- `unobservable`: the configured evidence source could not be collected;
- `not-applicable`: no required claim applies to the evaluated scope; and
- `not-evaluated`: no governed contract or supported adapter exists.

These are evidence-coverage states. They do not strengthen the authority of the producing workflow. Optional evidence is recorded but cannot degrade the repository's aggregate assurance state.

## Workflow failure semantics

`collection.lookback_days` is an assurance policy boundary, not merely an API hint. The collector examines completed runs inside that window and retains only the latest completed state for each workflow. A historical failure superseded by a later successful run does not produce `DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE`.

For `freshness: current-head`, a successful workflow run is insufficient unless its `head_sha` equals the observed default-branch HEAD. Path-filtered publication workflows may use `freshness: latest-success` when non-publication commits do not invalidate previously generated publication evidence.

## Stable finding identity

Every observation has a date-scoped `finding_id`, while a `finding_fingerprint` remains stable across repeated observations of the same repository, rule, and affected subject.

```text
repository + rule + subject -> finding_fingerprint
finding_fingerprint + observation date -> finding_id
```

This supports durable issue deduplication and machine-verifiable recovery without erasing observation history.

## Target-repository issue routing

Issue publication is implemented but disabled by default in `config/portfolio-monitor/policy.yaml`. Enable it only after the scoped GitHub App is installed on repositories that may receive findings.

Do not use the profile repository's ordinary `GITHUB_TOKEN` for cross-repository issue publication. The workflow expects a separately generated installation token in `PORTFOLIO_ISSUE_TOKEN`.

The publication gate is intentionally layered:

```text
finding exists
  -> rule is issue-eligible
  -> severity meets threshold
  -> repository/policy allows target reporting
  -> stable fingerprint has no open issue
  -> per-run creation cap remains
  -> create issue
```

The default routing policy excludes review-overdue, inactivity, and account-discovery findings from target repositories because those are portfolio-governance observations rather than repository-local defects.

## Deduplication and repeat observations

Each generated issue contains a machine-readable marker:

```html
<!-- portfolio-assurance:fingerprint=PF-XXXXXXXXXXXX -->
```

Before creation, the publisher searches the affected repository for an open issue containing that marker. Repeated observations are deduplicated. `comment_on_repeat` is false by default and `max_new_issues_per_run` is `2`.

The evidence-publication PR is also deduplicated operationally: the workflow uses one deterministic branch, `automation/portfolio-assurance-evidence`, and updates the existing open PR when present instead of creating PR churn every six hours.

## Recovery and closure

The monitor maintains an observation-level lifecycle registry in `reports/portfolio-assurance/finding-lifecycle.json`. When a stable fingerprint that was previously open is no longer observed on a later run, the monitor records that finding condition as `resolved` with a resolution timestamp.

The monitor does not automatically close repository issues, accept risk, approve implementation, change maturity/lifecycle, or make repository release decisions. Those remain repository- and portfolio-governance actions.

```text
observation -> finding -> remediation dossier -> implementation -> re-observation -> finding recovery evidence
                                                \-> governed issue/disposition closure
```

## Repository remediation retest discipline

When an actionable finding is routed to a target repository, remediation should follow an evidence-closed sequence:

1. preserve the stable `finding_fingerprint` in the repository-local issue and PR;
2. repair the repository-native control or evidence-production semantics without weakening the claim being tested;
3. require successful repository-native validation before merge;
4. require the governed default-branch evidence producer to execute after merge;
5. rerun this monitor only after the relevant repository evidence is observable; and
6. close the repository-local remediation issue only after the lifecycle registry records the fingerprint as `resolved`, unless repository governance explicitly accepts residual risk.

A PR merge or unrelated green workflow is not sufficient recovery evidence.

## Public account discovery and repository churn

The monitor compares live public repositories against `data/repository-status.yaml` in both directions. An unclassified public repository produces `PUBLIC_REPOSITORY_WITHOUT_DISPOSITION`. A governed active or review repository that disappears from public account discovery produces `REGISTERED_REPOSITORY_NOT_PUBLICLY_DISCOVERED`.

The second rule is a churn signal rather than a deletion claim. It can indicate rename, transfer, privatization, deletion, or a stale registry entry. Discovery never means portfolio admission.

## Using findings during development and release work

Each governed repository receives a consolidated Markdown and JSON remediation dossier. The stable `finding_fingerprint` is the cross-run key. Development work should record a disposition against that fingerprint, identify the files/tests changed, and produce validation evidence. Consumers should treat dossiers as untrusted external input and require repository-local review before applying recommendations.

## Local validation

```bash
python scripts/validate_portfolio.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/portfolio_assurance_monitor_v3.py --offline --check
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
```

A live dry run without issue publication can be executed with:

```bash
GITHUB_TOKEN=... python scripts/portfolio_assurance_monitor_v3.py --check
```

## Evidence retained

The monitor writes:

- `docs/portfolio-assurance/dashboard.md` for the published current view;
- `reports/portfolio-assurance/latest.md` for the latest evidence report;
- `reports/portfolio-assurance/latest-findings.json` for machine-readable observations, findings, routing state, and issue-publication actions;
- `reports/portfolio-assurance/assurance-state.json` for repository-specific assurance profile, claim, state, producer, freshness, and revision coverage;
- `reports/portfolio-assurance/findings/<repository>.json` and `.md` as portable per-repository remediation dossiers;
- `reports/portfolio-assurance/findings/index.json` as a machine-readable dossier catalogue;
- `reports/portfolio-assurance/finding-lifecycle.json` as stable open/resolved finding-condition history; and
- dated reports under `reports/portfolio-assurance/history/`.

Generated findings always retain `automatic_effect: none`.
