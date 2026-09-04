import copy
import json
import unittest

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
        self.assertEqual(candidate["state"], "waiting_external")
        self.assertEqual(candidate["dependency"]["kind"], "external")

    def test_closed_source_is_completed_and_non_executable(self):
        evidence = copy.deepcopy(self.evidence)
        evidence["repositories"].setdefault("TRQP-TSPP", {}).setdefault("issues", []).append(
            {
                "number": 99900,
                "title": "chore(governance): close public repository baseline gaps",
                "url": "https://github.com/sankarshanmukhopadhyay/TRQP-TSPP/issues/99900",
                "labels": [],
                "body": "Completed baseline maintenance.",
                "state": "closed",
                "updated_at": "2026-09-04T00:00:00Z",
                "observed_at": "2026-09-04T00:01:00Z",
            }
        )
        queue = build_queue(self.registry, self.config, evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "TRQP-TSPP:issue:99900")
        self.assertEqual(candidate["state"], "completed")
        self.assertEqual(candidate["priority"], 0)
        self.assertNotEqual(candidate["state"], "ready")

    def test_docs_roadmap_pull_request_is_not_execution_work(self):
        queue = build_queue(self.registry, self.config, self.evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "TRQP-TSPP:pull-request:68")
        self.assertEqual(candidate["lane"], "planning")
        self.assertNotEqual(candidate["lane"], "strategic")

    def test_ready_is_positive_claim(self):
        queue = build_queue(self.registry, self.config, self.evidence)
        for candidate in queue["candidates"]:
            if candidate["state"] == "ready":
                self.assertEqual(candidate["dependency"]["kind"], "none")
                self.assertNotEqual(candidate["complexity"], "consequential")

    def test_breaking_title_routes_to_judgment_without_label(self):
        evidence = copy.deepcopy(self.evidence)
        evidence["repositories"].setdefault("rahp-toolkit", {}).setdefault("issues", []).append(
            {
                "number": 99901,
                "title": "feat(controller)!: replace assurance state contract",
                "url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/issues/99901",
                "labels": [],
                "body": "Consumer-visible contract replacement.",
                "updated_at": "2026-09-03T00:00:00Z",
            }
        )
        queue = build_queue(self.registry, self.config, evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "rahp-toolkit:issue:99901")
        self.assertTrue(candidate["change"]["breaking"])
        self.assertEqual(candidate["state"], "needs_judgment")
        self.assertEqual(candidate["complexity"], "consequential")

    def test_security_type_routes_to_judgment_without_label(self):
        evidence = copy.deepcopy(self.evidence)
        evidence["repositories"].setdefault("rahp-toolkit", {}).setdefault("issues", []).append(
            {
                "number": 99902,
                "title": "security(runtime): reject cross-context disclosure",
                "url": "https://github.com/sankarshanmukhopadhyay/rahp-toolkit/issues/99902",
                "labels": [],
                "body": "Runtime security boundary hardening.",
                "updated_at": "2026-09-03T00:00:00Z",
            }
        )
        queue = build_queue(self.registry, self.config, evidence)
        candidate = next(c for c in queue["candidates"] if c["id"] == "rahp-toolkit:issue:99902")
        self.assertEqual(candidate["change"]["type"], "security")
        self.assertEqual(candidate["state"], "needs_judgment")


if __name__ == "__main__":
    unittest.main()
