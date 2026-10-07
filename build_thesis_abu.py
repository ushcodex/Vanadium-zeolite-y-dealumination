#!/usr/bin/env python3
"""Build the final thesis document in the ABU house format.

Formatting implemented from the Ahmadu Bello University postgraduate and
undergraduate project report conventions and the department's stated rules:

  * A4 paper, 1.5 inch binding margin on the left, 1 inch elsewhere
  * Times New Roman 12 pt, justified, double line spacing for body text
  * Chapter headings centred, bold, upper case, 14 pt
  * Section headings bold left aligned 12 pt, subsection headings bold italic
  * Tables and their captions 11 pt, single spacing
  * References 11 pt with a hanging indent of 0.5 inch, single spacing
  * Figures centred with an 11 pt caption below, numbered by chapter
  * Page numbers centred in the footer

Input : writing/thesis_src/*.md, figures/
Output: deliverables/thesis_ABU.docx
"""
import os
import re
import glob
import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = "/home/user/Vanadium-zeolite-y-dealumination"
SRC = os.path.join(ROOT, "writing", "thesis_src")
OUT = os.path.join(ROOT, "deliverables", "thesis_ABU.docx")
FONT = "Times New Roman"

CHAPTER_FILES = [
    "prelims.md",
    "ch1_introduction.md",
    "ch2_literature_review.md",
    "ch3_methodology.md",
    "ch4_results.md",
    "ch5_conclusions.md",
    "references.md",
]


# --------------------------------------------------------------- docx helpers
def set_base_style(doc):
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(12)
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), FONT)
    pf = st.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    pf.space_after = Pt(6)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY


def page_setup(doc):
    for s in doc.sections:
        s.page_height = Inches(11.69)
        s.page_width = Inches(8.27)
        s.left_margin = Inches(1.5)
        s.right_margin = Inches(1.0)
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)


def add_page_number_footer(section):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._r.addnext(fld)


def run_fmt(run, size=12, bold=False, italic=False, sup=False, sub=False,
            font=FONT):
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.superscript = sup
    run.font.subscript = sub
    rpr = run._element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), font)
    return run


SUP = {"\u2070": "0", "\u00b9": "1", "\u00b2": "2", "\u00b3": "3",
       "\u2074": "4", "\u2075": "5", "\u2076": "6", "\u2077": "7",
       "\u2078": "8", "\u2079": "9", "\u207b": "-", "\u207a": "+"}
SUB = {"\u2080": "0", "\u2081": "1", "\u2082": "2", "\u2083": "3",
       "\u2084": "4", "\u2085": "5", "\u2086": "6", "\u2087": "7",
       "\u2088": "8", "\u2089": "9"}


def add_rich(par, text, size=12, bold=False, italic=False):
    """Write text, turning unicode super/subscripts into real formatting."""
    i = 0
    buf = ""
    mode = None
    while i < len(text):
        c = text[i]
        if c in SUP:
            if mode != "sup":
                if buf:
                    run_fmt(par.add_run(buf), size, bold, italic, mode == "sup", mode == "sub")
                buf, mode = "", "sup"
            buf += SUP[c]
        elif c in SUB:
            if mode != "sub":
                if buf:
                    run_fmt(par.add_run(buf), size, bold, italic, mode == "sup", mode == "sub")
                buf, mode = "", "sub"
            buf += SUB[c]
        else:
            if mode:
                run_fmt(par.add_run(buf), size, bold, italic, mode == "sup", mode == "sub")
                buf, mode = "", None
            buf += c
        i += 1
    if buf:
        run_fmt(par.add_run(buf), size, bold, italic, mode == "sup", mode == "sub")


def add_md_runs(par, text, size=12, base_bold=False):
    """Handle **bold** and *italic* inline markdown."""
    for part in re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            add_rich(par, part[2:-2], size, bold=True)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            add_rich(par, part[1:-1], size, italic=True)
        else:
            add_rich(par, part, size, bold=base_bold)


