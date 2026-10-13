# Portfolio strategy context

Status: **working strategy context**  
Scope: Sankarshan Mukhopadhyay personal/upstream-facing portfolio and QBF Consulting institutional portfolio view  
Last updated: 2026-10-13

## Purpose

This note captures the strategic context behind the evidence-gated portfolio maturity work. It is intended to preserve the reasoning needed for later repository planning, issue triage, release decisions, and QBF/public-facing portfolio positioning.

It should be read with:

- `data/repository-status.yaml` — the canonical portfolio membership, maturity, lifecycle, authority, provenance and review-date register;
- `data/portfolio-evidence-gates.yaml` — the evidence-gated overlay describing maturity boundaries, next evidence gates, stop conditions and external dependencies; and
- `docs/portfolio-evidence-gates.md` — the operating guide for the evidence-gated overlay.

## Governing thesis

The portfolio should not optimize for activity volume, line count, or a continually expanding set of internal artifacts.

The portfolio should optimize for:

- clear claim boundaries;
- executable evidence;
- reusable assurance patterns;
- explicit stop conditions;
- public readability and adoption clarity;
- disciplined separation between personal/upstream-facing work and QBF institutional assets.

The central maturity rule is:

> A repository is mature when it can state what evidence it can produce internally, what evidence it cannot produce internally, and what external gate is required before further claims are justified.

This reframes a plateau from a negative signal into a governance question. A plateau may mean a repository is mature enough to stop internal tinkering until an external reviewer, implementer, user, upstream authority, or evidence-producing workflow appears.

## Why this became necessary

The portfolio contains repositories with different authority surfaces:

- personal and upstream-facing research/specification contributions;
- QBF Consulting public assets;
- assurance tooling;
- failure and falsification corpora;
- protocol and registry design work;
- applied labs and interop demonstrations;
- paper notes and research archives.

Without an evidence-gated maturity view, repositories can appear stalled, under-developed, or over-active for the wrong reasons.

The useful strategic question is not:

> What can be added next?

The useful strategic question is:

> What kind of evidence would make the next change legitimate?

## Portfolio boundary model

The portfolio should keep one shared maturity logic and expose different views.

```text
One maturity model / one evidence-gate vocabulary
Two major views:
1. Personal / upstream-facing portfolio
2. QBF institutional portfolio
```

The personal/upstream-facing view is suitable for:

- experimental work;
- upstream contribution preparation;
- analytical forks;
- speculative architecture;
- public learning artifacts;
- research notes and issue-driven exploration.

The QBF institutional view is suitable for:

- client-visible assurance assets;
- reusable frameworks;
- public consulting reference material;
- stable or evidence-gated methods;
- repositories that can support an institutional claim without overstating adoption, conformance or production readiness.

This separation should be a view boundary, not a duplication of governance logic.

## Evidence-gated maturity ladder

The recommended maturity ladder is:

```text
Concept
→ Claim
→ Contract
→ Fixture
→ Negative control
→ CI evidence
→ Evidence manifest
→ Independent reproduction gate
→ Assessment bridge
→ Non-synthetic target admission
→ External evidence
→ Determination
```

Not every repository needs every rung. But every repository should be able to say which rung it is currently on and what kind of evidence would move it forward.

## Repository role patterns

### Corpus repositories

A corpus repository should not only collect examples. It should define falsifiable propositions.

Expected evidence posture:

- failure proposition;
- claim boundary;
- evidence schema;
- negative controls where applicable;
- reproducibility guidance;
- explicit distinction between case documentation and assessed truth.

Example: `digital-trust-failure-corpus`.

### Toolkit repositories

A toolkit repository should produce evidence, not just output.

Expected evidence posture:

- input contract;
- execution path;
- machine-checkable result;
- audit/review record;
- failure mode visibility;
- clear statement of what the tool does not determine.

Example: `rahp-toolkit`.

### Protocol/specification repositories

A protocol or specification repository should define semantics and implementation expectations without claiming adoption or ecosystem validity prematurely.

Expected evidence posture:

- normative scope;
- authority model;
- lifecycle model;
- conformance or interop requirements;
- implementation or test evidence gates;
- relationship to upstream or external standards.

Examples: `agent-registry-protocol`, `tswg-trust-registry-protocol`.

### Interop and lab repositories

A lab repository should distinguish demonstration from assurance.

Expected evidence posture:

- experiment scope;
- participating components;
- composition assumptions;
- evidence captured;
- non-transferability of findings;
- clear route from experiment to reusable profile, test or issue.

Example: `trust-protocol-interop-lab`.

### Research and paper-note repositories

A research repository should preserve intellectual traceability without becoming a false implementation signal.

Expected evidence posture:

- source reviewed;
- interpretation boundary;
- issue linkage;
- relevance to portfolio themes;
- no implication of endorsement, adoption or implementation.

Example: `digital-governance-paper-notes`.

## CPC-001 as the reference example

The CPC-001 delegated-agent revocation work in `digital-trust-failure-corpus` is the current reference example for evidence-gated maturity.

It moved through:

1. baseline case framing;
2. protection contracts;
3. revocation semantics;
4. executable synthetic fixture;
5. deliberately defective target;
6. CI-backed synthetic evidence package;
7. independent reproduction template;
8. RAHP assessment bridge;
9. non-synthetic implementation admission gate;
10. candidate target selection register;
11. follow-up issue for identifying a real non-synthetic target.

The important strategic result is not that CPC-001 produced more files. The important result is that CPC-001 reached a defensible internal stop point.

Current evidence boundary:

```text
executed-synthetic-target
ci-executed-synthetic-target
```

Still absent:

