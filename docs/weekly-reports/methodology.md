---
layout: default
title: Weekly Reporting Methodology
parent: Weekly Portfolio Reports
---

# Weekly reporting methodology

## Scope and authority

Only public GitHub repositories owned by `sankarshanmukhopadhyay` and `qbf-consulting` are included in the headline counts. Contributions hosted upstream (including Trust Over IP) may be discussed with explicit upstream attribution but are **excluded from the two-owner counts**.

The reporting period is Monday 00:00:00 UTC to the following Monday 00:00:00 UTC, half-open `[start, end)`. Week 40's October-only seed covers October 1–4. Source queries are restricted by owner, PR author, and `merged_at`. A PR is counted once, in the period in which GitHub records its merge. Counts do not establish implementation quality, user impact, independent assurance, or acceptance by third-party authorities.

## Evidence levels

- **Observed:** a linked GitHub PR, release, workflow or repository artifact establishes the described event.
- **Interpreted:** a bounded editorial interpretation of observed changes.
- **Unknown:** tests, downstream adoption, correctness, deployment or conformance not independently verified.
- **Not scanned:** inaccessible sources; never presented as inactive.

Activity counts in the October backfill are author-attributed merged PR totals, **not** default-branch commit counts. Dates and repository owners are explicit. A merged PR may contain multiple commits; merges, squash merges and direct pushes are not treated as interchangeable. The initial backfill did not record per-repository SHA checkpoints; do not represent it as SHA-contiguous change accounting.

## Collection and publication

`scripts/weekly_portfolio_report.py` queries GitHub's search API with pagination, filters results to the requested half-open UTC interval, and records source PR URLs. It generates Markdown with a deterministic summary. It does not generate unsupported qualitative claims. The weekly workflow runs on Mondays and opens or updates a PR for the latest completed week. A maintainer reviews substance, evidence, links, CI and DCO before merging.

Weekly automation signs its own bot-authored commits with the bot's public noreply identity. It **must not** attach a human DCO certification on behalf of a person. Human edits should be separately committed with the actual contributor's verified noreply Git identity and `git commit -s`. A noreply address is still present in the public Signed-off-by trailer; a real/private address is not required.

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
