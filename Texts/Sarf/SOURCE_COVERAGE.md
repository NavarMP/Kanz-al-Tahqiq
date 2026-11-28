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
| Ajnās al-Ṣughrā | ajnas.pdf, pages 16–32 | ajnas-al-sughra/ajnas-al-sughra.md | All 17 pages received a first-pass OCR extraction. Pages 16–32 have had a visual screening pass; several flattened tables and exercise lines were restructured or corrected. A further spot-check of PDF pages 17–20 confirmed the opening outline, five-door table, footnote, and first practice sequence; these pages are not fully collated. No page has completed line-by-line collation. |
| Ajnās al-Kubrā | ajnas.pdf, pages 33–63 | ajnas-al-kubra/ajnas-al-kubra.md | All 31 pages received a first-pass OCR extraction and are present in the working text. Pages 33–63 have had a visual screening pass; pattern tables and workbook sections were restructured. No page has completed line-by-line collation. |
| Zanjān | zanjan.pdf, pages 16–94 | zanjan/zanjan-al-matn.md | All 79 pages received a first-pass OCR extraction and are present in the working text. Pages 16–25 received a visual screening pass; the augmented-form summaries and transitivity lesson/exercise were restructured from the scan. This was not line-by-line collation; all ten screened pages and the rest of the span remain uncollated. |

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

No page is currently marked fully collated. Mīzān's structural screening now covers PDF pages 16–109, including the emphatic verb paradigms, final noun chapter, and exercises. PDF pages 104–109 were additionally checked while rebuilding the closing emphatic activities and noun chapter; this was a coverage and structure check, not a glyph-by-glyph collation. For Ṣughrā, PDF pages 17–20 were spot-checked against the opening chapters and activities and the first exercise blocks were given clearer headings and lists. These checks do not make any page collated. Ṣughrā's screening pass corrected the presentation of the five-door reference table, the second exercise model and its ten examples, the fourteen augmented-form examples, the quadriliteral examples, and the verb-classification table. Kubrā's screening pass rebuilt its quadriliteral pattern summaries, closing count tables, and workbook outline; these readings and all restructured tables still need glyph-by-glyph comparison. Zanjān's screening pass covered pages 16–25 and reconstructed the transitivity lesson and paired exercise; it was not line-by-line collation. Keep all PDFs until every in-scope page has passed collation and the release checks in the implementation plan.
