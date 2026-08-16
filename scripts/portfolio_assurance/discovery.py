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
