import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from search_oa_related import citekey_from_work, catalog_rows, work_to_record  # noqa: E402


class CitekeyTests(unittest.TestCase):
    def test_citekey_uses_api_fields_only(self):
        work = {
            "authorships": [{"author": {"display_name": "Ada Example"}}],
            "publication_year": 2024,
            "doi": "https://doi.org/10.1234/abcd99",
        }
        self.assertEqual(citekey_from_work(work), "Example2024_abcd99")

    def test_missing_author_does_not_invent_a_name(self):
        work = {"authorships": [], "publication_year": 2020, "doi": "10.1/xyz"}
        key = citekey_from_work(work)
        self.assertTrue(key.startswith("Anon2020_"))


class RecordTests(unittest.TestCase):
    def test_work_to_record_does_not_fill_missing_doi(self):
        rec = work_to_record({"display_name": "Only a title", "authorships": []})
        self.assertEqual(rec["doi"], "")
        self.assertEqual(rec["title"], "Only a title")

    def test_catalog_rows_mark_gap_fill(self):
        rows = catalog_rows(
            [
                {
                    "citekey": "Example2024_x",
                    "title": "A",
                    "author": "Ada Example",
                    "year": "2024",
                    "journal": "J",
                    "doi": "10.1/abc",
                    "oa_status": "gold",
                }
            ]
        )
        self.assertEqual(len(rows), 1)
        self.assertTrue(rows[0]["gap_fill"])
        self.assertEqual(rows[0]["doi"], "10.1/abc")


if __name__ == "__main__":
    unittest.main()
