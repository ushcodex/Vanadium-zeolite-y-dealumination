#!/usr/bin/env python3
"""Build the ABU undergraduate thesis from writing/markdown/*.md.

The builder applies the supplied department format and the supervisor's specific
heading correction: chapter headings retain a left-aligned ``x.0 TITLE`` line
beneath a centered ``CHAPTER ONE`` label. It creates separately numbered
preliminary and main-text sections, plus dynamic contents and caption lists.
Update Word fields before printing (Ctrl+A, then F9).

Run from any directory with:
    python3 tools/build_thesis_docx.py

Outputs:
    deliverables/thesis_ABU.docx
    deliverables/Ahmad_Usman_Shehu_U19CE1068_Thesis.docx (identical compatibility copy)
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.enum.text import (
    WD_ALIGN_PARAGRAPH,
    WD_TAB_ALIGNMENT,
    WD_LINE_SPACING,
)
from docx.shared import Cm, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "writing" / "markdown"
FIGURE_DIR = ROOT / "figures"
DELIVERABLE_DIR = ROOT / "deliverables"
OUT = DELIVERABLE_DIR / "thesis_ABU.docx"
COMPAT_OUT = DELIVERABLE_DIR / "Ahmad_Usman_Shehu_U19CE1068_Thesis.docx"

FONT = "Times New Roman"
BODY_SIZE = 12
PAGE_WIDTH_CM = 21.0
LEFT_MARGIN_CM = 3.5
RIGHT_MARGIN_CM = 2.5
TEXT_WIDTH_CM = PAGE_WIDTH_CM - LEFT_MARGIN_CM - RIGHT_MARGIN_CM
MAX_FIGURE_HEIGHT_CM = 20.0

FILES = [
    "00_prelims.md",
    "01_chapter1.md",
    "02_chapter2.md",
    "03_chapter3.md",
    "04_chapter4.md",
    "05_chapter5.md",
    "06_references.md",
    "07_appendices.md",
]

HEADING_RE = re.compile(r"^(#{1,4})\s+(.*)$")
FIGURE_RE = re.compile(r"^\[FIG:\s*([^|]+?)\s*\|\s*(.+?)\s*\]$")
TABLE_RE = re.compile(r"^\[TBL:\s*(.+?)\s*\]$")
TABLE_ROW_RE = re.compile(r"^\|([^|].*\|)+$")
EQUATION_NUMBER_RE = re.compile(r"^\((?:\d+|[A-Z])\.\d+\)$")
SCRIPT_RE = re.compile(r"([_^])\{([^{}]+)\}")

SUBSCRIPT = {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
    "₊": "+", "₋": "-", "₌": "=", "₍": "(", "₎": ")",
    "ₐ": "a", "ₑ": "e", "ₕ": "h", "ₖ": "k", "ₗ": "l",
    "ₘ": "m", "ₙ": "n", "ₒ": "o", "ₚ": "p", "ₛ": "s",
    "ₜ": "t", "ₓ": "x", "ᵢ": "i", "ⱼ": "j",
}
SUPERSCRIPT = {
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
    "⁺": "+", "⁻": "-", "⁼": "=", "⁽": "(", "⁾": ")",
    "ⁿ": "n", "ⁱ": "i", "ᵈ": "d", "ᵗ": "t", "ᵒ": "o", "ˢ": "s",
}


@dataclass(frozen=True)
class CaptionRecord:
    kind: str
    caption: str
    bookmark: str


def set_run_font(run, *, size=BODY_SIZE, bold=False, italic=False,
                 sub=False, sup=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)
    if sub or sup:
        vert = rpr.find(qn("w:vertAlign"))
        if vert is None:
            vert = OxmlElement("w:vertAlign")
            rpr.append(vert)
        vert.set(qn("w:val"), "subscript" if sub else "superscript")
    return run


def set_style_font(style, *, size=BODY_SIZE, bold=False, italic=False):
    style.font.name = FONT
    style.font.size = Pt(size)
    style.font.bold = bold
    style.font.italic = italic
    style.font.color.rgb = RGBColor(0, 0, 0)
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def configure_document(doc):
    section = doc.sections[0]
    section.page_width = Cm(PAGE_WIDTH_CM)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(LEFT_MARGIN_CM)
    section.right_margin = Cm(RIGHT_MARGIN_CM)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.different_first_page_header_footer = True

    normal = doc.styles["Normal"]
    set_style_font(normal)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(12)
    normal.paragraph_format.first_line_indent = Cm(0)
    normal.paragraph_format.widow_control = True

    heading_specs = {
        1: (True, False, 18, 12, WD_ALIGN_PARAGRAPH.LEFT),
        2: (True, False, 12, 6, WD_ALIGN_PARAGRAPH.LEFT),
        3: (False, False, 8, 4, WD_ALIGN_PARAGRAPH.LEFT),
        4: (False, True, 8, 4, WD_ALIGN_PARAGRAPH.LEFT),
    }
    for level, (bold, italic, before, after, alignment) in heading_specs.items():
        style = doc.styles[f"Heading {level}"]
        set_style_font(style, bold=bold, italic=italic)
        pf = style.paragraph_format
        pf.alignment = alignment
        pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
        pf.space_before = Pt(before)
        pf.space_after = Pt(after)
        pf.first_line_indent = Cm(0)
        pf.keep_with_next = True
        pf.keep_together = True
        pf.widow_control = True

    # Keep headings black and disable Word's automatic blue heading colour.
    settings = doc.settings.element
    update_fields = settings.find(qn("w:updateFields"))
    if update_fields is None:
        update_fields = OxmlElement("w:updateFields")
        settings.append(update_fields)
    update_fields.set(qn("w:val"), "true")

    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    footer.paragraph_format.space_after = Pt(0)


def set_section_page_numbering(section, number_format, start=1):
    """Set the page-number format and restart value for a document section."""
    sect_pr = section._sectPr
    page_numbering = sect_pr.find(qn("w:pgNumType"))
    if page_numbering is None:
        page_numbering = OxmlElement("w:pgNumType")
        children = list(sect_pr)
        insert_at = next((i for i, child in enumerate(children)
                          if child.tag in {qn("w:cols"), qn("w:titlePg"),
                                           qn("w:docGrid")}), len(children))
        sect_pr.insert(insert_at, page_numbering)
    page_numbering.set(qn("w:fmt"), number_format)
    page_numbering.set(qn("w:start"), str(start))


def add_field(paragraph, instruction, *, placeholder=""):
    """Insert an updateable Word field and mark it dirty for recalculation."""
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    begin.set(qn("w:dirty"), "true")
    run._r.append(begin)

    run = paragraph.add_run()
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = instruction
    run._r.append(instr)

    run = paragraph.add_run()
    separate = OxmlElement("w:fldChar")
    separate.set(qn("w:fldCharType"), "separate")
    run._r.append(separate)

    if placeholder:
        set_run_font(paragraph.add_run(placeholder), size=BODY_SIZE)

    run = paragraph.add_run()
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(end)
    return paragraph


def inline_tokens(text):
    """Yield (text, bold, italic) segments from a small Markdown subset."""
    text = text.replace("&amp;", "&")
    pos = 0
    for match in re.finditer(r"\*\*(.+?)\*\*|\*(?!\s)(.+?)(?<!\s)\*", text):
        if match.start() > pos:
            yield text[pos:match.start()], False, False
        if match.group(1) is not None:
            yield match.group(1), True, False
        else:
            yield match.group(2), False, True
        pos = match.end()
    if pos < len(text):
        yield text[pos:], False, False


def render_inline(paragraph, text, *, size=BODY_SIZE, base_bold=False,
                  base_italic=False):
    def render_plain(chunk, bold, italic):
        if not chunk:
            return
        idx = 0
        plain = []
        mode = None

        def flush():
            nonlocal plain, mode
            if not plain:
                return
            value = "".join(plain)
            rendered = "".join(SUBSCRIPT.get(c, c) for c in value) if mode == "sub" else value
            rendered = "".join(SUPERSCRIPT.get(c, c) for c in rendered) if mode == "sup" else rendered
            run = paragraph.add_run(rendered)
            set_run_font(run, size=size, bold=base_bold or bold,
                         italic=base_italic or italic,
                         sub=mode == "sub", sup=mode == "sup")
            plain = []

        while idx < len(chunk):
            char = chunk[idx]
            next_mode = "sub" if char in SUBSCRIPT else "sup" if char in SUPERSCRIPT else None
            if next_mode != mode:
                flush()
                mode = next_mode
            plain.append(char)
            idx += 1
        flush()

    for chunk, bold, italic in inline_tokens(text):
        position = 0
        for match in SCRIPT_RE.finditer(chunk):
            render_plain(chunk[position:match.start()], bold, italic)
            run = paragraph.add_run(match.group(2))
            set_run_font(run, size=size, bold=base_bold or bold,
                         italic=base_italic or italic,
                         sub=match.group(1) == "_",
                         sup=match.group(1) == "^")
            position = match.end()
        render_plain(chunk[position:], bold, italic)
    return paragraph


def set_body_paragraph(paragraph, *, references=False, single=False,
                       after=12, left_indent=0, hanging=0):
    pf = paragraph.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE if single else WD_LINE_SPACING.DOUBLE
    pf.space_before = Pt(0)
    pf.space_after = Pt(after)
    pf.first_line_indent = Cm(-hanging) if hanging else Cm(0)
    pf.left_indent = Cm(left_indent)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT if references else WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.widow_control = True
    return paragraph


def add_bookmark(paragraph, name, bookmark_id):
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bookmark_id))
    start.set(qn("w:name"), name)
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bookmark_id))
    ppr = paragraph._p.pPr
    if ppr is not None:
        ppr.addnext(start)
    else:
        paragraph._p.insert(0, start)
    paragraph._p.append(end)


def bookmark_name(kind, caption):
    match = re.search(r"(Figure|Table)\s+(\d+)\.(\d+)", caption)
    if match:
        return f"{match.group(1)}_{match.group(2)}_{match.group(3)}"
    safe = re.sub(r"[^A-Za-z0-9_]", "_", caption)[:24]
    return f"{kind}_{safe}"


def strip_source(caption):
    return caption.split("| Source:", 1)[0].strip()


def caption_records(source_texts):
    records = []
    used = set()
    for name in FILES:
        text = source_texts[name]
        for raw in text.splitlines():
            line = raw.strip()
            fig = FIGURE_RE.match(line)
            tbl = TABLE_RE.match(line)
            if fig:
                caption = fig.group(2).strip()
                kind = "Figure"
            elif tbl:
                fields = [field.strip() for field in tbl.group(1).split("|")]
                caption = fields[0]
                kind = "Table"
            else:
                continue
            mark = bookmark_name(kind, caption)
            if mark in used:
                raise ValueError(f"Duplicate caption bookmark: {mark}")
            used.add(mark)
            records.append(CaptionRecord(kind, caption, mark))
    return records


def split_table_row(line):
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def set_table_borders(table):
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        item = OxmlElement(f"w:{edge}")
        item.set(qn("w:val"), "single")
        item.set(qn("w:sz"), "4")
        item.set(qn("w:space"), "0")
        item.set(qn("w:color"), "000000")
        borders.append(item)
    table._tbl.tblPr.append(borders)


def prevent_row_split(table):
    for row in table.rows:
        trpr = row._tr.get_or_add_trPr()
        cant_split = OxmlElement("w:cantSplit")
        trpr.append(cant_split)


def mark_repeat_header(row):
    trpr = row._tr.get_or_add_trPr()
    table_header = OxmlElement("w:tblHeader")
    table_header.set(qn("w:val"), "true")
    trpr.append(table_header)


class ThesisBuilder:
    def __init__(self):
        self.doc = Document()
        configure_document(self.doc)
        self.bookmark_id = 1
        self.caption_lookup = {}
        self.last_paragraph = None
        self.in_title = False
        self.title_lines = []
        self.suppress_next_heading_page_break = False

    def start_page_numbered_section(self, number_format, field_instruction):
        section = self.doc.add_section(WD_SECTION.NEW_PAGE)
        section.different_first_page_header_footer = False
        section.header.is_linked_to_previous = False
        section.footer.is_linked_to_previous = False
        set_section_page_numbering(section, number_format, start=1)

        footer = section.footer.paragraphs[0]
        for run in list(footer.runs):
            footer._p.remove(run._r)
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        footer.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        footer.paragraph_format.space_after = Pt(0)
        footer.paragraph_format.first_line_indent = Cm(0)
        add_field(footer, field_instruction)
        self.suppress_next_heading_page_break = True
        return section

    def add_paragraph(self, text="", *, style=None, alignment=None, after=12,
                      single=False, references=False, left_indent=0, hanging=0,
                      size=BODY_SIZE, bold=False, italic=False):
        paragraph = self.doc.add_paragraph(style=style)
        set_body_paragraph(paragraph, references=references, single=single,
                           after=after, left_indent=left_indent, hanging=hanging)
        if alignment is not None:
            paragraph.alignment = alignment
        if text:
            render_inline(paragraph, text, size=size, base_bold=bold,
                          base_italic=italic)
        self.last_paragraph = paragraph
        return paragraph

    def add_title_page(self, lines):
        for raw in lines:
            text = raw.strip()
            if not text:
                spacer = self.doc.add_paragraph()
                spacer.alignment = WD_ALIGN_PARAGRAPH.CENTER
                spacer.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
                spacer.paragraph_format.space_after = Pt(14)
                self.last_paragraph = spacer
                continue
            p = self.doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_together = True
            render_inline(p, text, size=BODY_SIZE,
                          base_bold=(text.isupper() or text.startswith("BY")))
            self.last_paragraph = p

    def add_heading(self, text, level):
        if level == 1:
            chapter = re.match(r"^([1-5])\.0\b", text.strip())
            if chapter:
                chapter_names = {
                    "1": "ONE", "2": "TWO", "3": "THREE",
                    "4": "FOUR", "5": "FIVE",
                }
                label = self.doc.add_paragraph()
                label.alignment = WD_ALIGN_PARAGRAPH.CENTER
                label.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
                label.paragraph_format.space_before = Pt(0)
                label.paragraph_format.space_after = Pt(0)
                label.paragraph_format.first_line_indent = Cm(0)
                label.paragraph_format.page_break_before = not self.suppress_next_heading_page_break
                label.paragraph_format.keep_with_next = True
                label.paragraph_format.keep_together = True
                render_inline(label, f"CHAPTER {chapter_names[chapter.group(1)]}",
                              size=BODY_SIZE, base_bold=True)

                paragraph = self.doc.add_paragraph(style="Heading 1")
                paragraph.paragraph_format.page_break_before = False
                paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                paragraph.paragraph_format.space_before = Pt(0)
                render_inline(paragraph, text.upper(), size=BODY_SIZE, base_bold=True)
                self.suppress_next_heading_page_break = False
            else:
                paragraph = self.doc.add_paragraph(style="Heading 1")
                paragraph.paragraph_format.page_break_before = not self.suppress_next_heading_page_break
                paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                render_inline(paragraph, text.upper(), size=BODY_SIZE, base_bold=True)
                self.suppress_next_heading_page_break = False
        else:
            paragraph = self.doc.add_paragraph(style=f"Heading {level}")
            paragraph.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            if level == 2:
                render_inline(paragraph, text, size=BODY_SIZE, base_bold=True)
            elif level == 3:
                render_inline(paragraph, text, size=BODY_SIZE)
            else:
                render_inline(paragraph, text, size=BODY_SIZE, base_italic=True)
        self.last_paragraph = paragraph
        return paragraph

    def render_title_if_needed(self):
        self.add_title_page(self.title_lines)
        self.title_lines = []
        self.in_title = False

    def render_figure(self, relative_path, caption):
        image_path = (FIGURE_DIR / relative_path).resolve()
        if not image_path.is_file():
            raise FileNotFoundError(f"Missing thesis figure: {image_path}")
        with Image.open(image_path) as image:
            width_px, height_px = image.size
        width_cm = width_px / 96 * 2.54
        height_cm = height_px / 96 * 2.54
        scale = min(1.0, TEXT_WIDTH_CM / width_cm,
                    MAX_FIGURE_HEIGHT_CM / height_cm)
        width_cm *= scale

        figure_par = self.doc.add_paragraph()
        figure_par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        figure_par.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        figure_par.paragraph_format.space_before = Pt(6)
        figure_par.paragraph_format.space_after = Pt(4)
        figure_par.paragraph_format.keep_together = True
        figure_par.paragraph_format.keep_with_next = True
        figure_par.add_run().add_picture(str(image_path), width=Cm(width_cm))
        self.last_paragraph = figure_par

        cap = self.add_paragraph(strip_source(caption), alignment=WD_ALIGN_PARAGRAPH.CENTER,
                                 after=12)
        cap.paragraph_format.keep_together = True
        record = self.caption_lookup[bookmark_name("Figure", caption)]
        add_bookmark(cap, record.bookmark, self.bookmark_id)
        self.bookmark_id += 1

    def render_table(self, caption, rows):
        caption_text = strip_source(caption)
        cap = self.add_paragraph(caption_text, alignment=WD_ALIGN_PARAGRAPH.LEFT,
                                 after=4)
        cap.paragraph_format.keep_with_next = True
        cap.paragraph_format.keep_together = True
        record = self.caption_lookup[bookmark_name("Table", caption)]
        add_bookmark(cap, record.bookmark, self.bookmark_id)
        self.bookmark_id += 1

        ncols = max(len(row) for row in rows)
        table = self.doc.add_table(rows=0, cols=ncols)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = True
        set_table_borders(table)
        for row_index, values in enumerate(rows):
            cells = table.add_row().cells
            for col_index in range(ncols):
                cell = cells[col_index]
                cell.text = ""
                paragraph = cell.paragraphs[0]
                set_body_paragraph(paragraph, single=False, after=2)
                paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
                value = values[col_index] if col_index < len(values) else ""
                render_inline(paragraph, value, size=BODY_SIZE,
                              base_bold=(row_index == 0))
            if row_index == 0:
                mark_repeat_header(table.rows[-1])
        for col_index in range(ncols):
            width = Cm(TEXT_WIDTH_CM / ncols)
            for row in table.rows:
                row.cells[col_index].width = width
        prevent_row_split(table)
        self.doc.add_paragraph().paragraph_format.space_after = Pt(8)
        self.last_paragraph = self.doc.paragraphs[-1]

    def add_equation_number(self, number):
        if self.last_paragraph is None:
            raise ValueError(f"Equation number {number} has no preceding equation")
        paragraph = self.last_paragraph
        paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
        paragraph.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        paragraph.paragraph_format.space_after = Pt(12)
        paragraph.paragraph_format.left_indent = Cm(0)
        paragraph.paragraph_format.right_indent = Cm(0)
        paragraph.paragraph_format.first_line_indent = Cm(0)
        paragraph.paragraph_format.keep_together = True
        paragraph.paragraph_format.tab_stops.add_tab_stop(
            Cm(TEXT_WIDTH_CM / 2), WD_TAB_ALIGNMENT.CENTER)
        paragraph.paragraph_format.tab_stops.add_tab_stop(
            Cm(TEXT_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT)

        leading_tab = paragraph.add_run("\t")._r
        paragraph._p.remove(leading_tab)
        if paragraph._p.pPr is not None:
            paragraph._p.pPr.addnext(leading_tab)
        else:
            paragraph._p.insert(0, leading_tab)
        paragraph.add_run("\t")
        render_inline(paragraph, number, size=BODY_SIZE)
        self.last_paragraph = paragraph

    def render_line(self, path, line, lines, index):
        if not line:
            return index

        # A figure directive.
        figure = FIGURE_RE.match(line)
        if figure:
            self.render_figure(figure.group(1).strip(), figure.group(2).strip())
            return index

        # A table directive: following pipe rows contain the header and body.
        table_match = TABLE_RE.match(line)
        if table_match:
            fields = [field.strip() for field in table_match.group(1).split("|")]
            caption, rows = fields[0], []
            for field in fields[1:]:
                row = [cell.strip() for cell in field.split(";")]
                # An optional Markdown separator row is ignored.
                if row and all(re.fullmatch(r"[-: ]+", cell or " ") for cell in row):
                    continue
                rows.append(row)
            self.render_table(caption, rows)
            return index

        # Equation numbers attach to the preceding display paragraph on the same line.
        if EQUATION_NUMBER_RE.fullmatch(line):
            self.add_equation_number(line)
            return index

        # Standard Markdown headings.
        heading = HEADING_RE.match(line)
        if heading:
            level = len(heading.group(1))
            self.add_heading(heading.group(2).strip(), level)
            return index

        # Ordered and unordered lists retain their numbering without a paragraph first-line indent.
        ordered = re.match(r"^(\d+)\.\s+(.*)$", line)
        if ordered:
            p = self.doc.add_paragraph()
            set_body_paragraph(p, after=6, left_indent=0.45)
            render_inline(p, f"{ordered.group(1)}. {ordered.group(2)}")
            self.last_paragraph = p
            return index
        if line.startswith("- "):
            p = self.doc.add_paragraph()
            set_body_paragraph(p, after=6, left_indent=0.45)
            render_inline(p, "– " + line[2:])
            self.last_paragraph = p
            return index

        # References use a standard hanging indent and remain double-spaced.
        is_reference = path.name == "06_references.md" and bool(re.match(r"^[A-Z][A-Za-zÀ-ž-]+,", line))
        if is_reference:
            p = self.add_paragraph(line, references=True, after=12,
                                   left_indent=1.27, hanging=1.27)
            return index

        # Ordinary prose. Markdown hard-wrapped lines are joined until a blank line.
        paragraph_lines = [line]
        j = index + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if (not nxt or HEADING_RE.match(nxt) or FIGURE_RE.match(nxt)
                    or TABLE_RE.match(nxt) or EQUATION_NUMBER_RE.fullmatch(nxt)
                    or re.match(r"^(\d+)\.\s+", nxt) or nxt.startswith("- ")):
                break
            paragraph_lines.append(nxt)
            j += 1
        text = " ".join(paragraph_lines)
        self.add_paragraph(text)
        return j - 1

    def render_source(self, filename, text):
        path = SOURCE_DIR / filename
        lines = text.splitlines()
        index = 0
        while index < len(lines):
            raw = lines[index]
            line = raw.strip()
            if line == "[TITLEPAGE]":
                self.in_title = True
                self.title_lines = []
                index += 1
                continue
            if line == "[/TITLEPAGE]":
                self.render_title_if_needed()
                if filename == "00_prelims.md":
                    self.start_page_numbered_section("lowerRoman", r"PAGE \* roman")
                index += 1
                continue
            if self.in_title:
                self.title_lines.append(raw)
                index += 1
                continue
            index = self.render_line(path, line, lines, index) + 1

    def add_front_matter_lists(self, records):
        # The dynamic TOC uses Heading 1–4 styles. The list headings themselves
        # use direct formatting so they do not appear inside their own TOC.
        self.add_front_heading("TABLE OF CONTENTS", page_break=True)
        toc = self.doc.add_paragraph()
        toc.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
        toc.paragraph_format.space_after = Pt(0)
        add_field(toc, r'TOC \o "1-4" \h \z \u')
        self.last_paragraph = toc

        self.add_front_heading("LIST OF TABLES", page_break=True)
        self.add_caption_list([record for record in records if record.kind == "Table"])

        self.add_front_heading("LIST OF FIGURES", page_break=True)
        self.add_caption_list([record for record in records if record.kind == "Figure"])

    def add_front_heading(self, text, *, page_break):
        p = self.doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
        p.paragraph_format.keep_with_next = True
        p.paragraph_format.page_break_before = page_break
        render_inline(p, text, size=BODY_SIZE, base_bold=True)
        self.last_paragraph = p

    def add_caption_list(self, records):
        for record in records:
            p = self.doc.add_paragraph()
            p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.left_indent = Cm(0)
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.tab_stops.add_tab_stop(Cm(TEXT_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            render_inline(p, strip_source(record.caption), size=BODY_SIZE)
            p.add_run("\t")
            add_field(p, f"PAGEREF {record.bookmark} \\h \\# \"00\"")
            self.last_paragraph = p


def validate_sources(source_texts):
    expected_chapters = [
        "# 1.0 INTRODUCTION",
        "# 2.0 LITERATURE REVIEW",
        "# 3.0 METHODOLOGY",
        "# 4.0 RESULTS AND DISCUSSION",
        "# 5.0 CONCLUSIONS AND RECOMMENDATIONS",
    ]
    actual = []
    for filename in FILES[1:6]:
        headings = [line.strip() for line in source_texts[filename].splitlines()
                    if re.match(r"^# ", line.strip())]
        if len(headings) != 1:
            raise ValueError(f"{filename} must contain one chapter-level heading; found {headings}")
        actual.append(headings[0])
    if actual != expected_chapters:
        raise ValueError(f"Unexpected chapter heading sequence: {actual}")

    prelims = source_texts["00_prelims.md"]
    expected_title = (
        "DENSITY FUNCTIONAL THEORY EVALUATION OF VANADIC ACID ZEOLITE Y "
        "DEALUMINATION IN RESIDUE FLUID CATALYTIC CRACKING REGENERATOR"
    )
    title_block = prelims.split("[TITLEPAGE]", 1)[1].split("[/TITLEPAGE]", 1)[0]
    title = next(line.strip() for line in title_block.splitlines() if line.strip())
    if title != expected_title:
        raise ValueError("The title page must retain the supervisor's quoted title")
    abstract_match = re.search(r"^# ABSTRACT\s+(.*?)(?=^# |\Z)", prelims, re.S | re.M)
    if not abstract_match:
        raise ValueError("Preliminary pages must contain an Abstract")
    abstract_paragraphs = [p.strip() for p in abstract_match.group(1).split("\n\n") if p.strip()]
    if len(abstract_paragraphs) != 1:
        raise ValueError("The abstract must be a single paragraph")
    abstract_words = len(abstract_paragraphs[0].split())
    if abstract_words >= 200:
        raise ValueError(f"The abstract must remain under 200 words; found {abstract_words}")

    chapter_one = source_texts["01_chapter1.md"]
    objective_section = re.search(
        r"## 1\.3 Aim and Objectives of the Study\s+(.*?)(?=\n## )", chapter_one, re.S)
    if not objective_section:
        raise ValueError("Chapter One must contain Section 1.3, Aim and Objectives of the Study")
    objectives = re.findall(r"^\d+\.\s+(.+)$", objective_section.group(1), re.M)
    if len(objectives) != 4:
        raise ValueError(f"Expected four objectives, found {len(objectives)}")
    for forbidden in ("faujasite", "report", "refine"):
        if any(re.search(rf"\b{forbidden}\b", objective.lower()) for objective in objectives):
            raise ValueError(f"Objectives must not contain the term {forbidden!r}")
    if "## 1.7" in chapter_one:
        raise ValueError("Remove the organisation-of-thesis section")
    if "entirely computational" in source_texts["03_chapter3.md"].lower():
        raise ValueError("Remove the unnecessary 'entirely computational' statement from methodology")
    appendix = source_texts.get("07_appendices.md", "")
    for required in ("Appendix A", "Appendix B", "calculation register", "substitution"):
        if required.lower() not in appendix.lower():
            raise ValueError(f"Appendices must include {required!r}")

    # Ensure that figure/table caption numbers are unique across chapters and appendices.
    records = caption_records(source_texts)
    captions = []
    for record in records:
        match = re.search(r"(?:[A-Z]|\d+)\.\d+", record.caption)
        if match:
            captions.append(f"{record.kind} {match.group()}")
    if len(captions) != len(set(captions)):
        raise ValueError("Duplicate figure/table caption numbers found")


def build():
    source_texts = {}
    for filename in FILES:
        file_path = SOURCE_DIR / filename
        if not file_path.is_file():
            raise FileNotFoundError(f"Missing thesis source: {file_path}")
        source_texts[filename] = file_path.read_text(encoding="utf-8")
    validate_sources(source_texts)
    records = caption_records(source_texts)

    builder = ThesisBuilder()
    title_block = source_texts[FILES[0]].split("[TITLEPAGE]", 1)[1].split("[/TITLEPAGE]", 1)[0]
    project_title = next(line.strip() for line in title_block.splitlines() if line.strip())
    builder.doc.core_properties.title = project_title
    builder.doc.core_properties.author = "Usman Shehu AHMAD"
    builder.doc.core_properties.subject = "B.Eng. Chemical Engineering undergraduate research project"
    builder.doc.core_properties.last_modified_by = "Usman Shehu AHMAD"
    builder.caption_lookup = {record.bookmark: record for record in records}
    builder.render_source(FILES[0], source_texts[FILES[0]])
    builder.add_front_matter_lists(records)
    for filename in FILES[1:]:
        if filename == "01_chapter1.md":
            builder.start_page_numbered_section("decimal", r'PAGE \# "00"')
        builder.render_source(filename, source_texts[filename])

    DELIVERABLE_DIR.mkdir(parents=True, exist_ok=True)
    builder.doc.save(OUT)
    shutil.copyfile(OUT, COMPAT_OUT)
    print(f"Wrote {OUT}")
    print(f"Wrote identical compatibility copy {COMPAT_OUT}")
    print(f"  Chapter-level headings: 5")
    print(f"  Objectives: 4")
    print(f"  Figures: {sum(r.kind == 'Figure' for r in records)}")
    print(f"  Tables: {sum(r.kind == 'Table' for r in records)}")


def main():
    build()


if __name__ == "__main__":
    main()
