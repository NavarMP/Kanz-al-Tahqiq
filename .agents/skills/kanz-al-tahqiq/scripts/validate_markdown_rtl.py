#!/usr/bin/env python3
"""
validate_markdown_rtl.py - Markdown RTL & Quality Linter
Part of the Kanz al-Taḥqīq Digital Humanities Skill (.agents/skills/kanz-al-tahqiq/)

Validates repository Markdown files for:
1. RTL tag encapsulation (<div dir="rtl" lang="ar">) when Arabic text is present.
2. Proper closing of HTML div containers.
3. Markdown table column balance (matching pipe counts).
4. Unclosed code blocks (e.g. Mermaid or Python).
5. Empty or malformed markdown links.
"""

import os
import re
import sys
import argparse

TARGET_DIRS = ["Texts", "Fest", "debate", "speech", "Conversation", "Articles", "Poem", "games"]
ARABIC_PATTERN = re.compile(r'[\u0600-\u06FF]')

def count_arabic_chars(text):
    return len(ARABIC_PATTERN.findall(text))

def check_file(filepath):
    errors = []
    warnings = []

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    content = "".join(lines)
    arabic_count = count_arabic_chars(content)

    # 1. RTL and HTML Div Checks
    has_rtl_open = bool(re.search(r'<div\s+[^>]*dir=["\']rtl["\']', content, re.IGNORECASE))
    all_open_divs = len(re.findall(r'<div\b(?![^>]*/>)', content, re.IGNORECASE))
    all_close_divs = len(re.findall(r'</div>', content, re.IGNORECASE))

    if arabic_count > 250 and not has_rtl_open:
        # Check if it's primarily an Arabic document
        total_chars = len(content.strip())
        if total_chars > 0 and (arabic_count / total_chars) > 0.25:
            warnings.append(f"Significant Arabic text ({arabic_count} chars) without root RTL container (<div dir=\"rtl\" lang=\"ar\">)")

    if all_open_divs != all_close_divs:
        errors.append(f"Mismatched <div> tags: {all_open_divs} open <div...> tag(s) vs {all_close_divs} close </div> tag(s)")

    # 2. Code block fence check (triple backticks)
    fence_count = sum(1 for line in lines if line.strip().startswith("```"))
    if fence_count % 2 != 0:
        errors.append(f"Unclosed code fence: found {fence_count} occurrences of '```'")

    # 3. Table Column Balance Check
    in_table = False
    expected_cols = 0
    table_start_line = 0

    for idx, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if line.startswith("|") and line.endswith("|"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            col_count = len(parts)

            if not in_table:
                in_table = True
                table_start_line = idx
                expected_cols = col_count
            else:
                # Check for separator row (e.g. |---|:---|)
                if all(re.match(r'^:?-+:?$', p) for p in parts if p):
                    continue
                if col_count != expected_cols:
                    warnings.append(f"Table at line {table_start_line} has mismatched columns at line {idx}: expected {expected_cols}, got {col_count}")
        else:
            in_table = False
            expected_cols = 0

    # 4. Empty links check [text]()
    for idx, raw_line in enumerate(lines, 1):
        if re.search(r'\[([^\]]+)\]\(\s*\)', raw_line):
            warnings.append(f"Empty Markdown link '[]()' at line {idx}")

    return errors, warnings, arabic_count

def main():
    parser = argparse.ArgumentParser(description="Kanz al-Tahqiq Markdown RTL & Quality Linter")
    parser.add_argument("--dir", type=str, default=".", help="Root directory to scan (defaults to repository root)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    root_dir = os.path.abspath(args.dir)
    print("=" * 80)
    print(f" Kanz al-Taḥqīq Quality & RTL Linter: {root_dir}")
    print("=" * 80)

    total_files = 0
    files_with_issues = 0
    total_errors = 0
    total_warnings = 0

    for target in TARGET_DIRS:
        target_path = os.path.join(root_dir, target)
        if not os.path.exists(target_path):
            continue

        for dirpath, _, filenames in os.walk(target_path):
            for fname in sorted(filenames):
                if not fname.endswith(".md"):
                    continue

                filepath = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(filepath, root_dir)
                total_files += 1

                errors, warnings, ar_chars = check_file(filepath)

                if errors or warnings:
                    files_with_issues += 1
                    total_errors += len(errors)
                    total_warnings += len(warnings)
                    print(f"\n[FILE] {rel_path} (Arabic chars: {ar_chars})")
                    for err in errors:
                        print(f"  ❌ ERROR  : {err}")
                    for warn in warnings:
                        print(f"  ⚠️  WARNING: {warn}")

    print("\n" + "=" * 80)
    print(f" Summary: Scanned {total_files} Markdown files.")
    print(f" Errors: {total_errors} | Warnings: {total_warnings}")
    print("=" * 80)

    if total_errors > 0 or (args.strict and total_warnings > 0):
        print("❌ Validation FAILED.")
        sys.exit(1)
    else:
        print("✅ Validation PASSED.")
        sys.exit(0)

if __name__ == "__main__":
    main()
