#!/usr/bin/env python3
"""
Utility script to extract and normalize text from Sharh al-Alfiyyah PDF.
Handles visual LTR reversal and Arabic Presentation Forms decomposition.
"""

import sys
import unicodedata
import pdfplumber

def extract_pages(pdf_path, start_page, end_page):
    output_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for p in range(start_page - 1, min(end_page, total)):
            page_text = pdf.pages[p].extract_text()
            if not page_text:
                continue
            lines = page_text.split('\n')
            output_lines.append(f"\n<!-- === الصفحة المطبوعة {p + 1} === -->\n")
            for line in lines:
                clean = line.strip()
                if not clean:
                    continue
                # Reverse visual LTR line to get logical RTL
                reversed_line = clean[::-1]
                # NFKD decomposes presentation forms like ﳌ, ﴍ to standard Arabic letters
                norm = unicodedata.normalize('NFKD', reversed_line)
                norm_c = unicodedata.normalize('NFC', norm)
                output_lines.append(norm_c)
    return '\n'.join(output_lines)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <start_page> <end_page> [pdf_path]")
        sys.exit(1)
    s = int(sys.argv[1])
    e = int(sys.argv[2])
    pdf = sys.argv[3] if len(sys.argv) > 3 else "Kanz-al-Tahqiq-pub/Texts/Nahw/alfiyyah/Sharh/ألفية ابن مالك طبعة جديدة.pdf"
    result = extract_pages(pdf, s, e)
    print(result[:1500])
