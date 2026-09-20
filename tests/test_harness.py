import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class HarnessLayoutTests(unittest.TestCase):
    def test_skill_and_agents_exist(self):
        self.assertTrue((ROOT / ".cursor/skills/review-harness/SKILL.md").is_file())
        self.assertTrue((ROOT / ".cursor/agents/literature-critic.md").is_file())
        self.assertTrue((ROOT / ".cursor/agents/literature-extractor.md").is_file())
        self.assertTrue((ROOT / ".cursor/agents/field-form-reader.md").is_file())
        self.assertTrue((ROOT / "scripts/check_harness.py").is_file())
        self.assertTrue((ROOT / ".cursor/skills/review-form-ml/SKILL.md").is_file())
        self.assertTrue((ROOT / "scripts/score_review_form.py").is_file())
        harness = (ROOT / ".cursor/skills/review-harness/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("max 3", harness.lower())
        self.assertIn("check_harness.py", harness)
        self.assertIn("literature-critic", harness)
        self.assertIn("check_review_craft.py", harness)
        self.assertNotIn("Lovable", harness)
        self.assertTrue((ROOT / "scripts/check_review_craft.py").is_file())

    def test_memory_is_form_only(self):
        index = (ROOT / "review/memory/index.md").read_text(encoding="utf-8")
        readme = (ROOT / "review/memory/README.md").read_text(encoding="utf-8")
        self.assertIn("form only", readme.lower())
        self.assertIn("generic-narrative.md", index)
        self.assertIn("endocrinology.md", index)
        self.assertIn("nanomedicine.md", index)
        self.assertIn("food-science.md", index)
        self.assertIn("neuroscience.md", index)
        food = (ROOT / "review/memory/food-science.md").read_text(encoding="utf-8")
        self.assertIn("Do not copy", food)
        critic = (ROOT / ".cursor/agents/literature-critic.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Critic verdict: PASS", critic)
        self.assertIn("Must not write the first draft", critic)


class CheckHarnessScriptTests(unittest.TestCase):
    def test_empty_dir_fails(self):
        import sys

        sys.path.insert(0, str(ROOT / "scripts"))
        import check_harness  # noqa: WPS433

        with tempfile.TemporaryDirectory() as tmp:
            problems = check_harness.evaluate(Path(tmp), full=True, run_scripts=False)
        self.assertTrue(problems)
        self.assertTrue(any("run dir missing" in p or "missing" in p for p in problems))

    def test_hpp_run_passes_full_without_rechecking_pdfs(self):
        import sys

        sys.path.insert(0, str(ROOT / "scripts"))
        import check_harness  # noqa: WPS433

        run = ROOT / "review" / "runs" / "2026-09-20-scopus-hpp"
        problems = check_harness.evaluate(run, full=True, run_scripts=False)
        self.assertEqual(problems, [], problems)
