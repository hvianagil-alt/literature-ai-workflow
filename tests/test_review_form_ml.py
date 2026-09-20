import json
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import review_form_features as feat  # noqa: E402
import review_form_model as model  # noqa: E402
import score_review_form as score  # noqa: E402
import check_article  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"


class FrontFeatureTests(unittest.TestCase):
    def test_published_like_abstract_has_contrast_not_catalog(self):
        title = (
            "Delayed recall of technical prose: a narrative review of format and domain"
        )
        abstract = (
            "Readers forget procedures within a week. Structured notes are widely "
            "recommended, yet whether format changes recall remains unsettled. "
            "Laboratory work generally points to a small benefit; the STEM test did not. "
            "Those patterns do not imply a semester-long habit."
        )
        f = feat.extract_front_features(title, abstract)
        self.assertGreater(f["title_has_colon"], 0.5)
        self.assertGreater(f["abstract_contrast_per_100w"], 0)
        self.assertEqual(f["abstract_has_citation"], 0)
        self.assertEqual(f["title_flourish"], 0)
        self.assertEqual(f["abstract_this_review_first_sentence"], 0)

    def test_catalog_abstract_flags(self):
        title = "Recent Advances in Notes: A Comprehensive Overview"
        abstract = (
            "This review discusses notes. First, we searched Scopus. Second, "
            "Author et al. found a striking effect. Third, more research is needed."
        )
        f = feat.extract_front_features(title, abstract)
        self.assertEqual(f["title_flourish"], 1)
        self.assertEqual(f["abstract_this_review_first_sentence"], 1)
        self.assertEqual(f["abstract_has_etal"], 1)
        self.assertEqual(f["abstract_ordinal"], 1)
        self.assertGreater(f["abstract_slogan_per_100w"], 0)


class FullFeatureTests(unittest.TestCase):
    def test_good_fixture_is_claim_first_with_table(self):
        text = (FIX / "good-article.md").read_text(encoding="utf-8")
        f = feat.extract_features(text)
        self.assertGreater(f["claim_first_ratio"], 0.5)
        self.assertEqual(f["has_markdown_table"], 1)
        self.assertEqual(f["has_results_h2"], 0)
        self.assertEqual(f["coverage_fulltext"], 1)

    def test_bad_fixture_is_catalog(self):
        text = (FIX / "bad-article.md").read_text(encoding="utf-8")
        f = feat.extract_features(text)
        self.assertEqual(f["has_results_h2"], 1)
        self.assertEqual(f["intro_bad_opener"], 1)
        self.assertGreater(f["process_outside_methods"] + f["abstract_acquisition"], 0)


class ModelTests(unittest.TestCase):
    def test_logreg_separates_published_from_catalog(self):
        positives = []
        negatives = []
        for i in range(12):
            t = (
                f"Phenomenon {i} in adjacent tissue: a narrative review of tension"
            )
            a = (
                "The clinical problem is unsolved. Current options already lower "
                "symptoms, yet they fail when the barrier is intact. Trial and "
                "observational work do not point the same way. Those patterns do "
                "not imply a guideline change."
            )
            positives.append(
                {
                    "field": "generic-narrative",
                    "features": feat.extract_front_features(t, a),
                }
            )
            nt, na = score.catalog_mutations(t, a)[0]
            negatives.append(
                {
                    "field": "generic-narrative",
                    "features": feat.extract_front_features(nt, na),
                }
            )
        bundle = model.train_bundle(positives, negatives, names=feat.FRONT_FEATURES, l2=0.4)
        self.assertGreater(bundle["train_auc"], 0.9)
        self.assertGreater(bundle["train_accuracy"], 0.9)
        good_vec = feat.vectorize(positives[0]["features"], feat.FRONT_FEATURES)
        bad_vec = feat.vectorize(negatives[0]["features"], feat.FRONT_FEATURES)
        p_good = model.score_vector(good_vec, bundle)["p_published_form"]
        p_bad = model.score_vector(bad_vec, bundle)["p_published_form"]
        self.assertGreater(p_good, 0.6)
        self.assertLess(p_bad, 0.4)

    def test_train_and_score_cli_on_fixtures(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            catalog = tmp_path / "gold-catalog.json"
            catalog.write_text(json.dumps({"records": []}) + "\n", encoding="utf-8")
            model_path = tmp_path / "model.json"
            rc = score.main(
                ["train", "--catalog", str(catalog), "--model", str(model_path)]
            )
            self.assertEqual(rc, 0, "train should work from fixtures alone")
            self.assertTrue(model_path.is_file())
            good = FIX / "good-article.md"
            bad = FIX / "bad-article.md"
            rc_good = score.main(
                [
                    "score",
                    "--article",
                    str(good),
                    "--model",
                    str(model_path),
                    "--min-p",
                    "0.45",
                ]
            )
            rc_bad = score.main(
                [
                    "score",
                    "--article",
                    str(bad),
                    "--model",
                    str(model_path),
                    "--min-p",
                    "0.45",
                ]
            )
            self.assertEqual(rc_good, 0)
            self.assertEqual(rc_bad, 1)


class CheckArticleFormModelTests(unittest.TestCase):
    def test_optional_form_model_flags_catalog_draft(self):
        with tempfile.TemporaryDirectory() as tmp:
            catalog = Path(tmp) / "gold-catalog.json"
            catalog.write_text(json.dumps({"records": []}) + "\n", encoding="utf-8")
            model_path = Path(tmp) / "model.json"
            self.assertEqual(
                score.main(["train", "--catalog", str(catalog), "--model", str(model_path)]),
                0,
            )
            text = (FIX / "bad-article.md").read_text(encoding="utf-8")
            problems = check_article.check(
                text, None, short=True, form_model_path=str(model_path)
            )
            self.assertTrue(
                any("published-review form score" in p.lower() for p in problems),
                problems,
            )


if __name__ == "__main__":
    unittest.main()
