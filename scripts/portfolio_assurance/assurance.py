from __future__ import annotations
from typing import Any, Callable

from portfolio_assurance.core import make_finding as base_finding

SUCCESS_CONCLUSIONS = {"success", "neutral", "skipped"}
STATE_PRIORITY = {
    "degraded": 5,
    "missing": 4,
    "unobservable": 3,
    "stale": 2,
    "satisfied": 1,
    "not-applicable": 0,
    "not-evaluated": 0,
}


def workflow_index(observation: dict[str, Any]) -> dict[str, dict[str, Any]]:
    workflows = observation.get("evidence", {}).get("workflow_runs", {})
    result: dict[str, dict[str, Any]] = {}
    for run in workflows.get("latest", []) if isinstance(workflows, dict) else []:
        path = str(run.get("path") or "")
        if path:
            result[path] = run
    return result


def evaluate_workflow_claim(
    claim_name: str,
    claim: dict[str, Any],
    observation: dict[str, Any],
) -> dict[str, Any]:
    evidence = claim.get("evidence", {})
    path = str(evidence.get("path") or "")
    required = bool(claim.get("required", False))
    freshness = str(evidence.get("freshness", "current-head"))
    workflows = observation.get("evidence", {}).get("workflow_runs", {})
    repository = observation.get("evidence", {}).get("repository", {})
    head_sha = repository.get("head_sha")

    result: dict[str, Any] = {
        "claim": claim_name,
        "required": required,
        "evidence_type": "github-workflow",
        "subject": path,
        "freshness_policy": freshness,
        "state": "not-evaluated",
        "reason": "claim has not been evaluated",
    }

    if not observation.get("available") or workflows.get("available") is False:
        result.update(state="unobservable", reason="workflow evidence is not observable")
        return result

    run = workflow_index(observation).get(path)
    if run is None:
        result.update(
            state="missing",
            reason="no completed workflow execution was observed inside the governed lookback window",
        )
        return result

    result["evidence"] = run
    conclusion = str(run.get("conclusion") or "")
    if conclusion not in SUCCESS_CONCLUSIONS:
        result.update(state="degraded", reason=f"latest completed workflow conclusion is {conclusion or 'unknown'}")
        return result

    if freshness == "current-head" and head_sha and run.get("head_sha") != head_sha:
        result.update(
            state="stale",
            reason="successful evidence does not cover the current default-branch HEAD",
            repository_head_sha=head_sha,
            evidence_head_sha=run.get("head_sha"),
        )
        return result

    result.update(state="satisfied", reason="successful workflow evidence satisfies the configured freshness policy")
    return result


def aggregate_state(claims: list[dict[str, Any]]) -> str:
    required = [claim for claim in claims if claim.get("required")]
    if not required:
        return "not-applicable"
    return max((str(claim.get("state", "not-evaluated")) for claim in required), key=lambda state: STATE_PRIORITY.get(state, 0))


def finding_for_claim(repository: str, observed_at: str, result: dict[str, Any]) -> dict[str, Any] | None:
    if not result.get("required"):
        return None
    state = result.get("state")
    subject = str(result.get("subject") or result.get("claim") or "assurance-evidence")
    evidence = {
        "claim": result.get("claim"),
        "state": state,
        "reason": result.get("reason"),
        "freshness_policy": result.get("freshness_policy"),
        "repository_head_sha": result.get("repository_head_sha"),
        "evidence_head_sha": result.get("evidence_head_sha"),
        "workflow": result.get("evidence"),
    }
    if state == "missing":
        rule_id, severity = "ASSURANCE_EVIDENCE_MISSING", "high"
        claim = "Required assurance evidence was not observed inside the governed evidence window."
        action = "Restore or execute the repository-native assurance control and publish observable evidence."
    elif state == "unobservable":
        rule_id, severity = "ASSURANCE_EVIDENCE_UNOBSERVABLE", "high"
        claim = "Required assurance evidence could not be observed by the portfolio monitor."
        action = "Restore evidence observability before treating the assurance claim as evaluated."
    elif state == "degraded":
        rule_id, severity = "ASSURANCE_CONTROL_FAILED", "high"
        claim = "The repository-native control bound to this assurance claim is currently failing."
        action = "Resolve the failing repository-native control or record an explicit governed disposition."
    elif state == "stale":
        rule_id, severity = "ASSURANCE_EVIDENCE_STALE", "medium"
        claim = "Required assurance evidence is successful but does not cover the current governed repository state."
        action = "Regenerate the assurance evidence against the current default-branch HEAD."
    else:
        return None
    finding = base_finding(repository, rule_id, severity, observed_at, claim, evidence, action, subject=subject)
    finding["dimension"] = "assurance"
    finding["remediation"] = {
        "objective": action,
        "acceptance_criteria": [
            "The required assurance claim evaluates to satisfied against the governed evidence contract.",
            "Evidence provenance identifies the workflow execution and repository revision it covers.",
        ],
        "verification": [
            "Run the repository-native assurance control.",
            "Rerun the portfolio assurance monitor and confirm the stable finding fingerprint is closed.",
        ],
    }
    return finding


