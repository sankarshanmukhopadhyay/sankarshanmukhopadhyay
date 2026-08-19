import tempfile
import unittest
from pathlib import Path

from scripts.check_internal_links import target_exists


class InternalLinkValidationTests(unittest.TestCase):
    def test_existing_target_resolves(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "page.md"
            target.write_text("# Page\n", encoding="utf-8")
            self.assertTrue(target_exists(target))

    def test_jekyll_html_target_resolves_to_markdown_source(self):
        with tempfile.TemporaryDirectory() as td:
            markdown = Path(td) / "finding.md"
            markdown.write_text("# Finding\n", encoding="utf-8")
            self.assertTrue(target_exists(Path(td) / "finding.html"))

    def test_missing_html_target_still_fails(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertFalse(target_exists(Path(td) / "missing.html"))


if __name__ == "__main__":
    unittest.main()
