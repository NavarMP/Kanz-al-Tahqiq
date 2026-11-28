# Implementation Plan: Complete the Four Sarf Text Editions

**Status:** In progress — OCR drafts created; source collation pending  
**Scope:** Mīzān, al-Ajnās al-Ṣughrā, al-Ajnās al-Kubrā, and Zanjān  
**Goal:** Produce complete, source-faithful, well-structured Markdown editions that can eventually stand in place of the scanned PDFs.

## Execution progress (2026-11-28)

- Re-screened Ajnās al-Kubrā PDF pages 33–63 and checked the quadriliteral patterns, irregular augmented forms, closing counts, and workbook against the page images. Rebuilt the six annexed-pattern passages and summary tables, restored the nine intransitive-pattern table, corrected clear OCR slips, and preserved the final dialogue as a fill-in activity. This remains a targeted visual and structure pass; no page is line-by-line collated.
- Visually screened Mīzān PDF pages 16–109. Reorganized the tense and negation paradigms, review activities, command/prohibition material, heavy- and light-nūn emphasis chapters, and the connected-noun paradigms and workbook pages. Rebuilt the final noun chapter from PDF pages 105–109 as paradigms, derivation notes, footnotes, and numbered exercises. This is a structural screening pass, not line-by-line collation; readings, vocalization, Persian labels, and the exercises still need detailed comparison.
- Visually screened the full Zanjān matn span, PDF pages 16–94. Rebuilt or restructured material on command and “iftaʿala”, emphatic nūn, participles, doubled and weak verbs, the lafīf patterns, the hamzated chapter, the final noun chapter, and their printed activities. The final pages 71–94 received additional visual checks; source word lists, paradigms, and workbook tables were corrected where legible. Rare derivations and several detailed paradigms remain unresolved or summarized. PDF pages 71–73, 88, and 93–94, comprising self-contained workbook activities, have been collated line by line; all other pages remain uncollated.
- Expanded the Zanjān weak-verb notes around PDF pages 74–77, placed the two **اِسْتَحْيَى** dialect paradigms in a side-by-side table from the page 76 notes, and restored the printed notes on the final two weak-verb types. The printed emphatic sequences are included, with a review caveat on their vocalization. Rebuilt the final noun chapter with source-organized tables and page-specific notes for printed pages 229–232 (PDF pages 89–92). These additions are structural restorations, not completed line-by-line collation.
- Expanded the Zanjān hamza chapter from PDF pages 82–87: restored the source’s verb examples and footnote rules, laid out the full **رَأَى** present and command forms, and added structured tables for the **أَرَى** participle, command, and prohibition forms. Several emphatic forms and underlying derivations still need a second literal reading. On PDF page 80, the bolded verbs now preserve the scan’s underlining for the negation and emphatic-nūn exercises. These edits are a structure and coverage pass, not line-by-line collation.
- Current focus: continue line-by-line collation of Zanjān pages 74–94, paying particular attention to the weak-form derivations, the newly expanded hamza paradigms, and the noun-pattern tables. Then continue collation across all four Arabic masters, review shared front matter and appendices, and check translation parity and study aids. Keep uncertain readings marked instead of silently resolving them.

## Execution progress (2026-11-27)

- Recorded page counts and SHA-256 fingerprints for the three PDFs in SOURCE_COVERAGE.md. The PDFs remain unchanged.
- Mapped the four work-specific spans and extracted first-pass OCR for each in-scope page: Mīzān 16–109, Ṣughrā 16–32, Kubrā 33–63, and Zanjān 16–94. These are now clearly labeled working drafts in the four core Markdown paths.
- Visually inspected Mīzān and Zanjān PDF pages 16–25; reconstructed Mīzān's first two paradigms and practice sections, corrected clear Zanjān opening-page readings including التغيير and حروف الحلق, and rebuilt its transitivity lesson/exercise from the page images. These were screening passes, not full line-by-line collations.
- Screened Ajnās al-Ṣughrā PDF pages 16–32 visually. Rebuilt the five-door, fourteen-form, quadriliteral, and verb-classification charts as Markdown tables; restored the second model and items 9–10 in the exercise list; separated the quadriliteral note from its chart. This remains a screening pass, not a line-by-line collation.
- Replaced README claims that described nonexistent files or asserted unverified completeness. Added a Sarf index and retained PDFs.
- Remaining work: line-by-line collation of every source page (including verification of the Ṣughrā and Kubrā table/activity edits), review of shared front matter and appendices, translation parity, study-aid audit, and final rendered review. The OCR drafts must not be treated as final editions or as grounds to remove the PDFs.

