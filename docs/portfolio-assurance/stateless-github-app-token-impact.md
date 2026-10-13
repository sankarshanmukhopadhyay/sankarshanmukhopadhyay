# Stateless GitHub App installation token impact audit

Date: 2026-10-13

## Purpose

GitHub has completed rollout of the stateless GitHub App installation token format. Newly minted installation tokens still use the `ghs_` prefix, but are now approximately 520 characters long and use the `ghs_APPID_JWT` representation. Token permissions, repository scoping, the one-hour expiration period, and the installation access-token REST endpoint are unchanged.

This audit records the expected impact across the `sankarshanmukhopadhyay` and `qbf-consulting` GitHub portfolios and identifies the surfaces that require runtime confirmation.

Primary GitHub notices:

- 2026-04-24: <https://github.blog/changelog/2026-04-24-notice-about-upcoming-new-format-for-github-app-installation-tokens/>
- 2026-05-15: <https://github.blog/changelog/2026-05-15-github-app-installation-tokens-per-request-override-header/>
- 2026-10-02: <https://github.blog/changelog/2026-10-02-stateless-github-app-installation-tokens-rolled-out/>

## Portfolio disposition

| Portfolio | Disposition | Rationale |
| --- | --- | --- |
| `sankarshanmukhopadhyay` | Evidence required for one confirmed GitHub App automation surface | The profile repository uses `actions/create-github-app-token@v2` in two workflows that publish and merge portfolio-assurance evidence. No static evidence of hard-coded `ghs_` length assumptions was found in repository code search. |
| `qbf-consulting` | No confirmed GitHub App installation-token producer found by static search | Repository workflows inspected so far use ordinary Actions tokens or GitHub CLI paths. No `create-github-app-token`, `ghs_`, or stateless-token override-header usage was found by code search. |

## Confirmed token-producing surfaces

### `sankarshanmukhopadhyay/sankarshanmukhopadhyay`

| File | Token source | Consumer path | Risk | Required evidence |
| --- | --- | --- | --- | --- |
| `.github/workflows/portfolio-assurance-monitor.yml` | `actions/create-github-app-token@v2` | `PORTFOLIO_ISSUE_TOKEN`, `GH_TOKEN`, `gh`, and authenticated `git push` | Medium | Successful workflow run after rollout; no token truncation; no token leakage; PR publication remains scoped to allowed evidence paths. |
| `.github/workflows/portfolio-assurance-evidence-merge.yml` | `actions/create-github-app-token@v2` | `GH_TOKEN` consumed by `gh pr list`, `gh pr view`, `gh pr checks`, and `gh pr merge` | Medium | Successful merge workflow run after rollout; required-check gate remains intact; no reliance on token length or JWT contents. |

The monitor workflow intentionally removes the default checkout credential and uses a scoped GitHub App token for evidence publication. That authority boundary remains sound, but the Git remote credential path must tolerate the longer token.

## Static search evidence

Searches performed through repository code search on 2026-10-13:

| Query | Scope | Result | Interpretation |
| --- | --- | --- | --- |
| `create-github-app-token` | `sankarshanmukhopadhyay` | 2 matches | Confirmed GitHub App installation-token producers in profile repository workflows. |
| `create-github-app-token` | `qbf-consulting` | 0 matches | No confirmed QBF GitHub App installation-token producer found by search. |
| `ghs_` | `sankarshanmukhopadhyay` | 0 matches | No obvious token-prefix regex or hard-coded legacy-token sample found. |
| `ghs_` | `qbf-consulting` | 0 matches | No obvious token-prefix regex or hard-coded legacy-token sample found. |
| `X-GitHub-Stateless-S2S-Token` | `sankarshanmukhopadhyay` | 0 matches | No production dependency on the temporary override header found. |
| `X-GitHub-Stateless-S2S-Token` | `qbf-consulting` | 0 matches | No production dependency on the temporary override header found. |

Static search is negative evidence only. It does not prove runtime compatibility because it may miss generated files, unindexed code, dependency behaviour, branch-only files, external services, or infrastructure outside GitHub repositories.

## Impact model

The token-format change is compatibility-significant only where repository code, workflow glue, storage, transport, or logging assumes a short opaque installation token.

### Compatibility risks

| Risk | Portfolio relevance | Required control |
| --- | --- | --- |
| Fixed token length such as 40 characters | No match found | Keep tokens opaque; reject fixed-length validation. |
| Regex constrained to legacy `ghs_` token shape | No match found | If token regex is ever introduced, use an opaque-token rule compatible with both formats. |
| Secret store or database field too short | No repository evidence found | Inspect only if tokens are persisted outside Actions runtime. |
| Authorization header truncation | Possible at Git/GitHub CLI boundary | Confirm via actual workflow execution. |
| Logging/redaction mismatch | Possible for long token in shell commands | Confirm logs redact token and do not expose full authenticated remote. |
| JWT claim introspection | No match found | Do not parse or authorize based on JWT body. |
| Dependency on temporary override header | No match found | No action unless future evidence contradicts search. |

