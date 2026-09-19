import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from screen_titles import decision, unique_id  # noqa: E402


class TitleDecisionTests(unittest.TestCase):
    def test_incretin_included(self):
        status, reason = decision("Oral semaglutide for obesity: a randomized trial")
        self.assertEqual(status, "title_include")
        self.assertIn("Incretin", reason)

    def test_yeast_excluded(self):
        status, reason = decision(
            "A hybrid system enables plasmid copy number control in yeast"
        )
        self.assertEqual(status, "title_exclude")
        self.assertIn("No GLP-1", reason)

    def test_vesicle_without_setting_excluded(self):
        status, reason = decision("Mesenchymal stem cell exosomes in orthopedic hardware coating")
        self.assertEqual(status, "title_exclude")
        self.assertIn("no metabolic", reason)

    def test_vesicle_with_diabetes_included(self):
        status, reason = decision(
            "AD-MSC exosomes in a hydrogel for diabetic wound healing"
        )
        self.assertEqual(status, "title_include")
        self.assertIn("Stem-cell", reason)

    def test_delivery_with_obesity_included(self):
        status, reason = decision("Microneedle nanoparticles for oral insulin in obesity")
        self.assertEqual(status, "title_include")
        self.assertIn("Delivery", reason)

    def test_anti_diabetic_borderline_kept(self):
        status, reason = decision(
            "The role of anti-diabetic drugs in NAFLD. Have we found the Holy Grail?"
        )
        self.assertEqual(status, "title_include")
        self.assertIn("Anti-diabetic", reason)


class UniqueIdTests(unittest.TestCase):
    def test_disambiguates_citekey_collisions(self):
        seen: dict[str, int] = {}
        a = unique_id({"citekey": "Lee2026", "doi": "10.1000/aaa-111"}, seen)
        b = unique_id({"citekey": "Lee2026", "doi": "10.1000/bbb-222"}, seen)
        self.assertEqual(a, "Lee2026")
        self.assertTrue(b.startswith("Lee2026__"))
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main()
