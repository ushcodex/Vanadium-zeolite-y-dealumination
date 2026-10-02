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
- Images: Centered with appropriate scaling
- Page Breaks: Strictly deduplicated so no empty/blank pages are created
"""
import os
import re
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
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
    cleaned_text = text.replace("$", "").replace("\\text{", "").replace("}", "")
    
    # Tokenizer for bold (**text**), italic (*text*), and code (`text`)
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
    
    # State tracking: True at start of document to prevent blank leading page
    last_element_was_page_break = True

    def add_page_break():
        nonlocal last_element_was_page_break
        if not last_element_was_page_break and len(doc.paragraphs) > 0:
            doc.add_page_break()
            last_element_was_page_break = True

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
                p = doc.add_paragraph()
                p.paragraph_format.line_spacing = 1.0
                p.paragraph_format.space_before = Pt(4)
                p.paragraph_format.space_after = Pt(6)
                p.paragraph_format.left_indent = Inches(0.5)
                run = p.add_run("\n".join(code_block_lines))
                run.font.name = "Consolas"
                run.font.size = Pt(9.5)
                code_block_lines = []
                last_element_was_page_break = False
            i += 1
            continue

        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Ignore markdown horizontal divider rules
        if stripped in ["---", "***", "___"]:
            i += 1
            continue

        # Handle Page Break directive
        if stripped == "\\newpage":
            add_page_break()
            i += 1
            continue

        # Handle Images: ![alt](path)
        img_match = re.match(r"^!\[(.*?)\]\((.*?)\)$", stripped)
        if img_match:
            img_path = img_match.group(2).strip()
            # If path doesn't exist relative to CWD, try relative to markdown directory
            if not os.path.exists(img_path):
                md_dir = os.path.dirname(md_path)
                candidate = os.path.join(md_dir, img_path)
                if os.path.exists(candidate):
                    img_path = candidate
            
            if os.path.exists(img_path):
                p_img = doc.add_paragraph()
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p_img.paragraph_format.space_before = Pt(8)
                p_img.paragraph_format.space_after = Pt(4)
                run_img = p_img.add_run()
                try:
                    run_img.add_picture(img_path, width=Inches(5.8))
                    last_element_was_page_break = False
                except Exception as e:
                    print(f"Warning: could not insert image {img_path}: {e}")
            i += 1
            continue

        # Handle Level 1 Markdown Headings
        if stripped.startswith("# "):
            heading_text = stripped[2:].strip()
            is_major_section = any(k in heading_text for k in [
                "TITLE", "CHAPTER", "ABSTRACT", "DECLARATION", "CERTIFICATION",
                "DEDICATION", "ACKNOWLEDGEMENTS", "TABLE OF CONTENTS",
                "LIST OF", "REFERENCES", "APPENDICES"
            ])
            if is_major_section:
                add_page_break()
            
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(10)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER if is_major_section else WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(heading_text)
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(16)
            last_element_was_page_break = False
            i += 1
            continue

        # Handle Level 2 Markdown Headings
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
            last_element_was_page_break = False
            i += 1
            continue

        # Handle Level 3 Markdown Headings
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
            last_element_was_page_break = False
            i += 1
            continue

        # Handle Level 4 Markdown Headings
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
            last_element_was_page_break = False
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
                # Skip separator lines (e.g. |---|---|)
                if re.match(r"^\|[\s\-:]+(\|[\s\-:]+)+\|$", t_line):
                    continue
                cells = [c.strip() for c in t_line.split("|")[1:-1]]
                rows_data.append(cells)

            if rows_data:
                num_cols = max(len(r) for r in rows_data)
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
                        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
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
                                run.font.size = Pt(10)
                        else:
                            for run in p.runs:
                                run.font.size = Pt(9.5)
                
                last_element_was_page_break = False
            continue

        # Handle Bulleted Lists
        if stripped.startswith("- ") or stripped.startswith("* "):
            item_text = stripped[2:].strip()
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.left_indent = Inches(0.4)
            add_formatted_runs(p, item_text)
            last_element_was_page_break = False
            i += 1
            continue

        # Handle Numbered Lists (e.g. "1. ", "2. ")
        num_match = re.match(r"^(\d+)\.\s+(.*)", stripped)
        if num_match:
            prefix = num_match.group(1) + ". "
            item_text = num_match.group(2).strip()
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.left_indent = Inches(0.4)
            r_num = p.add_run(prefix)
            r_num.bold = True
            add_formatted_runs(p, item_text)
            last_element_was_page_break = False
            i += 1
            continue

        # Handle Regular Paragraphs
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        
        # Center align special blocks (Title page elements or captions)
        if any(stripped.startswith(k) for k in [
            "**A DENSITY FUNCTIONAL THEORY", "**BY**", "**AHMAD USMAN", 
            "**Matriculation", "**BACHELOR OF ENGINEERING", "**OCTOBER, 2026**"
        ]):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif any(stripped.startswith(k) for k in [
            "*Source:*", "**Table ", "*Optimised ", "*Stationary-state ", 
            "*Validation ", "*Adsorption ", "*Audited ", "*Single-point "
        ]):
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        
        add_formatted_runs(p, stripped)
        last_element_was_page_break = False
        i += 1

    print(f"Saving compiled DOCX to: {docx_path}")
    doc.save(docx_path)
    print("DOCX generation completed successfully.")

if __name__ == "__main__":
    src_md = "writing/thesis/thesis_final.md"
    out_docx = "writing/thesis/thesis_final.docx"
    build_docx(src_md, out_docx)
    
    # Also compile to thesis_master.docx and work.docx
    for target in ["writing/thesis/thesis_master.docx", "writing/thesis/work.docx"]:
        try:
            shutil.copyfile(out_docx, target)
            print(f"Copied to {target}")
        except Exception as e:
            print(f"Warning copying to {target}: {e}")
