# Portfolio Drift Review

This checklist is used when a repository introduces a new schema, profile, control family, conformance output, runtime artifact, standards binding, or assurance declaration.

The purpose is to make portfolio maintenance reviewable. A relationship is operational only when there is artifact-level evidence such as a schema, example, conformance output, workflow, compatibility matrix, or evidence bundle. Shared vocabulary alone is not enough.

## Review inputs

| Input | Required? | Notes |
|---|---:|---|
| Repository name | Yes | Source repository that changed |
| Release or commit reference | Yes | Tag, branch, or commit under review |
| Changed artifact type | Yes | Schema, profile, control, fixture, evidence output, binding, documentation |
| Affected downstream repositories | Yes | Use `data/portfolio-relationships.yaml` as the starting point |
| Validation evidence | Yes | Link to tests, schema validation, link checks, or review notes |

## Drift classification

| Classification | Meaning | Required action |
|---|---|---|
| No portfolio drift | Change is local and does not alter cross-repo expectations | Record no-impact decision |
| Documentation drift | Cross-repo explanation, link, or onboarding path needs refresh | Update README or docs |
| Artifact drift | Schema, profile, example, evidence output, or fixture expectations changed | Update dependent examples/tests/profiles |
| Assurance drift | Assurance level, control expectation, verdict, or decision evidence changed | Update assurance mappings and validation notes |
| Standards drift | External standard or binding reference changed | Update crosswalks, compatibility notes, and issue references |

## Review questions

1. What repository changed?
2. What artifact or governance function changed?
3. Which relationship in `data/portfolio-relationships.yaml` is affected?
4. Is the relationship thematic or operational?
5. What downstream repository should be reviewed?
6. What evidence proves the review was completed?
7. Is a release note entry required?

## Minimum evidence

A completed drift review should produce at least one of the following:

- updated compatibility matrix;
- updated schema or fixture;
- updated example artifact;
- updated assurance/control mapping;
- updated README or onboarding note;
- explicit no-impact review note;
- issue reference for deferred downstream work.

## Suggested review record

```yaml
review_id: portfolio-drift-YYYYMMDD-NN
source_repo: example-repo
source_release: v0.0.0
change_type: schema_change
relationship_ids_reviewed:
  - example-source-to-example-target
drift_classification: artifact_drift
downstream_review_targets:
  - example-target-repo
evidence:
  - path: docs/compatibility-matrix.md
  - path: examples/example.json
result: downstream_update_required
follow_up_issue: null
```
