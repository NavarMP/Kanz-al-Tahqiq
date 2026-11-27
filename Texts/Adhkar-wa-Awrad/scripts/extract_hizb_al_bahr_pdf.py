#!/usr/bin/env python3
"""
extract_hizb_al_bahr_pdf.py
Extracts, spatially clusters, fuses diacritics, and normalizes the Arabic text of
Ḥizb al-Baḥr from `hizb-al-bahr-arabic.pdf`.
"""
import os
import re
import unicodedata
import pdfplumber

def extract_page_text(page):
    # Group characters into vertical lines by rounding top coordinate
    # Line height in this document is ~24-30 pt, but letters and diacritics are within ~8-12 pt
    lines_dict = {}
    
    # Sort chars vertically first
    for c in page.chars:
        # Round to nearest 10 pt band
        y_band = round(c['top'] / 10) * 10
        lines_dict.setdefault(y_band, []).append(c)
        
    line_texts = []
    for y in sorted(lines_dict.keys()):
        # Sort characters right-to-left: descending x0
        line_chars = sorted(lines_dict[y], key=lambda c: -c['x0'])
        line_str = "".join([c['text'] for c in line_chars])
        line_texts.append(line_str)
        
    return "\n".join(line_texts)

def normalize_arabic(text):
    # Normalize common Unicode variants from font
    text = text.replace('ک', 'ك')
    text = text.replace('ی', 'ي')
    text = text.replace('ۤ', '')  # Quranic prolongation symbol
    text = text.replace('ـ', '')  # Tatweel
    text = text.replace('ۡ', 'ْ')  # Quranic jazm to standard sukun
    text = text.replace('ٰ', 'َا') # Dagger alif to standard alif where appropriate or keep dagger
    
    # Clean whitespace around rub al-hizb symbol
    text = re.sub(r'\s*۞\s*', ' ۞\n', text)
    
    # Normalize NFC
    text = unicodedata.normalize('NFC', text)
    return text

def main():
    pdf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'hizb-al-bahr-arabic.pdf')
    if not os.path.exists(pdf_path):
        print(f"Error: {pdf_path} not found.")
        return 1
        
    print(f"Opening: {pdf_path}")
    with pdfplumber.open(pdf_path) as pdf:
        print(f"Total pages: {len(pdf.pages)}")
        for idx, page in enumerate(pdf.pages, 1):
            raw_text = extract_page_text(page)
            norm_text = normalize_arabic(raw_text)
            out_file = f"/Users/apple/.gemini/antigravity/brain/3cf60d33-a1e0-451e-97a3-ff756986d7c1/scratch/page_{idx}_extracted.txt"
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(norm_text)
            print(f"Page {idx} extracted -> {out_file} ({len(norm_text)} chars)")
            
    return 0

if __name__ == '__main__':
    main()
