#!/usr/bin/env python3
"""Validate required repository-local PROJECT-STATUS contracts against portfolio governance."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "data/repository-status.yaml"
SCHEMA_PATH = ROOT / "schemas/project-status.schema.json"
DEFAULT_OUTPUT = ROOT / "reports/portfolio-assurance/member-status-contracts.json"
OWNER = "sankarshanmukhopadhyay"
USER_AGENT = "portfolio-member-status-validator/1.0"


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return value


def request_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url: str, token: str | None) -> str:
    headers = {
        "Accept": "application/vnd.github.raw+json",
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8")


def required_member_contracts(status: dict[str, Any]) -> list[dict[str, Any]]:
    selected = []
    for repo in status.get("repositories", []):
        source = repo.get("status_source", {})
        if source.get("type") == "member-declaration" and source.get("required") is True:
            selected.append(repo)
    return selected


def add_error(result: dict[str, Any], code: str, message: str, evidence: Any = None) -> None:
    result["errors"].append({"code": code, "message": message, "evidence": evidence})


def validate_contract(repo: dict[str, Any], schema: dict[str, Any], token: str | None) -> dict[str, Any]:
    name = str(repo["name"])
    source = repo["status_source"]
    path = str(source.get("path", "PROJECT-STATUS.yaml"))
    result: dict[str, Any] = {
        "repository": name,
        "path": path,
        "available": False,
        "schema_valid": False,
        "registry_consistent": False,
        "authority_consistent": False,
        "errors": [],
    }

    try:
        metadata = request_json(f"https://api.github.com/repos/{OWNER}/{name}", token)
        branch = str(metadata.get("default_branch") or "main")
        raw = request_text(
            f"https://api.github.com/repos/{OWNER}/{name}/contents/{path}?ref={branch}", token
        )
        result["available"] = True
        result["default_branch"] = branch
    except urllib.error.HTTPError as error:
        add_error(result, "STATUS_DECLARATION_UNAVAILABLE", f"HTTP {error.code} while fetching declaration")
        return result
    except Exception as error:
        add_error(result, "STATUS_DECLARATION_UNAVAILABLE", str(error))
        return result

    try:
        declaration = yaml.safe_load(raw)
        if not isinstance(declaration, dict):
            raise ValueError("declaration must contain a YAML mapping")
    except Exception as error:
        add_error(result, "STATUS_DECLARATION_UNREADABLE", str(error))
        return result

    try:
        jsonschema.Draft202012Validator(schema).validate(declaration)
        result["schema_valid"] = True
    except jsonschema.ValidationError as error:
        add_error(
            result,
            "STATUS_DECLARATION_SCHEMA_INVALID",
            error.message,
            {"json_path": list(error.absolute_path), "schema_path": list(error.absolute_schema_path)},
        )

    project = declaration.get("project", {}) if isinstance(declaration.get("project"), dict) else {}
    expected_fields = {
        "name": name,
        "maturity": repo.get("maturity"),
        "lifecycle": repo.get("lifecycle"),
        "operational_status": repo.get("operational_status"),
        "specification_status": repo.get("specification_status"),
    }
    drift = {
        field: {"expected": expected, "observed": project.get(field)}
        for field, expected in expected_fields.items()
        if project.get(field) != expected
    }
    if drift:
        add_error(result, "STATUS_DECLARATION_REGISTRY_DRIFT", "Repository-local project state differs from the governed portfolio registry.", drift)
    else:
        result["registry_consistent"] = True

    authority = declaration.get("authority", {}) if isinstance(declaration.get("authority"), dict) else {}
    expected_scope = sorted(str(value) for value in repo.get("authority_scope", []))
    observed_scope = authority.get("normative_scope", [])
    if not isinstance(observed_scope, list):
        observed_scope = []
    observed_scope = sorted(str(value) for value in observed_scope)
    if observed_scope != expected_scope:
        add_error(
            result,
            "STATUS_DECLARATION_AUTHORITY_DRIFT",
            "Repository-local normative authority scope differs from the governed portfolio registry.",
            {"expected": expected_scope, "observed": observed_scope},
        )
    else:
        result["authority_consistent"] = True

    result["valid"] = (
        result["available"]
        and result["schema_valid"]
        and result["registry_consistent"]
        and result["authority_consistent"]
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    args = parser.parse_args()

    status = load_yaml(STATUS_PATH)
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    token = os.getenv("GITHUB_TOKEN")
    repositories = required_member_contracts(status)
    results = [validate_contract(repo, schema, token) for repo in repositories]
    failures = [result for result in results if not result.get("valid")]

    report = {
        "schema_version": "1.0",
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_registry": "data/repository-status.yaml",
        "contract_schema": "schemas/project-status.schema.json",
        "required_contracts": len(repositories),
        "valid_contracts": len(results) - len(failures),
        "invalid_contracts": len(failures),
        "results": results,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    if failures:
        print(f"Member status contract validation failed: {len(failures)} of {len(results)} repositories invalid.")
        for result in failures:
            print(f"- {result['repository']}")
            for error in result["errors"]:
                print(f"  - {error['code']}: {error['message']}")
        return 1

    print(f"Member status contract validation passed: {len(results)} required declarations are available, schema-valid, registry-consistent, and authority-consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
