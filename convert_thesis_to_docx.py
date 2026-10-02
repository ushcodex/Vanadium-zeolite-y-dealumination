# -*- coding: utf-8 -*-
"""
High-Fidelity Academic DOCX Converter for Ahmadu Bello University (ABU) Thesis
Converts thesis_final.md to a publication-grade Microsoft Word document (.docx)
Adhering to ABU Guidelines:
- Font: Times New Roman
- Sizes: Chapter Titles 16pt Bold, Subheadings 14pt/12pt Bold, Body 12pt
- Margins: Left 1.5 in (binding), Right 1.0 in, Top 1.0 in, Bottom 1.0 in
- Line Spacing: 1.5 lines with 6pt space after paragraphs
- Alignment: Justified
- Tables: Formal bordered tables with shaded headers
"""
import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set cell padding in twips."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex="F2F2F2"):
    """Set background color of a table cell."""
    shading_xml = f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>'
    cell._tc.get_or_add_tcPr().append(parse_xml(shading_xml))

def set_table_borders(table):
    """Set formal academic borders on table."""
    tblPr = table._tbl.tblPr
    borders_xml = f'''
    <w:tblBorders {nsdecls("w")}>
        <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>
        <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>
        <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
        <w:insideV w:val="none"/>
        <w:left w:val="none"/>
        <w:right w:val="none"/>
    </w:tblBorders>
    '''
    tblPr.append(parse_xml(borders_xml))

def add_formatted_runs(paragraph, text):
    """Parse inline markdown (bold, italic, code, math) and add formatted runs."""
    # Pattern to match bold (**text**), italic (*text*), code (`text`), math ($text$)
    # We replace math brackets with clean text
    cleaned_text = text.replace("$", "").replace("\\text{", "").replace("}", "")
    
    # Simple regex tokenizer for bold, italic, and regular text
    tokens = re.split(r'(\*\*[^*]+?\*\*|\*[^*]+?\*|`[^`]+?`)', cleaned_text)
    for token in tokens:
        if not token:
            continue
        if token.startswith("**") and token.endswith("**") and len(token) > 4:
            run = paragraph.add_run(token[2:-2])
            run.bold = True
        elif token.startswith("*") and token.endswith("*") and len(token) > 2:
            run = paragraph.add_run(token[1:-1])
            run.italic = True
        elif token.startswith("`") and token.endswith("`") and len(token) > 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(10)
        else:
            paragraph.add_run(token)

