import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from screen_fulltext import assess_text  # noqa: E402


class AssessFulltextTests(unittest.TestCase):
    def test_unreadable_short_text(self):
        status, reason = assess_text("Semaglutide in obesity", "too short")
        self.assertEqual(status, "unreadable")
        self.assertIn("too short", reason)

    def test_incretin_in_body_included(self):
        body = ("Abstract\n" + "Semaglutide reduced HbA1c in adults with type 2 diabetes. ") * 20
        status, reason = assess_text("A clinical trial", body)
        self.assertEqual(status, "include")
        self.assertIn("Incretin", reason)

    def test_terms_only_in_references_excluded(self):
        body = ("Methods\n" + "A digital weight management programme recruited adults with obesity. ") * 30
        refs = "\nReferences\n1. Wilding 2021 semaglutide STEP 1 GLP-1 receptor agonist trial.\n"
        status, reason = assess_text("Digital weight programme", body + refs)
        self.assertEqual(status, "exclude")
        self.assertIn("references", reason)

    def test_exosome_diabetes_included(self):
        body = (
            "Adipose MSC exosomes in a hydrogel were tested on diabetic wounds. " * 40
        )
        status, _ = assess_text("Exosome hydrogel", body)
        self.assertEqual(status, "include")


if __name__ == "__main__":
    unittest.main()
