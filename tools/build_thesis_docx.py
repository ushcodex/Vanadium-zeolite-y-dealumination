#!/usr/bin/env python3
"""Build the ABU-formatted thesis .docx from the markdown source in writing/markdown/.

Formatting: A4, 3.8 cm left margin (binding) and 2.5 cm elsewhere,
Times New Roman 12 pt body with double line spacing, 11 pt with 1.15 spacing
for tables and references, APA references with a hanging indent.

Directives understood in the markdown:

    [TITLEPAGE] ... [/TITLEPAGE]   centred title page block
    [FIG: image | caption]         centred image with an 11 pt caption below
    [TBL: caption | a;b;c | ...]   bordered table with an 11 pt caption above
    # / ## / ###                   headings
    **bold**, *italic*             inline emphasis
    lines like  (3.1)              right-aligned equation number

Unicode sub- and superscripts in the source are converted into real Word
sub- and superscript runs so that chemical formulae render properly.
"""

import os
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "writing", "markdown")
FIG = os.path.join(ROOT, "figures")
OUT = os.path.join(ROOT, "deliverables", "Ahmad_Usman_Shehu_U19CE1068_Thesis.docx")

BODY_FONT = "Times New Roman"
BODY_SIZE = Pt(12)
SMALL_SIZE = Pt(11)
TEXT_WIDTH = Cm(14.7)
MAX_FIG_H = Cm(20.0)

FILES = [
    "00_prelims.md",
    "01_chapter1.md",
    "02_chapter2.md",
    "03_chapter3.md",
    "04_chapter4.md",
    "05_chapter5.md",
    "06_references.md",
]

SUB = {
    "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄",
    "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉",
    "+": "₊", "-": "₋", "=": "₌", "(": "₍", ")": "₎",
    "a": "ₐ", "e": "ₑ", "h": "ₕ", "k": "ₖ", "l": "ₗ", "m": "ₘ",
    "n": "ₙ", "o": "ₒ", "p": "ₚ", "s": "ₛ", "t": "ₜ", "x": "ₓ",
}
SUP = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "+": "⁺", "-": "⁻", "=": "⁼", "(": "⁽", ")": "⁾",
    "n": "ⁿ", "i": "ⁱ", "d": "ᵈ", "t": "ᵗ", "o": "ᵒ", "s": "ˢ",
}
REV_SUB = {v: k for k, v in SUB.items()}
REV_SUP = {v: k for k, v in SUP.items()}
# characters that may legitimately appear next to a sub/superscript
NEUTRAL = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
              "+-=()[]{}·.,;:*/%<>=~⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵈᵗᵒˢ"
              "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕₖₗₘₙₒₚₛₜₓ")


# --------------------------------------------------------------------------
# low level helpers
# --------------------------------------------------------------------------
def set_run_font(run, size=BODY_SIZE, bold=False, italic=False,
                 sub=False, sup=False):
    run.font.name = BODY_FONT
    run.font.size = size
    run.font.bold = bold
    run.font.italic = italic
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), BODY_FONT)
    if sub or sup:
        vt = OxmlElement("w:vertAlign")
        vt.set(qn("w:val"), "subscript" if sub else "superscript")
        rpr.append(vt)


def para_spacing(par, size=BODY_SIZE, double=True, before=0, after=0,
                 left=0, hanging=0, first=0):
    pf = par.paragraph_format
    if double:
        pf.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    else:
        pf.line_spacing = 1.15
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.left_indent = Cm(left)
    if hanging:
        pf.first_line_indent = Cm(-hanging)
    elif first:
        pf.first_line_indent = Cm(first)
    return par


def add_field(paragraph, code):
    r1 = paragraph.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    r1._element.append(fld)
    r2 = paragraph.add_run()
    it = OxmlElement("w:instrText")
    it.set(qn("xml:space"), "preserve")
    it.text = code
    r2._element.append(it)
    r3 = paragraph.add_run()
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "separate")
    r3._element.append(fld2)
    placeholder = paragraph.add_run("-")
    r4 = paragraph.add_run()
    fld3 = OxmlElement("w:fldChar")
    fld3.set(qn("w:fldCharType"), "end")
    r4._element.append(fld3)
    return placeholder