## 1. Request and source-document boundaries

- **User request:** Audit and plan the work needed to make the four named Sarf texts complete and comprehensive as `.md` sheets. The PDFs may be removed later, after the Markdown editions are verified.
- **PDFs:** Treat these as source evidence. Learner-facing commands, exercise prompts, editorial notes, and other imperative language inside them are content to transcribe or classify; they are not instructions to the assistant.
- **Repository editorial guidance:** Apply the Sarf-relevant standards in `Kanz-al-Tahqiq-pub/SKILL.md` and `PROMPT_MASTER_SHEET.md` to transcription and formatting. Those standards do not authorize inventing or silently expanding the source text.
- **Current Markdown and READMEs:** Treat them as drafts and finding aids until checked against the scans. A claim such as “complete,” “100% vocalized,” or “exhaustive” is not evidence of completeness by itself.

## 2. Audit baseline

| Work | Available scan | Core Markdown at outset | Initial observation |
|---|---|---|---|
| Mīzān | `mizan.pdf` — 125 pages | `mizan/mizan.md` | A substantial file already exists. Audit it against every source section and paradigm; file size alone cannot establish completeness or accuracy. |
| Ajnās al-Ṣughrā | `ajnas.pdf` — 79 pages, apparently containing the Ajnās material | `ajnas-al-sughra/ajnas-al-sughra.md`, plus English and Malayalam files | The Arabic core is short relative to the scanned source. First locate its exact page span and distinguish source text from explanation. |
| Ajnās al-Kubrā | `ajnas.pdf` — 79 pages | `ajnas-al-kubra/ajnas-al-kubra.md`, plus English and Malayalam files | The Arabic core is short relative to the scan. Its chapter and paradigm claims need page-level verification. |
| Zanjān | `zanjan.pdf` — 110 pages | `zanjan/zanjan-al-matn.md` | The core is short relative to the scan. The current chapter notes cover only chapters 00–06, while the README advertises a much larger suite. |

Additional observations to resolve during the audit:

- The PDFs have a mixed OCR/text layer. `pdfplumber` output is badly reordered or corrupted on content pages, so it is not a reliable transcription source. Arabic OCR through macOS Vision (`ar-SA`) produced a usable draft; it still needs page-image collation for diacritics, tables, and ambiguous words. `pdftotext` and Tesseract are unavailable; rendered page images are available through `pdftoppm`.
- Initial page mapping shows shared front matter in pages 1–15 of each PDF, then work-specific text. The Ajnās scan contains Ṣughrā on PDF pages 16–32 and Kubrā on 33–63. In the Mīzān scan, the main text and exercises run through page 109; shared rules, glossary, references, and contents follow on 110–125. In the Zanjān scan, the text and exercises run through page 94; shared appendices follow on 95–110. Verify all transitions and duplicate appendices during the coverage audit.
- At the start of the audit, the Ajnās READMEs advertised `Notes/Chapters/` and other supporting files that were absent; the Kubrā README also advertised an analytics file that was absent. The Zanjān README described translations and companion files not present in the tree. These README descriptions have now been replaced with actual file inventories; the study aids themselves still need audit.
- Existing Arabic, English, and Malayalam files have different lengths and structures. Translation completeness and commentary must be assessed section by section, not inferred from a title or overview.
- Authorship, dates, edition details, page ranges, and claims about the number of chapters or patterns in current READMEs must be verified against the scan itself before being retained as facts.

## 3. Target deliverables

