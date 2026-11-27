# Sarf Source Coverage Ledger

This is the working map from the supplied scans to the Markdown editions. PDF page numbers below refer to the page index in each file, not the printed page number. The scans remain the authority until the transcription is collated. **OCR status means a draft was extracted; it does not mean the text has been proofread.**

## Source scans

| Scan | PDF pages | Working mapping | Status |
|---|---:|---|---|
| `mizan.pdf` | 125 | Mīzān, followed by shared Sarf appendices | OCR draft extracted; review pending |
| `ajnas.pdf` | 79 | Ajnās al-Ṣughrā, Ajnās al-Kubrā, followed by shared Sarf appendices | OCR draft extracted; review pending |
| `zanjan.pdf` | 110 | Zanjān, followed by shared Sarf appendices | OCR draft extracted; review pending |

The first 15 PDF pages appear to be the same front matter in all three scans. The appendix material also repeats across scans. Keep one verified copy of shared material in the shared Sarf files and link to it from each work instead of creating duplicate transcriptions.

## Work coverage

| Work/source range | Source contents identified so far | Markdown destination | Coverage / next action |
|---|---|---|---|
| Shared front matter: pp. 1–15 in all three scans | Third-edition preface, introduction, importance/history of ṣarf, ten principles, biographical/contextual pages | `sarf-auxiliary/mabadi-ilm-al-sarf.md` and Sarf landing page, after boundary review | Existing aid is not yet checked against the scans; identify what belongs in the shared guide versus the individual matn. |
| Mīzān: `mizan.pdf` pp. 16–109 | Title and proem; verb classifications; extensive 14-form paradigms; active/passive, imperative/prohibitive, emphatic nūn, derived nouns; exercises throughout | `mizan/mizan.md`; selected practice material may link to `mizan/Notes/04_pedagogical_drills.md` | Existing file is substantial but not page-verified. Match every source table, form, and exercise; separate core exposition from the exercises only when the source boundary is clear. |
| Ajnās al-Ṣughrā: `ajnas.pdf` pp. 16–32 | Title; five unaugmented triliteral doors; 14 augmented doors; quadriliteral patterns; seven verb classes; exercises | `ajnas-al-sughra/ajnas-al-sughra.md`; English and Malayalam counterparts; current `Notes/` study aids | Existing Arabic file is a partial editorial edition. Transcribe the full source sequence, including source exercises or a clearly linked complete exercise sheet. Check translation parity. |
| Ajnās al-Kubrā: `ajnas.pdf` pp. 33–63 | Title; transitive/intransitive proem; six triliteral doors; irregular forms; augmented and quadriliteral patterns; conclusion; extensive activities, tables, and dialogue practice | `ajnas-al-kubra/ajnas-al-kubra.md`; English and Malayalam counterparts; current `Notes/` study aids | Existing Arabic file is a partial editorial edition. Transcribe the full source sequence and reconcile the current 20-form claims with the scan. Check translation parity. |
| Zanjān: `zanjan.pdf` pp. 16–94 | Title and author note; matn chapters on verb classes, conjugation, weak and hamzated verbs, derived nouns; exercises interleaved; final activities on pp. 93–94 | `zanjan/zanjan-al-matn.md`; chapter notes and `Notes/Zanjan-Anshitah-Tadribiyyah.md` | Existing core and chapter notes cover only part of the scanned material. Map every matn section and every exercise before deciding what stays in the core file. |

## Shared appendix coverage

| Appendix | Available scan copies | Existing destination | Next action |
|---|---|---|---|
| Rules of iʿlāl/idghām | `mizan.pdf` pp. 110–111; `ajnas.pdf` pp. 64–65; `zanjan.pdf` pp. 95–96 | `sarf-auxiliary/qawaid-al-itilal-wal-idgham.md` | Compare all copies; transcribe one verified version and note meaningful differences. |
| Morphological glossary | `mizan.pdf` pp. 112–120; `ajnas.pdf` pp. 66–74; `zanjan.pdf` pp. 97–105 | `sarf-auxiliary/mujam-alfaz-al-ajnas.md` | The scans include an alphabetical glossary with examples and meanings. Check completeness, spelling, and ordering against each duplicate copy. |
| References | `mizan.pdf` p. 121; `ajnas.pdf` p. 75; `zanjan.pdf` p. 106 | Shared Sarf landing page or provenance section | Verify bibliographic spellings against the page image and preserve only references actually listed in the source. |
| Contents/index | `mizan.pdf` pp. 122–125; `ajnas.pdf` pp. 76–79; `zanjan.pdf` pp. 107–110 | Sarf landing page plus each work’s contents section | Use to verify the chapter outline and printed pagination; do not mistake the printed contents for matn text. |

## Review states

Use these values for the detailed page-by-page audit as it is completed:

- `not reviewed` — no source comparison yet.
- `OCR draft` — machine transcript exists but has not been collated.
- `collated` — text checked against the rendered source page.
- `query` — uncertain reading or layout issue requires an editorial decision.
- `excluded` — page is duplicate, blank, publisher matter, or outside the requested work; record the reason.

Current state: all work-specific PDF pages listed above have OCR drafts in a temporary workspace. No page has yet been fully collated, so all publication files remain subject to source review.
