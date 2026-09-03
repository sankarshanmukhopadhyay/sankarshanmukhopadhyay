---
layout: default
title: Portfolio Change Convention
parent: Portfolio Work Queue
nav_order: 3
---

# Portfolio change convention

Issues and pull requests should use a typed title:

```text
<type>(<scope>): <imperative summary>
```

Examples:

```text
fix(assurance): reject stale evidence after material change
feat(lifecycle): add bounded reassessment evidence
docs(adoption): add minimal TSMS implementation walkthrough
chore(governance): close public repository baseline gaps
test(composition): add negative cross-context correlation case
refactor(controller): separate routing from assessment execution
ci(pages): fail on unrendered documentation surfaces
security(runtime): reject cross-context disclosure
governance(authority): narrow release override scope
```

Supported types are `feat`, `fix`, `docs`, `test`, `chore`, `refactor`, `ci`, `perf`, `security`, and `governance`.

`security` and `governance` are first-class portfolio types because collapsing them into `fix` or `chore` would hide material assurance and authority consequences.

## Breaking changes

Use `!` for consumer-visible incompatibility:

```text
feat(schema)!: replace legacy lifecycle event contract
refactor(authority)!: remove implicit delegation fallback
```

`!` means breaking compatibility, not merely a large change. A breaking PR should contain a `BREAKING CHANGE` section describing affected consumers, migration, rollback/recovery, compatibility evidence, and whether assurance reassessment is required.

## Machine-readable issue metadata

Consequential issues should include a compact classification block where useful:

```yaml
change:
  type: governance
  scope: authority
  breaking: true
  authority_impact: material
  assurance_impact: material
```

The title remains the primary lightweight classification surface. Embedded metadata can add authority and assurance impact that the title cannot safely infer.

## Planner semantics

Change type, lifecycle state, impact, and priority are independent. A high-priority issue may correctly be `waiting_external`; a maintenance `chore` may be `ready` without entering the strategic work-now lane; a breaking/security/governance change must fail closed toward consequential judgment rather than silently appearing as a quick win.

The planner records whether change classification came from the typed title or inference. Untyped legacy issues remain visible but receive lower classification confidence.

See the [methodology](methodology.md) for the evidence-backed lifecycle and reconciliation model.
