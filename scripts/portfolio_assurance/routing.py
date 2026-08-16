from __future__ import annotations
from typing import Any
from .core import SEVERITY_RANK


def routing_decision(repo: dict[str, Any], finding: dict[str, Any], policy: dict[str, Any]) -> dict[str, Any]:
    cfg = policy.get("issue_routing", {})
    repo_cfg = repo.get("assurance_routing", {})
    enabled = bool(repo_cfg.get("target_issue_reporting", cfg.get("default_target_issue_reporting", False)))
    eligible_rules = set(repo_cfg.get("enabled_rules", cfg.get("eligible_rules", [])))
    excluded_rules = set(repo_cfg.get("excluded_rules", cfg.get("excluded_rules", [])))
    minimum = str(repo_cfg.get("minimum_severity", cfg.get("minimum_severity", "medium")))
    eligible = (
        enabled
        and finding["rule_id"] in eligible_rules
        and finding["rule_id"] not in excluded_rules
        and SEVERITY_RANK.get(finding["severity"], -1) >= SEVERITY_RANK.get(minimum, 2)
    )
    return {
        "eligible": eligible,
        "target": "target-repository" if eligible else "central-review",
        "minimum_severity": minimum,
    }
