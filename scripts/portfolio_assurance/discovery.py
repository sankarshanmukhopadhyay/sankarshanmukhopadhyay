from __future__ import annotations
import datetime as dt
from typing import Any, Callable
from .core import make_finding


def discover_public_repositories(owner: str, request_json: Callable[..., Any], token: str | None, timeout: int) -> list[dict[str, Any]]:
    repositories: list[dict[str, Any]] = []
    for page in range(1, 11):
        batch = request_json(f"https://api.github.com/users/{owner}/repos?type=public&sort=full_name&per_page=100&page={page}", token, timeout)
        if not isinstance(batch, list):
            break
        repositories.extend(batch)
        if len(batch) < 100:
            break
    return repositories


def discovery_findings(status: dict[str, Any], public_repositories: list[dict[str, Any]], observed_at: str, severity: str = "info") -> list[dict[str, Any]]:
    classified = {r.get("name") for r in status.get("repositories", []) if isinstance(r, dict)}
    classified.update({r.get("name") for r in status.get("account_dispositions", []) if isinstance(r, dict)})
    findings = []
    for repo in public_repositories:
        name = repo.get("name")
        if not name or name in classified or repo.get("fork") is True and repo.get("archived") is True:
            continue
        findings.append(make_finding(
            "sankarshanmukhopadhyay",
            "PUBLIC_REPOSITORY_WITHOUT_DISPOSITION",
            severity,
            observed_at,
            "A public account repository has no governed account-level portfolio disposition.",
            {"repository": name, "html_url": repo.get("html_url"), "archived": repo.get("archived"), "fork": repo.get("fork")},
            "Review the repository and assign an explicit included, adjacent, upstream-reference, adapted-upstream-work, historical, unrelated, or pending-review disposition. Discovery never auto-enrols a repository.",
            subject=name,
        ))
    return findings


def registered_repository_churn_findings(status: dict[str, Any], public_repositories: list[dict[str, Any]], observed_at: str, severity: str = "medium") -> list[dict[str, Any]]:
    """Flag governed active/review repositories that disappear from public account discovery.

    This is a portfolio-governance signal for rename, deletion, privatization, transfer, or stale registry state.
    It deliberately excludes historical, superseded, and archived records.
    """
    public_names = {r.get("name") for r in public_repositories if isinstance(r, dict) and r.get("name")}
    findings: list[dict[str, Any]] = []
    governed_dispositions = {"included", "adjacent", "upstream-reference", "adapted-upstream-work", "pending-review"}
    for repo in status.get("repositories", []):
        if not isinstance(repo, dict):
            continue
        name = repo.get("name")
        if not name or name in public_names:
            continue
        if repo.get("portfolio_disposition") not in governed_dispositions:
            continue
        if repo.get("lifecycle") in {"superseded", "archived"}:
            continue
        findings.append(make_finding(
            "sankarshanmukhopadhyay",
            "REGISTERED_REPOSITORY_NOT_PUBLICLY_DISCOVERED",
            severity,
            observed_at,
            "A governed active or review repository is no longer present in public account discovery; its registry identity may be stale.",
            {
                "registered_repository": name,
                "portfolio_disposition": repo.get("portfolio_disposition"),
                "lifecycle": repo.get("lifecycle"),
                "provenance": repo.get("provenance"),
            },
            "Determine whether the repository was renamed, transferred, privatized, deleted, or intentionally retired, then update the governed repository identity and relationships. Do not infer the new identity automatically.",
            subject=name,
        ))
    return findings
