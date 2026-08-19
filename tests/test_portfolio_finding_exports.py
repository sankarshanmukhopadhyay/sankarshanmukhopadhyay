import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import scripts.portfolio_assurance_monitor as monitor


class FindingExportTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 8, 19, 3, 0, tzinfo=dt.timezone.utc)
        self.policy = monitor.load_yaml(monitor.POLICY_PATH)

    def _finding(self, repository="repo-a"):
        return monitor.make_finding(
            repository,
            "REVIEW_OVERDUE",
            "high",
            monitor.iso(self.now),
            "The portfolio review date must not be expired.",
            {"next_review": "2026-08-01"},
            "Conduct and record a portfolio status review.",
            policy=self.policy,
        )

    def test_export_is_remediation_dossier_and_preserves_zero_finding_dossiers(self):
        finding = self._finding()
        policy = {**self.policy, "owner": "example", "publication": {**self.policy["publication"], "development_findings_directory": "reports/findings"}}
        status = {"repositories": [{"name": "repo-a"}, {"name": "repo-b"}]}
        observations = [{
            "repository": "repo-a",
            "observed_at": monitor.iso(self.now),
            "evidence": {"repository": {"default_branch": "main", "head_sha": "abc123"}},
        }]
        lifecycle = {"records": {finding["finding_fingerprint"]: {
            "status": "open", "first_observed": finding["observed_at"]
        }}}
        with tempfile.TemporaryDirectory() as td, patch.object(monitor, "ROOT", Path(td)), patch.object(
            monitor, "load_yaml", return_value=status
        ):
            monitor.write_finding_exports([finding], observations, policy, self.now, lifecycle)
            a = json.loads((Path(td) / "reports/findings/repo-a.json").read_text())
            b = json.loads((Path(td) / "reports/findings/repo-b.json").read_text())
            markdown = (Path(td) / "reports/findings/repo-a.md").read_text()
            zero_markdown = (Path(td) / "reports/findings/repo-b.md").read_text()
            index = json.loads((Path(td) / "reports/findings/index.json").read_text())
        self.assertEqual(a["schema_version"], "2.0")
        self.assertEqual(a["artifact_type"], "repository-remediation-dossier")
        self.assertEqual(a["repository_snapshot"]["head_sha"], "abc123")
        self.assertEqual(a["finding_count"], 1)
        self.assertEqual(a["findings"][0]["dimension"], "governance")
        self.assertTrue(a["findings"][0]["remediation"]["acceptance_criteria"])
        self.assertEqual(b["finding_count"], 0)
        self.assertEqual(len(index["repositories"]), 2)
        self.assertIn("Download:", markdown)
        self.assertIn("Acceptance criteria", markdown)
        self.assertIn("Repository remediation dossier", markdown)
        self.assertIn("not-evaluated", zero_markdown)

    def test_lifecycle_records_resolution_when_finding_disappears(self):
        finding = self._finding()
        policy = {**self.policy, "publication": {**self.policy["publication"], "finding_lifecycle": "lifecycle.json"}}
        previous = {
            "schema_version": "1.0",
            "generated_at": "2026-08-18T00:00:00Z",
            "records": {
                finding["finding_fingerprint"]: {
                    "finding_fingerprint": finding["finding_fingerprint"],
                    "repository": "repo-a",
                    "rule_id": finding["rule_id"],
                    "subject": "repository",
                    "dimension": "governance",
                    "status": "open",
                    "first_observed": "2026-08-18T00:00:00Z",
                    "last_observed": "2026-08-18T00:00:00Z",
                    "resolved_at": None,
                    "latest_finding_id": finding["finding_id"],
                }
            },
        }
        with tempfile.TemporaryDirectory() as td, patch.object(monitor, "ROOT", Path(td)):
            (Path(td) / "lifecycle.json").write_text(json.dumps(previous))
            updated = monitor.update_finding_lifecycle([], policy, self.now)
        record = updated["records"][finding["finding_fingerprint"]]
        self.assertEqual(record["status"], "resolved")
        self.assertIsNotNone(record["resolved_at"])


if __name__ == "__main__":
    unittest.main()
