---
layout: default
title: Portfolio Work Queue Reconciliation Notes
parent: Portfolio Work Queue
nav_order: 3
---

# Portfolio Work Queue reconciliation notes

The queue is useful only when `ready` means the observed issue or pull request is actually executable from the evidence available at generation time.

The reconciliation boundary therefore treats the following as falsifiers of `ready`:

- an issue body explicitly says implementation must wait for upstream/external ratification, decision, evidence, or independent implementation, even when no blocker label has been applied;
- a documentation-only roadmap pull request is presented as executable implementation work rather than as a planning/maintenance artifact;
- consequential authority, governance, security, normative or release decisions are presented as quick execution work.

These rules intentionally remain conservative. They do not infer completion from prose or close repository-local work automatically. Member repositories remain authoritative for actual completion and release state.
