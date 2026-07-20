---
title: TSMM and TIS Candidate Alignment
parent: Portfolio Status
nav_order: 2
---
# TSMM and TIS Candidate alignment

The July 2026 coordinated update establishes member-owned Candidate status contracts for TSMM and TIS and reconciles the portfolio registry with those declarations.

```mermaid
flowchart LR
  P[Portfolio governance] -->|classifies and presents| TSMM[TSMM Candidate]
  P -->|classifies and presents| TIS[TIS Candidate]
  TSMM -->|canonical semantic authority| TIS
  TIS -->|portable contracts| I[Implementations]
  I --> E[Conformance evidence]
  E --> A[Assurance conclusions]
  A -. accountable feedback .-> TSMM
  A -. accountable feedback .-> TIS
```

The portfolio repository owns portfolio disposition, tier, cross-repository presentation, and review scheduling. TSMM and TIS retain their own maturity, lifecycle, operational, specification, and normative-scope declarations.
