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
        self.assertIn("check_extraction.py", text)
        self.assertIn("table_from_notes.py", text)

    def test_report_writing_requires_rationale_outline(self):
        text = (ROOT / ".cursor/skills/report-writing/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("synthesis-rationale.md", text)
        self.assertIn("Section (e)", text)
        self.assertIn("token", text.lower())
        self.assertIn("usage-log.md", text)
        self.assertIn("review-prose", text)
        self.assertIn("6,000", text)
        self.assertIn("Match the spine", text)
        self.assertIn("Taken together", text)
        self.assertIn("This review discusses", text)
        self.assertIn("check_article.py", text)
        self.assertIn("article-qa", text)
        self.assertIn("In-article results tables", text)
        self.assertIn("Full term (ABBR)", text)
        self.assertIn("at most four", text)
        self.assertIn("Do not wait for the user", text)
        self.assertEqual(text.count("## Output"), 1)
        self.assertNotIn("glycaemia, safety, utilisation", text)
        self.assertNotIn("hepatic GLP-1", text)

    def test_review_prose_skill_exists(self):
        text = (ROOT / ".cursor/skills/review-prose/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("secondary", text.lower())
        self.assertIn("6,000", text)
        self.assertIn("Introduction", text)
        self.assertIn("stands as", text)
        self.assertIn("delve", text)
        self.assertIn("Not only X, but also Y", text)
        self.assertIn("Sentence construction", text)
        self.assertIn("Author et al.", text)
        self.assertIn("Match the spine", text)
        self.assertIn("present tense", text)
        self.assertIn("central argument", text)
        self.assertIn("form only", text)
        self.assertIn("Taken together", text)
        self.assertIn("Headings name topics", text)
        self.assertIn("This review discusses", text)
        self.assertIn("Tables in the article", text)
        self.assertIn("Table 1", text)
        self.assertIn("Do not put in the Abstract", text)
        self.assertIn("colon subtitle", text.lower())
        self.assertIn("Abbreviations", text)
        self.assertIn("T2D", text)
        self.assertIn("first-time", text)
        self.assertIn("generic Results", text)
        self.assertIn("Known failure", text)
        self.assertIn("Continuous prose", text)
        self.assertIn("`this`", text)
        self.assertIn("First/Second", text)
        self.assertNotIn("First, … Finally", text)
        self.assertIn("Keywords", text)
        self.assertIn("colon subtitle", text.lower())
        self.assertIn("Recent Advances", text)
        self.assertIn("Headings name topics", text)

    def test_first_conversation_skill_exists(self):
        path = ROOT / ".cursor/skills/first-conversation/SKILL.md"
        self.assertTrue(path.is_file())
        text = path.read_text(encoding="utf-8")
        self.assertIn("new user", text.lower())
        self.assertIn("Wait", text)
        self.assertNotIn("Lovable", text)
        self.assertFalse(
            (ROOT / ".cursor/skills/graphical-abstract/SKILL.md").is_file()
        )

    def test_agents_md_points_at_review_prose(self):
        text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(".cursor/skills/review-prose/SKILL.md", text)
        self.assertIn("review-prose", text)
        self.assertIn("form only", text)
        self.assertIn("present tense", text)
        self.assertIn("check_article.py", text)
        self.assertIn("check_extraction.py", text)
        self.assertIn("article-qa", text)
        self.assertLess(text.find("### 8. Quality gate"), text.find("### 9. Double-check"))
        self.assertLess(text.find("### 9. Double-check"), text.find("### 10. Iterate"))
        self.assertIn("numbered Markdown results tables", text)
        self.assertIn("double-check", text)
        self.assertIn("adjacent-field", text)
        self.assertIn("generic `## Results`", text)

    def test_readme_is_cloneable_and_lists_all_skills(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("github.com/hvianagil-alt/literature-ai-workflow", text)
        self.assertNotIn("<this-repo-url>", text)
        self.assertIn("cd literature-ai-workflow", text)
        self.assertNotIn("cd literature-ai\n", text)
        self.assertIn("Non-commercial", text)
        self.assertIn("double-check", text)
        self.assertIn("article.md", text)
        self.assertIn("ChatGPT", text)
        self.assertIn("Claude", text)
        self.assertIn("Cursor", text)
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("review-prose", agents)
        self.assertIn("article-qa", agents)
        self.assertIn("find-papers", agents)
        self.assertIn("export-manuscript", agents)
        self.assertIn("Table 1", agents)
        self.assertIn("T2D", agents)
        # Skill inventory lives in AGENTS.md, not the researcher README.
        self.assertIn("export-manuscript", agents)
        self.assertEqual(agents.count(".cursor/skills/"), 16)
        self.assertIn("first-conversation", agents)
        self.assertIn("### 0. First conversation", agents)
        self.assertNotIn("graphical-abstract", agents)
        self.assertNotIn("### 9b.", agents)

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
        self.assertIn("review kind", text)
        self.assertIn("topic or argument", text)
        self.assertIn("Table 1", text)
        self.assertIn("generic Results", text)

    def test_article_qa_skill_exists(self):
        text = (ROOT / ".cursor/skills/article-qa/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("check_article.py", text)
        self.assertIn("check_extraction.py", text)
        self.assertIn("not done", text.lower())
        self.assertIn("Table 1", text)
        self.assertIn("no citations", text.lower())
        self.assertIn("Full term (ABBR)", text)
        self.assertIn("glossary", text.lower())
        self.assertIn("thematic", text.lower())
        self.assertIn("Introduction is too short", text)
        self.assertIn("First/Second", text)

    def test_double_check_skill_exists(self):
        text = (ROOT / ".cursor/skills/double-check/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("spot-check", text.lower())
        self.assertIn("article-pass1.md", text)
        self.assertIn("double-check.md", text)
        self.assertIn("Abbreviations", text)
        self.assertIn("glossary", text.lower())
        self.assertIn("adjacent-field", text.lower())
        self.assertIn("generic Results", text)
        self.assertIn(".cursor/skills/double-check/SKILL.md", (ROOT / "AGENTS.md").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "scripts" / "table_from_notes.py").is_file())

    def test_find_papers_skill_exists(self):
        text = (ROOT / ".cursor/skills/find-papers/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("OpenAlex", text)
        self.assertIn("topic_search", text)
        self.assertIn("related_to_seeds", text)
        self.assertIn("find_papers.py", text)
        self.assertIn("Never fabricate", text)
        self.assertIn("contact email", text.lower())
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("find-papers", agents)
        self.assertIn("export-manuscript", agents)
        self.assertIn(".cursor/skills/export-manuscript/SKILL.md", agents)
        self.assertIn("If `papers/` is empty", agents)
        self.assertIn("journal quality", agents.lower())
        self.assertIn("last 6 years", agents)
        self.assertIn("--journal-quality", agents)
        self.assertIn("Seeds vs filters", agents)
        self.assertTrue((ROOT / "scripts" / "find_papers.py").is_file())
        self.assertIn("--journal-quality", text)
        self.assertIn("Seeds vs filters", text)
        related = (ROOT / ".cursor/skills/related-paper-exploration/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("find-papers", related)

    def test_export_manuscript_skill_exists(self):
        text = (ROOT / ".cursor/skills/export-manuscript/SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Times New Roman", text)
        self.assertIn("justified", text.lower())
        self.assertIn("export_manuscript.py", text)
        self.assertIn(".md", text)
        self.assertTrue((ROOT / "scripts" / "export_manuscript.py").is_file())
        self.assertTrue((ROOT / "templates" / "manuscript.css").is_file())

    def test_example_journal_article_passes_short_qa(self):
        import sys

        sys.path.insert(0, str(ROOT / "scripts"))
        import check_article  # noqa: WPS433

        article = (ROOT / "examples" / "sample-article.md").read_text(encoding="utf-8")
        table = (ROOT / "examples" / "literature-table.md").read_text(encoding="utf-8")
        problems = check_article.check(article, table, short=True)
        self.assertEqual(problems, [], problems)


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


class FullScopusRunArticleTests(unittest.TestCase):
    run_dir = ROOT / "review" / "runs" / "2026-09-19-scopus-oa-full"

    def test_article_body_is_journal_length_with_teaching_intro(self):
        text = (self.run_dir / "article.md").read_text(encoding="utf-8")
        body = text.split("## References", 1)[0]
        words = body.split()
        self.assertGreaterEqual(len(words), 6000, "body should be ~20 Word pages")
        intro = body.split("## 1. Introduction", 1)[1].split("## 2. Methods", 1)[0]
        intro_l = intro.lower()
        self.assertIn("incretin", intro_l)
        self.assertIn("automated insulin delivery", intro_l)
        self.assertIn("protease", intro_l)
        self.assertTrue("time in range" in intro_l or "tir" in intro_l)
        self.assertIn("hepatic", intro_l)
        lowered = body.lower()
        for banned in (
            "token estimate",
            "usage-log",
            "unpaywall",
            "oa export",
            "pdfs we could",
            "stands as a testament",
            "evolving landscape",
            "rich tapestry",
        ):
            self.assertNotIn(banned, lowered)
        self.assertNotIn("Additionally,", body)
        import re
        for banned_voice in (
            r"extracted lead",
            r"\bin this set\b",
            r"this introduction is that map",
            r"the paper's job",
            r"extracts used here",
        ):
            self.assertIsNone(re.search(banned_voice, lowered))
        # Claim-first: results sections must not be a stack of "Author et al. did".
        results = body.split("## 3. Clinical incretin use", 1)[1].split("## 7. Discussion", 1)[0]
        et_al_openers = 0
        for para in results.split("\n\n"):
            line = para.strip().split("\n", 1)[0]
            if line.startswith("et al.") or (
                "et al." in line[:80]
                and re.match(r"^[A-Z][a-zA-Z\-]+ et al\.", line)
            ):
                et_al_openers += 1
        self.assertLess(et_al_openers, 4)

    def test_abstract_is_a_topic_map_without_citations(self):
        import re

        text = (self.run_dir / "article.md").read_text(encoding="utf-8")
        title = text.split("\n", 1)[0]
        self.assertIn("narrative review", title.lower())
        abstract = text.split("## Abstract", 1)[1].split("## Keywords", 1)[0]
        self.assertIsNone(re.search(r"\[\d+\]", abstract))
        self.assertNotIn("et al.", abstract.lower())
        self.assertNotIn("MEDI7219", abstract)
        self.assertNotIn("54,972", abstract)
        self.assertIn("incretin", abstract.lower())
        self.assertNotIn("(TIR)", abstract)
        self.assertNotIn("(AID)", abstract)
        self.assertNotIn("(T2D)", abstract)

    def test_pass2_has_in_article_tables_and_claim_ready_worksheet(self):
        text = (self.run_dir / "article.md").read_text(encoding="utf-8")
        table = (self.run_dir / "table" / "literature-table.md").read_text(encoding="utf-8")
        self.assertIn("| Study |", text)
        self.assertIn("Table 1", text)
        self.assertIn("Table 2", text)
        self.assertIn("Table 3", text)
        self.assertNotIn("mechanical first-pass", table.lower())
        self.assertNotIn("extracted lead", table.lower())
        self.assertIn("Claim-ready facts", table)
        self.assertIn("type 2 diabetes (T2D)", text)
        self.assertIn("Type 1 diabetes (T1D)", text)
        self.assertIn("GLP-1 receptor agonist (GLP-1 RA)", text)
        log = (self.run_dir / "double-check.md").read_text(encoding="utf-8")
        self.assertIn("pass 1", log.lower())
        self.assertIn("pass 2", log.lower())
        self.assertIn("Abbreviations", log)


class ReviewCraftStudyTests(unittest.TestCase):
    run_dir = ROOT / "review" / "runs" / "2026-09-19-review-craft-study"
    article = ROOT / "review" / "runs" / "2026-09-19-scopus-oa-full" / "article.md"

    def test_form_only_notes_exist(self):
        readme = (self.run_dir / "README.md").read_text(encoding="utf-8")
        notes = (self.run_dir / "structure-notes.md").read_text(encoding="utf-8")
        for text in (readme, notes):
            self.assertIn("form only", text.lower())
        self.assertIn("Do **not** import", readme)
        self.assertIn("Match kind", notes)
        self.assertIn("present tense", notes.lower())
        self.assertIn("central argument", notes.lower())

    def test_craft_study_findings_were_not_imported_into_manuscript(self):
        text = self.article.read_text(encoding="utf-8")
        for banned in (
            "Jia 2025",
            "Beutler 2026",
            "Bair 2026",
            "Albaghlany",
            "Fabiano 2025",
        ):
            self.assertNotIn(banned, text)


if __name__ == "__main__":
    unittest.main()
