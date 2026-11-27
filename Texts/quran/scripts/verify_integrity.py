#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quran Markdown Integrity & Quality Assurance Test Suite
(Updated for Standard 604 Medina Mushaf Pages)
"""

import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURAHS_DIR = os.path.join(BASE_DIR, "surahs")
COMPLETE_FILE = os.path.join(BASE_DIR, "Quran-Complete.md")
INDEX_FILE = os.path.join(BASE_DIR, "INDEX.md")
PAGES_FILE = os.path.join(BASE_DIR, "PAGES.md")
README_FILE = os.path.join(BASE_DIR, "README.md")

TOTAL_QURAN_VERSES = 6236
TOTAL_SURAHS = 114
TOTAL_PAGES = 604

def test_files_exist():
    print("Testing core files existence...")
    assert os.path.isfile(COMPLETE_FILE), f"Missing {COMPLETE_FILE}"
    assert os.path.isfile(INDEX_FILE), f"Missing {INDEX_FILE}"
    assert os.path.isfile(PAGES_FILE), f"Missing {PAGES_FILE}"
    assert os.path.isfile(README_FILE), f"Missing {README_FILE}"
    assert os.path.isdir(SURAHS_DIR), f"Missing {SURAHS_DIR}"
    
    surah_files = [f for f in os.listdir(SURAHS_DIR) if f.endswith(".md")]
    assert len(surah_files) == TOTAL_SURAHS, f"Expected {TOTAL_SURAHS} surah files, found {len(surah_files)}"
    
    for f in surah_files:
        assert re.match(r"^\d{3}-[\w-]+\.md$", f), f"Filename {f} does not match 3-digit pattern"
        
    print(f"  [PASS] All {TOTAL_SURAHS} chapter files, PAGES.md, and core docs exist.")

def test_verse_counts():
    print("Testing verse counts across all files...")
    marker_pattern = re.compile(r"﴿[٠١٢٣٤٥٦٧٨٩]+﴾")
    
    total_markers_in_surahs = 0
    surah_files = sorted([f for f in os.listdir(SURAHS_DIR) if f.endswith(".md")])
    
    for f in surah_files:
        filepath = os.path.join(SURAHS_DIR, f)
        with open(filepath, "r", encoding="utf-8") as fh:
            content = fh.read()
            markers = marker_pattern.findall(content)
            count = len(markers)
            total_markers_in_surahs += count
            
            # Check Surah 1
            if f.startswith("001-"):
                assert count == 7, f"Surah 1 expected 7 ayahs, got {count}"
            # Check Surah 2
            if f.startswith("002-"):
                assert count == 286, f"Surah 2 expected 286 ayahs, got {count}"
            # Check Surah 9 (No bismillah)
            if f.startswith("009-"):
                assert count == 129, f"Surah 9 expected 129 ayahs, got {count}"
                assert "### بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ" not in content, "Surah 9 should NOT have Bismillah!"
            # Check Surah 114
            if f.startswith("114-"):
                assert count == 6, f"Surah 114 expected 6 ayahs, got {count}"
                
            # Verify RTL container
            assert '<div dir="rtl" lang="ar"' in content, f"{f} missing RTL container"
            assert '</div>' in content, f"{f} missing closing div"
            
    assert total_markers_in_surahs == TOTAL_QURAN_VERSES, f"Expected {TOTAL_QURAN_VERSES} verses, got {total_markers_in_surahs}"
    print(f"  [PASS] Exactly {total_markers_in_surahs:,} verses verified across 114 chapter files.")
    
    # Test Quran-Complete.md
    with open(COMPLETE_FILE, "r", encoding="utf-8") as fh:
        complete_content = fh.read()
        complete_markers = marker_pattern.findall(complete_content)
        assert len(complete_markers) == TOTAL_QURAN_VERSES, f"Complete file expected {TOTAL_QURAN_VERSES} verses, got {len(complete_markers)}"
        print(f"  [PASS] Exactly {len(complete_markers):,} verses verified in Quran-Complete.md.")

def test_pages_and_anchors():
    print(f"Testing 604 Medina Mushaf page anchors in Quran-Complete.md...")
    with open(COMPLETE_FILE, "r", encoding="utf-8") as fh:
        complete_content = fh.read()
        
    for p in range(1, TOTAL_PAGES + 1):
        anchor = f'<a id="page-{p:03d}"></a>'
        assert anchor in complete_content, f"Missing page anchor {anchor} in Quran-Complete.md"
        
    print(f"  [PASS] All {TOTAL_PAGES} page anchors (<a id=\"page-001\"> to <a id=\"page-604\">) resolve in Quran-Complete.md.")
    
    # Test PAGES.md registry
    print(f"Testing PAGES.md registry and link integrity...")
    with open(PAGES_FILE, "r", encoding="utf-8") as fh:
        pages_content = fh.read()
        
    for p in range(1, TOTAL_PAGES + 1):
        page_pattern = f"`{p:03d}`"
        assert page_pattern in pages_content, f"PAGES.md missing entry for page {p:03d}"
        complete_ref = f"Quran-Complete.md#page-{p:03d}"
        assert complete_ref in pages_content, f"PAGES.md missing link {complete_ref}"
        
    print(f"  [PASS] All {TOTAL_PAGES} pages indexed and linked in PAGES.md.")
    
    # Test Option B divider banners in Surah files
    print("Testing Option B page divider banners in Surah files...")
    surah_files = sorted([f for f in os.listdir(SURAHS_DIR) if f.endswith(".md")])
    for f in surah_files:
        filepath = os.path.join(SURAHS_DIR, f)
        with open(filepath, "r", encoding="utf-8") as fh:
            text = fh.read()
            # Assert Option B divider presence
            assert "<sub>─── 📖 صفحة" in text, f"Missing Option B page divider in {f}"
            
    print("  [PASS] Option B centered page divider banners verified across all Surah files.")

def test_surah_links():
    print("Testing cross-linking between files...")
    with open(INDEX_FILE, "r", encoding="utf-8") as fh:
        index_content = fh.read()
        
    assert "PAGES.md" in index_content, "INDEX.md missing reference to PAGES.md"
    
    for f in os.listdir(SURAHS_DIR):
        if not f.endswith(".md"): continue
        with open(os.path.join(SURAHS_DIR, f), "r", encoding="utf-8") as fh:
            surah_text = fh.read()
            assert "PAGES.md" in surah_text, f"{f} missing link to PAGES.md"
            links = re.findall(r"\[.*?\]\(([\w\.-]+\.md(?:#[\w-]+)?)\)", surah_text)
            for link in links:
                target_filename = link.split("#")[0]
                target_path = os.path.join(SURAHS_DIR, target_filename)
                assert os.path.isfile(target_path), f"Broken relative link {link} inside {f}"
                
    print("  [PASS] All cross-links and navigation bars resolve cleanly.")

def main():
    print("=== Running 604-Page Quran Verification Suite ===")
    test_files_exist()
    test_verse_counts()
    test_pages_and_anchors()
    test_surah_links()
    print("=== ALL 604-PAGE INTEGRITY TESTS PASSED (100% Scholarly Precision) ===")

if __name__ == "__main__":
    main()