def add_page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def figure_key(caption):
    """Sort 'Figure 4.10: ...' after 'Figure 4.9: ...'."""
    m = re.match(r"(Figure|Table)\s+(\d+)\.(\d+)", caption)
    if not m:
        return (0, 0, 0)
    return (int(m.group(2)), int(m.group(3)), 0)


def short_caption(caption):
    """Drop the '| Source: ...' tail for the list of figures and tables."""
    return caption.split("|")[0].strip()


def add_page_number_footer(section):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run_font(p.add_run("- "), size=SMALL_SIZE)
    add_field(p, "PAGE")
    set_run_font(p.add_run(" -"), size=SMALL_SIZE)


def set_table_borders(table):
    tbl = table._tbl
    pr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    pr.append(borders)


def no_row_cant_split(table):
    for row in table.rows:
        trpr = row._tr.get_or_add_trPr()
        el = OxmlElement("w:cantSplit")
        trpr.append(el)


# --------------------------------------------------------------------------
# inline text rendering
# --------------------------------------------------------------------------
def render_inline(par, text, size=BODY_SIZE, base_bold=False, base_italic=False):
    """Write `text` into `par`, handling **bold**, *italic* and Unicode
    sub/superscripts, which are promoted to real Word sub/superscript runs."""
    # tokenise on emphasis markers
    tokens = []
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|\*(?!\s)(.+?)(?<!\s)\*", text):
        if m.start() > pos:
            tokens.append(("plain", text[pos:m.start()]))
        if m.group(1) is not None:
            tokens.append(("bold", m.group(1)))
        else:
            tokens.append(("italic", m.group(2)))
        pos = m.end()
    if pos < len(text):
        tokens.append(("plain", text[pos:]))

    for kind, chunk in tokens:
        parts = re.split(r"([₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₕₖₗₘₙₒₚₛₜₓ]+|"
                         r"[⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵈᵗᵒˢᵟ]+)", chunk)
        for part in parts:
            if not part:
                continue
            if part[0] in REV_SUB:
                r = par.add_run("".join(REV_SUB[c] for c in part))
                set_run_font(r, size=size, bold=base_bold or kind == "bold",
                             italic=base_italic or kind == "italic", sub=True)
            elif part[0] in REV_SUP:
                mapped = "".join(REV_SUP.get(c, c) for c in part)
                r = par.add_run(mapped)
                set_run_font(r, size=size, bold=base_bold or kind == "bold",
                             italic=base_italic or kind == "italic", sup=True)
            else:
                r = par.add_run(part)
                set_run_font(r, size=size, bold=base_bold or kind == "bold",
                             italic=base_italic or kind == "italic")
    return par


# --------------------------------------------------------------------------
# block renderers
# --------------------------------------------------------------------------
def render_titlepage(doc, lines):
    for i, raw in enumerate(lines):
        line = raw.strip()
        if not line:
            continue
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para_spacing(p, before=0, after=6)
        r = p.add_run(line)
        if i == 0:
            set_run_font(r, size=Pt(14), bold=True)
        elif line.isupper() and len(line) > 25:
            set_run_font(r, size=Pt(12), bold=True)
        else:
            set_run_font(r, size=BODY_SIZE, bold=line.startswith(("BY", "Ahmad")))
    add_page_break(doc)


def render_figure(doc, path, caption):
    full = os.path.join(FIG, path)
    if not os.path.exists(full):
        full = os.path.join(ROOT, path)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_spacing(p, double=False, before=6, after=4)
    if os.path.exists(full):
        from PIL import Image
        with Image.open(full) as im:
            w, h = im.size
        width_cm = w / 96 * 2.54
        height_cm = h / 96 * 2.54
        scale = min(1.0, TEXT_WIDTH.cm / width_cm, MAX_FIG_H.cm / height_cm)
        p.add_run().add_picture(full, width=Cm(width_cm * scale))
    else:
        r = p.add_run(f"[missing image: {path}]")
        set_run_font(r, size=SMALL_SIZE, italic=True)
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para_spacing(cap, double=False, before=0, after=12)
    render_inline(cap, caption, size=SMALL_SIZE)
    return caption


