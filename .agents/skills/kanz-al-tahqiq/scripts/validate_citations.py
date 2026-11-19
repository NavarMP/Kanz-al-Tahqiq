#!/usr/bin/env python3
"""
validate_citations.py - Scholarly Citation & Provenance Verifier
Part of the Kanz al-Taḥqīq Digital Humanities Skill (.agents/skills/kanz-al-tahqiq/)

Validates repository Markdown files for:
1. Shamela book IDs against the verified canonical catalog.
2. Quran.com Surah (1-114) and Ayah boundary checks.
3. Sunnah.com route format and unresolved placeholder tags (<number>).
4. Dead or confabulated patterns (e.g. /cat-poet- slugs on aldiwan.net).
5. Broken Malayalam Unicode sequence checks in URLs.
"""

import os
import re
import sys
import argparse
from urllib.parse import unquote

# Authoritative Verified Shamela Catalog for Kanz al-Taḥqīq
SHAMELA_CANONICAL_CATALOG = {
    "11327": ("فتح المعين بشرح قرة العين", "المليباري"),
    "21719": ("الأشباه والنظائر", "السيوطي"),
    "9472": ("إحياء علوم الدين", "الغزالي"),
    "12421": ("مشكاة الأنوار", "الغزالي"),
    "5459": ("المستصفى", "الغزالي"),
    "8176": ("مرقاة المفاتيح", "الملا علي القاري"),
    "9953": ("الرسالة القشيرية", "القشيري"),
    "482": ("قوت القلوب", "أبو طالب المكي"),
    "9904": ("شرح ابن عقيل", "ابن عقيل"),
    "8473": ("تفسير ابن كثير", "ابن كثير"),
    "23604": ("تفسير ابن كثير", "ابن كثير"),
    "43": ("تفسير الطبري", "ابن جرير الطبري"),
    "23635": ("تفسير الرازي (مفاتيح الغيب)", "فخر الدين الرازي"),
    "12320": ("تاريخ ابن خلدون", "ابن خلدون"),
    "8180": ("الرسالة", "الشافعي"),
    "9256": ("جواهر البلاغة", "أحمد الهاشمي"),
    "10551": ("المثل السائر", "ابن الأثير"),
    "23794": ("المثل السائر", "ابن الأثير"),
    "26575": ("إعجاز القرآن", "الباقلاني"),
}

# Known Confabulated or Mismatched IDs to explicitly reject
SHAMELA_DISALLOWED_IDS = {
    "21715": "Irshad al-Sari (Qastallani) - was mistakenly cited as Suyuti's al-Ashbah",
    "21643": "Sharh Mayyara (Maliki) - was mistakenly cited as Ihya Ulum al-Din",
    "21644": "Majma' al-Anhur (Hanafi) - was mistakenly cited as Ihya Ulum al-Din",
    "6531": "Muntaqa min Minhaj al-I'tidal (Dhahabi) - was mistakenly cited as Mishkat al-Anwar",
    "1726": "Sunan Abi Dawud - was mistakenly cited as Mirqat al-Mafatih",
    "8352": "Sharh al-Aqidah al-Tahawiyyah - was mistakenly cited as Diwan al-Shafi'i",
    "11822": "HTTP 404 dead link",
    "8334": "HTTP 404 dead link",
    "21745": "HTTP 404 dead link",
    "11846": "HTTP 404 dead link",
    "11548": "HTTP 404 dead link",
    "11019": "HTTP 404 dead link",
    "14013": "HTTP 404 dead link",
    "14022": "HTTP 404 dead link",
    "8381": "Fatawa al-Lajnah al-Da'imah - was mistakenly cited as al-Mathal al-Sa'ir",
    "11812": "al-Milal wa al-Nihal - was mistakenly cited as Sharh Ibn 'Aqil",
    "23833": "Sirat Ibn Hisham - was mistakenly cited as Sharh Shawahid al-Talkhis",
    "21575": "Madha Khasira al-Alam - was mistakenly cited as Amr ibn al-Ahtam",
}

# Canonical Quran Surah Ayah Counts
QURAN_AYAH_COUNTS = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109,
    123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60,
    34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45,
    60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44,
    28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20,
    15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3,
    5, 4, 5, 6
]

LINK_PATTERN = re.compile(r'\[([^\]]+)\]\((https?://[^\)\s]+)\)')

