import tempfile
import unittest
from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_article  # noqa: E402
import check_extraction  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"


class CheckExtractionTests(unittest.TestCase):
    def test_stub_note_fails(self):
        problems = check_extraction.check_note(FIX / "bad-note.md")
        self.assertTrue(problems)
        joined = " ".join(problems).lower()
        self.assertIn("stub", joined)

    def test_claim_ready_note_passes(self):
        self.assertEqual(check_extraction.check_note(FIX / "good-note.md"), [])

    def test_mid_text_out_of_scope_does_not_skip_included_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "included.md"
            p.write_text(
                "# Title\n\n- **Screening:** included after full text.\n\n"
                "Creative writing was out of scope for the question.\n",
                encoding="utf-8",
            )
            problems = check_extraction.check_note(p)
            self.assertTrue(any("Claim-ready" in x for x in problems))

    def test_cli_fails_on_stub_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad-note.md"
            p.write_text((FIX / "bad-note.md").read_text(encoding="utf-8"), encoding="utf-8")
            from unittest.mock import patch

            with patch.object(sys, "argv", ["check_extraction.py", "--notes-dir", tmp]):
                self.assertEqual(check_extraction.main(), 1)

    def test_underscore_sidecar_files_are_not_treated_as_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            notes = Path(tmp)
            (notes / "good.md").write_text(
                (FIX / "good-note.md").read_text(encoding="utf-8"), encoding="utf-8"
            )
            (notes / "_synthesis-rationale.md").write_text(
                "# Synthesis rationale\n\nNot a paper note.\n", encoding="utf-8"
            )
            (notes / "_excluded-and-not-retrieved.md").write_text(
                "# Excluded\n\nLog, not a paper.\n", encoding="utf-8"
            )
            paths = check_extraction.included_note_paths(notes, None)
            self.assertEqual([p.name for p in paths], ["good.md"])
            self.assertEqual(check_extraction.check_note(notes / "good.md"), [])


class CheckArticleTests(unittest.TestCase):
    def test_bad_article_fails(self):
        text = (FIX / "bad-article.md").read_text(encoding="utf-8")
        table = (FIX / "example-table.md").read_text(encoding="utf-8")
        problems = check_article.check(text, table, short=True)
        self.assertTrue(any("this review discusses" in p.lower() or "opens with" in p.lower() for p in problems))
        self.assertTrue(any("banned phrase" in p.lower() or "unpaywall" in p.lower() or "extracted lead" in p.lower() or "in this set" in p.lower() for p in problems))
        self.assertTrue(any("heading names a paper" in p.lower() for p in problems))

    def test_good_short_article_passes_with_table(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        table = (FIX / "example-table.md").read_text(encoding="utf-8")
        problems = check_article.check(text, table, short=True)
        self.assertEqual(problems, [], problems)

    def test_short_flag_required_for_small_body(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        problems = check_article.check(text, None, short=False)
        self.assertTrue(any("word count" in p for p in problems))

    def test_missing_markdown_table_and_callout_fail(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        stripped = "\n".join(
            ln for ln in text.splitlines() if not ln.strip().startswith("|")
        )
        stripped = re.sub(r"\bTable\s+\d+\b", "the results", stripped)
        problems = check_article.check(stripped, None, short=True)
        self.assertTrue(any("markdown results table" in p.lower() for p in problems), problems)
        self.assertTrue(any("table n callout" in p.lower() for p in problems), problems)

    def test_table_without_in_text_callout_fails(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        stripped = re.sub(r"\bTable\s+\d+\b", "the grid", text)
        problems = check_article.check(stripped, None, short=True)
        self.assertTrue(any("table n callout" in p.lower() for p in problems), problems)
        self.assertFalse(any("markdown results table" in p.lower() for p in problems), problems)

    def test_abstract_citation_or_et_al_fails(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        cited = text.replace(
            "The practical next measurement is delayed STEM recall with domain as a planned factor.",
            "Al Researcher et al. raised recall by 18% [1]. The practical next measurement is delayed STEM recall with domain as a planned factor.",
            1,
        )
        problems = check_article.check(cited, None, short=True)
        self.assertTrue(any("abstract contains a citation" in p.lower() for p in problems), problems)
        self.assertTrue(any("abstract names a paper" in p.lower() for p in problems), problems)
