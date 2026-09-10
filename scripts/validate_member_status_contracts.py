#!/usr/bin/env python3
"""Validate required repository-local PROJECT-STATUS contracts against portfolio governance."""
from __future__ import annotations
import argparse, datetime as dt, json, os, urllib.error, urllib.request
from pathlib import Path
from typing import Any
import jsonschema, yaml
ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "data/repository-status.yaml"
STEWARDSHIP_PATH = ROOT / "data/repository-stewardship.yaml"
SCHEMA_PATH = ROOT / "schemas/project-status.schema.json"
DEFAULT_OUTPUT = ROOT / "reports/portfolio-assurance/member-status-contracts.json"
USER_AGENT = "portfolio-member-status-validator/1.1"

def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict): raise ValueError(f"{path} must contain a YAML mapping")
    return value

def repository_owner(name: str, stewardship: dict[str, Any]) -> str:
    entry = stewardship.get("repositories", {}).get(name, {})
    return str(entry.get("owner") or stewardship.get("default_owner") or "sankarshanmukhopadhyay")

def request_json(url: str, token: str | None) -> Any:
    headers={"Accept":"application/vnd.github+json","User-Agent":USER_AGENT,"X-GitHub-Api-Version":"2022-11-28"}
    if token: headers["Authorization"]=f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=20) as response: return json.loads(response.read().decode())

def request_text(url: str, token: str | None) -> str:
    headers={"Accept":"application/vnd.github.raw+json","User-Agent":USER_AGENT,"X-GitHub-Api-Version":"2022-11-28"}
    if token: headers["Authorization"]=f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=20) as response: return response.read().decode()

def required_member_contracts(status):
    return [r for r in status.get("repositories",[]) if r.get("status_source",{}).get("type")=="member-declaration" and r.get("status_source",{}).get("required") is True]

def add_error(result, code, message, evidence=None): result["errors"].append({"code":code,"message":message,"evidence":evidence})

def validate_contract(repo, schema, stewardship, token):
    name=str(repo["name"]); owner=repository_owner(name,stewardship); source=repo["status_source"]; path=str(source.get("path","PROJECT-STATUS.yaml"))
    result={"repository":name,"owner":owner,"path":path,"available":False,"schema_valid":False,"registry_consistent":False,"authority_consistent":False,"errors":[]}
    try:
        metadata=request_json(f"https://api.github.com/repos/{owner}/{name}",token); branch=str(metadata.get("default_branch") or "main")
        raw=request_text(f"https://api.github.com/repos/{owner}/{name}/contents/{path}?ref={branch}",token); result.update(available=True,default_branch=branch)
    except urllib.error.HTTPError as error: add_error(result,"STATUS_DECLARATION_UNAVAILABLE",f"HTTP {error.code} while fetching declaration"); return result
    except Exception as error: add_error(result,"STATUS_DECLARATION_UNAVAILABLE",str(error)); return result
    try:
        declaration=yaml.safe_load(raw)
        if not isinstance(declaration,dict): raise ValueError("declaration must contain a YAML mapping")
    except Exception as error: add_error(result,"STATUS_DECLARATION_UNREADABLE",str(error)); return result
    try: jsonschema.Draft202012Validator(schema).validate(declaration); result["schema_valid"]=True
    except jsonschema.ValidationError as error: add_error(result,"STATUS_DECLARATION_SCHEMA_INVALID",error.message,{"json_path":list(error.absolute_path),"schema_path":list(error.absolute_schema_path)})
    project=declaration.get("project",{}) if isinstance(declaration.get("project"),dict) else {}
    expected={"name":name,"maturity":repo.get("maturity"),"lifecycle":repo.get("lifecycle"),"operational_status":repo.get("operational_status"),"specification_status":repo.get("specification_status")}
    drift={field:{"expected":value,"observed":project.get(field)} for field,value in expected.items() if project.get(field)!=value}
    if drift: add_error(result,"STATUS_DECLARATION_REGISTRY_DRIFT","Repository-local project state differs from the governed portfolio registry.",drift)
    else: result["registry_consistent"]=True
    authority=declaration.get("authority",{}) if isinstance(declaration.get("authority"),dict) else {}; expected_scope=sorted(map(str,repo.get("authority_scope",[]))); observed_scope=authority.get("normative_scope",[]); observed_scope=sorted(map(str,observed_scope if isinstance(observed_scope,list) else []))
    if observed_scope!=expected_scope: add_error(result,"STATUS_DECLARATION_AUTHORITY_DRIFT","Repository-local normative authority scope differs from the governed portfolio registry.",{"expected":expected_scope,"observed":observed_scope})
    else: result["authority_consistent"]=True
    result["valid"]=all(result[k] for k in ["available","schema_valid","registry_consistent","authority_consistent"]); return result

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--output",default=str(DEFAULT_OUTPUT)); args=parser.parse_args()
    status=load_yaml(STATUS_PATH); stewardship=load_yaml(STEWARDSHIP_PATH); schema=json.loads(SCHEMA_PATH.read_text()); token=os.getenv("GITHUB_TOKEN"); repositories=required_member_contracts(status)
    results=[validate_contract(r,schema,stewardship,token) for r in repositories]; failures=[r for r in results if not r.get("valid")]
    report={"schema_version":"1.1","generated_at":dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z"),"source_registry":"data/repository-status.yaml","stewardship_registry":"data/repository-stewardship.yaml","contract_schema":"schemas/project-status.schema.json","required_contracts":len(repositories),"valid_contracts":len(results)-len(failures),"invalid_contracts":len(failures),"results":results}
    output=Path(args.output); output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(report,indent=2)+"\n")
    if failures:
        print(f"Member status contract validation failed: {len(failures)} of {len(results)} repositories invalid.")
        for result in failures:
            print(f"- {result['owner']}/{result['repository']}")
            for error in result["errors"]: print(f"  - {error['code']}: {error['message']}")
        return 1
    print(f"Member status contract validation passed: {len(results)} required declarations are available, schema-valid, registry-consistent, and authority-consistent."); return 0
if __name__=="__main__": raise SystemExit(main())
