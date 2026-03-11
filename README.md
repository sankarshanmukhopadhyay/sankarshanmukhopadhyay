# Sankarshan Mukhopadhyay

I build **digital trust infrastructure**: governance patterns, assurance
tooling, and interoperable artifacts for institutions deploying
verifiable data systems.

The focus is practical.

If a governance idea cannot be implemented, tested, and audited, it is
not infrastructure.

My work sits at the intersection of three layers:

-   **Verifiable identity and data systems**\
    credentials, registries, trust lists, and interoperable trust
    frameworks

-   **Assurance and conformance infrastructure**\
    testing, evidence bundles, compatibility matrices, and audit
    artifacts

-   **Operational AI governance**\
    risk-tiered workflows, runtime controls, and deployable governance
    tooling

I contribute to work across **Trust Over IP (ToIP)**, **LF Decentralized Trust**,
**UN/CEFACT** and adjacent standards ecosystems, with an emphasis on artifacts
that real institutions can ship.

---

# Ecosystem Map

```
                    Digital Trust Infrastructure
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
  Trust Registries       Assurance Systems      Governance Artifacts
        │                      │                      │
        │                      │                      │
   TRQP-TSPP           TRQP Conformance Suite    DPI AI Governance Lab
        │                      │                      │
        │                      │                      │
 TRQP Assurance Hub      Evidence Bundles       Governance Templates
        │
        │
 Agent Identity Layer
        │
 Agent Name Assurance Baseline
        │
 ERC-8004 CSP

                               │
               ────────────────┴───────────────
               Trust Systems Meta Model (TSMM)
               shared vocabulary · abstract reference model
               ────────────────────────────────
```

These repositories collectively explore how **trust infrastructure can
become testable, auditable, and interoperable across ecosystems**.

---

# Start Here

If you are new to this work, the easiest entry points are:

### Trust Registries and TRQP

Start with the implementation and assurance pathway for trust registry
deployments.

-   TRQP Assurance Hub\
    <https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub>

-   TRQP Conformance Suite\
    <https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite>

-   TRQP-TSPP\
    <https://github.com/sankarshanmukhopadhyay/TRQP-TSPP>

Together these form a **non-monorepo adoption path for TRQP ecosystems**.

---

### Digital Public Infrastructure and AI Governance

Operationalizing governance for AI systems interacting with public
infrastructure.

-   DPI AI Governance Artifacts\
    <https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts>

-   DPI AI Governance Lab\
    <https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab>

These projects focus on turning governance concepts into **deployable
review frameworks and reusable artifacts**.

---

### Agent Identity and Name Assurance

Security profiles and baselines for software agents participating in
trust ecosystems.

-   Agent Name Assurance Baseline\
    <https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline>

-   ERC-8004 CSP\
    <https://github.com/sankarshanmukhopadhyay/ERC-8004-CSP>

ERC-8004 is an emerging Ethereum-ecosystem standard for agent identity
registration and verification. The CSP (Consumer Security Profile) in this
repository defines how relying parties should interpret and handle
signals from ERC-8004-conformant agents within a broader trust
ecosystem — connecting on-chain agent registration to the assurance and
governance expectations defined in ANAB and the TRQP cluster.

This work focuses on reducing ecosystem risk and improving verification
cycles for agent identities.

---

### Conformance Assurance for Decentralized Trust Graphs

Portable conformance profiles, risk assessment, and assurance artefacts
for Decentralized Trust Graph ecosystems.

-   DTG Conformance & Assurance (DCAS)\
    <https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance>

DCAS provides the verifier workflow and repeatable evaluation method
used to assess conformance claims across this portfolio, including those
produced by the Agent Name Assurance Baseline.

---

### Conceptual Foundations

The three operational clusters above share recurring structural
patterns: entities and roles, bounded authority, artifacts and claims,
policy-governed trust decisions, evidence, and effects. TSMM extracts
those patterns into a portable abstract reference model that can be
studied and applied across implementations without requiring a specific
protocol or profile.

-   Trust Systems Meta Model (TSMM)\
    <https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model>

**Status: draft reference model, actively developed.** Useful for
understanding the shared vocabulary and structural assumptions across
this portfolio. Not a prerequisite for adopting any of the operational
repos — but rewarding for those who want to understand why the portfolio
is structured the way it is.

---

# Writing and Public Work

**The Trust Graph**\
Essays on digital trust infrastructure, governance-by-design, and
verifiable data economies. Published on Substack.

<https://substack.com/@thetrustgraph>

LinkedIn\
<http://linkedin.com/in/sankarshan>

About\
<https://about.me/sankarshan.mukhopadhyay/>

---

# Collaboration

If you are:

-   implementing trust registries or verifiable data infrastructure
-   building assurance pipelines for verifiable data ecosystems
-   operationalizing AI governance in public systems

Open a GitHub issue with:

1.  Your use case in one paragraph
2.  Your constraints (policy, latency, budget, ecosystem)
3.  A concrete definition of done

Small, testable increments beat big rewrites.\
High signal beats high ceremony.
