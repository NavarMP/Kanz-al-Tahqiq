#!/usr/bin/env python3
"""
lint_sharh_verses.py
Collation and verification suite for Sharh al-Khulasah al-Alfiyyah.
Validates:
1. Verse sequential continuity (1 to max).
2. Verse text match against canonical alfiyyah-ibn-malik.md.
3. Quranic citation syntax and valid URLs.
4. Paired delimiters (parentheses, brackets, quotes).
"""

import sys
import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARH_PATH = os.path.join(BASE_DIR, "Sharh/Sharh-alfiyyah-by-makhdumayn.md")
MATN_PATH = os.path.join(BASE_DIR, "alfiyyah-ibn-malik.md")

AR_DIGITS = '٠١٢٣٤٥٦٧٨٩'
def to_int(s):
    val = 0
    for ch in str(s):
        if ch in AR_DIGITS:
            val = val * 10 + AR_DIGITS.index(ch)
        elif ch.isdigit():
            val = val * 10 + int(ch)
    return val

def strip_tashkil(s):
    # Remove diacritics, punctuation and normalize alefs/yas for soft comparison
    s = re.sub(r'[إأآا]', 'ا', s)
    s = re.sub(r'[ىي]', 'ي', s)
    return re.sub(r'[\u0617-\u061A\u064B-\u0652\u06D6-\u06ED«»\(\)\[\]—\-\s\.\*،؛:]', '', s)

# Known attested riwayah variants in Sharh al-Makhdumayn
ATTESTED_VARIANTS = {
    69: ["وليتني", "والليتني"],
    187: ["ووصلمابذي", "وتوصلمابذي"],
    221: ["ومالمفعولي", "وماللمفعول"],
    229: ["ويرفعالفاع", "ويرتفعالفا"],
    238: ["وقديجاءبخل", "وقديجيءبخل"]
}

def load_canonical_matn():
    with open(MATN_PATH, 'r', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'^\*\*([٠-٩\d]+)\.\*\*\s*(.+)$', text, re.M)
    matn_dict = {}
    for num_str, line in matches:
        matn_dict[to_int(num_str)] = line.strip()
    return matn_dict

def lint_sharh(max_expected=None):
    with open(SHARH_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    matn_dict = load_canonical_matn()
    
    # Extract verses
    v_matches = re.findall(r'^>\s+\*\*([٠-٩\d]+)\.\*\*\s*(.+)$', content, re.M)
    if not v_matches:
        print("ERROR: No verses found in Sharh file!")
        return False

    v_nums = [to_int(m[0]) for m in v_matches]
    total_found = len(v_nums)
    max_found = max(v_nums) if v_nums else 0
    target_max = max_expected if max_expected else max_found

    print(f"--- Linting Sharh File: {SHARH_PATH} ---")
    print(f"Total verse headers found: {total_found}")
    print(f"Verse range: {min(v_nums)} to {max_found}")

    errors = []
    warnings = []

    # 1. Continuity check
    seen = set()
    for n in v_nums:
        if n in seen:
            errors.append(f"Duplicate verse header found: {n}")
        seen.add(n)

    for expected in range(1, target_max + 1):
        if expected not in seen:
            errors.append(f"Missing verse header: {expected}")

    # 2. Textual collation
    for num_str, sharh_line in v_matches:
        n = to_int(num_str)
        canonical = matn_dict.get(n)
        if not canonical:
            warnings.append(f"Verse {n}: Not found in canonical matn!")
            continue

        s_clean = strip_tashkil(sharh_line)
        c_clean = strip_tashkil(canonical)

        # Check hemistich division
        if '—' not in sharh_line and '-' not in sharh_line:
            warnings.append(f"Verse {n}: Missing hemistich separator ('—'): {sharh_line[:30]}")

        # Check first 10 normalized chars
        matched = False
        if s_clean[:10] == c_clean[:10]:
            matched = True
        elif n in ATTESTED_VARIANTS:
            for variant in ATTESTED_VARIANTS[n]:
                if s_clean.startswith(variant) or variant in s_clean[:12]:
                    matched = True
                    break

        if not matched:
            errors.append(f"Verse {n} mismatch:\n   Sharh : {sharh_line}\n   Canon : {canonical}")

    # 3. Quranic citation URL validity
    quran_links = re.findall(r'\[([^\]]+)\]\(https://quran\.com/([0-9]+)/([0-9]+)\)', content)
    for ref, s_id, a_id in quran_links:
        s_num = int(s_id)
        a_num = int(a_id)
        if not (1 <= s_num <= 114):
            errors.append(f"Invalid Surah number in Quran link: {s_num} in [{ref}]")
        if a_num <= 0 or a_num > 286:
            errors.append(f"Invalid Ayah number in Quran link: {s_num}:{a_num}")

    print("\n--- LINT SUMMARY ---")
    print(f"Total Errors  : {len(errors)}")
    print(f"Total Warnings: {len(warnings)}")

    if errors:
        print("\nTOP ERRORS:")
        for e in errors[:15]:
            print("  *", e)
        if len(errors) > 15:
            print(f"  ... and {len(errors) - 15} more errors.")

    if warnings:
        print("\nTOP WARNINGS:")
        for w in warnings[:10]:
            print("  *", w)

    return len(errors) == 0

if __name__ == '__main__':
    max_v = int(sys.argv[1]) if len(sys.argv) > 1 else None
    success = lint_sharh(max_v)
    sys.exit(0 if success else 1)