def evaluate_repository_assurance(
    repo: dict[str, Any],
    observation: dict[str, Any],
    contract: dict[str, Any] | None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    name = str(repo.get("name"))
    observed_at = str(observation.get("observed_at"))
    if not contract:
        state = {
            "repository": name,
            "profile": None,
            "state": "not-evaluated",
            "claims": [],
            "reason": "no assurance contract is configured",
        }
        return state, []

    claim_results: list[dict[str, Any]] = []
    for claim_name, claim in contract.get("claims", {}).items():
        evidence = claim.get("evidence", {})
        evidence_type = evidence.get("type")
        if evidence_type == "github-workflow":
            result = evaluate_workflow_claim(str(claim_name), claim, observation)
        else:
            result = {
                "claim": str(claim_name),
                "required": bool(claim.get("required", False)),
                "evidence_type": evidence_type,
                "subject": str(evidence.get("path") or claim_name),
                "state": "not-evaluated",
                "reason": f"no adapter is implemented for evidence type {evidence_type}",
            }
        claim_results.append(result)

    findings = [finding for result in claim_results if (finding := finding_for_claim(name, observed_at, result))]
    state = {
        "repository": name,
        "profile": contract.get("profile"),
        "state": aggregate_state(claim_results),
        "claims": claim_results,
        "required_claims": len([claim for claim in claim_results if claim.get("required")]),
        "satisfied_required_claims": len([claim for claim in claim_results if claim.get("required") and claim.get("state") == "satisfied"]),
    }
    return state, findings


def evaluate_portfolio_assurance(
    repos: list[dict[str, Any]],
    observations: list[dict[str, Any]],
    contracts: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    by_observation = {str(obs.get("repository")): obs for obs in observations}
    configured = contracts.get("repositories", {})
    states: dict[str, dict[str, Any]] = {}
    findings: list[dict[str, Any]] = []
    for repo in repos:
        name = str(repo.get("name"))
        state, repo_findings = evaluate_repository_assurance(repo, by_observation[name], configured.get(name))
        states[name] = state
        findings.extend(repo_findings)
    return states, findings


def render_assurance_section(repos: list[dict[str, Any]], states: dict[str, dict[str, Any]]) -> str:
    lines = [
        "## Assurance evidence coverage",
        "",
        "The assurance state below is calculated from repository-specific evidence contracts. The monitor evaluates whether required evidence exists, succeeds, and covers the governed repository revision; it does not replace the authority of the evidence-producing repository or tool.",
        "",
        "| Repository | Profile | Assurance state | Required claims | Evidence coverage |",
        "|---|---|---|---:|---:|",
    ]
    for repo in repos:
        name = str(repo.get("name"))
        state = states[name]
        required = int(state.get("required_claims", 0))
        satisfied = int(state.get("satisfied_required_claims", 0))
        lines.append(f"| [{name}](https://github.com/sankarshanmukhopadhyay/{name}) | `{state.get('profile') or 'unconfigured'}` | **{state.get('state')}** | {required} | {satisfied}/{required} |")
        for claim in state.get("claims", []):
            marker = "required" if claim.get("required") else "optional"
            lines.append(f"| ↳ `{claim.get('claim')}` | {marker} | `{claim.get('state')}` |  | {claim.get('reason')} |")
    lines.append("")
    return "\n".join(lines)
