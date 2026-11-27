# Arabic Text Repair: Implementation Plan

**Status:** Core implementation complete; full scholarly collation remains editorial work.

## 1. Identify the failure — complete

The Arabic in the generated editions came from `ar_raw`, an OCR extraction with letters separated, reordered, or split across hemistichs. The generator's Arabic cleanup only collapsed spaces, so it reproduced the damaged text in the main edition, chapters, and index.

## 2. Establish a canonical text source — complete

- Added `ar_sadr` and `ar_ajuz` as the publishable first and second hemistichs for all 188 verses in `scripts/verses_188.json`.
- Kept `ar_raw` for provenance; the generator no longer publishes it.
- Recorded `ar_source` on each verse to distinguish scan-based transcription from digital cross-checks.
- Used the supplied print scan as the controlling witness and corrected obvious line-wrap fragments in the canonical fields. Digital transcriptions are cross-checks and may preserve variant readings.

## 3. Make generation fail safely and render RTL consistently — complete

- Resolve the project directory relative to the generator so it can run from another checkout.
- Require both canonical hemistich fields; missing Arabic stops generation instead of silently emitting partial verses.
- Strip invisible bidirectional controls and normalize whitespace only. Do not guess at OCR repairs in the build step.
- Wrap each hemistich in an Arabic right-to-left span in the main edition, study edition, chapter excerpts, and concordance.
- Remove unsupported claims that the entire text has been critically verified or that meter has been automatically checked.

## 4. Rebuild published files — complete

Regenerate the Arabic and Malayalam editions, all 14 chapter files, the concordance, study materials, README, and Sharh index from the canonical fields. Review representative opening, middle, and closing verses, including passages whose OCR had split words across lines.

## 5. Editorial follow-up — ongoing

Compare all 188 canonical couplets and their vocalization against the supplied print scan, recording genuine edition differences separately from OCR or layout errors. Have uncertain readings reviewed by a qualified Arabic editor before presenting the text as a critical edition. The current digital text is a repaired reading edition, not a claim of a fully collated critical edition.
