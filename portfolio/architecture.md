# Portfolio Architecture

## Operating model

The portfolio is a federation of repositories with separate release authority and explicit dependency relationships.

```text
Canonical concepts (TSMM)
        ↓
Portable contracts (TIS)
        ↓
Governance patterns and failure tests (TGA)
        ↓
Domain profiles, protocols, implementations, and assurance systems
        ↓
Conformance evidence and adoption outcomes
```

## Authority boundaries

- **TSMM** owns canonical cross-portfolio semantic concepts.
- **TIS** owns reusable machine-readable schema contracts.
- **TGA** incubates governance patterns, implementation guidance, and negative assurance tests.
- Domain repositories own their protocol, profile, implementation, or assurance scope.
- This profile repository owns portfolio classification and relationship metadata only.

## Enforcement

The relationship registry must declare each authority claim. The validator rejects duplicate canonical authority claims and unknown dependencies.

## Revocation

Authority can be superseded only through an explicit registry change identifying the new owner and a release-impact record describing migration and compatibility consequences.