```text
independent-reproduction
completed-rahp-assessment
non-synthetic-implementation
consumer-usability-validation
```

This is the pattern to reuse: internal readiness should stop when the next valid claim requires external evidence.

## Strategic implications

### 1. More work is not always more maturity

A repository can become less credible if it continues producing internal artifacts after it has reached an evidence boundary.

Valid next work should improve at least one of:

- evidence quality;
- adoption clarity;
- independent reproducibility;
- assessment readiness;
- implementation binding;
- public documentation usability;
- governance or release hygiene.

### 2. Stop conditions are portfolio assets

A stop condition is not a sign of abandonment. It is a control that prevents overclaiming.

Examples:

- pause until upstream accepts or rejects a contribution;
- pause until an independent reviewer reproduces results;
- pause until a non-synthetic target exists;
- pause until there is user or implementer feedback;
- pause until a release candidate has a real adoption path.

### 3. QBF should inherit evidence, not ambiguity

A repository should not be made institutionally prominent merely because it exists or because it is active.

For QBF relevance, ask:

- What claim would QBF make by pointing to this repository?
- What evidence supports that claim?
- What evidence is explicitly absent?
- Is the repository advisory, research, product-like, protocol-like, or assurance-facing?
- What should not be claimed in client or public-facing material?

### 4. Personal and QBF views should remain interoperable

Personal/upstream-facing work can feed QBF assets, but only through an explicit evidence boundary.

Possible relationships:

- QBF consumes a personal/upstream-facing method;
- QBF hosts the institutional version;
- QBF references but does not maintain the work;
- QBF treats the work as research context only;
- QBF deliberately excludes the work from institutional claims.

## Operating questions for future work

Before opening a new issue or PR, ask:

1. What claim is this repository currently making?
2. What evidence does it currently produce?
3. What evidence is missing?
4. Can the missing evidence be produced internally?
5. If not, who or what must produce it?
6. Does the proposed change advance an evidence gate or only add polish?
7. Is this work personal/upstream-facing, QBF-facing, or shared?
8. What should remain explicitly unclaimed after the change?
9. What test, CI check, schema, manifest, or review artifact will make the change auditable?
10. What stop condition should apply after the change?

## Portfolio triage rule

A repository should be categorized into one of these planning states:

| State | Meaning | Appropriate next action |
|---|---|---|
| `continue-internal-build` | More internal work can materially improve evidence, clarity or adoption | Open bounded issue/PR |
| `evidence-gated-pause` | Internal preparation is sufficient; next progress requires external evidence | Record stop condition and wait |
| `upstream-dependent` | Next progress depends on upstream review, merge or standards decision | Track upstream and avoid downstream drift |
| `adoption-dependent` | Next progress requires implementer/user feedback | Improve onboarding only if it reduces adoption friction |
| `assessment-ready` | Repository is ready for RAHP or equivalent assessment | Run assessment or prepare assessment issue |
| `maintenance-only` | Repository is mature enough; only hygiene/security/docs fixes justified | Avoid feature expansion |
| `archive-or-supersede` | Repository is no longer the right locus of work | Record lineage and redirect |

## Recommended near-term portfolio process

### Step 1 — Use the evidence overlay as the working queue

Do not treat all repositories equally. Start with the repositories listed in `data/portfolio-evidence-gates.yaml` and expand only when a repository needs an evidence-gate decision.

### Step 2 — Add evidence gates incrementally

Avoid converting the entire portfolio at once. Add or refine records when:

- a repository reaches a stop condition;
- a repository is being moved toward QBF relevance;
- a new release or public-facing claim is planned;
- a repository appears to be plateauing;
- a recurring discussion reveals unclear evidence boundaries.

### Step 3 — Use CPC-001 as the template

When a repository appears mature or stalled, ask whether it has:

- claim boundary;
- evidence boundary;
- negative control or falsification mechanism;
- external evidence gate;
- stop condition;
- next legitimate PR type.

### Step 4 — Separate documentation polish from evidence movement

Documentation work is justified when it improves consumption, onboarding, or claim clarity. It is not justified merely because another document can be written.

### Step 5 — Make future strategy work machine-checkable where possible

Prefer:

- YAML registers;
- schemas;
- testable status files;
- CI checks;
- evidence manifests;
- bounded issue templates;
- reproducibility instructions.

Use narrative documents only where they explain the operating model.

## Next valid portfolio-level work

The next useful portfolio-level increments are:

1. Expand `data/portfolio-evidence-gates.yaml` to 3–5 additional repositories that are currently ambiguous or plateauing.
2. Add a small reporting script that renders the evidence-gate overlay into a public Markdown table.
3. Add a QBF-facing filtered view that lists only institutional assets and their claim boundaries.
4. Review whether `digital-trust-failure-corpus`, `agent-registry-protocol`, and `rahp-toolkit` together form a coherent assurance-method pathway.
5. Identify repositories that should move to `maintenance-only` or `evidence-gated-pause`.

## What not to do next

Do not create broad new workstreams merely to keep repositories active.

Avoid:

- speculative feature expansion without evidence gate movement;
- creating QBF duplicates of personal portfolio records;
- claiming conformance, adoption, or assurance from synthetic evidence;
- treating demos as production proof;
- using CI success as independent validation;
- moving repositories into QBF-facing prominence without claim boundaries.

## Working conclusion

The portfolio strategy is now evidence-gated rather than activity-gated.

The practical operating rule is:

> Continue work when it moves evidence, clarity, adoption or assessment readiness. Pause work when the next valid claim requires evidence the repository cannot produce internally.

This creates a disciplined bridge between the personal/upstream-facing portfolio and the QBF institutional portfolio without duplicating governance or inflating claims.
