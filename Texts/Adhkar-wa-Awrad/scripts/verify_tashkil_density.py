#!/usr/bin/env python3
"""
verify_tashkil_density.py
Measures the Tashkil density of Arabic markdown files in Texts/Adhkar-wa-Awrad.
Ensures Arabic prayers, ayahs, and hadiths meet the threshold (>= 0.70).
"""
import os
import re
import sys

# Arabic vowel diacritics: Fathah, Dammah, Kasrah, Fathatan, Dammatan, Kasratan, Sukun, Shaddah
HARAKAT = re.compile(r'[\u064B-\u0652\u0670]')
ARABIC_LETTERS = re.compile(r'[\u0621-\u064A]')

def check_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    letters = len(ARABIC_LETTERS.findall(content))
    harakat = len(HARAKAT.findall(content))

    if letters == 0:
        return 0, 0, 0.0

    ratio = harakat / letters
    return letters, harakat, ratio

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Checking Tashkil density in: {base_dir}\n")

    files_checked = 0
    warnings = 0

    for root, dirs, files in os.walk(base_dir):
        if 'scripts' in root:
            continue
        for file in sorted(files):
            if file.endswith('.md'):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, base_dir)
                letters, harakat, ratio = check_file(path)
                files_checked += 1
                status = "✅ PASS" if ratio >= 0.70 else "⚠️ LOW"
                if ratio < 0.70 and letters > 100:
                    warnings += 1
                print(f"[{status}] {rel_path:<45} Letters: {letters:>5} | Harakat: {harakat:>5} | Density: {ratio:0.1%}")

    print(f"\nCompleted: {files_checked} files checked. Low density warnings: {warnings}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
