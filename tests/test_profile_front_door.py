import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
STATUS = ROOT / "data" / "repository-status.yaml"

EXPECTED_FRONT_DOOR = {
    "open-national-digital-trust-framework",
    "governance-authority-assurance-metamodel",
    "trust-systems-meta-model",
    "trust-infrastructure-schemas",
    "agent-registry-protocol",
    "PolicyMesh",
    "rahp-toolkit",
    "digital-trust-failure-corpus",
    "dtg-privacy-implementation-profile",
    "TRQP-TSPP",
    "cawg-trqp-verifier-refimpl",
    "trqp-conformance-suite",
    "trqp-assurance-hub",
}


class ProfileFrontDoorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = README.read_text(encoding="utf-8")
        registry = yaml.safe_load(STATUS.read_text(encoding="utf-8"))
        cls.status = {item["name"]: item for item in registry["repositories"]}

    def test_front_door_maturity_matches_canonical_registry(self):
        for name in EXPECTED_FRONT_DOOR:
            self.assertIn(name, self.status, f"{name} missing from canonical registry")
            maturity = self.status[name]["maturity"].replace("-", " ").title()
            pattern = rf"\|[^\n]*{re.escape(name)}[^\n]*\|\s*{re.escape(maturity)}\s*\|"
            self.assertRegex(
                self.readme,
                pattern,
                f"README maturity for {name} must match data/repository-status.yaml",
            )

    def test_front_door_points_to_canonical_status_source(self):
        self.assertIn("data/repository-status.yaml", self.readme)

    def test_glossary_is_visible(self):
        self.assertIn("trust-infrastructure-glossary", self.readme)

    def test_maintainer_section_is_separate(self):
        self.assertIn("## For maintainers and contributors", self.readme)


if __name__ == "__main__":
    unittest.main()
