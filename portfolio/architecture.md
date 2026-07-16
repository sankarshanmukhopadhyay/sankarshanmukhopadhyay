# Portfolio Architecture

## Operating model

The portfolio is a federation of independently governed repositories and explicitly identified upstream forks. Portfolio membership does not transfer normative authority.

```text
                         GOVERNANCE AND AUTHORITY
                Governance, Authority and Assurance Metamodel
                                      │
                    normative rules, profiles, and controls
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
 SEMANTIC FOUNDATION          MACHINE CONTRACTS             APPLIED PATTERNS
 Trust Systems Meta Model     Trust Infrastructure Schemas  Trust Graph Artifacts
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      │
                         DOMAIN AND PROTOCOL SYSTEMS
                Agent Registry Protocol · TRQP · ZKP · AGTP
                                      │
                     tests, implementations, and validators
                                      │
                       CONFORMANCE AND ASSURANCE
          suites · reference verifiers · evidence · review conclusions
```

## Authority boundaries

- **GAAM** owns its normative governance, authority, delegation, revocation, assurance, accountability, appeal, and remedy model.
- **TSMM** owns canonical cross-portfolio semantic concepts within its declared scope.
- **TIS** owns reusable machine-readable schema contracts.
- **Trust Graph Artifacts** incubates applied governance patterns and negative-assurance tests.
- **Agent Registry Protocol** owns its protocol-specific records, APIs, profiles, and conformance model.
- Domain repositories own their protocol, profile, implementation, or assurance scope.
- This profile repository owns portfolio classification, provenance, and relationship metadata only.
- Upstream projects retain all governance and release authority for forked repositories.

## Relationship classes

Relationships are declared as normative dependency, profile adoption, informative alignment, support, constraint, evidence production, reference implementation, incubation, or `fork-of`. A relationship has no authority effect beyond its explicit constraint.

## Fork provenance

A fork must declare its canonical upstream repository, use `portfolio_governance: fork-only`, and carry a matching `fork-of` relationship. Fork-local work is evidence about the fork only unless accepted upstream.

## Enforcement and revocation

The validator rejects duplicate authority claims, unknown dependencies, ungoverned relationship types, fork entries without upstream provenance, and fork relationships that do not match the status registry. Authority can be superseded only through an explicit registry change and a release-impact record describing migration and compatibility consequences.
