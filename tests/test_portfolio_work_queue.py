import json
import unittest
from pathlib import Path

import yaml

from scripts.portfolio_work_queue import ROOT, build_queue, eligible_repositories, render_markdown, validate_queue


class PortfolioWorkQueueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = yaml.safe_load((ROOT / "data/repository-status.yaml").read_text())
        cls.config = yaml.safe_load((ROOT / "config/portfolio-work-queue.yaml").read_text())
        cls.evidence = json.loads((ROOT / "tests/fixtures/work-queue-evidence.json").read_text())

    def build(self):
        return build_queue(self.registry, self.config, self.evidence)

    def test_scope_is_governed(self):
        eligible = eligible_repositories(self.registry, self.config)
        queue = self.build()
        self.assertTrue(queue["candidates"])
        self.assertTrue(all(c["repository"] in eligible for c in queue["candidates"]))

    def test_dependency_noise_does_not_outrank_release_work(self):
        queue = self.build()
        release = next(c for c in queue["candidates"] if c["repository"] == "TRQP-TSPP")
        dependency = next(c for c in queue["candidates"] if c["repository"] == "rahp-toolkit")
        self.assertGreater(release["priority"], dependency["priority"])
        self.assertEqual(dependency["state"], "maintenance")

    def test_external_blocker_not_ready(self):
        queue = self.build()
        blocked = next(c for c in queue["candidates"] if c["id"].endswith(":78"))
        self.assertEqual(blocked["state"], "waiting-external")

    def test_consequential_change_requires_judgment(self):
        queue = self.build()
        candidate = next(c for c in queue["candidates"] if c["id"].endswith(":77"))
        self.assertEqual(candidate["complexity"], "consequential")
        self.assertEqual(candidate["state"], "needs-judgment")

    def test_output_is_deterministic_for_fixed_evidence(self):
        first = self.build()
        second = self.build()
        self.assertEqual(first, second)
        self.assertEqual([], validate_queue(first))

    def test_render_exposes_required_views(self):
        page = render_markdown(self.build(), self.config)
        for heading in ["## Work now", "## Highest leverage", "## By available time", "## Needs judgment", "## Blocked or waiting", "## Maintenance lane"]:
            self.assertIn(heading, page)


if __name__ == "__main__":
    unittest.main()
