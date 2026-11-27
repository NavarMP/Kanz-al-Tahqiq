#!/usr/bin/env python3
"""
lint_transliteration.py - Academic Arabic Transliteration Linter & Normalizer
Part of the Kanz al-Taḥqīq Digital Humanities Skill (.agents/skills/kanz-al-tahqiq/)

Enforces the Kanz al-Taḥqīq Arabic-English Transliteration Master Standard:
1. Normalizes Unicode to Form C (NFC) - eliminates Latin decomposed combining marks.
2. Flags ASCII straight quotes (') and backticks (`) used for Hamzah (ʾ U+02BE) or ʿAyn (ʿ U+02BF).
3. Flags colloquial contractions in running text (e.g. inshallah, mashallah, alhamdulillah, saw, pbuh).
4. Verifies universal definite article hyphenation (al-noun) and flags unhyphenated 'al noun'.
5. Flags non-assimilated vs assimilated solar articles to ensure consistency.
6. Provides an automated in-place --fix capability.
"""

import os
import re
import sys
import argparse
import unicodedata

# Colloquial or non-scholarly abbreviations to formal standard mappings
SLANG_MAP = {
    r"\binshallah\b": "in shāʾ Allāh",
    r"\binsha'allah\b": "in shāʾ Allāh",
    r"\binshaallah\b": "in shāʾ Allāh",
    r"\bmashallah\b": "mā shāʾ Allāh",
    r"\bmasha'allah\b": "mā shāʾ Allāh",
    r"\balhamdulillah\b": "al-ḥamdu lillāh",
    r"\bwalhamdulillah\b": "wa-al-ḥamdu lillāh",
    r"\bsubhanallah\b": "subḥāna Allāh",
    r"\bjazakallah\b": "jazāka Allāhu khayran",
    r"\bjazakallahu\s+khair\b": "jazāka Allāhu khayran",
    r"\bjazakallahu\s+khayran\b": "jazāka Allāhu khayran",
    r"\b(pbuh|saw|sws)\b": "ﷺ",
}

# Solar prefixes in IJMES style (for detection/warning in ALA-LC standard)
SOLAR_PREFIX_PATTERN = re.compile(
    r"\b(ash|ar|an|ad|adh|at|ath|az|as|aṣ|aḍ|aṭ|aẓ)-([a-zāīūḥṣḍṭẓ])",
    re.IGNORECASE
)

# Unhyphenated definite article: 'al ' followed by transliterated latin noun
UNHYPHENATED_AL_PATTERN = re.compile(
    r"\b(al|Al)\s+([a-zA-Zāīūḥṣḍṭẓʿʾ]{2,})"
)

# Straight quotes/backticks inside words (potential Hamzah or Ayn)
MIDWORD_STRAIGHT_QUOTE = re.compile(r"([a-zA-Zāīūḥṣḍṭẓ])'([a-zA-Zāīūḥṣḍṭẓ])")
MIDWORD_BACKTICK = re.compile(r"([a-zA-Zāīūḥṣḍṭẓ])`([a-zA-Zāīūḥṣḍṭẓ])")

TARGET_EXTENSIONS = {".md", ".txt"}
TARGET_DIRS = ["Texts", "Fest", "debate", "speech", "Conversation", "Articles", "Poem", "Song"]


def is_latin_combining(ch):
    """Check if character is a combining diacritic outside Arabic and Malayalam blocks."""
    code = ord(ch)
    # Arabic blocks: 0x0600-0x06FF, 0x0750-0x077F, 0x08A0-0x08FF
    # Malayalam block: 0x0D00-0x0D7F
    if (0x0600 <= code <= 0x06FF) or (0x0750 <= code <= 0x077F) or (0x08A0 <= code <= 0x08FF) or (0x0D00 <= code <= 0x0D7F):
        return False
    return unicodedata.combining(ch) > 0


def is_doc_or_rule_context(line):
    """Check if line is documenting a negative example or regex rule rather than running prose."""
    lower = line.lower()
    indicators = [
        "incorrect:", "prohibition", "never write", "find colloquial",
        "danger", "regex", "slang_map", "slang spellings", 'prefix": ";saw'
    ]
    return any(ind in lower for ind in indicators)