## Validation plan

### Runtime checks for profile repository workflows

1. Run `Portfolio assurance monitor` on the `audit/stateless-github-app-tokens` branch or after merge.
2. Confirm `Create scoped portfolio issue token` succeeds.
3. Confirm `Create repository-scoped publication token` succeeds.
4. Confirm evidence publication either:
   - creates or updates the governed evidence PR; or
   - exits cleanly because there is no evidence delta.
5. Confirm logs do not reveal token contents.
6. Confirm any generated PR changes remain limited to:
   - `docs/portfolio-assurance/dashboard.md`
   - `reports/portfolio-assurance/**`
7. Run `Merge portfolio assurance evidence` on a qualifying governed evidence PR.
8. Confirm the required-check gate remains effective before merge.

### Static regression expectations

A future static scanner, if added to portfolio-assurance tooling, should flag:

```text
ghs_[A-Za-z0-9]{36}
len(token) == 40
len(github_token) == 40
TOKEN_LENGTH = 40
VARCHAR(40) columns used for GitHub installation tokens
X-GitHub-Stateless-S2S-Token used outside temporary local validation
JWT claim parsing applied to ghs_ installation tokens
```

This audit does not add such a scanner yet because current evidence shows one bounded runtime surface rather than a portfolio-wide recurring defect class.

## Repository-by-repository initial register

| Repository | Initial classification | Notes |
| --- | --- | --- |
| `sankarshanmukhopadhyay/sankarshanmukhopadhyay` | Evidence required | Confirmed `actions/create-github-app-token@v2` use in two portfolio-assurance workflows. |
| `sankarshanmukhopadhyay/dtg-portfolio-monitor` | Evidence required | Likely portfolio automation consumer; no confirmed App token producer in current search. |
| `sankarshanmukhopadhyay/trust-ecosystem-monitor` | Low to medium | Uses `GITHUB_TOKEN` for collection paths; ordinary token pass-through appears likely, but custom client handling should remain opaque. |
| `sankarshanmukhopadhyay/uncefact-portfolio-monitor` | Evidence required | Monitor-style automation should be checked if active. |
| `sankarshanmukhopadhyay/rahp-toolkit` | Low to medium | CI/release automation may use GitHub tokens; no confirmed App token generation from current search. |
| `sankarshanmukhopadhyay/trqp-assurance-hub` | Low | Observed token use appears to be maintained Actions/GitHub CLI paths. |
| `sankarshanmukhopadhyay/trust-protocol-interop-lab` | Evidence required | Interop automation should be checked if it performs authenticated cross-repository operations. |
| `sankarshanmukhopadhyay/kiranaos` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/digital-trust-failure-corpus` | Low | Release workflow uses `github.token` through GitHub CLI; no custom token-shape handling observed. |
| `qbf-consulting/agent-registry-protocol` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/trust-infrastructure-schemas` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/trust-systems-meta-model` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/governance-authority-assurance-metamodel` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/open-national-digital-trust-framework` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/qbf-consulting.github.io` | Low | Site publication should rely on standard Actions token handling. |
| `qbf-consulting/.github` | Low | No confirmed App token generation from current search. |
| `qbf-consulting/signal-ledger` | Low | No confirmed App token generation from current search. |

## Decision

Do not open issues across every repository.

Open one portfolio-level tracker in `sankarshanmukhopadhyay/sankarshanmukhopadhyay` because the confirmed token-producing workflows live there and because the repository already owns the portfolio-assurance control plane.

Only open repository-specific remediation issues if runtime validation or deeper inspection finds an actual token-format defect.

## Residual risk

- Runtime compatibility of the confirmed GitHub App workflows remains pending until a post-rollout workflow run is inspected.
- This audit does not inspect external secret managers, local developer machines, or infrastructure outside GitHub repositories.
- Code search is not a complete proof of absence.
- Dependencies used by Actions and GitHub CLI are assumed to handle GitHub's token format unless runtime evidence shows otherwise.

## Completion criteria

This tranche is complete when:

- this audit artifact is merged;
- the tracker issue links this document;
- the two confirmed profile-repository workflows have one successful post-rollout execution or a documented non-execution reason;
- any discovered incompatibility has a repository-local issue or PR;
- no production code depends on the temporary override header after 2026-11-30.
