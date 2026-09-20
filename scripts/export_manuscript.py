#!/usr/bin/env python3
"""Export article.md to HTML (always) and optionally Word/PDF via Pandoc.

HTML uses Times New Roman and justified body text so a browser Print-to-PDF
works without extra software. DOCX/PDF require pandoc on PATH.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

CSS = """
@page { margin: 2.5cm; }
body {
  font-family: "Times New Roman", "Liberation Serif", Times, serif;
  font-size: 12pt;
  line-height: 1.5;
  text-align: justify;
  max-width: 16.5cm;
  margin: 2cm auto;
  color: #111;
}
h1, h2, h3, h4 { text-align: left; font-weight: bold; line-height: 1.25; }
h1 { font-size: 16pt; }
h2 { font-size: 14pt; margin-top: 1.4em; }
h3 { font-size: 12pt; font-style: italic; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; margin: 1em 0; text-align: left; }
th, td { border: 1px solid #333; padding: 0.3em 0.45em; vertical-align: top; }
th { background: #f3f3f3; }
code, pre { font-family: "Times New Roman", Times, serif; font-size: 11pt; }
blockquote { margin-left: 1.5em; font-style: italic; }
"""


def md_inline(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def markdown_to_html(md: str, title: str) -> str:
    lines = md.splitlines()
    out: list[str] = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="utf-8">',
        f"<title>{html.escape(title)}</title>",
        f"<style>{CSS}</style>",
        "</head>",
        "<body>",
    ]
    i = 0
    in_list = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+:?", lines[i + 1]):
            if in_list:
                out.append("</ul>")
                in_list = False
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i])
                i += 1
            body_rows = [r for r in rows if not re.match(r"^\s*\|?\s*:?-+", r)]
            if body_rows:
                out.append("<table>")
                for n, row in enumerate(body_rows):
                    cells = [c.strip() for c in row.strip().strip("|").split("|")]
                    tag = "th" if n == 0 else "td"
                    out.append("<tr>" + "".join(f"<{tag}>{md_inline(c)}</{tag}>" for c in cells) + "</tr>")
                out.append("</table>")
            continue
        if re.match(r"^#{1,4}\s+", line):
            if in_list:
                out.append("</ul>")
                in_list = False
            hashes, rest = re.match(r"^(#{1,4})\s+(.*)$", line).groups()
            level = len(hashes)
            out.append(f"<h{level}>{md_inline(rest)}</h{level}>")
            i += 1
            continue
        if re.match(r"^[-*]\s+", line):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{md_inline(re.sub(r'^[-*]\s+', '', line))}</li>")
            i += 1
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if not line.strip():
            i += 1
            continue
        para = [line]
        i += 1
        while (
            i < len(lines)
            and lines[i].strip()
            and not lines[i].startswith("#")
            and not lines[i].startswith("|")
            and not re.match(r"^[-*]\s+", lines[i])
        ):
            para.append(lines[i])
            i += 1
        out.append("<p>" + md_inline(" ".join(para)) + "</p>")
    if in_list:
        out.append("</ul>")
    out.extend(["</body>", "</html>"])
    return "\n".join(out)


def style_docx(path: Path) -> None:
    """Force Times New Roman 12 pt and justified body in a Pandoc .docx."""
    try:
        from docx import Document
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        from docx.oxml.ns import qn
        from docx.shared import Pt
    except ImportError:
        return
    doc = Document(path)
    for style in doc.styles:
        try:
            font = style.font
            font.name = "Times New Roman"
            rpr = style.element.get_or_add_rPr()
            rfonts = rpr.find(qn("w:rFonts"))
            if rfonts is None:
                from docx.oxml import OxmlElement

                rfonts = OxmlElement("w:rFonts")
                rpr.append(rfonts)
            rfonts.set(qn("w:ascii"), "Times New Roman")
            rfonts.set(qn("w:hAnsi"), "Times New Roman")
            rfonts.set(qn("w:cs"), "Times New Roman")
            if style.name == "Normal":
                font.size = Pt(12)
        except (AttributeError, ValueError, KeyError):
            continue
    for para in doc.paragraphs:
        name = (para.style.name if para.style is not None else "") or ""
        if name.startswith("Heading"):
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        else:
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    doc.save(path)


def write_pdf_from_html(html_path: Path, dest: Path) -> str | None:
    try:
        from weasyprint import HTML
    except ImportError:
        return "weasyprint is not installed"
    try:
        HTML(filename=str(html_path)).write_pdf(str(dest))
    except Exception as exc:  # noqa: BLE001 — surface engine errors to the CLI
        return str(exc)
    return None


def run_pandoc(src: Path, dest: Path) -> str | None:
    if not shutil.which("pandoc"):
        return "pandoc is not installed"
    args = [
        "pandoc",
        str(src),
        "-o",
        str(dest),
        "-f",
        "markdown",
        "--standalone",
        "-V",
        "mainfont=Times New Roman",
        "-V",
        "fontsize=12pt",
        "-V",
        "geometry:margin=2.5cm",
    ]
    if dest.suffix.lower() == ".html":
        args.extend(["--css", str(Path(__file__).resolve().parents[1] / "templates" / "manuscript.css")])
    try:
        subprocess.run(args, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:
        return exc.stderr or str(exc)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--format", default="html", help="comma list: html,docx,pdf")
    args = parser.parse_args()
    src = Path(args.article)
    if not src.is_file():
        print(f"FAIL missing article: {src}", file=sys.stderr)
        return 2
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    wanted = [p.strip().lower() for p in args.format.split(",") if p.strip()]
    md = src.read_text(encoding="utf-8")
    title = src.stem
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        title = m.group(1).strip()
    stem = src.stem
    ok = []
    fail = []
    html_path = out_dir / f"{stem}.html"
    if "html" in wanted or "pdf" in wanted:
        # Built-in HTML is self-contained (Times + justify). Pandoc HTML
        # only links an external CSS file and fails the style checks.
        html_path.write_text(markdown_to_html(md, title), encoding="utf-8")
        if "html" in wanted:
            ok.append(str(html_path))
    for fmt in wanted:
        if fmt == "html":
            continue
        dest = out_dir / f"{stem}.{fmt}"
        if fmt == "pdf":
            err = write_pdf_from_html(html_path, dest) if html_path.is_file() else "HTML missing"
            if err:
                err = run_pandoc(src, dest) or err
            if err and not dest.is_file():
                fail.append(f"{fmt}: {err}")
            else:
                ok.append(str(dest))
            continue
        err = run_pandoc(src, dest)
        if err:
            fail.append(f"{fmt}: {err}")
            continue
        if fmt == "docx":
            style_docx(dest)
        ok.append(str(dest))
    print("OK " + ", ".join(ok) if ok else "FAIL no files written")
    for item in fail:
        print(f"SKIP {item}", file=sys.stderr)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
