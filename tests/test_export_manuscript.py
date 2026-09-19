import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import export_manuscript  # noqa: E402


class ExportManuscriptTests(unittest.TestCase):
    def test_html_is_times_and_justified(self):
        md = "# Title\n\nA paragraph with **bold**.\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
        html = export_manuscript.markdown_to_html(md, "Title")
        self.assertIn("Times New Roman", html)
        self.assertIn("text-align: justify", html)
        self.assertIn("<table>", html)
        self.assertIn("<h1>", html)

    def test_cli_writes_html(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "article.md"
            src.write_text("# Hello\n\nWorld.\n", encoding="utf-8")
            out = Path(tmp) / "export"
            from unittest.mock import patch

            with patch.object(
                sys,
                "argv",
                [
                    "export_manuscript.py",
                    "--article",
                    str(src),
                    "--out-dir",
                    str(out),
                    "--format",
                    "html",
                ],
            ):
                self.assertEqual(export_manuscript.main(), 0)
            html = (out / "article.html").read_text(encoding="utf-8")
            self.assertIn("Times New Roman", html)
            self.assertIn("World", html)
