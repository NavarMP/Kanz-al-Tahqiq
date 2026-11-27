#!/usr/bin/env python3
"""
markdown_to_docx.py - Multilingual Markdown to Microsoft Word (.docx) Converter
Engineered for Kanz al-Tahqiq: Supports Arabic (RTL), Malayalam, and English typography.

Usage:
    python3 markdown_to_docx.py input.md [output.docx]
"""

import sys
import os
import re
import argparse
from typing import List, Tuple, Dict, Any, Optional

try:
    import docx
    from docx import Document
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
except ImportError:
    print("Error: python-docx is not installed. Run 'pip install python-docx' first.", file=sys.stderr)
    sys.exit(1)

# Typography font choices
FONT_LATIN = "Georgia"
FONT_ARABIC = "Amiri"
FONT_MALAYALAM = "Manjari"
COLOR_PRIMARY = RGBColor(17, 34, 51)       # Deep slate / teal
COLOR_SECONDARY = RGBColor(70, 80, 95)    # Slate gray
COLOR_CALLOUT_BORDER = "1B6B93"           # Hex for callouts
COLOR_TABLE_HEADER_BG = "EAEFF5"          # Soft blue-gray for table headers

# Regex patterns for script detection
RE_ARABIC = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]')
RE_MALAYALAM = re.compile(r'[\u0D00-\u0D7F]')


def is_predominantly_arabic(text: str) -> bool:
    """Check if string contains Arabic characters."""
    return bool(RE_ARABIC.search(text))


def is_malayalam(text: str) -> bool:
    """Check if string contains Malayalam characters."""
    return bool(RE_MALAYALAM.search(text))