def check_and_lint_content(content, filepath="", fix=False):
    errors = []
    warnings = []
    fixed_content = content
    changes_made = False

    # 1. Unicode NFC Normalization check
    nfc_content = unicodedata.normalize('NFC', content)
    latin_combining_count = sum(1 for ch in content if is_latin_combining(ch))

    if content != nfc_content:
        if latin_combining_count > 0:
            errors.append(f"Unicode NFD detected ({latin_combining_count} Latin decomposed combining marks). Normalize to NFC.")
        if fix:
            fixed_content = nfc_content
            changes_made = True

    lines = (fixed_content if fix else content).splitlines(keepends=True)
    new_lines = []
    in_code_block = False

    for line_idx, line in enumerate(lines, start=1):
        modified_line = line
        stripped = line.strip()

        # Handle code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            new_lines.append(modified_line)
            continue

        if in_code_block or stripped.startswith("<!--"):
            new_lines.append(modified_line)
            continue

        doc_context = is_doc_or_rule_context(line)

        # 2. Check for colloquial contractions in active text
        if not doc_context:
            for pattern, replacement in SLANG_MAP.items():
                matches = re.findall(pattern, modified_line, re.IGNORECASE)
                if matches:
                    errors.append(f"Line {line_idx}: Colloquial slang '{matches[0]}' found. Standard is '{replacement}'.")
                    if fix:
                        modified_line = re.sub(pattern, replacement, modified_line, flags=re.IGNORECASE)
                        changes_made = True

        # 3. Check for mid-word backtick
        backtick_matches = MIDWORD_BACKTICK.findall(modified_line)
        if backtick_matches and not doc_context:
            errors.append(f"Line {line_idx}: Backtick '`' used inside word ({backtick_matches[0][0]}`{backtick_matches[0][1]}). Use 'ʿ' (U+02BF).")
            if fix:
                modified_line = MIDWORD_BACKTICK.sub(r"\1ʿ\2", modified_line)
                changes_made = True

        # 4. Check for straight single apostrophe inside words
        quote_matches = MIDWORD_STRAIGHT_QUOTE.findall(modified_line)
        if quote_matches and not doc_context:
            for m in quote_matches:
                pair = f"{m[0]}'{m[1]}".lower()
                # Exclude standard English contractions
                if pair not in ["n't", "'s", "'d", "'ll", "'ve", "'re"]:
                    warnings.append(f"Line {line_idx}: Straight apostrophe in '{m[0]}'{m[1]}'. Use 'ʾ' (U+02BE) for Hamzah or 'ʿ' (U+02BF) for ʿAyn.")

        # 5. Check for unhyphenated 'al ' (e.g. 'al kitāb')
        if not doc_context:
            unhyphenated_matches = UNHYPHENATED_AL_PATTERN.findall(modified_line)
            if unhyphenated_matches:
                for art, nxt in unhyphenated_matches:
                    # Ignore common English names/phrases
                    if nxt.lower() not in ["gore", "pacino", "capone"]:
                        errors.append(f"Line {line_idx}: Unhyphenated definite article '{art} {nxt}...'. Must be '{art}-{nxt}...'.")
                        if fix:
                            modified_line = re.sub(r"\b" + art + r"\s+" + nxt, f"{art}-{nxt}", modified_line)
                            changes_made = True

        # 6. Informational check for assimilated solar articles (ALA-LC consistency)
        if not doc_context:
            solar_matches = SOLAR_PREFIX_PATTERN.findall(modified_line)
            if solar_matches:
                for pref, letter in solar_matches:
                    warnings.append(f"Line {line_idx}: Phonetic solar assimilation '{pref}-{letter}' found. Kanz al-Taḥqīq standard is ALA-LC 'al-{letter}'.")

        new_lines.append(modified_line)

    if fix and changes_made:
        fixed_content = "".join(new_lines)

    return errors, warnings, fixed_content, changes_made


def process_file(filepath, fix=False, verbose=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"⚠️  [SKIP] Non-UTF-8 file: {filepath}")
        return 0, 0

    errors, warnings, fixed_content, changed = check_and_lint_content(content, filepath, fix=fix)

    if fix and changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"✨ [FIXED] {filepath}")

    if errors or (warnings and verbose):
        status_icon = "❌" if errors else "⚠️ "
        print(f"{status_icon} {filepath}")
        for err in errors:
            print(f"   [ERROR]   {err}")
        if verbose:
            for warn in warnings:
                print(f"   [WARNING] {warn}")
        print()

    return len(errors), len(warnings)


def main():
    parser = argparse.ArgumentParser(
        description="Academic Arabic Transliteration Linter for Kanz al-Taḥqīq"
    )
    parser.add_argument("paths", nargs="*", help="File or directory paths to audit")
    parser.add_argument("--all", action="store_true", help="Audit all Markdown files in the repository")
    parser.add_argument("--fix", action="store_true", help="Automatically normalize Unicode NFC and fix errors")
    parser.add_argument("-v", "--verbose", action="store_true", help="Display non-critical warnings")

    args = parser.parse_args()

    files_to_check = []

    if args.all:
        for root_dir in [os.getcwd(), os.path.join(os.getcwd(), "Kanz-al-Tahqiq-pub")]:
            if not os.path.exists(root_dir):
                continue
            for d in TARGET_DIRS:
                full_d = os.path.join(root_dir, d)
                if os.path.exists(full_d):
                    for root, _, files in os.walk(full_d):
                        for file in files:
                            if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                                files_to_check.append(os.path.join(root, file))
            # Also check root md files
            for file in os.listdir(root_dir):
                if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                    files_to_check.append(os.path.join(root_dir, file))
    elif args.paths:
        for p in args.paths:
            if os.path.isfile(p):
                files_to_check.append(p)
            elif os.path.isdir(p):
                for root, _, files in os.walk(p):
                    for file in files:
                        if any(file.endswith(ext) for ext in TARGET_EXTENSIONS):
                            files_to_check.append(os.path.join(root, file))
    else:
        parser.print_help()
        sys.exit(0)

    unique_files = list(dict.fromkeys(files_to_check))

    if not unique_files:
        print("No matching markdown files found.")
        sys.exit(0)

    print(f"🔍 Auditing {len(unique_files)} files against Kanz al-Taḥqīq Transliteration Standard...")
    print("=" * 70)

    total_errors = 0
    total_warnings = 0

    for fpath in unique_files:
        errs, warns = process_file(fpath, fix=args.fix, verbose=args.verbose)
        total_errors += errs
        total_warnings += warns

    print("=" * 70)
    print(f"Audit Complete: {len(unique_files)} files scanned | {total_errors} errors | {total_warnings} warnings.")

    if total_errors > 0 and not args.fix:
        print("\n💡 Run with '--fix' to automatically resolve Unicode NFC and standard contractions.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
