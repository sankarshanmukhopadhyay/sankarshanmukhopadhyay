# Contributing

Contributions should improve portfolio legibility, machine-verifiable governance, adoption guidance, or cross-repository interoperability.

## Before opening a change

- Identify the repository or portfolio relationship affected.
- State whether the change alters authority, lifecycle, dependency, adoption, or presentation.
- Prefer machine-readable updates over narrative-only assertions.
- Do not assign release authority to this profile repository.

## Validation

Before submitting a substantive change, run the same core checks exercised by CI:

```bash
python scripts/validate_portfolio.py
python scripts/portfolio_assurance_monitor_v3.py --offline --check
python -m unittest discover -s tests -p 'test_*.py'
python scripts/check_internal_links.py
python scripts/check_site_navigation.py
```

For changes affecting the published site, also run:

```bash
bundle exec jekyll build --trace
```

A contribution is ready when the relevant checks pass, links introduced by the change are valid, and any affected review or impact record is updated.

## Pull request evidence

Include:

- the governance claim being changed;
- the files that enforce it;
- the validation performed;
- any unresolved limitation or follow-up.
