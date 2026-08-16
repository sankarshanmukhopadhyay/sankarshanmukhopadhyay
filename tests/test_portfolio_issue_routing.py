from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from portfolio_assurance.core import make_finding
from portfolio_assurance.routing import routing_decision
from portfolio_assurance import github_issues

class IssueRoutingTests(unittest.TestCase):
    def setUp(self):
        self.policy=yaml.safe_load((ROOT/'config/portfolio-monitor/policy.yaml').read_text())
        self.repo={'name':'example','assurance_routing':{'target_issue_reporting':True,'minimum_severity':'medium'}}

    def finding(self, subject='validate.yml'):
        f=make_finding('example','DEFAULT_BRANCH_WORKFLOW_UNRESOLVED_FAILURE','medium','2026-08-16T00:00:00Z','claim',{},'fix',subject=subject)
        f['routing']=routing_decision(self.repo,f,self.policy)
        return f

    def test_actionable_failure_is_eligible(self):
        self.assertTrue(self.finding()['routing']['eligible'])

    def test_info_observation_is_not_routed(self):
        f=make_finding('example','NO_RECENT_ACTIVITY','info','2026-08-16T00:00:00Z','claim',{},'review')
        self.assertFalse(routing_decision(self.repo,f,self.policy)['eligible'])

    def test_issue_body_contains_stable_machine_marker_and_governance_boundary(self):
        f=self.finding()
        body=github_issues.render_issue_body(f)
        self.assertIn(github_issues.issue_marker(f['finding_fingerprint']),body)
        self.assertIn('Governance boundary',body)
        self.assertIn('Closure evidence',body)

    @patch.object(github_issues,'find_open_issue')
    @patch.object(github_issues,'create_issue')
    def test_open_issue_deduplicates_without_new_issue(self,create_issue,find_open_issue):
        find_open_issue.return_value={'number':42,'html_url':'https://example.invalid/issues/42'}
        records=github_issues.publish_findings('owner',[self.finding()],'token',self.policy)
        create_issue.assert_not_called()
        self.assertEqual('deduplicated',records[0]['action'])

    @patch.object(github_issues,'find_open_issue',return_value=None)
    @patch.object(github_issues,'create_issue')
    def test_creation_cap_suppresses_excess_findings(self,create_issue,_find):
        create_issue.side_effect=[{'html_url':'https://example.invalid/1'},{'html_url':'https://example.invalid/2'}]
        findings=[self.finding('a.yml'),self.finding('b.yml'),self.finding('c.yml')]
        records=github_issues.publish_findings('owner',findings,'token',self.policy)
        self.assertEqual(2,create_issue.call_count)
        self.assertEqual('suppressed-run-cap',records[-1]['action'])

if __name__=='__main__': unittest.main()
