import importlib.util
from pathlib import Path
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "pam_v3", ROOT / "scripts/portfolio_assurance_monitor_v3.py"
)
pam_v3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pam_v3)


class PortfolioAssuranceWorkflowInventoryTests(unittest.TestCase):
    def setUp(self):
        self.policy = pam_v3.legacy.load_yaml(
            ROOT / "config/portfolio-monitor/policy.yaml"
        )
        self.repo = {"name": "rahp-toolkit"}
        self.observation = {
            "repository": "rahp-toolkit",
            "available": True,
            "evidence": {
                "workflow_runs": {
                    "available": True,
                    "workflows_examined": 2,
                    "unresolved_failures": 1,
                    "latest": [
                        {
                            "workflow_id": 100,
                            "name": "validate",
                            "path": ".github/workflows/validate.yml",
                            "conclusion": "success",
                        },
                        {
                            "workflow_id": 200,
                            "name": "Publish RAHP v1.5.0",
                            "path": ".github/workflows/release-v1.5.0.yml",
                            "conclusion": "failure",
                        },
                    ],
                    "unresolved": [
                        {
                            "workflow_id": 200,
                            "name": "Publish RAHP v1.5.0",
                            "path": ".github/workflows/release-v1.5.0.yml",
                            "conclusion": "failure",
                        }
                    ],
                }
            },
        }

    def test_removed_workflow_is_retired_not_unresolved(self):
        inventory = {
            "workflows": [
                {
                    "id": 100,
                    "path": ".github/workflows/validate.yml",
                    "state": "active",
                },
                {
                    "id": 300,
                    "path": ".github/workflows/release.yml",
                    "state": "active",
                },
            ]
        }
        with mock.patch.object(pam_v3.legacy, "request_json", return_value=inventory):
            pam_v3.bind_current_workflow_inventory(
                "sankarshanmukhopadhyay",
                self.repo,
                self.observation,
                self.policy,
                "token",
            )

        state = self.observation["evidence"]["workflow_runs"]
        self.assertTrue(state["active_inventory_available"])
        self.assertEqual(0, state["unresolved_failures"])
        self.assertEqual([], state["unresolved"])
        self.assertEqual(1, state["workflows_examined"])
        self.assertEqual(1, state["retired_workflows_examined"])
        self.assertEqual(
            ".github/workflows/release-v1.5.0.yml",
            state["retired"][0]["path"],
        )
        self.assertEqual(
            [".github/workflows/validate.yml"],
            [record["path"] for record in state["latest"]],
        )

    def test_inventory_failure_preserves_conservative_failure(self):
        with mock.patch.object(
            pam_v3.legacy,
            "request_json",
            side_effect=RuntimeError("inventory unavailable"),
        ):
            pam_v3.bind_current_workflow_inventory(
                "sankarshanmukhopadhyay",
                self.repo,
                self.observation,
                self.policy,
                "token",
            )

        state = self.observation["evidence"]["workflow_runs"]
        self.assertFalse(state["active_inventory_available"])
        self.assertEqual(1, state["unresolved_failures"])
        self.assertEqual(
            ".github/workflows/release-v1.5.0.yml",
            state["unresolved"][0]["path"],
        )


if __name__ == "__main__":
    unittest.main()