def body_par(doc, text, size=12, spacing="double", indent_first=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing_rule = (WD_LINE_SPACING.DOUBLE if spacing == "double"
                            else WD_LINE_SPACING.SINGLE)
    pf.space_after = Pt(6 if spacing == "double" else 2)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent_first:
        pf.first_line_indent = Inches(0.5)
    add_md_runs(p, text, size)
    return p


def heading(doc, text, level):
    if level == 1:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        add_rich(p, text.upper(), 14, bold=True)
    elif level == 2:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        add_md_runs(p, text, 12, base_bold=True)
    else:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        add_md_runs(p, text, 12, base_bold=True)
    return p


def add_figure(doc, path, caption):
    if not os.path.exists(path):
        print("  ! missing figure:", path)
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    p.add_run().add_picture(path, width=Inches(5.4))
    c = doc.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(12)
    c.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    add_md_runs(c, caption, 11)


def add_table(doc, rows, caption):
    """rows[0] is the header. caption is placed above the table."""
    if caption:
        c = doc.add_paragraph()
        c.paragraph_format.space_before = Pt(12)
        c.paragraph_format.space_after = Pt(4)
        c.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        add_md_runs(c, caption, 11)
    t = doc.add_table(rows=0, cols=len(rows[0]))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_i, row in enumerate(rows):
        cells = t.add_row().cells
        for c_i, val in enumerate(row):
            par = cells[c_i].paragraphs[0]
            par.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            par.paragraph_format.space_after = Pt(1)
            par.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_rich(par, val.strip(), 11, bold=(r_i == 0))
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(10)
    sp.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    return t


# ------------------------------------------------------------ markdown reader
IMG = re.compile(r"^!\[(.*?)\]\((.*?)\)\s*$")
H = re.compile(r"^(#{1,4})\s+(.*)$")
TBL_SEP = re.compile(r"^\|?[\s:\-|]+\|[\s:\-|]*$")


def is_table_row(line):
    st = line.strip()
    return (st.startswith("|") and st.endswith("|") and st.count("|") >= 2
            and len(st) > 2)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def render_markdown(doc, text, references=False):
    lines = text.split("\n")
    i = 0
    table_caption = None
    centring = False
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(8)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_rich(p, "\n".join(buf), 10)
            for r in p.runs:
                r.font.name = "Consolas"
            continue

        # horizontal rule
        if re.match(r"^-{3,}$", stripped):
            i += 1
            continue

        # image
        m = IMG.match(stripped)
        if m:
            cap, path = m.group(1), m.group(2)
            add_figure(doc, os.path.join(ROOT, path), cap)
            i += 1
            continue

        # heading
        m = H.match(stripped)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if level == 2:
                centring = title.upper() == "TITLE PAGE"
            heading(doc, title, level)
            i += 1
            continue

        # table
        if is_table_row(stripped):
            rows = []
            while i < len(lines) and is_table_row(lines[i].strip()):
                if not TBL_SEP.match(lines[i].strip()):
                    rows.append(split_row(lines[i]))
                i += 1
            # the caption is the paragraph immediately after the table
            cap = ""
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"^Table\s+\d", lines[j].strip()):
                cap = lines[j].strip()
                i = j + 1
            add_table(doc, rows, cap)
            continue

        if references:
            if stripped and not stripped.startswith("#"):
                rp = doc.add_paragraph()
                rf = rp.paragraph_format
                rf.line_spacing_rule = WD_LINE_SPACING.SINGLE
                rf.space_after = Pt(10)
                rf.alignment = WD_ALIGN_PARAGRAPH.LEFT
                rf.left_indent = Inches(0.5)
                rf.first_line_indent = Inches(-0.5)
                add_md_runs(rp, stripped, 11)
                i += 1
                continue

        if centring and not stripped.startswith("Table ") and not stripped.startswith("|"):
            cp = body_par(doc, stripped)
            cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            i += 1
            continue

        body_par(doc, stripped)
        i += 1


def add_page_break(doc):
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


# ---------------------------------------------------------------------- build
def main():
    doc = Document()
    set_base_style(doc)
    page_setup(doc)
    add_page_number_footer(doc.sections[0])

    first = True
    for fn in CHAPTER_FILES:
        path = os.path.join(SRC, fn)
        if not os.path.exists(path):
            print("missing chapter file:", path)
            continue
        if not first:
            add_page_break(doc)
        first = False
        text = open(path, encoding="utf-8").read()
        print("rendering", fn, "(%d chars)" % len(text))
        render_markdown(doc, text, references=(fn == "references.md"))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print("\nwrote", OUT)


if __name__ == "__main__":
    main()
