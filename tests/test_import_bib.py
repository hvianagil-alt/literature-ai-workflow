import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from import_bib import parse_bibtex  # noqa: E402
from phase_log import estimate_tokens  # noqa: E402


SAMPLE = """Scopus
EXPORT DATE: 19 September 2026

@ARTICLE{Boye2026,
	author = {Boye, Kristina S. and Stewart, Katie D.},
	title = {Development of the Patient Satisfaction with Medication for Diabetes (PSMD) questionnaire},
	year = {2026},
	journal = {Journal of Patient-Reported Outcomes},
	doi = {10.1186/s41687-026-01037-w},
	note = {Cited by: 0; All Open Access; Gold Open Access}
}

@ARTICLE{Li2026,
	author = {Li, Anni},
	title = {A hybrid system enables plasmid copy number control in yeast},
	year = {2026},
	doi = {10.1038/s41467-026-75973-y},
	note = {Cited by: 0; All Open Access; Gold Open Access}
}
"""


class ParseBibTests(unittest.TestCase):
    def test_parses_scopus_header_and_two_articles(self):
        recs = parse_bibtex(SAMPLE)
        self.assertEqual(len(recs), 2)
        self.assertEqual(recs[0]["citekey"], "Boye2026")
        self.assertEqual(recs[0]["doi"], "10.1186/s41687-026-01037-w")
        self.assertTrue(recs[0]["gold_oa"])
        self.assertEqual(recs[1]["citekey"], "Li2026")

    def test_does_not_invent_missing_fields(self):
        recs = parse_bibtex("@article{X, title = {Only a title},\n}")
        self.assertEqual(recs[0]["doi"], "")
        self.assertEqual(recs[0]["year"], "")


class TokenEstimateTests(unittest.TestCase):
    def test_chars_div_4(self):
        self.assertEqual(estimate_tokens(0), 0)
        self.assertEqual(estimate_tokens(4), 1)
        self.assertEqual(estimate_tokens(5), 2)


if __name__ == "__main__":
    unittest.main()
