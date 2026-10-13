from pathlib import Path
import unittest

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
OVERLAY = ROOT / "data/portfolio-evidence-gates.yaml"


class PortfolioEvidenceGateOverlayTests(unittest.TestCase):
    def _load(self):
        self.assertIsNotNone(yaml, "PyYAML is required by repository validation")
        with OVERLAY.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        self.assertIsInstance(data, dict)
        return data

    def test_overlay_has_required_control_surface(self):
        data = self._load()
        self.assertEqual(data["schema_version"], "0.1")
        self.assertEqual(data["scope"]["basis"], "data/repository-status.yaml")
        self.assertIn("controlled_vocabularies", data)
        self.assertIn("initial_calibration", data)
        self.assertGreaterEqual(len(data["initial_calibration"]), 5)

    def test_all_calibrated_records_use_controlled_values(self):
        data = self._load()
        vocab = data["controlled_vocabularies"]
        portfolio_views = set(vocab["portfolio_view"])
        gate_states = set(vocab["gate_state"])
        evidence_gates = set(vocab["evidence_gate"])
        stop_conditions = set(vocab["stop_condition"])

        required_fields = {
            "repository",
            "owner",
            "portfolio_view",
            "repo_role",
            "current_maturity_boundary",
            "claim_boundary",
            "next_evidence_gate",
            "gate_state",
            "stop_condition",
            "external_dependency",
            "qbf_relevance",
        }

        for record in data["initial_calibration"]:
            self.assertTrue(required_fields.issubset(record), record.get("repository"))
            self.assertIn(record["portfolio_view"], portfolio_views)
            self.assertIn(record["gate_state"], gate_states)
            self.assertIn(record["stop_condition"], stop_conditions)
            self.assertIsInstance(record["next_evidence_gate"], list)
            self.assertTrue(record["next_evidence_gate"])
            self.assertTrue(set(record["next_evidence_gate"]).issubset(evidence_gates))

    def test_external_wait_states_are_not_marked_complete(self):
        data = self._load()
        for record in data["initial_calibration"]:
            if record["stop_condition"].startswith("pause-until-"):
                self.assertNotEqual(record["gate_state"], "complete", record["repository"])

    def test_qbf_institutional_records_preserve_claim_boundaries(self):
        data = self._load()
        qbf_records = [
            record for record in data["initial_calibration"]
            if record["portfolio_view"] == "qbf-institutional"
        ]
        self.assertGreaterEqual(len(qbf_records), 2)
        for record in qbf_records:
            boundary = record["claim_boundary"].lower()
            self.assertTrue(
                any(term in boundary for term in ["not", "without", "should not"]),
                record["repository"],
            )


if __name__ == "__main__":
    unittest.main()
