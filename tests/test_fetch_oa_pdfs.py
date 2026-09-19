import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from fetch_oa_pdfs import looks_like_pdf, pdf_urls_from_html  # noqa: E402


class PdfDetectionTests(unittest.TestCase):
    def test_keeps_percent_pdf_header(self):
        self.assertTrue(looks_like_pdf(b"%PDF-1.7 rest", "https://x.example/file"))

    def test_rejects_html_even_at_pdf_url(self):
        html = b"<!DOCTYPE html><html><body>not a pdf</body></html>"
        self.assertFalse(
            looks_like_pdf(html, "https://www.mdpi.com/2077-0383/14/13/4619/pdf")
        )

    def test_rejects_empty(self):
        self.assertFalse(looks_like_pdf(b"", "https://x.example/a.pdf"))


class HtmlPdfLinkTests(unittest.TestCase):
    def test_citation_pdf_url_and_relative_href(self):
        html = """
        <meta name="citation_pdf_url" content="https://pub.example/article.pdf">
        <a href="/2077-0383/14/13/4619/pdf">PDF</a>
        """
        urls = pdf_urls_from_html(html, "https://www.mdpi.com/2077-0383/14/13/4619")
        self.assertIn("https://pub.example/article.pdf", urls)
        self.assertIn("https://www.mdpi.com/2077-0383/14/13/4619/pdf", urls)
