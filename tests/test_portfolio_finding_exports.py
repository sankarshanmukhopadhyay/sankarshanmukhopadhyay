import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import scripts.portfolio_assurance_monitor as monitor
from scripts.portfolio_assurance.core import make_finding


class FindingExportTests(unittest.TestCase):
    def test_export_preserves_stable_fingerprint_and_zero_finding_feeds(self):
        now = dt.datetime(2026, 8, 17, 8, 0, tzinfo=dt.timezone.utc)
        finding = make_finding(
            "repo-a", "RULE_A", "high", monitor.iso(now), "claim", {"proof": True}, "fix it"
        )
        policy = {
            "owner": "example",
            "publication": {"development_findings_directory": "reports/findings"},
        }
        status = {"repositories": [{"name": "repo-a"}, {"name": "repo-b"}]}
        with tempfile.TemporaryDirectory() as td, patch.object(monitor, "ROOT", Path(td)), patch.object(
            monitor, "load_yaml", return_value=status
        ):
            monitor.write_finding_exports([finding], policy, now)
            a = json.loads((Path(td) / "reports/findings/repo-a.json").read_text())
            b = json.loads((Path(td) / "reports/findings/repo-b.json").read_text())
            index = json.loads((Path(td) / "reports/findings/index.json").read_text())
        self.assertEqual(a["finding_count"], 1)
        self.assertEqual(a["findings"][0]["finding_fingerprint"], finding["finding_fingerprint"])
        self.assertEqual(b["finding_count"], 0)
        self.assertEqual(len(index["repositories"]), 2)
        self.assertTrue(a["$schema"].endswith("portfolio-finding-feed.schema.json"))


if __name__ == "__main__":
    unittest.main()
