import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class WorkflowRequiresRationaleTests(unittest.TestCase):
    def test_agents_md_has_rationale_gate_before_article(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("synthesis-rationale", text)
        self.assertIn("(a)", text)
        self.assertIn("(e)", text)
        self.assertIn("just write the review", text)
        self.assertLess(text.find("synthesis-rationale.md"), text.find("### 7."))

    def test_skills_table_points_at_synthesis_rationale(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(".cursor/skills/synthesis-rationale/SKILL.md", text)

    def test_literature_table_handoff_is_rationale_then_report(self):
        text = (ROOT / ".cursor/skills/literature-table/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("table → synthesis-rationale", text)
        self.assertIn("report-writing", text)

    def test_report_writing_requires_rationale_outline(self):
        text = (ROOT / ".cursor/skills/report-writing/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("synthesis-rationale.md", text)
        self.assertIn("Section (e)", text)
        self.assertIn("token", text.lower())
        self.assertIn("usage-log.md", text)

    def test_synthesis_rationale_skill_exists_with_quality_bar(self):
        text = (ROOT / ".cursor/skills/synthesis-rationale/SKILL.md").read_text(
            encoding="utf-8"
        )
        for heading in (
            "(a) What each included study actually measured",
            "(b) Themes the data support vs themes that would be forced",
            "(c) Real disagreements and why",
            "(d) What this sample cannot answer",
            "(e) Outline of the review",
        ):
            self.assertIn(heading, text)
        self.assertIn("article.md", text)
        self.assertIn("hard sequencing gate", text.lower())


class MiniReviewRunTests(unittest.TestCase):
    run_dir = ROOT / "review" / "runs" / "2026-09-19-scopus-oa"

    def test_rationale_has_required_sections_and_all_seven_papers(self):
        text = (self.run_dir / "synthesis-rationale.md").read_text(encoding="utf-8")
        for marker in ("## (a)", "## (b)", "## (c)", "## (d)", "## (e)"):
            self.assertIn(marker, text)
        for paper in (
            "Wu 2026",
            "Jeong 2026",
            "Zhang 2026",
            "Khater 2026",
            "Chen 2026",
            "Guo 2026",
            "Boye 2026",
        ):
            self.assertIn(paper, text)
        self.assertIn("Decision to write", text)

    def test_article_has_no_token_or_phase_meter(self):
        text = (self.run_dir / "article.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for banned in (
            "token estimate",
            "est_total",
            "characters/4",
            "usage-log",
            "phase meter",
            "est_input_tokens",
        ):
            self.assertNotIn(banned, lowered)
        self.assertIn("## Abstract", text)
        self.assertIn("## References", text)
        self.assertNotIn("catalogue of abstracts", text.lower())


if __name__ == "__main__":
    unittest.main()