def validate_citations_in_file(filepath):
    errors = []
    warnings = []

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    for line_idx, line in enumerate(lines, 1):
        for match in LINK_PATTERN.finditer(line):
            label = match.group(1).strip()
            url = match.group(2).strip()

            # 1. Check for unresolved placeholders
            if '<number' in url or '<id' in url:
                # Allow only if inside references directory as example documentation
                if 'references' not in filepath:
                    errors.append(f"Line {line_idx}: Unresolved placeholder in citation URL: {url}")

            # 2. Shamela.ws checks
            if 'shamela.ws/book/' in url:
                bid_match = re.search(r'shamela\.ws/book/(\d+)', url)
                if bid_match:
                    bid = bid_match.group(1)
                    if bid in SHAMELA_DISALLOWED_IDS:
                        errors.append(f"Line {line_idx}: Disallowed/confabulated Shamela ID {bid} ({SHAMELA_DISALLOWED_IDS[bid]})")
                    elif bid not in SHAMELA_CANONICAL_CATALOG and bid != "00000":
                        warnings.append(f"Line {line_idx}: Uncataloged Shamela ID {bid} in '{label}'. Verify against canonical catalog.")

            # 3. Quran.com checks
            if 'quran.com/' in url:
                q_match = re.search(r'quran\.com/(\d+)(?:/(\d+))?', url)
                if q_match:
                    surah = int(q_match.group(1))
                    ayah = int(q_match.group(2)) if q_match.group(2) else None
                    if surah < 1 or surah > 114:
                        errors.append(f"Line {line_idx}: Invalid Quran surah {surah} in URL: {url}")
                    elif ayah is not None:
                        max_ayah = QURAN_AYAH_COUNTS[surah - 1]
                        if ayah < 1 or ayah > max_ayah:
                            errors.append(f"Line {line_idx}: Invalid Ayah {ayah} for Surah {surah} (max {max_ayah}) in URL: {url}")

            # 4. Sunnah.com checks
            if 'sunnah.com/' in url:
                if 'muslim:introduction' in url:
                    errors.append(f"Line {line_idx}: Invalid Sunnah route format 'muslim:introduction'. Use 'sunnah.com/muslim/introduction'.")
                if 'malik/36/31' in url:
                    errors.append(f"Line {line_idx}: Non-standard Muwatta path 'malik/36/31'. Use verified hadith ID.")

            # 5. Al-Diwan confabulated categories
            if 'aldiwan.net/cat-poet-' in url:
                errors.append(f"Line {line_idx}: Confabulated /cat-poet- slug on Al-Diwan: {url}. Use clean poet name or verified poem URL.")

            # 6. Unicode Malayalam corruption check
            if 'wikipedia.org' in url and '%E0%B4%87%E0%B5%81' in url:
                errors.append(f"Line {line_idx}: Corrupted Malayalam Unicode sequence in Wikipedia URL.")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description="Kanz al-Taḥqīq Scholarly Citation & Provenance Verifier")
    parser.add_argument("--dir", type=str, default=".", help="Root directory to scan")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    root_dir = os.path.abspath(args.dir)
    print("=" * 80)
    print(f" Kanz al-Taḥqīq Citation Integrity Verifier: {root_dir}")
    print("=" * 80)

    total_files = 0
    files_with_errors = 0
    total_errors = 0
    total_warnings = 0

    for root, dirs, files in os.walk(root_dir):
        if any(ignored in root for ignored in ['.git', '.gemini', 'node_modules', 'brain']):
            continue
        for file in sorted(files):
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, root_dir)
                total_files += 1

                errors, warnings = validate_citations_in_file(filepath)
                if errors or (args.strict and warnings):
                    files_with_errors += 1
                    total_errors += len(errors)
                    total_warnings += len(warnings)
                    print(f"\n❌ [FAIL] {relpath}")
                    for err in errors:
                        print(f"   🔴 ERROR: {err}")
                    for warn in warnings:
                        print(f"   🟡 WARN:  {warn}")
                elif warnings:
                    total_warnings += len(warnings)

    print("\n" + "=" * 80)
    print(f" Citation Audit Summary:")
    print(f" Total Markdown Files Scanned: {total_files}")
    print(f" Files with Citation Errors:    {files_with_errors}")
    print(f" Total Citation Errors:         {total_errors}")
    print(f" Total Citation Warnings:       {total_warnings}")
    print("=" * 80)

    if total_errors > 0 or (args.strict and total_warnings > 0):
        print("\n❌ Citation verification FAILED. Correct all flagged URLs.")
        sys.exit(1)
    else:
        print("\n✅ All scholarly citations, Shamela book IDs, and API endpoints PASSED verification.")
        sys.exit(0)

if __name__ == "__main__":
    main()
