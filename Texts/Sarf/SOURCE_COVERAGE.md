# Sarf Source Coverage Ledger

This ledger maps the three scans to the four Arabic working texts. PDF page numbers mean the page index in the PDF file, not the printed page number. OCR status means text was extracted; it does not mean it was proofread.

## Source scans

| Scan | Pages | SHA-256 |
|---|---:|---|
| mizan.pdf | 125 | 8f9f7ee8c3fec1bc7dd4d1b598deff2670f69725d8e4a78a25518bad18629764 |
| ajnas.pdf | 79 | 2e0c7ade50735af5952f7be4776c94ad127a40d73ac837303d89da2000c736b0 |
| zanjan.pdf | 110 | 00585523ccb6b115b2b3974ba00f1f1e9619921f80c1cec535bfbfbc5a957c66 |

The scans are retained unchanged. These hashes identify the copies used for this transcription pass.

## Provisional page map and review state

| Work or material | Scan span | Markdown destination | Current state |
|---|---|---|---|
| Shared front matter | Pages 1–15 in all three scans | sarf-auxiliary/mabadi-ilm-al-sarf.md and the Sarf index, after review | Not yet OCR-transcribed or collated. Boundaries and duplicate copies still need review. |
| Mīzān | mizan.pdf, pages 16–109 | mizan/mizan.md | All 94 pages received a first-pass OCR extraction and are present in the working text. Pages 16–109 received a structural visual screening pass. Tense and negation paradigms, review exercises, command/prohibition sections, heavy- and light-nūn emphasis chapters, connected-noun paradigms, and printed activities were reorganized as structured text and tables. This is not line-by-line collation; no page has completed full collation, and readings and diacritics remain to be checked. |
| Ajnās al-Ṣughrā | ajnas.pdf, pages 16–32 | ajnas-al-sughra/ajnas-al-sughra.md | All 17 pages received a first-pass OCR extraction. Pages 16–32 have had a visual screening pass; several flattened tables and exercise lines were restructured or corrected. Supplementary spot-checks of PDF pages 17–32 confirmed the opening outline, five-door table, basic- and augmented-triliteral activities, quadriliteral patterns, derived forms, verb classifications, and closing workbook tasks. Clear scan-supported OCR slips were corrected, the quadriliteral chapters and final activities were restructured, and the printed homework was restored as a separate section. These pages are not fully collated. No page has completed line-by-line collation. |
| Ajnās al-Kubrā | ajnas.pdf, pages 33–63 | ajnas-al-kubra/ajnas-al-kubra.md | All 31 pages received a first-pass OCR extraction and are present in the working text. Pages 33–63 received a visual screening pass; supplementary checks covered the irregular augmented forms, quadriliteral patterns, closing counts, and workbook on pages 36–63. Clear OCR slips were corrected, the six annexed patterns and nine intransitive patterns were structured as tables, and the final dialogue was restored as a fill-in exercise. No page has completed line-by-line collation. |
| Zanjān | zanjan.pdf, pages 16–94 | zanjan/zanjan-al-matn.md | All 79 pages received a first-pass OCR extraction and visual structural screening. Earlier passes rebuilt the augmented-form summaries and transitivity lesson, command/emphatic-nūn and participle activities, doubled-verb chapter/workbook, and mithāl/ajwaf/nāqiṣ material. Pages 71–81 received additional checks and restructuring of deficient-verb exercises, the two lafīf lessons, and their workbook; PDF pages 74–77 now include a side-by-side table of the Hijazi and Tamimi forms of اِسْتَحْيَى and restored notes on the final two weak-verb types, with emphatic-form vocalization still under review. On PDF page 80, the marked verbs in the negation and emphatic-nūn exercises are now distinguished in Markdown. Pages 82–88 received a structured hamza-chapter pass; pages 82–87 now include source-ordered verb examples and footnote rules, the full surface-form sequence for رَأَى, and structured conjugation tables for أَرَى. Some emphatic forms and underlying derivations still need a second literal reading. Pages 89–94 received a structured pass on time/place nouns, instrument nouns, and closing exercises. PDF pages 89–92 now include restored source-organized tables and page-specific note summaries, but remain uncollated. PDF pages 71–73, 88, and 93–94 are fully collated line by line. Several rare derivations and detailed paradigms remain unresolved or summarized; every other page remains uncollated. |

OCR can miss or misorder table cells, footnotes, faint marks, and text behind scan watermarks. “Present in the working text” records the extraction pass, not a claim that every printed glyph was captured accurately.

The opening page ranges above are the current working map. Recheck all boundaries against the scans before the shared front matter or appendices are consolidated.

## Shared appendices

| Appendix | Available copies | Destination | State |
|---|---|---|---|
| Rules of iʿlāl and idghām | mizan.pdf pp. 110–111; ajnas.pdf pp. 64–65; zanjan.pdf pp. 95–96 | sarf-auxiliary/qawaid-al-itilal-wal-idgham.md | Not yet collated. Compare repeated copies and preserve meaningful differences. |
| Glossary | mizan.pdf pp. 112–120; ajnas.pdf pp. 66–74; zanjan.pdf pp. 97–105 | sarf-auxiliary/mujam-alfaz-al-ajnas.md | Not yet collated. Check entries, examples, ordering, and meanings against a scan. |
| References | mizan.pdf p. 121; ajnas.pdf p. 75; zanjan.pdf p. 106 | Sarf index or provenance sections | Not yet reviewed. |
| Contents/index | mizan.pdf pp. 122–125; ajnas.pdf pp. 76–79; zanjan.pdf pp. 107–110 | Sarf index and work READMEs | Not yet reviewed. Use to confirm section sequence and printed pagination. |

## Review-state definitions

- OCR draft — extracted by OCR and not yet collated.
- Spot-checked — one or more readings compared visually; the page is not fully collated.
- Collated — the entire page, including table layout, footnotes, and diacritics, has been checked against the scan.
- Query — an unresolved reading or layout question is recorded.
- Excluded — a page is outside the work or duplicate material; document why.

Zanjān PDF pages 71–73, 88, and 93–94 are currently marked fully collated. The targeted comparisons of pages 74–87, including the expanded hamza paradigms and page 80 exercise markings, are structural checks only; they do not make those pages collated. Mīzān's structural screening covers PDF pages 16–109, including the emphatic verb paradigms, final noun chapter, and exercises. PDF pages 104–109 were additionally checked while rebuilding the closing emphatic activities and noun chapter; this was a coverage and structure check, not a glyph-by-glyph collation. For Ṣughrā, PDF pages 17–32 were spot-checked against the opening chapters, paradigms, and workbook; exercise sequences and final chapters were given clearer headings and lists, and several pattern readings were corrected from the scan. These checks do not make any page collated. Ṣughrā's screening pass corrected the presentation of the five-door reference table, the second exercise model and its ten examples, the fourteen augmented-form examples, the quadriliteral examples, and the verb-classification table. Kubrā's screening pass and follow-up checks rebuilt its annexed-pattern summaries, corrected clear irregular-form OCR slips, restored the closing count tables, and preserved the dialogue blanks; all readings still need glyph-by-glyph comparison. Zanjān's visual structural screening now covers pages 16–94, including the final weak-verb material, hamza chapter, noun patterns, and printed activities. Several rare forms remain unresolved. Keep all PDFs until every in-scope page has passed collation and the release checks in the implementation plan.