def build_docx(md_path, docx_path):
    print(f"Reading markdown from: {md_path}")
    with open(md_path, "r", encoding="utf-8", errors="ignore") as f:
        md_text = f.read()

    doc = docx.Document()

    # Configure ABU Thesis Page Margins (Left 1.5 in, others 1.0 in)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.5)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Base Style Settings
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(12)
    font_normal.color.rgb = RGBColor(0, 0, 0)
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.space_after = Pt(6)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    lines = md_text.splitlines()
    i = 0
    total_lines = len(lines)

    in_code_block = False
    code_block_lines = []

    while i < total_lines:
        line = lines[i]
        stripped = line.strip()

        # Handle Code Fences
        if stripped.startswith("```"):
            if not in_code_block:
                in_code_block = True
                code_block_lines = []
            else:
                in_code_block = False
                # Output code block as a shaded paragraph
                p = doc.add_paragraph()
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                p.paragraph_format.left_indent = Inches(0.5)
                run = p.add_run("\n".join(code_block_lines))
                run.font.name = "Consolas"
                run.font.size = Pt(9.5)
                code_block_lines = []
            i += 1
            continue

        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue

        # Handle Page Break directive
        if stripped == "\\newpage":
            doc.add_page_break()
            i += 1
            continue

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Handle Markdown Headings
        if stripped.startswith("# "):
            heading_text = stripped[2:].strip()
            # If it's a major chapter or preliminary heading, add page break if not at the very top
            if len(doc.paragraphs) > 2:
                doc.add_page_break()
            
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(12)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if ("TITLE" in heading_text or "CHAPTER" in heading_text or "ABSTRACT" in heading_text or "DECLARATION" in heading_text or "CERTIFICATION" in heading_text or "DEDICATION" in heading_text or "ACKNOWLEDGEMENTS" in heading_text or "TABLE OF CONTENTS" in heading_text or "LIST OF" in heading_text or "REFERENCES" in heading_text or "APPENDICES" in heading_text) else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(16)
            i += 1
            continue

        if stripped.startswith("## "):
            heading_text = stripped[3:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(13.5)
            i += 1
            continue

        if stripped.startswith("### "):
            heading_text = stripped[4:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)
            i += 1
            continue

        if stripped.startswith("#### "):
            heading_text = stripped[5:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.italic = True
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(12)
            i += 1
            continue

        # Handle Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines = []
            while i < total_lines and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            
            # Parse table lines
            rows_data = []
            for t_line in table_lines:
                # Check if it's a separator line (e.g. |---|---|)
                if re.match(r"^\|[\s\-:]+(\|[\s\-:]+)+\|$", t_line):
                    continue
                # Split cells
                cells = [c.strip() for c in t_line.split("|")[1:-1]]
                rows_data.append(cells)

            if rows_data:
                num_cols = max(len(r) for r in rows_data)
                # Pad rows to have same column count
                for r in rows_data:
                    while len(r) < num_cols:
                        r.append("")

                word_table = doc.add_table(rows=len(rows_data), cols=num_cols)
                word_table.alignment = WD_TABLE_ALIGNMENT.CENTER
                set_table_borders(word_table)

                for r_idx, r_data in enumerate(rows_data):
                    row = word_table.rows[r_idx]
                    is_header = (r_idx == 0)
                    for c_idx, val in enumerate(r_data):
                        cell = row.cells[c_idx]
                        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
                        if is_header:
                            set_cell_shading(cell, "EAEAEA")
                        
                        p = cell.paragraphs[0]
                        p.paragraph_format.line_spacing = 1.15
                        p.paragraph_format.space_after = Pt(2)
                        p.paragraph_format.space_before = Pt(2)
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if is_header or len(val) < 15 else WD_ALIGN_PARAGRAPH.LEFT
                        
                        add_formatted_runs(p, val)
                        if is_header:
                            for run in p.runs:
                                run.bold = True
                                run.font.size = Pt(10.5)
                        else:
                            for run in p.runs:
                                run.font.size = Pt(10)
                
                # Add a trailing space after table
                p_after = doc.add_paragraph()
                p_after.paragraph_format.space_after = Pt(6)
            continue

        # Handle Bulleted Lists
        if stripped.startswith("- ") or stripped.startswith("* "):
            item_text = stripped[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.left_indent = Inches(0.5)
            add_formatted_runs(p, item_text)
            i += 1
            continue

        # Handle Numbered Lists (e.g. "1. ", "2. ")
        num_match = re.match(r"^(\d+)\.\s+(.*)", stripped)
        if num_match:
            prefix = num_match.group(1) + ". "
            item_text = num_match.group(2).strip()
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.left_indent = Inches(0.5)
            r_num = p.add_run(prefix)
            r_num.bold = True
            add_formatted_runs(p, item_text)
            i += 1
            continue

        # Handle Regular Paragraphs
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Center align special blocks (like title page elements or captions)
        if stripped.startswith("**A DENSITY FUNCTIONAL THEORY") or stripped.startswith("**AHMAD USMAN") or stripped.startswith("**Matriculation") or stripped.startswith("**BY**") or stripped == "<br>":
            if stripped != "<br>":
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif stripped.startswith("*Source:*") or stripped.startswith("**Table ") or stripped.startswith("*Optimised ") or stripped.startswith("*Stationary-state ") or stripped.startswith("*Validation ") or stripped.startswith("*Adsorption "):
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        
        if stripped != "<br>":
            add_formatted_runs(p, stripped)

        i += 1

    print(f"Saving compiled DOCX to: {docx_path}")
    doc.save(docx_path)
    print("DOCX generation completed successfully.")

if __name__ == "__main__":
    src_md = "writing/thesis/thesis_final.md"
    out_docx = "writing/thesis/thesis_final.docx"
    build_docx(src_md, out_docx)
    
    # Also create work.docx so the user can access either name
    work_docx = "writing/thesis/work.docx"
    import shutil
    shutil.copyfile(out_docx, work_docx)
    print(f"Copied to {work_docx}")