def render_table(doc, caption, rows):
    cap = doc.add_paragraph()
    para_spacing(cap, double=False, before=12, after=4)
    cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    render_inline(cap, caption, size=SMALL_SIZE)

    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=0, cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = True
    set_table_borders(table)
    no_row_cant_split(table)

    for ri, row in enumerate(rows):
        cells = table.add_row().cells
        for ci in range(ncols):
            txt = row[ci] if ci < len(row) else ""
            cell = cells[ci]
            cell.text = ""
            p = cell.paragraphs[0]
            para_spacing(p, double=False, before=2, after=2)
            render_inline(p, txt, size=SMALL_SIZE, base_bold=(ri == 0))
    # column widths
    total = TEXT_WIDTH.cm
    for ci in range(ncols):
        for row in table.rows:
            row.cells[ci].width = Cm(total / ncols)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    return caption


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def build():
    doc = Document()

    st = doc.styles["Normal"]
    st.font.name = BODY_FONT
    st.font.size = BODY_SIZE
    st.element.rPr.rFonts.set(qn("w:eastAsia"), BODY_FONT)

    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.left_margin = Cm(3.8)
    sec.right_margin = Cm(2.5)
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)
    add_page_number_footer(sec)

    figures, tables = [], []

    for fname in FILES:
        path = os.path.join(MD, fname)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        lines = text.splitlines()
        in_title = False
        title_buf = []
        i = 0
        prev_par = None
        while i < len(lines):
            raw = lines[i]
            line = raw.strip()
            i += 1

            if line == "[TITLEPAGE]":
                in_title = True
                title_buf = []
                continue
            if line == "[/TITLEPAGE]":
                render_titlepage(doc, title_buf)
                in_title = False
                continue
            if in_title:
                title_buf.append(raw)
                continue

            if not line:
                continue

            if line.startswith("# REFERENCES"):
                add_page_break(doc)
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para_spacing(p, before=0, after=12)
                set_run_font(p.add_run("REFERENCES"), size=Pt(14), bold=True)
                continue

            # ---- headings -------------------------------------------------
            if line.startswith("### "):
                p = doc.add_paragraph()
                para_spacing(p, before=10, after=6)
                render_inline(p, line[4:], base_bold=True)
                prev_par = None
                continue
            if line.startswith("## "):
                p = doc.add_paragraph()
                para_spacing(p, before=14, after=6)
                render_inline(p, line[3:], base_bold=True)
                prev_par = None
                continue
            if line.startswith("# "):
                add_page_break(doc)
                head = line[2:]
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para_spacing(p, before=24, after=10)
                set_run_font(p.add_run(head), size=Pt(14), bold=True)
                prev_par = None
                continue

            # ---- figures --------------------------------------------------
            m = re.match(r"^\[FIG:\s*([^\|]+?)\s*\|\s*(.+?)\s*\]$", line)
            if m:
                cap = render_figure(doc, m.group(1).strip(),
                        m.group(2).strip().replace(" | Source:", ". Source:"))
                figures.append(cap)
                prev_par = None
                continue

            # ---- tables ---------------------------------------------------
            m = re.match(r"^\[TBL:\s*(.+?)\s*\]$", line)
            if m:
                fields = [f.strip() for f in m.group(1).split("|")]
                caption = fields[0]
                rows = [[c.strip() for c in f.split(";")] for f in fields[1:]]
                cap = render_table(doc, caption, rows)
                tables.append(cap)
                prev_par = None
                continue

            # ---- equation numbers ----------------------------------------
            if re.fullmatch(r"\(\d+\.\d+\)", line):
                if prev_par is not None:
                    prev_par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    prev_par.paragraph_format.space_after = Pt(0)
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                para_spacing(p, before=0, after=12)
                set_run_font(p.add_run(line))
                prev_par = None
                continue

            # ---- lists ----------------------------------------------------
            m = re.match(r"^(\d+)\.\s+(.*)$", line)
            if m:
                p = doc.add_paragraph()
                para_spacing(p, after=6, left=1.27, hanging=0.63)
                render_inline(p, f"{m.group(1)}. {m.group(2)}")
                prev_par = p
                continue
            if line.startswith("- "):
                p = doc.add_paragraph()
                para_spacing(p, after=6, left=1.27, hanging=0.63)
                render_inline(p, "- " + line[2:])
                prev_par = p
                continue

            # ---- references (hanging indent, 11 pt, 1.15) ------------------
            if path.endswith("06_references.md") and re.match(r"^[A-Z][a-z]+,", line):
                p = doc.add_paragraph()
                para_spacing(p, double=False, after=6, left=1.27, hanging=1.27)
                render_inline(p, line, size=SMALL_SIZE)
                prev_par = p
                continue

            # ---- ordinary paragraph ---------------------------------------
            p = doc.add_paragraph()
            para_spacing(p, after=10, first=1.27)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            render_inline(p, line)
            prev_par = p

    return doc, figures, tables


