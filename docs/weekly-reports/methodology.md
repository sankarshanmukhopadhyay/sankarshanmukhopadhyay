---
layout: default
title: Weekly Reporting Methodology
parent: Weekly Portfolio Reports
---

# Weekly reporting methodology

## Scope and authority

Only public GitHub repositories owned by `sankarshanmukhopadhyay` and `qbf-consulting` are included in the headline counts. Contributions hosted upstream (including Trust Over IP) may be discussed with explicit upstream attribution but are **excluded from the two-owner counts**.

The reporting period is Monday 00:00:00 UTC to the following Monday 00:00:00 UTC, half-open `[start, end)`. Week 40's October-only seed covers October 1–4. The October editorial backfill used owner-scoped, author-attributed merged PRs. Its counts are not equivalent to the broader schema 2.0 event counts used for operational reports. A PR merge is attributed to the period of GitHub's recorded merge timestamp. Counts do not establish implementation quality, user impact, independent assurance, or acceptance by third-party authorities.

## Evidence levels

- **Observed:** a linked GitHub PR, release, workflow or repository artifact establishes the described event.
- **Interpreted:** a bounded editorial interpretation of observed changes.
- **Unknown:** tests, downstream adoption, correctness, deployment or conformance not independently verified.
- **Not scanned:** inaccessible sources; never presented as inactive.

Activity counts in the October backfill are author-attributed merged PR totals, **not** default-branch commit counts. Dates and repository owners are explicit. A merged PR may contain multiple commits; merges, squash merges and direct pushes are not treated as interchangeable. The initial backfill did not record per-repository SHA checkpoints; do not represent it as SHA-contiguous change accounting.

## Collection and publication

`scripts/weekly_portfolio_report.py` queries GitHub's search API with pagination, filters results to the requested half-open UTC interval, and records source PR URLs. It generates Markdown with a deterministic summary. It does not generate unsupported qualitative claims. The weekly workflow runs on Mondays and may also be dispatched manually or after reporting-code changes reach `main`. It scans from the first operational week (26 October 2026) through the last fully completed UTC week, generates **all missing complete Markdown/JSON pairs**, and updates the navigable archive index in the same change. It refuses to overwrite a report or silently accept a partial Markdown/JSON pair. No GitHub API token, incomplete source search, or malformed index is treated as a successful report. A run with no missing completed week produces no PR. A maintainer reviews substance, source completeness, links, CI and DCO before merging. Successful generation alone does not publish a report.

The workflow requires the configured repository-scoped GitHub App token to create reviewable PRs. The job-scoped `GITHUB_TOKEN` remains valid for read-only collection but is intentionally not used to publish PRs, since its generated PR events do not ordinarily trigger required CI workflows. Missing App credentials fail visibly without attempting a lower-assurance publication path. It proposes a unique branch per run without pushing directly to protected `main`. After a report PR is merged, the normal Pages workflow deploys the reviewed site. The Pages build checks rendered weekly-report routes.\n\nWeekly automation signs its own bot-authored commits with the bot's public noreply identity. It **must not** attach a human DCO certification on behalf of a person. Human edits should be separately committed with the actual contributor's verified noreply Git identity and `git commit -s`. A noreply address is still present in the public Signed-off-by trailer; a real/private address is not required.

## Known limitations

- No claim of exhaustively collecting collaborators' authored PRs, direct pushes or private repositories.
- No like-for-like test count or CI coverage changes until repository-specific baselines are established.
- No inference of a repository's maturity or assurance state from PR counts.
- The weekly source query is GitHub's API snapshot at run time; late edits may change descriptions, but merge timestamps remain the reporting attribution.
- GitHub search imposes query pagination and result bounds. Any incomplete result or overflow must fail rather than silently produce a complete-looking report.
- Historical backfill describes evidence available at preparation time, not a historical snapshot of every PR's state as of the original Sunday.

## Expanded contribution footprint (schema 2.0)

Starting with reports generated after the October backfill, GitHub collection searches the **author's public contributions across all repository owners**, not merely the two maintained scopes. Each event is attributed to either `portfolio` (repository owned by `sankarshanmukhopadhyay` or `qbf-consulting`) or `external` (all other owners). Owner identity is not a claim of authorship, acceptance authority, or maturity.

The ledger records five separately dated lifecycle events: PR opened, PR merged, PR closed without merge, issue opened, and issue closed. One PR can have an opening event in one week and a merger in another; neither event is silently dropped. Closure of a merged PR is **not** counted again as unmerged closure. Items are deduplicated by platform, type, repository, number and event. Records include source URLs and event timestamps. Report sections separate portfolio and external work, and keep GitHub metadata distinct from editorial impact statements.

**Coverage exclusions:** Issue/PR review comments, review submissions, discussions, GitLab and other standards platforms, commits pushed directly, private contributions, and contributions authored by other maintainers are not included. In particular, comments on existing upstream issues are important activity that this collector **does not yet represent**. Do not call the result a complete contribution inventory. Adding comments/reviews requires a separate event source with stable IDs and timestamps, not inference from `updated_at`.

The original October Week 40–43 backfill remains an immutable **legacy owner-scoped merged-PR editorial baseline**. No historical report should be rewritten with broader totals without a separately traceable reconciliation; schema 2.0 starts with newly generated weeks. The generator refuses incomplete GitHub searches and refuses to overwrite archived reports. No automated determination of substantive merit, acceptance, conformance or assurance is made.

## October 2026 external GitHub reconciliation (27 October)

The Week 40–43 published narratives were originally scoped to personal/QBF author-attributed PR merges. An additive, dated external contribution section was appended to each report on 27 October 2026. The expanded external observations use GitHub issue search restricted to public repositories outside both owner scopes, `author:sankarshanmukhopadhyay`, and the respective inclusive October calendar days. Values were cross-checked against source links. They are separate event counts, not an amendment of the original owner-scoped baseline. Week 40 is October 1–4 only.

| Week | External PRs opened | External PRs merged | External issues opened |
|---|---:|---:|---:|
| 40 | 0 | 0 | 2 |
| 41 | 11 | 4 | 4 |
| 42 | 1 | 3 | 0 |
| 43 | 7 | 3 | 12 |

This October reconciliation does not purport to reconstruct discussions, reviews, GitLab activity, private contributions or a historical point-in-time GitHub snapshot. External PR merge is evidence of upstream integration but not of independent assurance or normative approval beyond that project's documented process. Current generator schema 2.0 applies to future weeks; October appendices are a separately sourced retrospective.
