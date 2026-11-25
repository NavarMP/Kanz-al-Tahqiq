# Repository instructions

## Project shape

This is a text-first digital humanities archive, not an application with a package build or framework. Most changes are UTF-8 Markdown and companion media. The README.md is the collection overview; `SKILL.md` and `.agents/skills/kanz-al-tahqiq/SKILL.md` are the detailed editorial specifications.

- `Texts/<discipline>/<work>/` contains classical source text plus translations and `Notes/`.
- `Texts/Mantiq/tasrih-al-mantiq/`, `Texts/Fiqh/fath-al-muin/`, and `Texts/Nahw/alfiyyah/` are the main maintained study-text collections.
- `Articles/Malayalam/`, `speech/<Arabic|English|Malayalam>/`, and `debate/<arabic|malayalam>/` contain public-facing prose and stage material.
- `Conversation/`, `Poem/`, `Song/`, and `games/` hold supplementary material.
- `.agents/skills/kanz-al-tahqiq/` owns scholarly editorial rules, references, and validation scripts.
- `.agents/skills/kanz-vocal-arts/` owns the optional Markdown-to-audio production pipeline.
- `test_verses.py` is a small poem-corpus fixture, and `.agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py` carries the active 26-verse verification corpus.

## Verification commands

There is no package manifest or full application test suite. Run repository checks directly with Python 3:

```bash
# Load the standalone verse fixture
python3 test_verses.py

# Audit all indexed poetic shawahid
python3 .agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py --check-all

# Analyze or look up one verse
python3 .agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py --verse "فإن يك بعض الناس سيفا لدولة"

# Validate RTL containers, div balance, fences, and table pipes
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py

# Validate one Markdown subtree (the script's --dir option accepts a directory)
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py --dir Texts/Mantiq

# Validate citations and Shamela/Quran/Sunnah routes across Markdown and DOCX
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_citations.py
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_citations.py --dir debate

# Treat linter warnings as failures
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py --strict
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_citations.py --strict
```

The RTL linter currently reports some repository warnings even when it finds no structural errors. The strict mode is appropriate for changed files only when their existing warnings have been resolved.

## Editorial conventions

- Keep source text, translation, study commentary, speeches, and other derived layers distinguishable. Do not silently merge a translation or AI-assisted draft into the classical source.
- Preserve existing Arabic vocalization (`tashkīl`) and NFC Unicode. Do not remove harakat, rhyme vowels, or OCR-corrected forms while formatting.
- Wrap predominantly Arabic documents or substantial Arabic sections with `<div dir="rtl" lang="ar">`; close with `</div>`. Keep inline Arabic isolated with `<span dir="rtl" lang="ar">...</span>` when mixed with Malayalam or English.
- Keep math blocks and formulas in LTR containers so bidirectional rendering does not alter them.
- Mermaid labels containing Arabic, Malayalam, parentheses, or HTML tags must use double-quoted node labels.
- Follow the repository's trilingual lexical schema: Arabic headword, transliteration, English, Malayalam, and usage/meaning. Use the transliteration conventions in `.agents/skills/kanz-al-tahqiq/references/trilingual_terminology_map.md`.
- Record the edition, author/work, publisher, page or section, and stable source URL when they are known. Mark preliminary, machine-assisted, OCR-derived, or unreviewed text explicitly.
- Qur'an citations must use Quran.com with valid surah/ayah routes. Prophetic hadith citations must use a verified Sunnah.com route. Classical text IDs must match the Shamela catalog; do not reuse an unrelated or dead ID.
- Poetry/shawāhid entries should identify the poet and meter and link to a verifiable poem source. Update both `test_verses.py` and `check_verse_meter.py` when intentionally changing its 26-verse corpus.

## Audio work

Audio production is optional and self-contained under `.agents/skills/kanz-vocal-arts/`. Use the unified runner for a complete release:

```bash
python3 .agents/skills/kanz-vocal-arts/scripts/produce_art.py \
  path/to/script.md \
  --genre speech \
  --title "Title" \
  --artist "Kanz al-Taḥqīq"
```
