# Portfolio governance path migration

The v0.2.0 profile integration establishes `portfolio/` as the canonical human-readable governance control surface.

| Previous path | Canonical path | Compatibility |
|---|---|---|
| `docs/portfolio-architecture.md` | `portfolio/architecture.md` | Previous path retained as pointer |
| `docs/portfolio-drift-review.md` | `portfolio/drift-review.md` | Previous path retained as pointer |
| `docs/release-impact-template.md` | `portfolio/release-impact-template.md` | Previous path retained as pointer |
| `data/portfolio-relationships.yaml` | `data/portfolio-relationships.yaml` | Unchanged and canonical |

New release-specific material belongs under:

```text
portfolio/release-impact/
portfolio/releases/<version>/
```

Do not copy canonical governance documents back into `docs/`. The compatibility files are intentionally minimal so there is only one maintained source for each document.