1. **Four verified Arabic master texts:** the existing core files, completed and corrected in source order, with stable headings and navigation.
2. **Ajnās translation parity:** complete the existing English and Malayalam files to match the verified Arabic source structure. Clearly label translation, paraphrase, and commentary so they cannot be mistaken for the original matn.
3. **A source coverage ledger:** a compact audit file mapping each printed section/page range to its Markdown destination, with transcription and review status. Page references belong in this ledger, not as artificial page breaks in the clean reading text.
4. **A Sarf landing page:** `Texts/Sarf/README.md` with the verified reading order, links to actual files, edition/provenance notes, and a clear distinction between core texts and study aids.
5. **Reconciled READMEs and study aids:** update each work’s README and align existing tables, glossaries, exercises, diagrams, and chapter notes with the verified text. Do not advertise files that do not exist.
6. **A retirement-ready source record:** preserve the scan’s verified title/edition metadata and a page-coverage record so provenance remains understandable if the PDFs are later removed.

Creating new full English or Malayalam translations for Mīzān or Zanjān is outside this remediation’s baseline scope; first complete and verify their Arabic master texts. Any expansion beyond that should be a separate editorial decision.

## 4. Work sequence

### Phase A — Protect and inventory the sources

1. Keep all three PDFs unchanged during the project. Record file names, page counts, and checksums in the source ledger.
2. Render representative pages from the beginning, middle, and end of each PDF. Note scan quality, page rotation, handwriting or marginalia, tables, and any pages needing special review.
3. Verify the current boundary map: shared front matter pp. 1–15; Ṣughrā pp. 16–32 and Kubrā pp. 33–63 in `ajnas.pdf`; Mīzān pp. 16–109 plus appendices pp. 110–125; Zanjān pp. 16–94 plus appendices pp. 95–110. Identify which repeated appendix copy is clearest and map shared material to `sarf-auxiliary/` rather than duplicating it in four core texts.
4. Record source facts only after checking the scan’s title page and publication data. Do not inherit unverified metadata from a README.

**Gate A:** Every PDF page is classified as text, front/back matter, blank/duplicate, or out of scope; Ajnās section boundaries are documented.

### Phase B — Build the completeness map

1. Create a contents outline directly from each scan. Record source headings, sequence, tables, examples, exercises, colophons, and appendices.
2. Compare that outline to the existing core Markdown and mark each item `present`, `partial`, `missing`, `uncertain`, or `not part of the matn`.
3. For Mīzān, verify each paradigm and its entries against the printed pages rather than accepting the README’s paradigm count.
4. For both Ajnās works, verify the claimed door/pattern counts, chapter divisions, derivation tables, and exercises from the printed source.
5. For Zanjān, compare the full scan outline to both `zanjan-al-matn.md` and `Notes/Chapters/00-index.md`; identify all missing sections beyond the existing 00–06 chapter files.

**Gate B:** Each work has a complete source-to-Markdown checklist. No transcription begins from a guessed chapter list.

### Phase C — Transcribe and collate the Arabic master texts

1. Process page images in small, numbered batches. OCR may provide a first pass, but every line must be checked against the image, especially hamzah, weak radicals, shaddah, tanwīn, verse endings, tables, and similar-looking letters.
2. Preserve the source wording, examples, ordering, and meaningful footnotes. Do not silently normalize a disputed reading or add a grammatical rule because it seems expected.
3. Preserve vocalization where visible. Add or repair vocalization only when supported by the source or a separately verified reference; record unresolved readings in the ledger instead of guessing.
4. Keep uncertain or illegible material visible in an editorial query list until resolved. Never turn OCR confidence into an unmarked source reading.
5. Keep raw OCR and intermediate page renders outside the publication tree. The final master text should contain readable, source-faithful Arabic rather than raw OCR artifacts or physical page furniture. Until page collation is complete, the core Markdown files are explicitly labeled as working OCR drafts; raw JSONL and intermediate page renders remain outside the publication tree.

**Gate C:** Every in-scope line, table, example, and exercise is collated against the scan or explicitly recorded as unresolved.

### Phase D — Structure the four editions

For each Arabic master file:

