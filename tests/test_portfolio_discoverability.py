import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class PortfolioDiscoverabilityTests(unittest.TestCase):
    def test_all_portfolio_members_are_on_a_public_surface(self):
        status = yaml.safe_load((ROOT / "data/repository-status.yaml").read_text(encoding="utf-8"))
        surfaces = "\n".join(
            (ROOT / path).read_text(encoding="utf-8")
            for path in ("README.md", "docs/portfolio-status.md", "portfolio/architecture.md")
        )
        missing = [
            repo["name"]
            for repo in status["repositories"]
            if repo.get("portfolio_member") and repo["name"] not in surfaces
        ]
        self.assertEqual([], missing)

    def test_validator_passes_with_discoverability_control_enabled(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_portfolio.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, msg=result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
