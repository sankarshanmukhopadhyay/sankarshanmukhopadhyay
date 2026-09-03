import json
import unittest
from pathlib import Path

import yaml

from scripts.portfolio_work_queue import ROOT, build_queue


class PortfolioWorkQueueReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = yaml.safe_load((ROOT / "data/repository-status.yaml").read_text())
        cls.config = yaml.safe_load((ROOT / "config/portfolio-work-queue.yaml").read_text())
        fixture = ROOT / "tests/fixtures/work-queue-reconciliation-evidence.json"
        cls.evidence = json.loads(fixture.read_text())

    def test_unlabelled_explicit_upstream_wait_is_not_ready(self):
        queue = build_queue(self.registry, self.config, self.evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "rahp-toolkit:issue:88")
        self.assertEqual(candidate["state"], "waiting-external")

    def test_docs_roadmap_pull_request_is_not_execution_work(self):
        queue = build_queue(self.registry, self.config, self.evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "TRQP-TSPP:pull-request:68")
        self.assertEqual(candidate["state"], "maintenance")


if __name__ == "__main__":
    unittest.main()
