import unittest
from datetime import date
from scripts.weekly_portfolio_report import last_week, search, collect, render


def hit(repo, number, pr=False, merged=None, created="2026-10-20T10:00:00Z",
        closed=None):
    obj = {"repository_url": "https://api.github.com/repos/" + repo, "number": number,
           "title": "bounded contribution", "html_url": f"https://github.com/{repo}/{'pull' if pr else 'issues'}/{number}",
           "created_at": created, "closed_at": closed}
    if pr:
        obj["pull_request"] = {"merged_at": merged}
    return obj


class WeeklyPortfolioTests(unittest.TestCase):
    def test_completed_window(self):
        self.assertEqual((date(2026, 10, 19), date(2026, 10, 26)), last_week(date(2026, 10, 26)))

    def test_cross_owner_merge_and_issue_creation(self):
        def fetch(url, token):
            from urllib.parse import urlsplit, parse_qs
            q = parse_qs(urlsplit(url).query)["q"][0]
            if "is:pull-request" in q and "merged:" in q:
                records = [hit("trustoverip/dtgwg-rahp-tf", 33, True, merged="2026-10-22T12:00:00Z")]
            elif "is:issue" in q and "created:" in q:
                records = [hit("unrelated/project", 12)]
            else:
                records = []
            return {"total_count": len(records), "incomplete_results": False, "items": records}
        ev = collect(date(2026, 10, 19), date(2026, 10, 26), "token", fetch)
        self.assertEqual(2, len(ev["events"]))
        self.assertEqual(1, ev["counts"]["external|pull-request|merged"])
        self.assertEqual(1, ev["counts"]["external|issue|created"])
        self.assertIn("External and upstream", render(ev))

    def test_merged_pr_not_reported_as_unmerged_closure(self):
        x = hit("trustoverip/upstream", 13, True, merged="2026-10-21T10:00:00Z",
                closed="2026-10-21T10:00:00Z")
        def fetch(url, token):
            return {"total_count": 1, "incomplete_results": False, "items": [x]}
        self.assertEqual([], search("pull-request", "closed", date(2026,10,19), date(2026,10,26), "", fetch))

    def test_strict_half_open_interval(self):
        x = hit("qbf-consulting/test", 1, created="2026-10-26T00:00:00Z")
        def fetch(url, token):
            return {"total_count": 1, "incomplete_results": False, "items": [x]}
        self.assertEqual([], search("issue", "created", date(2026,10,19), date(2026,10,26), "", fetch))

    def test_incomplete_search_fails_closed(self):
        def fetch(url, token):
            return {"total_count": 101, "incomplete_results": True, "items": []}
        with self.assertRaises(RuntimeError):
            search("issue", "created", date(2026,10,19), date(2026,10,26), "", fetch)

    def test_search_uses_supported_sort_for_closed_events(self):
        from urllib.parse import urlsplit, parse_qs
        seen = []
        def fetch(url, token):
            seen.append(parse_qs(urlsplit(url).query)["sort"][0])
            return {"total_count": 0, "incomplete_results": False, "items": []}
        search("issue", "closed", date(2026,10,19), date(2026,10,26), "", fetch)
        search("pull-request", "merged", date(2026,10,19), date(2026,10,26), "", fetch)
        search("issue", "created", date(2026,10,19), date(2026,10,26), "", fetch)
        self.assertEqual(["updated", "updated", "created"], seen)


if __name__ == "__main__":
    unittest.main()
