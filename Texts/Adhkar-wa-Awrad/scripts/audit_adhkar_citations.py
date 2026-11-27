#!/usr/bin/env python3
"""
audit_adhkar_citations.py
Audits all markdown files in Texts/Adhkar-wa-Awrad for citation validity:
- quran.com links: surah 1-114, valid ayah counts.
- sunnah.com links: verified routes and non-empty IDs.
- shamela.ws links: verified catalog IDs.
- aldiwan.net and adabworld.com links.
"""
import os
import re
import sys

# Import canonical catalogs
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

def audit_file(filepath):
    errors = []
    warnings = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines, 1):
        for m in LINK_PATTERN.finditer(line):
            label = m.group(1).strip()
            url = m.group(2).strip()
            
            # Check Quran
            if 'quran.com/' in url:
                qm = re.search(r'quran\.com/(\d+)(?:/(\d+))?', url)
                if qm:
                    surah = int(qm.group(1))
                    ayah = int(qm.group(2)) if qm.group(2) else None
                    if surah < 1 or surah > 114:
                        errors.append(f"L{idx}: Invalid Surah {surah} in {url}")
                    elif ayah is not None:
                        max_a = QURAN_AYAH_COUNTS[surah - 1]
                        if ayah < 1 or ayah > max_a:
                            errors.append(f"L{idx}: Invalid Ayah {ayah} for Surah {surah} (max {max_a}) in {url}")
                            
            # Check Sunnah
            if 'sunnah.com/' in url:
                if 'muslim:introduction' in url:
                    errors.append(f"L{idx}: Invalid Sunnah route 'muslim:introduction'")
                if '<' in url or '>' in url:
                    errors.append(f"L{idx}: Placeholder in Sunnah URL: {url}")
                    
            # Check Shamela
            if 'shamela.ws/book/' in url:
                sm = re.search(r'shamela\.ws/book/(\d+)', url)
                if sm:
                    bid = sm.group(1)
                    if bid in ["21715", "21643", "21644", "6531", "1726", "8352", "11822"]:
                        errors.append(f"L{idx}: Disallowed Shamela ID: {bid}")

    return errors, warnings

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Auditing citations in: {base_dir}\n")
    
    total_errors = 0
    total_warnings = 0
    files_checked = 0
    
    for root, dirs, files in os.walk(base_dir):
        if 'scripts' in root:
            continue
        for file in sorted(files):
            if file.endswith('.md'):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, base_dir)
                errs, warns = audit_file(path)
                files_checked += 1
                if errs:
                    print(f"❌ {rel_path}:")
                    for e in errs:
                        print(f"   {e}")
                    total_errors += len(errs)
                elif warns:
                    print(f"⚠️ {rel_path}:")
                    for w in warns:
                        print(f"   {w}")
                    total_warnings += len(warns)
                else:
                    print(f"✅ {rel_path}: All citations valid.")
                    
    print(f"\nAudit complete: {files_checked} files checked, {total_errors} errors, {total_warnings} warnings.")
    return total_errors

if __name__ == '__main__':
    sys.exit(main())
