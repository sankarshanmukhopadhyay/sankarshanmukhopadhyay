import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch
from scripts import weekly_portfolio_report as reporting
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
            if "is:pr" in q and "type:issue" not in q and "merged:" in q:
                records = [hit("trustoverip/dtgwg-rahp-tf", 33, True, merged="2026-10-22T12:00:00Z")]
            elif "type:issue" in q and "-is:pr" in q and "created:" in q:
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

    def test_catch_up_discovers_each_missing_completed_week(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(reporting, "ROOT", Path(tmp)):
            self.assertEqual(
                [date(2026, 10, 26), date(2026, 11, 2)],
                reporting.missing_completed_weeks(date(2026, 11, 13)),
            )
            md, ledger = reporting.output_paths(date(2026, 10, 26))
            md.parent.mkdir(parents=True)
            ledger.parent.mkdir(parents=True)
            md.write_text("draft", encoding="utf-8")
            ledger.write_text("{}", encoding="utf-8")
            self.assertEqual(
                [date(2026, 11, 2)],
                reporting.missing_completed_weeks(date(2026, 11, 13)),
            )

    def test_partial_archive_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(reporting, "ROOT", Path(tmp)):
            md, _ = reporting.output_paths(date(2026, 10, 26))
            md.parent.mkdir(parents=True)
            md.write_text("unpaired report", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "Partial weekly archive"):
                reporting.missing_completed_weeks(date(2026, 11, 13))

    def test_index_tracks_existing_ledgers_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(reporting, "ROOT", Path(tmp)):
            index = Path(tmp) / "docs/weekly-reports/index.md"
            index.parent.mkdir(parents=True)
            index.write_text("# Weekly Portfolio Reports\n\n"
                             "## October 2026\n\n- curated October archive\n\n"
                             "[Reporting methodology](methodology.md)\n", encoding="utf-8")
            for start in [date(2026, 10, 26), date(2026, 11, 2)]:
                md, ledger = reporting.output_paths(start)
                md.parent.mkdir(parents=True, exist_ok=True)
                ledger.parent.mkdir(parents=True, exist_ok=True)
                md.write_text("report", encoding="utf-8")
                ledger.write_text("{}", encoding="utf-8")
            reporting.update_archive_index()
            text = index.read_text(encoding="utf-8")
            self.assertIn("(2026/week-44.html)", text)
            self.assertIn("(2026/week-45.html)", text)
            self.assertLess(text.index("week-45.html"), text.index("week-44.html"))
            self.assertIn("curated October archive", text)
            reporting.update_archive_index()
            self.assertEqual(text, index.read_text(encoding="utf-8"))

    def test_index_does_not_publish_report_without_ledger(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(reporting, "ROOT", Path(tmp)):
            index = Path(tmp) / "docs/weekly-reports/index.md"
            index.parent.mkdir(parents=True)
            index.write_text("[Reporting methodology](methodology.md)", encoding="utf-8")
            md, _ = reporting.output_paths(date(2026, 10, 26))
            md.parent.mkdir(parents=True)
            md.write_text("report", encoding="utf-8")
            with self.assertRaisesRegex(RuntimeError, "missing evidence ledger"):
                reporting.update_archive_index()

    def test_empty_pull_request_metadata_is_still_a_pull_request(self):
        item = hit("trustoverip/upstream", 44, pr=True, created="2026-10-27T12:00:00Z")
        item["pull_request"] = {}  # Present but falsey, as a sparse API response.
        def fetch(url, token):
            return {"total_count": 1, "incomplete_results": False, "items": [item]}
        result = search("pull-request", "created", date(2026, 10, 26),
                        date(2026, 11, 2), "token", fetch)
        self.assertEqual(1, len(result))
        self.assertEqual("pull-request", result[0]["kind"])

    def test_issue_query_excludes_prs_and_counts_issue_events(self):
        from urllib.parse import parse_qs, urlsplit
        seen = []
        issue = hit("trustoverip/upstream", 45, created="2026-10-28T12:00:00Z")
        def fetch(url, token):
            query = parse_qs(urlsplit(url).query)["q"][0]
            seen.append(query)
            records = [issue] if "type:issue" in query and "created:" in query else []
            return {"total_count": len(records), "incomplete_results": False,
                    "items": records}
        result = collect(date(2026, 10, 26), date(2026, 11, 2), "token", fetch)
        self.assertEqual(1, result["counts"]["external|issue|created"])
        self.assertEqual("complete", result["collection_status"])
        self.assertTrue(any("type:issue -is:pr" in q for q in seen))
        self.assertTrue(any("is:pr" in q and "type:issue" not in q for q in seen))

    def test_wrong_kind_issue_search_fails_instead_of_reporting_zero(self):
        pr = hit("trustoverip/upstream", 44, pr=True, created="2026-10-27T12:00:00Z")
        def fetch(url, token):
            return {"total_count": 1, "incomplete_results": False, "items": [pr]}
        with self.assertRaisesRegex(RuntimeError, "Cross-kind GitHub search response"):
            search("issue", "created", date(2026, 10, 26),
                   date(2026, 11, 2), "token", fetch)

    def test_conflicting_url_and_type_metadata_fails_closed(self):
        item = hit("trustoverip/upstream", 44, pr=True)
        item["html_url"] = item["html_url"].replace("/pull/", "/issues/")
        def fetch(url, token):
            return {"total_count": 1, "incomplete_results": False, "items": [item]}
        with self.assertRaisesRegex(RuntimeError, "Contradictory kind metadata"):
            search("pull-request", "created", date(2026, 10, 19),
                   date(2026, 10, 26), "token", fetch)



if __name__ == "__main__":
    unittest.main()