def set_cell_background(cell, color_hex: str):
    """Set shading/background color of a docx table cell."""
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner padding for a table cell (in dxa: 20 dxa = 1 pt)."""
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)


def apply_bidi_to_paragraph(p):
    """Enable Right-to-Left bidirectional layout on paragraph."""
    pPr = p._p.get_or_add_pPr()
    bidi = parse_xml(f'<w:bidi {nsdecls("w")}/>')
    pPr.append(bidi)
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT


def format_run_fonts(run, text: str, size_pt: float = 11, bold: bool = False, italic: bool = False, color: Optional[RGBColor] = None):
    """Apply intelligent multilingual font binding to a run."""
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = color
    
    if is_predominantly_arabic(text):
        run.font.name = FONT_ARABIC
        run.font.size = Pt(size_pt + 3)  # Arabic script renders clearer with +3pt
    elif is_malayalam(text):
        run.font.name = FONT_MALAYALAM
        run.font.size = Pt(size_pt + 0.5)
    else:
        run.font.name = FONT_LATIN
        run.font.size = Pt(size_pt)


def parse_inline_markdown(p, text: str, base_size: float = 11, base_color: Optional[RGBColor] = None):
    """Parse basic markdown inline syntax: bold, italic, code, links, and HTML spans."""
    # Strip HTML tags like <span dir="rtl" lang="ar"> or </span>
    clean_text = re.sub(r'<span[^>]*>', '', text)
    clean_text = re.sub(r'</span>', '', clean_text)
    
    # Simple regex tokenizer for bold/italic/code/text
    tokens = re.split(r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`.*?`|\[.*?\]\(.*?\))', clean_text)
    
    for token in tokens:
        if not token:
            continue
        
        bold = False
        italic = False
        content = token
        
        if token.startswith('***') and token.endswith('***'):
            bold = True
            italic = True
            content = token[3:-3]
        elif token.startswith('**') and token.endswith('**'):
            bold = True
            content = token[2:-2]
        elif token.startswith('*') and token.endswith('*'):
            italic = True
            content = token[1:-1]
        elif token.startswith('`') and token.endswith('`'):
            content = token[1:-1]
            run = p.add_run(content)
            run.font.name = "Courier New"
            run.font.size = Pt(base_size - 1)
            continue
        elif token.startswith('[') and '](' in token and token.endswith(')'):
            m = re.match(r'\[(.*?)\]\((.*?)\)', token)
            if m:
                label, url = m.groups()
                run = p.add_run(label)
                format_run_fonts(run, label, size_pt=base_size, bold=bold, italic=True, color=RGBColor(27, 107, 147))
                continue
        
        run = p.add_run(content)
        format_run_fonts(run, content, size_pt=base_size, bold=bold, italic=italic, color=base_color)


def parse_yaml_frontmatter(lines: List[str]) -> Tuple[Dict[str, str], List[str]]:
    """Extract YAML frontmatter if present at the top of the markdown file."""
    metadata = {}
    if not lines or lines[0].strip() != "---":
        return metadata, lines

    end_idx = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx != -1:
        for line in lines[1:end_idx]:
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip().lower()] = val.strip().strip('"').strip("'")
        return metadata, lines[end_idx + 1:]
    
    return metadata, lines


def convert_markdown_to_docx(md_path: str, docx_path: str):
    """Main compilation routine."""
    with open(md_path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    metadata, lines = parse_yaml_frontmatter(raw_lines)
    
    doc = Document()
    
    # Configure 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Insert Title / Cover Block if frontmatter is available
    if metadata.get("title"):
        title_p = doc.add_paragraph()
        title_p.paragraph_format.space_before = Pt(30)
        title_p.paragraph_format.space_after = Pt(8)
        run_title = title_p.add_run(metadata.get("title"))
        format_run_fonts(run_title, metadata.get("title"), size_pt=24, bold=True, color=COLOR_PRIMARY)
        
        if metadata.get("subtitle"):
            sub_p = doc.add_paragraph()
            sub_p.paragraph_format.space_after = Pt(12)
            run_sub = sub_p.add_run(metadata.get("subtitle"))
            format_run_fonts(run_sub, metadata.get("subtitle"), size_pt=14, italic=True, color=COLOR_SECONDARY)
            
        byline_p = doc.add_paragraph()
        byline_p.paragraph_format.space_after = Pt(24)
        author = metadata.get("author", "")
        date = metadata.get("date", "")
        meta_str = f"Author: {author}   |   Date: {date}" if author and date else (author or date)
        if meta_str:
            run_meta = byline_p.add_run(meta_str)
            format_run_fonts(run_meta, meta_str, size_pt=10, italic=True, color=COLOR_SECONDARY)
            
        doc.add_page_break()

    in_rtl_block = False
    in_code_block = False
    table_buffer: List[str] = []

    def flush_table(buffer: List[str]):
        if not buffer:
            return
        
        # Parse table rows
        rows_data = []
        for line in buffer:
            parts = [c.strip() for c in line.strip().strip('|').split('|')]
            # Skip alignment separators like |:---|:---:|
            if parts and all(re.match(r'^:?-+:?$', p) for p in parts if p):
                continue
            if parts:
                rows_data.append(parts)
        
        if not rows_data:
            return

        col_count = max(len(r) for r in rows_data)
        table = doc.add_table(rows=len(rows_data), cols=col_count)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        for r_idx, row in enumerate(rows_data):
            for c_idx in range(col_count):
                cell_text = row[c_idx] if c_idx < len(row) else ""
                cell = table.cell(r_idx, c_idx)
                cell.text = ""  # Clear default text
                cell_p = cell.paragraphs[0]
                cell_p.paragraph_format.space_before = Pt(3)
                cell_p.paragraph_format.space_after = Pt(3)
                
                is_header = (r_idx == 0)
                if is_header:
                    set_cell_background(cell, COLOR_TABLE_HEADER_BG)
                    parse_inline_markdown(cell_p, cell_text, base_size=10, base_color=COLOR_PRIMARY)
                    for r in cell_p.runs:
                        r.bold = True
                else:
                    parse_inline_markdown(cell_p, cell_text, base_size=9.5)
                
                if is_predominantly_arabic(cell_text):
                    apply_bidi_to_paragraph(cell_p)

                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)

        # Space after table
        after_p = doc.add_paragraph()
        after_p.paragraph_format.space_after = Pt(12)

    # Line by line markdown iteration
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Handle RTL div boundaries
        if '<div dir="rtl"' in stripped or 'dir="rtl"' in stripped:
            in_rtl_block = True
            i += 1
            continue
        elif '</div>' in stripped and in_rtl_block:
            in_rtl_block = False
            i += 1
            continue

        # Handle page breaks
        if 'page-break-after: always' in stripped or stripped == '\\newpage':
            flush_table(table_buffer)
            table_buffer = []
            doc.add_page_break()
            i += 1
            continue

        # Handle code blocks
        if stripped.startswith('```'):
            flush_table(table_buffer)
            table_buffer = []
            in_code_block = not in_code_block
            i += 1
            continue

        if in_code_block:
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            run = p.add_run(line.rstrip('\n'))
            run.font.name = "Courier New"
            run.font.size = Pt(9.5)
            i += 1
            continue

        # Handle Markdown Tables
        if stripped.startswith('|') and stripped.endswith('|'):
            table_buffer.append(stripped)
            i += 1
            continue
        else:
            if table_buffer:
                flush_table(table_buffer)
                table_buffer = []

        # Empty lines
        if not stripped:
            i += 1
            continue

        # Headings
        if stripped.startswith('#'):
            h_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
            if h_match:
                level = len(h_match.group(1))
                h_text = h_match.group(2)
                h_text_clean = re.sub(r'<[^>]*>', '', h_text).strip()
                
                h_p = doc.add_paragraph()
                sizes = {1: 18, 2: 15, 3: 13, 4: 11.5, 5: 11, 6: 10.5}
                size = sizes.get(level, 12)
                
                h_p.paragraph_format.space_before = Pt(14)
                h_p.paragraph_format.space_after = Pt(6)
                
                parse_inline_markdown(h_p, h_text_clean, base_size=size, base_color=COLOR_PRIMARY)
                for r in h_p.runs:
                    r.bold = True
                
                if in_rtl_block or is_predominantly_arabic(h_text_clean):
                    apply_bidi_to_paragraph(h_p)
                
                i += 1
                continue

        # Blockquotes / Callout Alerts
        if stripped.startswith('>'):
            quote_text = stripped.lstrip('>').strip()
            # Clean callout alerts like > [!NOTE]
            is_alert = False
            for alert_tag in ['[!NOTE]', '[!IMPORTANT]', '[!TIP]', '[!WARNING]', '[!CAUTION]']:
                if alert_tag in quote_text:
                    quote_text = quote_text.replace(alert_tag, f"**{alert_tag[2:-1]}:**")
                    is_alert = True
            
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.right_indent = Inches(0.4)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(4)
            
            parse_inline_markdown(p, quote_text, base_size=10.5, base_color=COLOR_SECONDARY)
            for r in p.runs:
                r.italic = True
                
            if in_rtl_block or is_predominantly_arabic(quote_text):
                apply_bidi_to_paragraph(p)
                
            i += 1
            continue

        # Bullet and Numbered Lists
        list_match = re.match(r'^(\*|-|\d+\.)\s+(.*)', stripped)
        if list_match:
            bullet_sym = list_match.group(1)
            item_text = list_match.group(2)
            
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.3)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            
            prefix = "• " if bullet_sym in ['*', '-'] else f"{bullet_sym} "
            run_pfx = p.add_run(prefix)
            run_pfx.bold = True
            
            parse_inline_markdown(p, item_text, base_size=11)
            
            if in_rtl_block or is_predominantly_arabic(item_text):
                apply_bidi_to_paragraph(p)
                
            i += 1
            continue

        # Standard Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        
        parse_inline_markdown(p, stripped, base_size=11)
        
        if in_rtl_block or is_predominantly_arabic(stripped):
            apply_bidi_to_paragraph(p)

        i += 1

    # Final table flush if any
    flush_table(table_buffer)

    # Save output document
    os.makedirs(os.path.dirname(os.path.abspath(docx_path)), exist_ok=True)
    doc.save(docx_path)
    print(f"Successfully compiled: '{md_path}' -> '{docx_path}'")


def main():
    parser = argparse.ArgumentParser(
        description="Compile Multilingual Markdown to styled Microsoft Word (.docx) with Arabic, Malayalam, and English typography."
    )
    parser.add_argument("input_md", help="Path to input Markdown file")
    parser.add_argument("output_docx", nargs="?", help="Path to output .docx file (default: same name with .docx extension)")
    
    args = parser.parse_args()
    
    input_path = os.path.abspath(args.input_md)
    if not os.path.exists(input_path):
        print(f"Error: File '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)
        
    if args.output_docx:
        output_path = os.path.abspath(args.output_docx)
    else:
        output_path = os.path.splitext(input_path)[0] + ".docx"
        
    convert_markdown_to_docx(input_path, output_path)


if __name__ == "__main__":
    main()
