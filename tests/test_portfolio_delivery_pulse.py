from datetime import datetime, timezone

from scripts.portfolio_delivery_pulse import commit_kind, inject, render_markdown, summarize

NOW = datetime(2026, 9, 4, 2, 30, tzinfo=timezone.utc)


def test_commit_classification_separates_automation_and_maintenance():
    bot = {"commit": {"message": "update generated data"}, "author": {"login": "dependabot[bot]", "type": "Bot"}}
    monitor = {"commit": {"message": "chore(monitor): update DTG portfolio observations"}}
    deps = {"commit": {"message": "chore(deps): bump actions/checkout"}}
    feature = {"commit": {"message": "feat(assurance): add evidence contract"}}

    assert commit_kind(bot) == "automated"
    assert commit_kind(monitor) == "automated"
    assert commit_kind(deps) == "maintenance"
    assert commit_kind(feature) == "substantive"


def test_summarize_respects_rolling_windows_and_active_repo_semantics():
    evidence = {
        "alpha": {
            "commits": [
                {"timestamp": "2026-09-03T10:00:00Z", "kind": "substantive"},
                {"timestamp": "2026-09-03T11:00:00Z", "kind": "automated"},
                {"timestamp": "2026-08-20T10:00:00Z", "kind": "substantive"},
            ],
            "merged_prs": [{"timestamp": "2026-09-02T10:00:00Z"}],
            "closed_issues": [],
            "releases": [],
        },
        "beta": {
            "commits": [{"timestamp": "2026-09-03T10:00:00Z", "kind": "maintenance"}],
            "merged_prs": [],
            "closed_issues": [],
            "releases": [],
        },
    }
    seven = summarize(evidence, NOW, 7)
    assert seven["commits"] == 3
    assert seven["substantive_commits"] == 1
    assert seven["automated_commits"] == 1
    assert seven["maintenance_commits"] == 1
    assert seven["merged_prs"] == 1
    assert seven["active_repositories"] == 1


def test_render_and_inject_expose_interpretation_boundary():
    pulse = {
        "windows": {
            "7d": {"commits": 10, "substantive_commits": 5, "maintenance_commits": 2, "automated_commits": 3, "merged_prs": 4, "closed_issues": 6, "releases": 1, "active_repositories": 3},
            "30d": {"commits": 40, "substantive_commits": 20, "maintenance_commits": 8, "automated_commits": 12, "merged_prs": 15, "closed_issues": 22, "releases": 3, "active_repositories": 7},
        }
    }
    block = render_markdown(pulse)
    page = inject("# Portfolio Work Queue\n\n## Work now\n", block)
    assert "## Portfolio delivery pulse" in page
    assert "not a project-health" in page
    assert page.index("## Portfolio delivery pulse") < page.index("## Work now")
