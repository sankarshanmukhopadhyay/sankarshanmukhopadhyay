#!/usr/bin/env python3
"""Portfolio assurance monitor v3: evidence-contract evaluation over v2 collection."""
from __future__ import annotations
import argparse, json, os
from pathlib import Path
from typing import Any
import portfolio_assurance_monitor as legacy
from portfolio_assurance.assurance import evaluate_portfolio_assurance, render_assurance_section
ROOT=Path(__file__).resolve().parents[1]
CONTRACTS_PATH=ROOT/"config/portfolio-monitor/assurance-contracts.yaml"
STEWARDSHIP_PATH=ROOT/"data/repository-stewardship.yaml"
ASSURANCE_STATE_PATH=ROOT/"reports/portfolio-assurance/assurance-state.json"

def repo_owner(repo, stewardship, fallback):
    return str(stewardship.get("repositories",{}).get(str(repo["name"]),{}).get("owner") or stewardship.get("default_owner") or fallback)

def bind_assurance_findings(repos,findings,policy):
    by_repo={str(r["name"]):r for r in repos}; result=[]
    for finding in findings:
        repo=by_repo.get(str(finding.get("repository")))
        if repo is not None: finding["routing"]=legacy.routing_decision(repo,finding,policy)
        result.append(legacy.enrich_finding(finding,policy))
    return result

def bind_current_workflow_inventory(owner,repo,observation,policy,token):
    if not observation.get("available"): return
    workflow_state=observation.get("evidence",{}).get("workflow_runs")
    if not isinstance(workflow_state,dict) or workflow_state.get("available") is False: return
    timeout=int(policy["collection"]["request_timeout_seconds"]); name=str(repo["name"])
    try: inventory=legacy.request_json(f"https://api.github.com/repos/{owner}/{name}/actions/workflows?per_page=100",token,timeout)
    except Exception as error: workflow_state["active_inventory_available"]=False; workflow_state["active_inventory_error"]=str(error); return
    workflows=inventory.get("workflows",[]) if isinstance(inventory,dict) else []; active_paths={str(i.get("path")) for i in workflows if isinstance(i,dict) and i.get("path") and i.get("state")!="deleted"}
    workflow_state["active_inventory_available"]=True; workflow_state["active_workflow_paths"]=sorted(active_paths)
    latest=list(workflow_state.get("latest",[])); retired=list(workflow_state.get("retired",[])); active_latest=[]
    for record in latest:
        path=record.get("path") if isinstance(record,dict) else None
        (retired if path and str(path) not in active_paths else active_latest).append(record)
    active_unresolved=[r for r in workflow_state.get("unresolved",[]) if not r.get("path") or str(r.get("path")) in active_paths]
    workflow_state.update(latest=active_latest,retired=retired,workflows_examined=len(active_latest),retired_workflows_examined=len(retired),unresolved=active_unresolved,unresolved_failures=len(active_unresolved))

def inject_assurance_section(report,section):
    marker="## Governance boundary"; return report.replace(marker,f"{section}\n\n{marker}",1) if marker in report else f"{report}\n\n{section}\n"

def write_assurance_state(states,generated_at):
    ASSURANCE_STATE_PATH.parent.mkdir(parents=True,exist_ok=True); ASSURANCE_STATE_PATH.write_text(json.dumps({"schema_version":"1.0","generated_at":generated_at,"authority":"evidence-coverage-observation","states":states},indent=2)+"\n")

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--offline",action="store_true"); parser.add_argument("--check",action="store_true"); parser.add_argument("--publish-issues",action="store_true"); args=parser.parse_args()
    status=legacy.load_yaml(legacy.STATUS_PATH); policy=legacy.load_yaml(legacy.POLICY_PATH); contracts=legacy.load_yaml(CONTRACTS_PATH); stewardship=legacy.load_yaml(STEWARDSHIP_PATH); repos=legacy.selected_repositories(status,policy)
    if not repos: raise SystemExit("No repositories selected by portfolio monitor policy")
    missing=sorted({str(r["name"]) for r in repos}-set(contracts.get("repositories",{})))
    if missing: raise SystemExit(f"Missing assurance contracts for monitored repositories: {', '.join(missing)}")
    now=legacy.utc_now(); token=os.getenv("GITHUB_TOKEN")
    observations=[legacy.offline_observation(r,now) if args.offline else legacy.collect_repository(repo_owner(r,stewardship,policy["owner"]),r,policy,token,now) for r in repos]
    if not args.offline:
        for repo,obs in zip(repos,observations): bind_current_workflow_inventory(repo_owner(repo,stewardship,policy["owner"]),repo,obs,policy,token)
    findings=[f for r,o in zip(repos,observations) for f in legacy.evaluate(r,o,policy,now)]
    assurance_states,assurance_findings=evaluate_portfolio_assurance(repos,observations,contracts); findings.extend(bind_assurance_findings(repos,assurance_findings,policy))
    # Account discovery remains scoped to the personal account; transferred portfolio members are deliberately excluded from churn inference.
    if not args.offline and policy.get("discovery",{}).get("enabled",False):
        try:
            public_repos=legacy.discover_public_repositories(policy["owner"],legacy.request_json,token,int(policy["collection"]["request_timeout_seconds"]))
            findings.extend([legacy.enrich_finding(f,policy) for f in legacy.discovery_findings(status,public_repos,legacy.iso(now),str(policy["discovery"].get("severity","info")))])
        except Exception as error:
            findings.append(legacy.enrich_finding(legacy._make_finding(policy["owner"],"ACCOUNT_DISCOVERY_UNAVAILABLE","low",legacy.iso(now),"Public account discovery could not be completed.",{"error":str(error)},"Review GitHub API availability and monitor permissions; do not infer portfolio completeness from this run.",subject="public-account-discovery"),policy))
    publication_records=[]; issue_cfg=policy.get("issue_routing",{}); issue_token=os.getenv("PORTFOLIO_ISSUE_TOKEN")
    if args.publish_issues and issue_cfg.get("enabled",False):
        if not issue_token: publication_records.append({"action":"skipped","reason":"PORTFOLIO_ISSUE_TOKEN not configured"})
        else: publication_records=legacy.publish_findings(policy["owner"],findings,issue_token,policy,f"https://{policy['owner']}.github.io/{policy['owner']}/docs/portfolio-assurance/dashboard.html")
    section=render_assurance_section(repos,assurance_states); dashboard=inject_assurance_section(legacy.render_report(repos,observations,findings,now,publication_role="dashboard"),section); evidence=inject_assurance_section(legacy.render_report(repos,observations,findings,now,publication_role="evidence"),section)
    if not args.check: legacy.write_outputs(dashboard,evidence,findings,observations,policy,now,publication_records); write_assurance_state(assurance_states,legacy.iso(now))
    counts={}
    for state in assurance_states.values(): counts[str(state.get("state","not-evaluated"))]=counts.get(str(state.get("state","not-evaluated")),0)+1
    print(f"Portfolio assurance monitor v3: {len(repos)} repositories, {len(findings)} findings, assurance[{', '.join(f'{k}={v}' for k,v in sorted(counts.items()))}], {len(publication_records)} issue actions, mode={'offline' if args.offline else 'live'}"); return 0
if __name__=="__main__": raise SystemExit(main())
