import datetime as dt
import importlib.util
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pam", ROOT / "scripts/portfolio_assurance_monitor.py")
pam = importlib.util.module_from_spec(spec); spec.loader.exec_module(pam)

class PortfolioAssuranceMonitorTests(unittest.TestCase):
    def setUp(self):
        self.status = pam.load_yaml(ROOT / "data/repository-status.yaml")
        self.policy = pam.load_yaml(ROOT / "config/portfolio-monitor/policy.yaml")
        self.now = dt.datetime(2026, 7, 29, tzinfo=dt.timezone.utc)

    def test_scope_is_flagship_original_and_excludes_control_plane(self):
        repos = pam.selected_repositories(self.status, self.policy)
        self.assertTrue(repos)
        self.assertNotIn("sankarshanmukhopadhyay", {r["name"] for r in repos})
        self.assertTrue(all(r["tier"] == "flagship" and r["provenance"] == "original" for r in repos))

    def test_findings_never_change_status_automatically(self):
        finding = pam.make_finding("example", "TEST", "info", "2026-07-29T00:00:00Z", "claim", {}, "review")
        self.assertEqual("none", finding["automatic_effect"])
        self.assertRegex(finding["finding_id"], r"^PAM-[A-F0-9]{12}$")

    def test_offline_generation_is_deterministic_and_publishable(self):
        repos = pam.selected_repositories(self.status, self.policy)
        observations = [pam.offline_observation(repo, self.now) for repo in repos]
        findings = [f for repo, obs in zip(repos, observations) for f in pam.evaluate(repo, obs, self.policy, self.now)]
        dashboard = pam.render_report(repos, observations, findings, self.now, publication_role="dashboard")
        evidence = pam.render_report(repos, observations, findings, self.now, publication_role="evidence")
        self.assertIn("Portfolio Assurance Dashboard", dashboard)
        self.assertIn("parent: Portfolio Assurance Monitor", dashboard)
        self.assertNotIn("nav_exclude: true", dashboard)
        self.assertIn("Portfolio Assurance Report — 2026-07-29", evidence)
        self.assertIn("nav_exclude: true", evidence)
        self.assertIn("search_exclude: true", evidence)
        self.assertIn("first-party", dashboard)
        self.assertIn("automatic", dashboard.lower())

    def test_publication_role_is_explicit(self):
        repos = pam.selected_repositories(self.status, self.policy)
        observations = [pam.offline_observation(repo, self.now) for repo in repos]
        with self.assertRaises(ValueError):
            pam.render_report(repos, observations, [], self.now, publication_role="unknown")

if __name__ == "__main__": unittest.main()
