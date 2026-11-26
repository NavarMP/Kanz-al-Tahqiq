#!/usr/bin/env python3
"""
extract_sharh_engine.py
Advanced extraction engine for Sharh al-Alfiyyah PDF.
Features:
- Bounding-box filtering to strip running headers (top 48 pt) and footers (bottom 45 pt).
- Visual LTR to logical RTL conversion with BiDi normalization.
- Presentation forms decomposition (NFKD -> NFC).
- Arabic-Indic digit reversal restoration.
"""

import sys
import unicodedata
import re
import pdfplumber

def reverse_persian_arabic_digits(text):
    # Detect reversed digit sequences like ٥٨١ -> ١٨٥
    def rev_match(m):
        return m.group(0)[::-1]
    return re.sub(r'[٠-٩0-9]{2,}', rev_match, text)

def extract_pages(pdf_path, start_page, end_page, crop_headers=True):
    output = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for p in range(start_page - 1, min(end_page, total)):
            page = pdf.pages[p]
            p_num = p + 1
            h = page.height
            w = page.width
            
            if crop_headers and h > 100:
                # crop top 48pt and bottom 45pt
                cropped = page.crop((0, 48, w, h - 45))
                page_text = cropped.extract_text()
            else:
                page_text = page.extract_text()
                
            if not page_text:
                continue
                
            lines = page_text.split('\n')
            output.append(f"\n<!-- === PDF_PAGE_{p_num} === -->\n")
            for line in lines:
                clean = line.strip()
                if not clean:
                    continue
                # Ignore running title remnants if any survived cropping
                if 'ألفية الإمام ابن مالك' in clean or 'شرح الخلاصة الألفية' in clean:
                    continue
                # Reverse visual LTR line to get logical RTL
                reversed_line = clean[::-1]
                # Normalize presentation forms to standard Arabic characters
                norm = unicodedata.normalize('NFKD', reversed_line)
                norm_c = unicodedata.normalize('NFC', norm)
                # Fix reversed digits
                norm_c = reverse_persian_arabic_digits(norm_c)
                output.append(norm_c)
    return '\n'.join(output)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <start_page> <end_page> [pdf_path]")
        sys.exit(1)
    s = int(sys.argv[1])
    e = int(sys.argv[2])
    pdf = sys.argv[3] if len(sys.argv) > 3 else "Kanz-al-Tahqiq-pub/Texts/Nahw/alfiyyah/Sharh/ألفية ابن مالك طبعة جديدة.pdf"
    res = extract_pages(pdf, s, e)
    print(res[:2500])
