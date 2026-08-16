from pathlib import Path
import sys
import unittest
import yaml
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from portfolio_assurance.discovery import discovery_findings

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.status=yaml.safe_load((ROOT/'data/repository-status.yaml').read_text())

    def test_unknown_public_repo_is_nominated_not_enrolled(self):
        findings=discovery_findings(self.status,[{'name':'new-public-repo','html_url':'https://github.com/example/new-public-repo','archived':False,'fork':False}],'2026-08-16T00:00:00Z')
        self.assertEqual(1,len(findings))
        self.assertEqual('PUBLIC_REPOSITORY_WITHOUT_DISPOSITION',findings[0]['rule_id'])
        self.assertEqual('none',findings[0]['automatic_effect'])
        self.assertFalse(findings[0]['routing']['eligible'])

    def test_classified_repo_is_not_rediscovered(self):
        findings=discovery_findings(self.status,[{'name':'rahp-toolkit','archived':False,'fork':False}],'2026-08-16T00:00:00Z')
        self.assertEqual([],findings)

    def test_lightweight_account_disposition_is_not_rediscovered(self):
        findings=discovery_findings(self.status,[{'name':'glusterfs','archived':False,'fork':False}],'2026-08-16T00:00:00Z')
        self.assertEqual([],findings)

if __name__=='__main__': unittest.main()