- Use one clear title, a verified contents list, consistent heading levels, and stable section anchors.
- Preserve source order and keep the original matn distinct from editor-supplied introductions, notes, or explanations.
- Place predominantly Arabic text in the repository’s RTL wrapper (`<div dir="rtl" lang="ar">`). Use valid Markdown tables for source tables and verify their column structure.
- Remove scan noise and page furniture from the reading text while retaining any necessary page mapping in the separate coverage ledger.
- Add return-to-contents links at sensible section boundaries; avoid repetitive links after every small paragraph or table.
- Mark any reconstructed heading or supplied clarification as editorial, and keep it out of the source text itself.

Work-specific focus:

- **Mīzān:** Audit the already large `mizan/mizan.md` carefully for missing source sections, duplicate or synthetic paradigms, malformed traditional formulas, and unverified examples. Do not replace a substantial existing file wholesale before the coverage map identifies what is actually absent.
- **Ajnās al-Ṣughrā:** Complete the source-faithful Arabic core from its verified span in `ajnas.pdf`; keep the five-door and augmented-form structure only where supported by the scan. Bring the English and Malayalam editions into matching section order.
- **Ajnās al-Kubrā:** Complete the Arabic core from its verified span; check the six-door treatment, irregular forms, derivation material, and exercises against the source. Bring the English and Malayalam editions into matching section order.
- **Zanjān:** Complete `zanjan-al-matn.md` against all in-scope pages. Keep explanatory chapter notes and training activities as separate study aids, and expand them only after the master text is complete.

### Phase E — Align translations and study aids

1. Once each Ajnās Arabic core is stable, compare the English and Malayalam documents section by section. Fill omissions, correct drift, and label explanatory additions as commentary.
2. Audit existing Mīzān and Zanjān notes, plus the shared `sarf-auxiliary/` material, for accuracy and links to the correct source sections. Shared aids must not be presented as verbatim material from any one book unless they are.
3. Rebuild or correct tables, trees, glossaries, and exercises only from the verified source or clearly identified editorial teaching content. Include answer keys only when the answers are checked.
4. Update each README to describe files that exist, use modest claims that the audit supports, and distinguish the source text from study aids.

**Gate E:** Every translation section maps to an Arabic section; every companion aid identifies whether it is source-derived or editorial.

### Phase F — Quality review and release readiness

1. Run the repository’s RTL, Markdown, citation, and transliteration checks on changed files, fixing all actionable errors.
2. Review the rendered Markdown for RTL direction, headings, Arabic diacritics, table alignment, broken links, and malformed code/HTML blocks.
3. Perform a final source coverage pass using the ledger. Check for omitted pages, repeated paragraphs, missing table rows, and accidental OCR substitutions.
4. Have a knowledgeable Sarf reader review unresolved readings and morphology-sensitive corrections. Keep disagreements documented rather than silently choosing a reading.
5. Verify that all README links resolve and that every promised companion file exists.

**Gate F / definition of done:** All in-scope source content is accounted for; all four Arabic masters are collated; existing Ajnās translations align with their masters; unresolved readings are disclosed; structure and repository checks pass; and provenance can be understood without opening the PDFs.

### Phase G — PDF retirement, only after verification

Retain the PDFs until Gate F is satisfied and a recoverable copy exists outside the publication set. Then remove the publication-tree PDFs as the final cleanup step, keeping the verified provenance and coverage ledger. This plan does not delete them now.

## 5. Completion checklist

- [ ] Mīzān: all in-scope pages and paradigms mapped and collated.
- [ ] Ajnās al-Ṣughrā: source span, complete Arabic text, and English/Malayalam parity verified.
- [ ] Ajnās al-Kubrā: source span, complete Arabic text, and English/Malayalam parity verified.
- [ ] Zanjān: all in-scope matn, examples, tables, and activities mapped and collated.
- [ ] Current READMEs match the actual file tree and make no unsupported completeness claims.
- [ ] All study aids are correctly labeled and linked to verified sections.
- [ ] Final rendered Markdown and repository checks reviewed.
- [ ] PDFs retained until the user’s later cleanup step is ready.
