# Portfolio calibration pass — 2026-10

Status: initial portfolio-level calibration pass  
Basis: `data/repository-status.yaml`, `data/portfolio-evidence-gates.yaml`, and the strategy context in `docs/portfolio-strategy-context.md`

## Purpose

This calibration pass applies the evidence-gated maturity model to a bounded repository set.

It is not a general backlog exercise. It answers a narrower portfolio-governance question:

> For each repository, what evidence would justify more work, and where should work pause until external evidence exists?

## Calibration principle

The portfolio should not treat activity volume, issue count, documentation expansion, or line count as evidence of maturity.

The operative rule is:

> Continue work when it improves adoption clarity, evidence quality, assessment readiness, implementation binding, independent reproducibility, release evidence, usability validation, or documentation usability. Pause work when the next valid claim requires evidence the repository cannot produce internally.

## Calibrated repository set

| Repository | View | Role | Current gate state | Stop condition |
|---|---|---|---|---|
| `digital-trust-failure-corpus` | QBF institutional | Failure corpus and assurance workbench | Waiting external evidence | Pause until external evidence |
| `rahp-toolkit` | Personal/upstream-facing | Assessment toolkit and evidence controller | Ready | Pause until external evidence |
| `agent-registry-protocol` | QBF institutional | Agent authority control protocol | Ready | Pause until implementation target |
| `tswg-trust-registry-protocol` | Personal/upstream-facing | Downstream analysis and upstream convergence | Waiting external evidence | Pause until upstream decision |
| `trust-protocol-interop-lab` | Shared | Experimental interop and evidence lab | Ready | Pause until external evidence |
| `open-national-digital-trust-framework` | QBF institutional | Jurisdiction-neutral trust framework | Waiting external evidence | Pause until external evidence |
| `governance-authority-assurance-metamodel` | QBF institutional | Governance authority metamodel | Ready | Pause until external evidence |
| `trust-systems-meta-model` | QBF institutional | Canonical semantic model | Ready | Pause until external evidence |
| `trust-infrastructure-schemas` | QBF institutional | Portable schema contracts | Ready | Continue internal hardening |
| `trust-graph-artifacts` | QBF institutional | Executable governance incubator | Ready | Continue internal hardening |
| `digital-governance-paper-notes` | Personal/upstream-facing | Research review archive | Ready | Maintenance only |
| `kiranaos` | Personal/upstream-facing | Applied product demonstrator | Waiting external evidence | Pause until external evidence |

## Findings

### 1. Several repositories are mature enough to stop internal expansion

The following repositories should not accumulate more internal scaffolding unless an external evidence event appears:

- `digital-trust-failure-corpus`
- `open-national-digital-trust-framework`
- `tswg-trust-registry-protocol`
- `kiranaos`

For these repositories, the next meaningful step depends on one or more of:

- external implementation target;
- independent reviewer or reproducer;
- adoption or deployment evidence;
- upstream decision;
- user or operator feedback.

### 2. QBF institutional assets should be judged by claim boundary, not activity

For QBF-facing repositories, the primary maturity question is:

> What may QBF safely claim from this evidence state?

The calibrated QBF assets are not all at the same stage.

| Repository | Safe current posture |
|---|---|
| `digital-trust-failure-corpus` | Executable synthetic evidence and evidence-gated assurance cases |
| `agent-registry-protocol` | Candidate protocol semantics; needs implementation/adoption evidence |
| `open-national-digital-trust-framework` | Stable public framework; needs adoption evidence for stronger claims |
| `governance-authority-assurance-metamodel` | Candidate authority semantics; needs external review or implementation binding |
| `trust-systems-meta-model` | Portfolio semantic backbone; needs dependent alignment evidence |
| `trust-infrastructure-schemas` | Machine-verifiable contract layer; can continue internal validation and examples |
| `trust-graph-artifacts` | Incubator; should promote only reusable tested patterns |

### 3. `trust-infrastructure-schemas` and `trust-graph-artifacts` still justify internal work

