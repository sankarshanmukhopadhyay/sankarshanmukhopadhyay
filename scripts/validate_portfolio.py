#!/usr/bin/env python3
"""Validate the portfolio governance control surface and status federation contracts."""
from __future__ import annotations
from datetime import date
from pathlib import Path
import json, sys
try:
    import yaml
except ImportError:
    print('ERROR: PyYAML is required: pip install PyYAML', file=sys.stderr); raise SystemExit(2)
ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'data/repository-status.yaml'; REL=ROOT/'data/portfolio-relationships.yaml'; SCHEMA=ROOT/'schemas/project-status.schema.json'
REQUIRED=['README.md','LICENSE','GOVERNANCE.md','CONTRIBUTING.md','CHANGELOG.md','ROADMAP.md','portfolio/README.md','portfolio/architecture.md','portfolio/adoption-checklist.md','portfolio/drift-review.md','data/repository-status.yaml','data/portfolio-relationships.yaml','schemas/project-status.schema.json','templates/PROJECT-STATUS.yaml','docs/portfolio-classification-policy.md','config/portfolio-monitor/policy.yaml','scripts/portfolio_assurance_monitor.py','scripts/portfolio_assurance/core.py','scripts/portfolio_assurance/discovery.py','scripts/portfolio_assurance/routing.py','scripts/portfolio_assurance/github_issues.py','schemas/portfolio-observation.schema.json','schemas/portfolio-finding.schema.json','schemas/portfolio-finding-feed.schema.json','docs/portfolio-assurance/findings.md','docs/portfolio-assurance/index.md','docs/portfolio-assurance/methodology.md','docs/portfolio-assurance/operations.md','.github/workflows/portfolio-assurance-monitor.yml','LICENSES.md','LICENSE-CODE','LICENSE-CONTENT']

def load_yaml(p):
    with p.open(encoding='utf-8') as f: v=yaml.safe_load(f)
    if not isinstance(v,dict): raise ValueError(f'{p} must contain a mapping')
    return v

