import unittest
from datetime import date
from scripts.weekly_portfolio_report import last_week


class WeeklyPortfolioTests(unittest.TestCase):
    def test_completed_week(self):
        self.assertEqual((date(2026, 10, 19), date(2026, 10, 26)),
                         last_week(date(2026, 10, 26)))

    def test_midweek(self):
        self.assertEqual((date(2026, 10, 19), date(2026, 10, 26)),
                         last_week(date(2026, 10, 29)))


if __name__ == "__main__":
    unittest.main()
