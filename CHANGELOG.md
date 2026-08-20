# Changelog


## 2026-08-16 — Portfolio assurance routing and portfolio refresh

- Promoted `rahp-toolkit` into the original flagship assurance portfolio and retained `dtgwg-rahp-tf` as historical/superseded lineage.
- Added `route-story-studio` as an explicit pending-review account disposition rather than inferring portfolio membership.
- Corrected workflow-failure semantics to evaluate the latest completed state per workflow within the governed lookback window.
- Added stable finding fingerprints, target-repository routing policy, issue deduplication, and per-run publication caps.
- Added public-account discovery for repositories lacking a governed disposition without automatic enrolment.
- Added optional GitHub App based cross-repository issue publication; the capability remains disabled until explicitly configured.
- Expanded assurance methodology, operations guidance, schemas, and automated tests.

All notable changes to the portfolio coordination repository are documented here.

## [Unreleased]

### Added

- Added repository remediation dossiers as the canonical portfolio-to-repository handoff artifact, with rendered views plus direct Markdown and JSON downloads.
- Added repository snapshot provenance, including the observed default-branch commit SHA when available.
- Added remediation objectives, acceptance criteria, verification guidance, assessment dimensions, and stable finding lifecycle evidence.
- Added `finding-lifecycle.json` so open findings retain first/last-observed state and later disappearance is recorded as resolution rather than silently discarded.
- Added fail-closed findings for unavailable required status-declaration evidence and unavailable workflow evidence.
- Added schema-backed, per-repository portfolio finding feeds in downloadable JSON and Markdown forms, plus a machine-readable feed index.
- Added documentation for using unresolved assurance findings as explicit development and release-planning inputs while preserving repository-local disposition authority.

- Added `PolicyMesh` as governed supporting work for bounded policy/mandate evaluation and enforcement.
- Added `trust-protocol-interop-lab` as the cross-protocol composition and interoperability-assurance layer.
- Added `dtg-portfolio-monitor` as the wider DTG ecosystem situational-awareness layer.
- Replaced the former active `dtgwg-rahp-tf` presentation with the standalone original `rahp-toolkit`; the old fork record remains historical lineage.
- Added typed relationships for PolicyMesh semantic alignment, ecosystem-signal nomination, interoperability pressure testing, and standalone RAHP assurance support while retaining historical upstream provenance separately.
- Added public portfolio-member discoverability validation.
- Added split licensing for software and written portfolio content.

### Changed

- Pinned the portfolio relationship contract to Trust Infrastructure Schemas v0.13.0 and the reviewed canonical semantic authority to Trust Systems Meta Model v0.24.0.
- Added machine-verifiable TSMM/TIS relationship contract and alignment-evidence references to the canonical portfolio relationship registry.
- Rescoped development finding feeds into consolidated repository remediation dossiers intended to travel with repository source during implementation work.
- Separated operational and governance evaluation from substantive assurance and cross-specification assurance; unevaluated dimensions are now explicit rather than implicitly green.
- Changed zero-finding language so it claims only that evaluated rules produced no findings, not that the repository or portfolio is fully assured.
- Updated the portfolio register and public surfaces for the transition from `ctwg-main-glossary` to the independently governed `trust-infrastructure-glossary`.
- Linked assurance dashboard finding counts to repository-scoped development feeds and included those feeds in workflow artifacts.
- Reorganised supporting work by capability rather than as a flat repository list.
- Extended the five-plane architecture with cross-cutting policy execution, interoperability, and ecosystem-observation capabilities without creating new authority planes.
- Distinguished portfolio assurance, ecosystem observation, interoperability experimentation, conformance, security hardening, and RAHP pressure testing.
- Reclassified `PolicyMesh` from pending review/incubating to included/supporting based on its repository-local status declaration.
- Normalised the changelog into one current Unreleased section.

### Governance

- Enforced the TSMM/TIS authority split in portfolio validation: TSMM remains canonical semantic authority, TIS remains portable serialization/validation authority, and this repository remains portfolio classification authority.
- Observation signals may nominate human review but cannot create interoperability claims or portfolio classifications.
- Interoperability experiments own only experimental compositions, evidence, findings, and maturity claims.
- RAHP findings and tooling do not transfer governance, release, or adoption authority to reviewed specifications or external deployments.

## [0.3.0] - 2026-07-20

### Added

- Added the Open National Digital Trust Framework as a flagship working draft and national-framework adoption entry point.
- Added typed ONDTF relationships to GAAM, TSMM, TIS, and DTG Conformance and Assurance.
- Added `adapted-upstream-work` as a governed portfolio disposition.
- Added explicit repository provenance, upstream location, portfolio-governance scope, maturity, and upstream-adoption status metadata.
- Added machine-verifiable `fork-of` relationships for adapted and upstream-reference repositories.

### Changed

- Evolved the portfolio from a four-plane to a five-plane architecture with a frameworks-and-adoption plane.
- Reclassified `dtgwg-zkp-tf` as featured adapted upstream work with fork-local implementation-draft maturity.
- Strengthened validator rules for fork-local maturity, governance scope, upstream attribution, and membership.
- Aligned TSMM and TIS as Candidate repositories with member-owned status contracts.
- Added the TIS-to-TSMM normative dependency and bounded authority constraint.
- Added coordinated release-impact evidence and Just The Docs publication controls.
- Rebalanced featured work around GAAM, Agent Registry Protocol, TSMM, TIS, Trust Graph Artifacts, and the TRQP assurance stack.
- Separated original flagship work from upstream-derived collaborative work.

## Earlier portfolio-governance foundation

### Added

- Machine-readable repository lifecycle and authority registries.
- Portfolio governance, architecture, drift-review, adoption, and release-impact controls.
- Automated validation and GitHub Actions enforcement.
- GitHub Pages-compatible documentation entry point.
- Federated `PROJECT-STATUS.yaml` contract, JSON Schema, template, and validation controls.
- Embedded Portfolio Assurance Monitor with registry-derived scope, deterministic finding rules, evidence schemas, reporting, tests, and automation.

### Changed

- Reframed the profile README as an adoption-oriented portfolio landing page with explicit evidence and authority boundaries.
- Separated portfolio disposition, strategic tier, maturity, lifecycle, operational status, specification status, provenance, and authority.
- Adopted a controlled maturity vocabulary and a curated portfolio boundary.