def main():
    errors=[]
    for f in REQUIRED:
        if not (ROOT/f).is_file(): errors.append(f'missing required file: {f}')
    try: status=load_yaml(STATUS); rel=load_yaml(REL); json.loads(SCHEMA.read_text())
    except Exception as e: print(f'ERROR: {e}',file=sys.stderr); return 1
    voc=status.get('controlled_vocabularies',{})
    required_vocab=['portfolio_disposition','tier','maturity','lifecycle','operational_status','specification_status']
    for k in required_vocab:
        if not isinstance(voc.get(k),list) or not voc[k]: errors.append(f'missing controlled vocabulary: {k}')
    repos=status.get('repositories',[]); names=set(); scopes={}; today=date.today()
    account_dispositions=status.get('account_dispositions',[])
    public_surfaces=[ROOT/'README.md', ROOT/'docs/portfolio-status.md', ROOT/'portfolio/architecture.md']
    surface_text='\n'.join(p.read_text(encoding='utf-8') for p in public_surfaces if p.is_file())
    for i,r in enumerate(repos):
        if not isinstance(r,dict): errors.append(f'repositories[{i}] must be mapping'); continue
        n=r.get('name')
        if not n: errors.append(f'repositories[{i}] missing name'); continue
        if n in names: errors.append(f'duplicate repository: {n}')
        names.add(n)
        for field,vkey in [('portfolio_disposition','portfolio_disposition'),('tier','tier'),('maturity','maturity'),('lifecycle','lifecycle'),('operational_status','operational_status'),('specification_status','specification_status')]:
            if r.get(field) not in set(voc.get(vkey,[])): errors.append(f'{n}: invalid {field} {r.get(field)!r}')
        if r.get('maturity') in {'active','active-stack-component','community-draft','candidate-specification','upstream-derived'}: errors.append(f'{n}: maturity improperly contains lifecycle/specification/provenance value')
        prov=r.get('provenance')
        if prov not in {'original','fork','mirror','archived-import','collaborative-host'}: errors.append(f'{n}: invalid provenance {prov!r}')
        if prov=='fork':
            if not r.get('upstream'): errors.append(f'{n}: fork must declare upstream')
            if r.get('portfolio_disposition') not in {'historical','adapted-upstream-work'} and r.get('maturity')!='upstream-tracking': errors.append(f'{n}: active reference fork must use upstream-tracking maturity')
            if r.get('portfolio_disposition')=='adapted-upstream-work' and r.get('maturity') not in {'working-draft','implementation-draft','candidate','pilot-ready','stable','maintenance'}: errors.append(f'{n}: adapted upstream work must declare evidence-based fork-local maturity')
            expected_governance='fork-derived-extension' if r.get('portfolio_disposition')=='adapted-upstream-work' else 'fork-only'
            if r.get('portfolio_governance')!=expected_governance: errors.append(f'{n}: fork must use {expected_governance} governance')
        elif r.get('upstream'): errors.append(f'{n}: non-fork must not declare upstream')
        expected_member=r.get('portfolio_disposition') in {'included','adjacent','upstream-reference','adapted-upstream-work','historical'}
        if r.get('portfolio_member') is not expected_member: errors.append(f'{n}: portfolio_member conflicts with portfolio_disposition')
        ss=r.get('status_source',{})
        if not isinstance(ss,dict) or not ss.get('type') or not ss.get('path'): errors.append(f'{n}: missing status_source contract')
        for f in ('last_portfolio_review','next_review'):
            try: date.fromisoformat(str(r[f]))
            except Exception: errors.append(f'{n}: {f} must be ISO date')
        try:
            if date.fromisoformat(str(r['next_review'])) < today and r.get('lifecycle')=='active': errors.append(f'{n}: review overdue')
        except Exception: pass
        for s in r.get('authority_scope',[]):
            if s in scopes: errors.append(f'authority scope {s!r} claimed by {scopes[s]} and {n}')
            scopes[s]=n
    for r in repos:
        if r.get('portfolio_member') and r.get('name') not in surface_text:
            errors.append(f"{r.get('name')}: portfolio member is not discoverable from a designated public portfolio surface")
    account_names=set()
    for i,r in enumerate(account_dispositions):
        if not isinstance(r,dict): errors.append(f'account_dispositions[{i}] must be mapping'); continue
        n=r.get('name'); disposition=r.get('portfolio_disposition')
        if not n: errors.append(f'account_dispositions[{i}] missing name'); continue
        if n in names or n in account_names: errors.append(f'duplicate account disposition: {n}')
        account_names.add(n)
        if disposition not in set(voc.get('portfolio_disposition',[])): errors.append(f'{n}: invalid account disposition {disposition!r}')
        if disposition in {'included','adjacent','upstream-reference','adapted-upstream-work','pending-review'}:
            errors.append(f'{n}: active or review dispositions require a full repositories[] governance record')
        if not r.get('reason'): errors.append(f'{n}: account disposition requires reason')
    ext={x.get('name') for x in rel.get('external_repositories',[]) if isinstance(x,dict)}; fork_pairs=set(); types=set(rel.get('relationship_types',[]))

    # The portfolio owns classification/topology, while TIS owns the portable
    # relationship serialization contract and TSMM owns canonical semantics.
    relationship_contract=rel.get('relationship_contract',{})
    expected_contract={
        'authority':'trust-infrastructure-schemas',
        'version':'v0.13.0',
        'schema':'https://raw.githubusercontent.com/sankarshanmukhopadhyay/trust-infrastructure-schemas/v0.13.0/portfolio/portfolio-relationship.schema.json',
    }
    if not isinstance(relationship_contract,dict):
        errors.append('relationship_contract must be a mapping')
        relationship_contract={}
    for k,v in expected_contract.items():
        if relationship_contract.get(k)!=v:
            errors.append(f"relationship_contract.{k} must be {v!r}")
    sem_auth=relationship_contract.get('semantic_authority',{})
    if sem_auth.get('repository')!='trust-systems-meta-model' or sem_auth.get('reviewed_version')!='v0.24.0':
        errors.append('relationship_contract.semantic_authority must pin trust-systems-meta-model v0.24.0')
    class_auth=relationship_contract.get('classification_authority',{})
    if class_auth.get('repository')!='sankarshanmukhopadhyay':
        errors.append('relationship_contract.classification_authority must remain sankarshanmukhopadhyay')

    tsmm_tis_pair={}
    for x in rel.get('relationships',[]):
        if x.get('from') not in names: errors.append(f"relationship from unknown {x.get('from')!r}")
        if x.get('to') not in names and x.get('to') not in ext: errors.append(f"relationship to unknown {x.get('to')!r}")
        if x.get('type') not in types: errors.append(f"ungoverned relationship type {x.get('type')!r}")
        if not x.get('constraint'): errors.append(f'relationship lacks constraint: {x!r}')
        contract=x.get('contract')
        if contract is not None:
            if not isinstance(contract,dict):
                errors.append(f"relationship contract must be mapping: {x!r}")
            else:
                if contract.get('semantics') not in {'canonical','derived','independent','not-applicable'}:
                    errors.append(f"invalid relationship contract semantics: {x!r}")
                if contract.get('serialization') not in {'canonical','independent','not-applicable'}:
                    errors.append(f"invalid relationship contract serialization: {x!r}")
        verification=x.get('verification')
        if verification is not None:
            if not isinstance(verification,dict) or not verification.get('source') or not verification.get('artifact'):
                errors.append(f"invalid relationship verification contract: {x!r}")
        if x.get('type')=='fork-of': fork_pairs.add((x.get('from'),x.get('to')))
        if (x.get('from'),x.get('to')) in {
            ('trust-infrastructure-schemas','trust-systems-meta-model'),
            ('trust-systems-meta-model','trust-infrastructure-schemas')
        }:
            tsmm_tis_pair[(x.get('from'),x.get('to'))]=x

    tis_to_tsmm=tsmm_tis_pair.get(('trust-infrastructure-schemas','trust-systems-meta-model'))
    if not tis_to_tsmm or tis_to_tsmm.get('type')!='normative-dependency':
        errors.append('TIS -> TSMM must remain a normative-dependency')
    elif tis_to_tsmm.get('contract')!={'semantics':'canonical','serialization':'independent'}:
        errors.append('TIS -> TSMM must preserve canonical semantics and independent serialization')
    elif tis_to_tsmm.get('verification')!={'source':'trust-infrastructure-schemas','artifact':'artifacts/portfolio/portfolio-alignment.json'}:
        errors.append('TIS -> TSMM must cite TIS portfolio alignment evidence')

    tsmm_to_tis=tsmm_tis_pair.get(('trust-systems-meta-model','trust-infrastructure-schemas'))
    if not tsmm_to_tis or tsmm_to_tis.get('type')!='informative-alignment':
        errors.append('TSMM -> TIS must remain an informative-alignment')
    elif tsmm_to_tis.get('contract')!={'semantics':'canonical','serialization':'independent'}:
        errors.append('TSMM -> TIS must preserve canonical semantics and independent serialization')
    elif tsmm_to_tis.get('verification')!={'source':'trust-systems-meta-model','artifact':'artifacts/portfolio/portfolio-alignment.json'}:
        errors.append('TSMM -> TIS must cite TSMM portfolio alignment evidence')
    for r in repos:
        if r.get('provenance')=='fork' and (r.get('name'),r.get('upstream')) not in fork_pairs: errors.append(f"{r.get('name')}: missing fork-of relationship")
    if errors:
        print('Portfolio validation failed:'); [print('- '+e) for e in errors]; return 1
    print(f"Portfolio validation passed: {len(names)} classified repositories, {len(account_names)} lightweight account dispositions, {len(scopes)} authority scopes, {len(rel.get('relationships',[]))} relationships.")
    return 0
if __name__=='__main__': raise SystemExit(main())
