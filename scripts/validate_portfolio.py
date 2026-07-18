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
REQUIRED=['README.md','LICENSE','GOVERNANCE.md','CONTRIBUTING.md','CHANGELOG.md','ROADMAP.md','portfolio/README.md','portfolio/architecture.md','portfolio/adoption-checklist.md','portfolio/drift-review.md','data/repository-status.yaml','data/portfolio-relationships.yaml','schemas/project-status.schema.json','templates/PROJECT-STATUS.yaml','docs/portfolio-classification-policy.md']

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
            if r.get('maturity')!='upstream-tracking' and r.get('portfolio_disposition')!='historical': errors.append(f'{n}: active fork must use upstream-tracking maturity')
            if r.get('portfolio_governance')!='fork-only': errors.append(f'{n}: fork must use fork-only governance')
        elif r.get('upstream'): errors.append(f'{n}: non-fork must not declare upstream')
        expected_member=r.get('portfolio_disposition') in {'included','adjacent','upstream-reference','historical'}
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
    ext={x.get('name') for x in rel.get('external_repositories',[]) if isinstance(x,dict)}; fork_pairs=set(); types=set(rel.get('relationship_types',[]))
    for x in rel.get('relationships',[]):
        if x.get('from') not in names: errors.append(f"relationship from unknown {x.get('from')!r}")
        if x.get('to') not in names and x.get('to') not in ext: errors.append(f"relationship to unknown {x.get('to')!r}")
        if x.get('type') not in types: errors.append(f"ungoverned relationship type {x.get('type')!r}")
        if not x.get('constraint'): errors.append(f'relationship lacks constraint: {x!r}')
        if x.get('type')=='fork-of': fork_pairs.add((x.get('from'),x.get('to')))
    for r in repos:
        if r.get('provenance')=='fork' and (r.get('name'),r.get('upstream')) not in fork_pairs: errors.append(f"{r.get('name')}: missing fork-of relationship")
    if errors:
        print('Portfolio validation failed:'); [print('- '+e) for e in errors]; return 1
    print(f"Portfolio validation passed: {len(names)} classified repositories, {len(scopes)} authority scopes, {len(rel.get('relationships',[]))} relationships.")
    return 0
if __name__=='__main__': raise SystemExit(main())