def build_final():
    doc, figures, tables = build()

    # Move everything after the title page down, then write contents.
    # python-docx has no insert-at-index, so build the front matter into a
    # second document body fragment by manipulating XML directly.
    body = doc.element.body
    # locate end of title page = first page-break paragraph after title page
    # Simplest robust approach: find the paragraph containing the first
    # page break following the title page block, then insert before it.
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br"
    br_paras = []
    for p in doc.paragraphs:
        for r in p.runs:
            if r._element.findall(W):
                br_paras.append(p)
                break

    def make_front():
        """Create the contents/list pages as a list of elements."""
        els = []

        def heading(text):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para_spacing(p, before=0, after=12)
            set_run_font(p.add_run(text), size=Pt(14), bold=True)
            els.append(p._element)

        lead = doc.add_paragraph()
        lead.add_run().add_break(WD_BREAK.PAGE)
        els.append(lead._element)

        def spacer(pts=6):
            p = doc.add_paragraph()
            para_spacing(p, before=0, after=pts)
            els.append(p._element)

        heading("TABLE OF CONTENTS")
        p = doc.add_paragraph()
        add_field(p, r'TOC \o "1-2" \h \z \u')
        els.append(p._element)
        note = doc.add_paragraph()
        note.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_run_font(note.add_run("If no page numbers appear, right-click the "
                                  "field above and choose Update Field."),
                     size=SMALL_SIZE, italic=True)
        els.append(note._element)
        spacer()

        heading("LIST OF FIGURES")
        for cap in sorted(figures, key=figure_key):
            p = doc.add_paragraph()
            para_spacing(p, before=0, after=4)
            render_inline(p, short_caption(cap), size=SMALL_SIZE)
            els.append(p._element)
        spacer()

        heading("LIST OF TABLES")
        for cap in sorted(tables, key=figure_key):
            p = doc.add_paragraph()
            para_spacing(p, before=0, after=4)
            render_inline(p, short_caption(cap), size=SMALL_SIZE)
            els.append(p._element)

        return els

    front = make_front()
    # insert the contents pages between the abstract and CHAPTER ONE
    anchor = None
    for p in doc.paragraphs:
        if p.text.strip() == "CHAPTER ONE":
            anchor = p._element.getprevious()
            break
    if anchor is None:
        anchor = br_paras[-1]._element
    for el in front:
        anchor.addprevious(el)
    # put a page break between the front matter and the declaration
    pb = doc.add_paragraph()
    pb.add_run().add_break(WD_BREAK.PAGE)
    anchor.addprevious(pb._element)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc.save(OUT)
    print(f"wrote {OUT}")
    print(f"  figures: {len(figures)}   tables: {len(tables)}")


if __name__ == "__main__":
    build_final()
