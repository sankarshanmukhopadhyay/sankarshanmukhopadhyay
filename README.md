# Sankarshan Mukhopadhyay

I build **testable trust infrastructure**: governance patterns, assurance toolchains, and machine-verifiable artifacts for institutions deploying verifiable data, trust registries, and agent-mediated systems.

My work is built around a simple premise:

**If a governance claim cannot be implemented, tested, audited, and contested in operation, it is not yet infrastructure.**

That premise runs across this portfolio. The objective is not to produce more policy language. The objective is to turn governance, trust, and assurance into operational systems that can survive real deployment conditions.

## What this portfolio is trying to prove

This work is organized around four propositions:

1. **Trust systems should be testable, not ceremonial.**  
   A trust registry, directory, or verifier does not become trustworthy because it cites a standard. It becomes trustworthy when its behavior can be checked, its claims can be challenged, and its evidence can travel.

2. **Governance should be machine-operable, not just documented.**  
   Rules that cannot be bound to artifacts, controls, decision points, and evidence flows are too weak for high-stakes infrastructure.

3. **Agent participation requires bounded authority and verifiable assurance.**  
   As software agents begin to act across institutional and economic systems, identity alone is not enough. Names, mandates, scopes, and verification expectations need to be operationalized.

4. **Interoperability needs evidence, profiles, and repeatable control surfaces.**  
   Cross-ecosystem trust cannot depend on interpretation alone. It needs profiles, conformance pathways, evidence contracts, and deployable assurance mechanisms.

## Ecosystem map

```text
Trust Registry Infrastructure
├── TRQP Assurance Hub
├── TRQP Conformance Suite
└── TRQP-TSPP

Assurance and Conformance
└── DTG Conformance & Assurance (DCAS)

Operational AI Governance
├── DPI AI Governance Artifacts
└── DPI AI Governance Lab

Agent Identity and Delegated-Action Assurance
├── Agent Name Assurance Baseline
├── Trust Infrastructure Schema
└── ERC-8004 CSP

Conceptual Foundations
└── Trust Systems Meta Model (TSMM)
```

## Portfolio map

### 1. Trust registry infrastructure

Implementation and assurance pathways for trust registries and related trust distribution systems.

- [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub)
- [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite)
- [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP)

These repositories collectively explore how trust registry deployments can become testable, auditable, and portable across ecosystems rather than remaining largely declarative. Together they provide a **non-monorepo adoption path** for TRQP ecosystems that want assurance without collapsing implementation diversity.

### 2. Assurance and conformance systems

Portable conformance methods, assurance overlays, evidence bundles, and verifier-oriented evaluation workflows.

- [DTG Conformance & Assurance (DCAS)](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance)

This layer focuses on the repeatable evaluation of trust claims. The aim is to move from informal ecosystem confidence to structured, reviewable, and reusable assurance outputs.

### 3. Operational AI governance

Governance artifacts and implementation scaffolding for AI systems operating in institutional and public-interest settings.

- [DPI AI Governance Artifacts](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts)
- [DPI AI Governance Lab](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab)

The emphasis here is practical: reusable controls, review structures, policy artifacts, and governance templates that can be deployed rather than merely discussed.

### 4. Agent identity and delegated-action assurance

Security baselines and machine-readable trust structures for software agents participating in trust ecosystems.

- [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline)
- [Trust Infrastructure Schema](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas)

This cluster focuses on a problem that is becoming harder, not easier: how relying parties should identify, classify, and trust software agents that may act with delegated authority across systems. The central question is not just whether an agent exists, but whether it is operating under intelligible names, bounded mandates, and reviewable assurance expectations.

The **Trust Infrastructure Schema** repo provides a machine-readable schema layer for expressing trust actors, claims, bindings, and structural relationships that recur across registry, assurance, and agent participation workflows.

This lane is complemented by cross-portfolio assurance work, especially [DTG Conformance & Assurance (DCAS)](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance), which provides evaluation and verifier-oriented assessment paths for operational trust claims.

Additional ecosystem-specific bindings and profiles, including [ERC-8004 CSP](https://github.com/sankarshanmukhopadhyay/ERC-8004-CSP), extend parts of this work into substrate-specific agent registration and verification environments. ERC-8004 CSP is the Ethereum-facing branch of this broader agent assurance logic rather than the primary anchor of the portfolio.

### 5. Conceptual foundations and abstract modeling

Shared vocabulary and abstract reference modeling across trust systems.

- [Trust Systems Meta Model (TSMM)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model)

TSMM captures recurring structural patterns across the portfolio: entities and roles, bounded authority, artifacts and claims, policy-governed decisions, evidence, verification, and downstream effects. It is useful for readers who want to understand the deeper architectural assumptions connecting the operational repositories.

## Start here

Different readers usually enter this work through different operational problems.

### If you care about trust registries and verifiable data infrastructure

Start with:

- [TRQP Assurance Hub](https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub)
- [TRQP Conformance Suite](https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite)
- [TRQP-TSPP](https://github.com/sankarshanmukhopadhyay/TRQP-TSPP)

Together these form a practical **non-monorepo adoption path** for making trust registry behavior testable and assurance claims exportable.

### If you care about assurance and conformance evaluation

Start with:

- [DTG Conformance & Assurance (DCAS)](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance)

This is the clearest entry point into the portfolio’s work on verifier-oriented assessment, portable assurance outputs, and repeatable trust evaluation methods.

### If you care about AI governance in deployable form

Start with:

- [DPI AI Governance Artifacts](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts)
- [DPI AI Governance Lab](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab)

These projects translate governance concepts into control structures, review mechanisms, and reusable artifacts.

### If you care about agent trust, naming, and delegated participation

Start with:

- [Agent Name Assurance Baseline](https://github.com/sankarshanmukhopadhyay/agent-name-assurance-baseline)
- [Trust Infrastructure Schema](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schema)

This is the most direct path into the portfolio’s work on agent identity, naming discipline, machine-readable trust structures, and assurance expectations for delegated action.

### If you want the abstract model behind the portfolio

Start with:

- [Trust Systems Meta Model (TSMM)](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model)

TSMM is not a prerequisite for using the operational repositories. It is the place to go if you want the shared language and model logic behind them.

## Standards and ecosystem orientation

I contribute to and draw from work across Trust Over IP, LF Decentralized Trust, UN/CEFACT, and adjacent standards and implementation ecosystems. The portfolio is intended to help convert standards-aligned trust claims into artifacts, controls, and assurance paths that can survive deployment.

## Writing and public work

### The Trust Graph

Essays on digital trust infrastructure, governance-by-design, delegated authority, and verifiable data economies.

- [Substack](https://thetrustgraph.substack.com)

### Elsewhere

- [LinkedIn](https://www.linkedin.com/in/sankarshan)
- [About](https://about.me/sankarshan.mukhopadhyay/)

## Collaboration

This portfolio is most useful for people who are:

- implementing trust registries or verifiable data infrastructure
- building assurance pipelines and evidence workflows
- operationalizing AI governance in institutional settings
- designing trust, identity, and control surfaces for software agents

If that is your problem space, open a GitHub issue with:

1. your use case in one paragraph  
2. your constraints, including policy, latency, budget, and ecosystem  
3. a concrete definition of done  

Small, testable increments beat large rewrites.  
Operational clarity beats ceremonial confidence.
