---
layout: default
title: Operations
parent: Portfolio Assurance Monitor
nav_order: 4
---

# Portfolio assurance operations

The Portfolio Assurance Monitor is an evidence-producing governance control. It observes governed repositories, evaluates deterministic operational, governance, and assurance-evidence rules, detects account-level classification drift, and can route narrowly scoped actionable findings to affected repositories. Observation and publication do not transfer repository, release, specification, risk-acceptance, or portfolio authority.

## Scheduled execution

The workflow reevaluates portfolio evidence every six hours and may also be invoked manually. It also runs when governed monitor configuration, repository status data, monitor implementation, the monitor workflow, or the core assurance-operations documentation changes. Generated report commits do not retrigger the monitor.

Its normal sequence is:

1. validate portfolio governance data;
2. execute the monitor tests;
3. collect repository metadata, default-branch HEAD, status declarations, and workflow evidence;
4. evaluate deterministic operational and governance findings;
5. evaluate repository-specific assurance evidence contracts, including required/optional semantics and freshness against governed revisions;
6. discover public repositories that lack an account-level disposition;
7. optionally route eligible findings to affected repositories;
8. render the dashboard, assurance-state artifact, remediation dossiers, and finding lifecycle evidence;
9. validate documentation links; and
10. commit changed evidence surfaces.

The six-hour cadence is an operational responsiveness control rather than an assurance claim. Repository-local evidence remains authoritative for the meaning of the underlying validation or conformance result.

## Assurance evidence contracts

Repository-specific contracts are defined in `config/portfolio-monitor/assurance-contracts.yaml`. A contract binds an explicit repository-native control to an assurance claim and states whether that evidence is required or optional and whether it must cover the current default-branch HEAD or may rely on the latest successful publication-specific execution.

The current evidence states are:

- `satisfied`: required evidence exists, succeeded, and meets the configured freshness policy;
- `degraded`: the required evidence-producing control completed unsuccessfully;
- `stale`: successful evidence exists but does not cover the governed revision required by policy;
- `missing`: required evidence was not observed inside the governed evidence window;
- `unobservable`: the configured evidence source could not be collected;
- `not-applicable`: no required claim applies to the evaluated scope; and
- `not-evaluated`: no governed contract or supported adapter exists.

These are evidence-coverage states. They do not silently strengthen the authority of the producing workflow. A successful conformance workflow, for example, is reported as successful evidence from that workflow; the portfolio monitor does not independently redefine what conformance means.

Optional evidence is recorded but cannot degrade the repository's aggregate assurance state. This keeps specialized mechanisms, including RAHP pressure tests, available as evidence sources without making any one mechanism the universal portfolio assurance provider.

## Workflow failure semantics

`collection.lookback_days` is an assurance policy boundary, not merely an API hint. The collector examines completed runs inside that window and retains only the latest completed state for each workflow. A historical failure that has been superseded by a later successful run does not produce `DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE`.

The API result count and assurance time window are deliberately separate controls:

```yaml
collection:
  lookback_days: 7
  workflow_runs_per_repository: 50
```

The result count limits collection volume. The lookback window determines which evidence is admissible for operational workflow health and repository-specific workflow evidence claims.

For `freshness: current-head`, a successful workflow run is insufficient unless its `head_sha` equals the observed default-branch HEAD. For path-filtered publication workflows, contracts may use `freshness: latest-success` when non-publication commits do not invalidate previously generated publication evidence.

## Stable finding identity

Every observation has a date-scoped `finding_id`, while a `finding_fingerprint` remains stable across repeated observations of the same repository, rule, and affected subject.

```text
repository + rule + subject -> finding_fingerprint
finding_fingerprint + observation date -> finding_id
```

This distinction permits durable issue deduplication and machine-verifiable recovery without erasing observation history.

## Target-repository issue routing

Issue publication is implemented but **disabled by default** in `config/portfolio-monitor/policy.yaml`. Enable it only after a scoped GitHub App is installed on the repositories that may receive findings.

Recommended GitHub App permissions:

| Permission | Access |
|---|---|
| Metadata | Read |
| Actions | Read |
| Contents | Read and write* |
| Issues | Read and write |

\* `Contents: Read and write` is required only because this App is also the explicitly delegated publisher for generated assurance evidence in this profile repository. The workflow mints a separate publication token scoped to `sankarshanmukhopadhyay/sankarshanmukhopadhyay`; issue-routing and evidence-publication tokens remain separate.

Do not use the profile repository's ordinary `GITHUB_TOKEN` for cross-repository issue publication. That token is repository-scoped. The workflow expects a separately generated installation token in `PORTFOLIO_ISSUE_TOKEN`.

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

The default routing policy excludes review-overdue, inactivity, and account-discovery findings from target repositories. Those are portfolio-governance observations rather than repository-local defects.

## GitHub App workflow setup

Configure repository secrets:

- `PORTFOLIO_ASSURANCE_APP_ID`
- `PORTFOLIO_ASSURANCE_APP_PRIVATE_KEY`

