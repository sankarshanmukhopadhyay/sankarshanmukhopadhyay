# Portfolio evidence gates

This page explains the evidence-gated maturity overlay in `data/portfolio-evidence-gates.yaml`.

The overlay refines the existing portfolio maturity register. It does not replace `data/repository-status.yaml`, which remains the canonical control surface for portfolio membership, tier, maturity, lifecycle, authority, provenance and review dates.

## Purpose

The existing register answers:

- is the repository part of the curated portfolio;
- what role does it play;
- what maturity and lifecycle state is declared;
- what authority scope does it claim;
- when must it next be reviewed.

The evidence-gate overlay answers a different question:

> What kind of evidence would justify more work?

This distinction matters because some repositories do not need another internal documentation or implementation tranche. They need an external evidence event, such as an implementation target, independent reproduction, upstream decision, assessment result, release evidence or adoption feedback.

## Portfolio views

The overlay uses one shared maturity logic with two portfolio views.

| View | Meaning |
|---|---|
| `personal-upstream-facing` | Personal, experimental, upstream-facing or contribution-oriented work. |
| `qbf-institutional` | Institutional, assurance, protocol, corpus or client-facing QBF work. |
| `shared` | Work that can support both personal upstream-facing experiments and QBF assurance propositions. |

The views are not separate governance systems. They are filtered interpretations of the same evidence-gate model.

## Evidence-gate fields

Each calibrated repository records:

| Field | Meaning |
|---|---|
| `repo_role` | What role the repository plays in the portfolio. |
| `current_maturity_boundary` | What the repository can currently support or prove. |
| `claim_boundary` | What must not be claimed from the current evidence state. |
| `next_evidence_gate` | The evidence event that would justify the next tranche. |
| `gate_state` | Whether the gate is ready, blocked, complete, or awaiting external evidence. |
| `stop_condition` | When work should pause instead of continuing internally. |
| `external_dependency` | What external input, target, reviewer, adopter, or upstream decision is required. |
| `qbf_relevance` | Whether and how the repository matters to QBF's institutional surface. |

## Operating rule

A new tranche should be justified only if it improves at least one of:

- adoption clarity;
- evidence quality;
- assessment readiness;
- implementation binding;
- independent reproducibility;
- documentation usability;
- release or audit evidence.

If the next valid improvement requires a target, reviewer, upstream decision or adopter, the repository should pause at its maturity boundary rather than accumulate internal scaffolding.

## Example: CPC-001 in DTFC

The CPC-001 work in `qbf-consulting/digital-trust-failure-corpus` is the reference pattern.

It now has:

- baseline case framing;
- protection contracts;
- revocation semantics;
- executable synthetic fixture;
- defective target;
- CI-backed synthetic evidence package;
- independent reproduction template;
- RAHP assessment bridge;
- non-synthetic target admission gate;
- candidate target selection register.

Its current evidence boundary remains only:

- `executed-synthetic-target`;
- `ci-executed-synthetic-target`.

The next valid tranche requires one of:

- non-synthetic implementation target;
- independent reproduction;
- actual RAHP assessment result.

That is why CPC-001 is treated as internally ready but externally evidence-gated.

## Relationship to QBF

The QBF view should not duplicate the personal portfolio register. It should derive from the same evidence-gate logic and use a narrower public claim boundary.

For QBF-facing repositories, the key question is not merely whether the repository is active. The question is:

> What evidence can QBF safely rely on or present without overstating adoption, implementation assurance, consumer safety or ecosystem conformance?

## Maintenance

When updating the overlay:

1. Keep `data/repository-status.yaml` as the canonical membership and maturity register.
2. Add or revise evidence gates only when the repository has a clear next evidence dependency.
3. Do not convert fixtures, CI, documentation, or issue closure into independent reproduction or production assurance.
4. Prefer explicit pause conditions over low-value internal work.
5. Use pull requests so the claim boundary and evidence boundary remain reviewable.
