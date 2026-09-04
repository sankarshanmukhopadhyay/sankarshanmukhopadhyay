import unittest
from datetime import datetime, timezone

from scripts.portfolio_delivery_pulse import commit_kind, inject, render_markdown, summarize

NOW = datetime(2026, 9, 4, 2, 30, tzinfo=timezone.utc)


class PortfolioDeliveryPulseTests(unittest.TestCase):
    def test_commit_classification_separates_automation_and_maintenance(self):
        bot = {"commit": {"message": "update generated data"}, "author": {"login": "dependabot[bot]", "type": "Bot"}}
        monitor = {"commit": {"message": "chore(monitor): update DTG portfolio observations"}}
        deps = {"commit": {"message": "chore(deps): bump actions/checkout"}}
        feature = {"commit": {"message": "feat(assurance): add evidence contract"}}

        self.assertEqual("automated", commit_kind(bot))
        self.assertEqual("automated", commit_kind(monitor))
        self.assertEqual("maintenance", commit_kind(deps))
        self.assertEqual("substantive", commit_kind(feature))

    def test_summarize_respects_rolling_windows_and_active_repo_semantics(self):
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
        self.assertEqual(3, seven["commits"])
        self.assertEqual(1, seven["substantive_commits"])
        self.assertEqual(1, seven["automated_commits"])
        self.assertEqual(1, seven["maintenance_commits"])
        self.assertEqual(1, seven["merged_prs"])
        self.assertEqual(1, seven["active_repositories"])

    def test_render_and_inject_expose_interpretation_boundary(self):
        pulse = {
            "windows": {
                "7d": {"commits": 10, "substantive_commits": 5, "maintenance_commits": 2, "automated_commits": 3, "merged_prs": 4, "closed_issues": 6, "releases": 1, "active_repositories": 3},
                "30d": {"commits": 40, "substantive_commits": 20, "maintenance_commits": 8, "automated_commits": 12, "merged_prs": 15, "closed_issues": 22, "releases": 3, "active_repositories": 7},
            }
        }
        block = render_markdown(pulse)
        page = inject("# Portfolio Work Queue\n\n## Work now\n", block)
        self.assertIn("## Portfolio delivery pulse", page)
        self.assertIn("not a project-health", page)
        self.assertLess(page.index("## Portfolio delivery pulse"), page.index("## Work now"))


if __name__ == "__main__":
    unittest.main()