Then set `issue_routing.enabled: true`. The workflow uses `actions/create-github-app-token` to mint a short-lived installation token and invokes:

```bash
python scripts/portfolio_assurance_monitor_v3.py --publish-issues
```

If the App credentials are absent, evidence collection and evaluation may proceed, but protected-branch evidence publication fails closed and no cross-repository issue writes occur.

For protected-branch publication, add the installed Portfolio Assurance GitHub App itself to the `protect-main` ruleset bypass list with **Always allow**. Do not grant a user, administrator role, or generic workflow principal a bypass. The repository-side publication token is scoped to this repository, and the workflow independently rejects generated changes outside `docs/portfolio-assurance/dashboard.md` and `reports/portfolio-assurance/**`.

## Deduplication and repeat observations

Each generated issue contains a machine-readable marker:

```html
<!-- portfolio-assurance:fingerprint=PF-XXXXXXXXXXXX -->
```

Before creation, the publisher searches the affected repository for an open issue containing that marker. Repeated observations are deduplicated. `comment_on_repeat` is false by default to avoid repetitive issue traffic.

The default `max_new_issues_per_run` is `2`, providing a hard blast-radius limit even when multiple repositories fail simultaneously.

## Recovery and closure

The monitor maintains an observation-level lifecycle registry in `reports/portfolio-assurance/finding-lifecycle.json`. When a stable fingerprint that was previously open is no longer observed on a later run, the monitor records that finding condition as `resolved` with a resolution timestamp. This is machine-verifiable recovery evidence.

The monitor still does **not** automatically close GitHub issues, accept risk, approve implementation, change maturity/lifecycle, or make repository release decisions. Those remain repository- and portfolio-governance actions.

This preserves the distinction:

```text
observation -> finding -> remediation dossier -> implementation -> re-observation -> finding recovery evidence
                                                \-> governed issue/disposition closure
```

Finding-condition recovery is machine-verifiable; implementation acceptance and issue closure authority remain governed.


## Repository remediation retest discipline

When an actionable finding is routed to a target repository, remediation SHOULD follow an evidence-closed sequence:

1. preserve the stable `finding_fingerprint` in the repository-local issue and PR;
2. repair the repository-native control or evidence-production semantics without weakening the claim being tested;
3. require successful repository-native validation before merge;
4. require the governed default-branch evidence producer to execute after merge;
5. rerun this monitor only after the relevant repository evidence is observable; and
6. close the repository-local remediation issue only after the lifecycle registry records the fingerprint as `resolved`, unless repository governance explicitly accepts the residual risk.

A PR merge or an unrelated green workflow is not sufficient recovery evidence. The authoritative implementation claim remains with the producing repository; the Portfolio Assurance Monitor independently records whether the configured evidence contract is now satisfied.

This sequence provides a machine-verifiable control loop:

```text
finding fingerprint
  -> repository-local remediation
  -> native validation
  -> default-branch evidence
  -> portfolio re-observation
  -> lifecycle resolution
  -> governed issue closure
```

## Public account discovery and repository churn

The monitor compares live public repositories against `data/repository-status.yaml` in both directions. An unclassified public repository produces `PUBLIC_REPOSITORY_WITHOUT_DISPOSITION`. A governed active or review repository that disappears from public account discovery produces `REGISTERED_REPOSITORY_NOT_PUBLICLY_DISCOVERED`.

The second rule is a churn signal rather than a deletion claim. It can indicate rename, transfer, privatization, deletion, or a stale registry entry. The monitor does not guess the replacement identity; a human must update the governed repository record and any affected relationships. Historical, superseded, and archived records are excluded to avoid churn noise.

Discovery never means portfolio admission. The expected remediation for a new repository is to assign one governed disposition such as `included`, `adjacent`, `upstream-reference`, `adapted-upstream-work`, `historical`, `unrelated`, or `pending-review`.

## Using findings during development and release work

Each governed repository receives a consolidated Markdown and JSON remediation dossier. The recommended development pattern is to download the target repository's Markdown dossier and supply it alongside the repository source at the beginning of a release or implementation cycle. The JSON form provides the equivalent machine-readable contract. This makes unresolved findings explicit requirements for review without silently converting monitor recommendations into normative changes.

The stable `finding_fingerprint` is the cross-run key. Development work should record a disposition against that fingerprint, identify the files/tests changed, and produce validation evidence. A later monitor run then provides independent recovery evidence if the underlying condition is no longer observed.

Consumers SHOULD treat the dossier as untrusted external input to the implementation process: validate its schema/shape, preserve the source URL and generation timestamp, and require repository-local review before applying any recommended change.

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
- `reports/portfolio-assurance/findings/<repository>.json` and `.md` as portable, per-repository remediation dossiers;
- `reports/portfolio-assurance/findings/index.json` as a machine-readable dossier catalogue;
- `reports/portfolio-assurance/finding-lifecycle.json` as stable open/resolved finding-condition history; and
- dated reports under `reports/portfolio-assurance/history/`.

Generated findings always retain `automatic_effect: none`.