Most repositories should pause when external evidence is missing. Two repositories still justify internal hardening:

- `trust-infrastructure-schemas`
- `trust-graph-artifacts`

Reason: internal work can still materially improve machine-verifiability, examples, validation coverage and reusable pattern quality.

This is different from adding more narrative. Internal hardening remains valid only when it creates:

- schemas;
- validation artifacts;
- runnable examples;
- reusable governance patterns;
- negative tests;
- promotion candidates for governed repositories.

### 4. `digital-governance-paper-notes` should remain maintenance-only

The research archive is useful, but it should not become a permanent source of new implementation tranches.

The valid motion is:

```text
paper note → synthesis need → issue or artifact in another repository
```

Not:

```text
paper note → endless local expansion inside the notes archive
```

### 5. `kiranaos` needs user feedback, not more speculative completion

The repo can remain an applied demonstrator, but further work should be tied to:

- deployment candidate;
- user validation;
- issue-template feedback;
- concrete operator need.

Internal MVP polishing is no longer the strongest portfolio-level use of effort unless it improves adoption clarity or reduces user friction.

## Recommended near-term portfolio moves

### A. Keep CPC-001 paused until evidence changes

`digital-trust-failure-corpus` should not continue CPC-001 internally until one of these exists:

- non-synthetic target;
- independent reproduction;
- actual RAHP assessment.

### B. Use `trust-infrastructure-schemas` for the next internal hardening tranche

This is the best candidate for more internal work because it can still produce machine-verifiable value without external dependency.

Potential next tranche:

```text
schema/examples: add evidence-gate record examples and validation fixtures
```

### C. Use `trust-graph-artifacts` only for promoted reusable patterns

Do not add general writing. Add only artifacts that can later be promoted into:

- schemas;
- test fixtures;
- assurance cases;
- implementation guides;
- reusable governance controls.

### D. Treat ARPA as implementation-gated

`agent-registry-protocol` should continue only where work improves:

- implementation binding;
- interop evidence;
- adoption clarity;
- release evidence.

Further semantic elaboration is useful only if it helps an implementation or assurance case.

### E. Treat ONDTF as adoption-gated

`open-national-digital-trust-framework` should avoid more internal framework expansion unless tied to:

- adoption story;
- jurisdictional review;
- implementation mapping;
- deployment or public institutional feedback.

## Portfolio triage states

Future reviews should classify repositories into one of these states:

| State | Meaning | Next action |
|---|---|---|
| Continue internal hardening | Internal work can still produce verifiable value | Create bounded PR tranche |
| Ready but evidence-gated | Internal foundation exists; next claim requires external evidence | Pause and record gate |
| Upstream-gated | Progress depends on upstream maintainers or standards body | Track upstream; avoid duplicate local expansion |
| Adoption-gated | Stronger claims require adopter, user or deployment feedback | Seek adopter/reviewer; avoid speculative work |
| Maintenance-only | Repository is useful but should not generate new work | Keep docs, links and CI healthy |
| Incubator | Work may proceed only if output can be promoted into governed artifacts | Create small experimental tranche with promotion criteria |

## Anti-patterns to avoid

- Treating a passing CI run as independent assurance.
- Treating documentation completeness as adoption evidence.
- Treating repository activity as maturity.
- Treating downstream analysis as upstream acceptance.
- Treating synthetic fixtures as product safety.
- Treating research notes as institutional position.
- Treating framework stability as jurisdictional adoption.
- Starting new tranches when the next required input is external.

## Resulting operating recommendation

The portfolio is not stalled. It is entering a phase where progress should be increasingly evidence-selective.

The next best work is not to generate many new issues. It is to select only those tranches that move one of these:

- evidence boundary;
- claim boundary;
- adoption pathway;
- assessment readiness;
- implementation binding;
- release/audit posture;
- machine-verifiability.

Everything else should be treated as maintenance or paused until a concrete evidence event appears.
