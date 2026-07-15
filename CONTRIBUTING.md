# Contributing

Contributions should improve portfolio legibility, machine-verifiable governance, adoption guidance, or cross-repository interoperability.

## Before opening a change

- Identify the repository or portfolio relationship affected.
- State whether the change alters authority, lifecycle, dependency, adoption, or presentation.
- Prefer machine-readable updates over narrative-only assertions.
- Do not assign release authority to this profile repository.

## Validation

Run:

```bash
python scripts/validate_portfolio.py
```

A contribution is ready when the validator passes, links introduced by the change are valid, and any affected review or impact record is updated.

## Pull request evidence

Include:

- the governance claim being changed;
- the files that enforce it;
- the validation performed;
- any unresolved limitation or follow-up.
