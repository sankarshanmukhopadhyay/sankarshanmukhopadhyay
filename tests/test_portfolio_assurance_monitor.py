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
        self.now = dt.datetime(2026, 8, 16, 5, 0, tzinfo=dt.timezone.utc)

    def test_scope_is_flagship_original_and_excludes_control_plane(self):
        repos = pam.selected_repositories(self.status, self.policy)
        names = {r["name"] for r in repos}
        self.assertTrue(repos)
        self.assertNotIn("sankarshanmukhopadhyay", names)
        self.assertIn("rahp-toolkit", names)
        self.assertNotIn("dtgwg-rahp-tf", names)
        self.assertTrue(all(r["tier"] == "flagship" and r["provenance"] == "original" for r in repos))

    def test_findings_have_stable_fingerprint_and_no_automatic_effect(self):
        a = pam.make_finding("example", "TEST", "info", "2026-08-16T00:00:00Z", "claim", {}, "review", subject="build.yml")
        b = pam.make_finding("example", "TEST", "info", "2026-08-17T00:00:00Z", "claim", {}, "review", subject="build.yml")
        self.assertEqual("none", a["automatic_effect"])
        self.assertRegex(a["finding_id"], r"^PAM-[A-F0-9]{12}$")
        self.assertRegex(a["finding_fingerprint"], r"^PF-[A-F0-9]{12}$")
        self.assertEqual(a["finding_fingerprint"], b["finding_fingerprint"])
        self.assertNotEqual(a["finding_id"], b["finding_id"])

    def test_latest_success_supersedes_historical_failure(self):
        runs = [
            {"workflow_id": 1, "name": "Validate", "status": "completed", "conclusion": "success", "created_at": "2026-08-16T04:00:00Z"},
            {"workflow_id": 1, "name": "Validate", "status": "completed", "conclusion": "failure", "created_at": "2026-08-15T04:00:00Z"},
        ]
        state = pam.latest_workflow_states(runs, self.now, 7)
        self.assertEqual(0, state["unresolved_failures"])
        self.assertEqual(1, state["workflows_examined"])

    def test_latest_failure_is_unresolved(self):
        runs = [
            {"workflow_id": 1, "name": "Validate", "path": ".github/workflows/validate.yml", "status": "completed", "conclusion": "failure", "created_at": "2026-08-16T04:00:00Z", "html_url": "https://example.invalid/run"},
            {"workflow_id": 1, "name": "Validate", "status": "completed", "conclusion": "success", "created_at": "2026-08-15T04:00:00Z"},
        ]
        state = pam.latest_workflow_states(runs, self.now, 7)
        self.assertEqual(1, state["unresolved_failures"])
        self.assertEqual("failure", state["unresolved"][0]["conclusion"])

    def test_lookback_window_is_enforced(self):
        runs = [{"workflow_id": 1, "name": "Old", "status": "completed", "conclusion": "failure", "created_at": "2026-07-01T04:00:00Z"}]
        state = pam.latest_workflow_states(runs, self.now, 7)
        self.assertEqual(0, state["completed_examined"])
        self.assertEqual(0, state["unresolved_failures"])

    def test_offline_generation_is_publishable(self):
        repos = pam.selected_repositories(self.status, self.policy)
        observations = [pam.offline_observation(repo, self.now) for repo in repos]
        findings = [f for repo, obs in zip(repos, observations) for f in pam.evaluate(repo, obs, self.policy, self.now)]
        dashboard = pam.render_report(repos, observations, findings, self.now, publication_role="dashboard")
        evidence = pam.render_report(repos, observations, findings, self.now, publication_role="evidence")
        self.assertIn("Portfolio Assurance Dashboard", dashboard)
        self.assertIn("parent: Portfolio Assurance Monitor", dashboard)
        self.assertIn("Portfolio Assurance Report — 2026-08-16", evidence)
        self.assertIn("first-party", dashboard)
        self.assertIn("Assessment boundary", dashboard)
        self.assertIn("`not-evaluated`", dashboard)
        self.assertIn("download MD", dashboard)

    def test_publication_role_is_explicit(self):
        repos = pam.selected_repositories(self.status, self.policy)
        observations = [pam.offline_observation(repo, self.now) for repo in repos]
        with self.assertRaises(ValueError):
            pam.render_report(repos, observations, [], self.now, publication_role="unknown")

    def test_required_status_evidence_fails_closed_when_unobserved(self):
        repo = next(r for r in pam.selected_repositories(self.status, self.policy) if r.get("status_source", {}).get("required"))
        observation = pam.offline_observation(repo, self.now)
        observation["evidence"].pop("status_declaration", None)
        findings = pam.evaluate(repo, observation, self.policy, self.now)
        self.assertIn("STATUS_DECLARATION_UNOBSERVED", {f["rule_id"] for f in findings})

    def test_unavailable_workflow_evidence_is_a_finding(self):
        repo = pam.selected_repositories(self.status, self.policy)[0]
        observation = pam.offline_observation(repo, self.now)
        observation["evidence"]["workflow_runs"] = {"available": False, "error": "denied"}
        findings = pam.evaluate(repo, observation, self.policy, self.now)
        workflow = next(f for f in findings if f["rule_id"] == "WORKFLOW_EVIDENCE_UNAVAILABLE")
        self.assertEqual(workflow["dimension"], "operational")
        self.assertTrue(workflow["remediation"]["acceptance_criteria"])

    def test_zero_findings_do_not_claim_complete_assurance(self):
        repos = pam.selected_repositories(self.status, self.policy)
        observations = [pam.offline_observation(repo, self.now) for repo in repos]
        dashboard = pam.render_report(repos, observations, [], self.now, publication_role="dashboard")
        self.assertIn("not-evaluated", dashboard)
        self.assertIn("does **not** mean", dashboard)

if __name__ == "__main__": unittest.main()
