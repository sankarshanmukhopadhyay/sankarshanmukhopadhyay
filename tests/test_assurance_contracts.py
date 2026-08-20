import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from portfolio_assurance.assurance import evaluate_repository_assurance


class AssuranceContractTests(unittest.TestCase):
    def observation(self, head_sha="abc", conclusion="success", run_sha="abc", path=".github/workflows/validate.yml"):
        return {
            "repository": "example",
            "observed_at": "2026-08-20T10:00:00Z",
            "available": True,
            "evidence": {
                "repository": {"head_sha": head_sha, "default_branch": "main"},
                "workflow_runs": {
                    "available": True,
                    "latest": [
                        {
                            "path": path,
                            "conclusion": conclusion,
                            "head_sha": run_sha,
                            "html_url": "https://example.invalid/run/1",
                        }
                    ],
                },
            },
        }

    def contract(self, required=True, freshness="current-head"):
        return {
            "profile": "test-profile",
            "claims": {
                "validation": {
                    "required": required,
                    "evidence": {
                        "type": "github-workflow",
                        "path": ".github/workflows/validate.yml",
                        "freshness": freshness,
                    },
                }
            },
        }

    def test_success_at_current_head_is_satisfied(self):
        repo = {"name": "example"}
        state, findings = evaluate_repository_assurance(repo, self.observation(), self.contract())
        self.assertEqual("satisfied", state["state"])
        self.assertEqual([], findings)

    def test_success_for_old_head_is_stale(self):
        repo = {"name": "example"}
        state, findings = evaluate_repository_assurance(
            repo,
            self.observation(head_sha="new", run_sha="old"),
            self.contract(),
        )
        self.assertEqual("stale", state["state"])
        self.assertEqual("ASSURANCE_EVIDENCE_STALE", findings[0]["rule_id"])

    def test_failed_required_control_is_degraded(self):
        repo = {"name": "example"}
        state, findings = evaluate_repository_assurance(
            repo,
            self.observation(conclusion="failure"),
            self.contract(),
        )
        self.assertEqual("degraded", state["state"])
        self.assertEqual("ASSURANCE_CONTROL_FAILED", findings[0]["rule_id"])

    def test_missing_required_control_is_finding(self):
        repo = {"name": "example"}
        observation = self.observation()
        observation["evidence"]["workflow_runs"]["latest"] = []
        state, findings = evaluate_repository_assurance(repo, observation, self.contract())
        self.assertEqual("missing", state["state"])
        self.assertEqual("ASSURANCE_EVIDENCE_MISSING", findings[0]["rule_id"])

    def test_optional_failure_does_not_degrade_repository(self):
        repo = {"name": "example"}
        state, findings = evaluate_repository_assurance(
            repo,
            self.observation(conclusion="failure"),
            self.contract(required=False),
        )
        self.assertEqual("not-applicable", state["state"])
        self.assertEqual([], findings)
        self.assertEqual("degraded", state["claims"][0]["state"])


if __name__ == "__main__":
    unittest.main()
