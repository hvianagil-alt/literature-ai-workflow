import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from search_oa_related import (  # noqa: E402
    build_openalex_filters,
    catalog_rows,
    citekey_from_work,
    work_to_record,
)


class FilterTests(unittest.TestCase):
    def test_default_journal_quality_requires_journal_articles(self):
        filters = build_openalex_filters()
        self.assertIn("is_oa:true", filters)
        self.assertIn("has_doi:true", filters)
        self.assertIn("type:article", filters)
        self.assertIn("primary_location.source.type:journal", filters)
        self.assertTrue(all("from_publication_date" not in f for f in filters))

    def test_year_window_and_doaj(self):
        filters = build_openalex_filters(
            from_year=2020, to_year=2026, journal_quality="doaj"
        )
        self.assertIn("from_publication_date:2020-01-01", filters)
        self.assertIn("to_publication_date:2026-12-31", filters)
        self.assertIn("primary_location.source.is_in_doaj:true", filters)

    def test_cited_preset_uses_default_floor(self):
        filters = build_openalex_filters(journal_quality="cited")
        self.assertIn("cited_by_count:>10", filters)

    def test_none_allows_preprints(self):
        filters = build_openalex_filters(journal_quality="none")
        self.assertNotIn("type:article", filters)
        self.assertTrue(all("source.type" not in f for f in filters))

    def test_bad_journal_quality_raises(self):
        with self.assertRaises(ValueError):
            build_openalex_filters(journal_quality="q1")


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
        self.assertEqual(rec["source_type"], "")
        self.assertFalse(rec["is_in_doaj"])

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
        self.assertEqual(rows[0]["origin"], "gap_fill")

    def test_catalog_rows_can_mark_seed_search(self):
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
            ],
            origin="related_to_seeds",
        )
        self.assertFalse(rows[0]["gap_fill"])
        self.assertEqual(rows[0]["origin"], "related_to_seeds")


class FindPapersCliTests(unittest.TestCase):
    def test_per_page_cap_rejects_without_network(self):
        import sys
        from unittest.mock import patch

        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
        import find_papers  # noqa: WPS433

        with patch.object(
            sys,
            "argv",
            [
                "find_papers.py",
                "--query",
                "x",
                "--mailto",
                "a@b.c",
                "--run-dir",
                "/tmp",
                "--per-page",
                "99",
            ],
        ):
            self.assertEqual(find_papers.main(), 2)


if __name__ == "__main__":
    unittest.main()
