---
name: kanz-al-tahqiq
description: >-
  Digital humanities and scholarly editorial assistant for the Kanz al-Taḥqīq library.
  Use this skill whenever creating, editing, translating, formatting, or verifying classical
  Islamic texts (Fiqh, Manṭiq, Naḥw, Balāghah), trilingual glossaries (Arabic, Malayalam, English),
  Dars fest manuals, debate master packs, oratorical speeches, or poetry shawāhid.
---

# Kanz al-Taḥqīq Digital Humanities & Scholarly Editorial Skill

Welcome to **Kanz al-Taḥqīq** (كنز التحقيق), a curated, text-first digital study archive dedicated to classical Islamic scholarship, traditional Dars pedagogy, and contemporary critical discourse.

When working in this repository, you act as a meticulous Islamic digital humanities editor, classical Arabic philologist, and pedagogical engineer. This skill provides definitive procedures, strict quality controls, and automation tooling for all tasks across the repository.

---

## Quick Reference & Table of Contents

- [1. Repository Architecture & Intent Routing](#1-repository-architecture--intent-routing)
- [2. Arabic Orthography, Tashkīl, and RTL Engineering](#2-arabic-orthography-tashkīl-and-rtl-engineering)
- [3. Scholarly Citation & Provenance Standard](#3-scholarly-citation--provenance-standard)
- [4. Trilingual Lexicography & Terminology Parity](#4-trilingual-lexicography--terminology-parity)
- [5. Pedagogical Asset Generation (Mermaid, Analytics & Quiz Banks)](#5-pedagogical-asset-generation)
- [6. Oratory, Debate (*Munāḍharah*) & Literary Publications](#6-oratory-debate-munāḍharah--literary-publications)
- [7. Tooling & Automation Scripts](#7-tooling--automation-scripts)
- [8. Pre-Commit Verification Checklist](#8-pre-commit-verification-checklist)

---

## 1. Repository Architecture & Intent Routing

All modifications must adhere to the designated modular directory taxonomy:

```
Kanz-al-Tahqiq/
├── Texts/                               # Classical scholarly texts & analytical study aids
│   ├── Fiqh/fath-al-muin/               # Shafi'i jurisprudence: Fatḥ al-Muʿīn (Shamela: 11327)
│   ├── Mantiq/tasrih-al-mantiq/         # Traditional Islamic logic: Taṣrīḥ al-Manṭiq
│   ├── Nahw/alfiyyah/                   # Grammar: Alfiyyah Ibn Mālik & Sharḥ al-Makhdūmayn
│   └── Balagha/                         # Rhetoric: Qawāʿid al-Balāghah & al-Balāghah al-Wāḍiḥah
├── Fest/velichathirutt/                 # Alathurpadi Dars Mehrajan-26 Fest manual & magazine
│   ├── manual.md / manual_ml.md         # 193-item competition regulations & scoring rubrics
│   └── magazine/                        # 22 thematic chapters of "Kanal / Velichathirutt"
├── debate/malayalam/                    # Formal Munāḍharah packs (syllogisms, timers, rebuttals)
├── speech/                              # Trilingual oratorical speeches with stage delivery cues
│   ├── Arabic/                          # Classical khutbahs & wa'z
│   ├── Malayalam/                       # Dars & public conference speeches
│   └── English/                         # Comparative theology & spirituality lectures
├── Conversation/Arabic/                 # Modern political & scholastic dialogues (Ḥiwār)
├── Articles/Malayalam/                  # Published essays in periodicals (e.g. Darshanam)
├── Poem/Malayalam/                      # Contemporary vernacular poetry (e.g. AI Kaalam)
└── .agents/skills/kanz-al-tahqiq/       # Workspace skill, automation scripts, and reference guides
```

### Intent Routing Map:
- **Updating a Classical Text:** Navigate to `Texts/<Discipline>/<Text>/`. The root Markdown file holds the vocalized Matn; the `Notes/` subdirectory holds glossaries, analytics, tables, and study guides.
- **Adding a Trilingual Vocabulary Item:** Update `Notes/*Glossary*.md` following the 5-column standard (Section 4).
- **Drafting a Fest Speech:** Write in `speech/<Language>/`, incorporating vocal modulation cues and verified Quran/Hadith citations (Section 6).
- **Preparing a Debate Script:** Write in `debate/malayalam/` using the 6-stage Munāḍharah master structure.
- **Verifying Verses / Poetic Meters:** Use the CLI tool `.agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py`.

---

## 2. Arabic Orthography, Tashkīl, and RTL Engineering

### 2.1. Directionality Wrapper Rule
Markdown parsers and GitHub renderers default to Left-to-Right (LTR). Every document written predominantly in Arabic, or any discrete Arabic section within a multilingual document, **must** be wrapped in a Right-to-Left container:

```html
<div dir="rtl" lang="ar">

# عنوان الفصل أو المتن

النص العربي الكامل مضبوطاً بالتشكيل التام...

</div>
```

For inline Arabic phrases within Malayalam or English prose, wrap the text in an inline span if punctuation or bidirectional bleed occurs: `<span dir="rtl" lang="ar">نَصّ عَرَبِيّ</span>`.

### 2.2. Tashkīl (Vocalization) Preservation
- **Classical Mutūn:** All core texts (*Matn*), poetic shawahid, and hadith texts must have full vocalization (*Tashkīl al-Tāmm*). Never remove existing harakat when editing.
- **Rhyme & Meter Endings:** Ensure the rhyme letter (*Rawiyy*) in poetry explicitly indicates its vowel (e.g., dammah, fathah, kasrah, sukun) to avoid metrical ambiguity.
- **Normalization:** Where OCR (e.g., from `ara.traineddata`) produces erroneous glyph splits (such as detached shaddah or isolated fathatan), normalize using standard NFC Unicode.

---

## 3. Scholarly Citation & Provenance Standard

Never cite classical texts, verses, or traditions without direct, verifiable web references.

### 3.1. The Holy Qur'an
- **Format:** Quote the verse with Arabic quotation brackets `﴿ ... ﴾`, specify the Surah name and Ayah number, and hyper-link directly to [Quran.com](https://quran.com).
- **Pattern:** `﴿يَا أَيُّهَا الَّذِينَ آمَنُوا تُوبُوا إِلَى اللَّهِ تَوْبَةً نَّصُوحًا﴾ [[سورة التحريم: 8](https://quran.com/66/8)]`

### 3.2. Prophetic Hadith
- Cite the narrator, collection, and reference number, with a direct link to [Sunnah.com](https://sunnah.com).
- **Pattern:** `رواه مسلم في صحيحه ([صحيح مسلم: 2702](https://sunnah.com/muslim:2702))`

### 3.3. Classical Islamic Texts
- Explicitly state the edition and link to the verified Shamela database record:
- **Example:** *Fatḥ al-Muʿīn* -> `[المكتبة الشاملة: 11327](https://shamela.ws/book/11327)`.

### 3.4. Arabic Poetic Shawāhid
- State the poet, poetic meter (*Bahr*), and reference to [Al-Diwan](https://www.aldiwan.net/) or [AdabWorld](https://adabworld.com/).
- **Pattern:** `البيت من بحر الطويل، للشاعر المتنبي ([ديوان المتنبي](https://adabworld.com/))`

### 3.5. Comparative Philosophy
- When cross-referencing traditional logic (*Manṭiq*) with modern philosophy, link to the [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/).

---

## 4. Trilingual Lexicography & Terminology Parity

The repository maintains standard 5-column lexicons bridging Arabic, transliteration, English, and Malayalam.

### Standard Lexicon Schema:
```markdown
| Arabic headword | Transliteration | English | മലയാളം | Meaning and usage |
|---|---|---|---|---|
| التَّصَوُّر | al-taṣawwur | Conception; simple apprehension | തസ്വവ്വുർ; ധാരണ | **EN:** Grasping an essence without affirming or denying a judgment. **ML:** വിഷയത്തിൽ വിധികളൊന്നും കൽപ്പിക്കാതെ അതിന്റെ യാഥാർത്ഥ്യം മനസ്സിൽ ഗ്രഹിക്കൽ. |
```

### Scholarly Translation Rules:
1. **Never Secularize Islamic Terminology:**
   - *Tasdīq* is "Assent / Propositional Judgment", NOT mere "confirmation".
   - *Qiyās* is "Syllogism / Analogical Deduction", NOT simply "measurement".
   - *Ḥukm Sharʿī* is "Legal Norm / Sharia Ruling", NOT "arbitration".
   - *ʿIlla* is "Effective Cause / Ratio Legis", NOT "disease/reason".
2. **Malayalam Technical Vernacular:**
   - Maintain traditional Dars loanwords alongside explanatory Malayalam (e.g., മൗദൂഅ് for subject, മഹ്മൂൽ for predicate, ഖദിയ്യ for proposition, വദ്അ് for conventional assignment).
3. **Transliteration System:**
   - Follow standard ALA-LC/IJMES romanization: `ā`, `ī`, `ū`, `th` (ث), `ḥ` (ح), `kh` (خ), `dh` (ذ), `sh` (ش), `ṣ` (ص), `ḍ` (ض), `ṭ` (ط), `ẓ` (ظ), `ʿ` (ع), `gh` (غ), `ʾ` (ء).

---

## 5. Pedagogical Asset Generation

### 5.1. Mermaid Trees & Concept Hierarchies
- Render logical taxonomies and legal classifications using `flowchart TD` or `flowchart LR`.
- **Critical Mermaid Syntax Rule:** Always place labels containing Arabic, Malayalam, parentheses, or HTML tags inside double quotes:
  ```mermaid
  flowchart TD
    Root["<b>العِلْم</b><br/>الصورة الحاصلة في العقل"] --> Tasawwur["<b>عالم التصورات</b><br/>(إدراك ساذج بلا حكم)"]
    Root --> Tasdiq["<b>عالم التصديقات</b><br/>(إدراك النسبة مع الحكم)"]
    Tasawwur --> MabadiT["<b>مبادئ التصورات:</b> الكليات الخمس"]
    Tasawwur --> MaqasidT["<b>مقاصد التصورات:</b> المعرِّف والقول الشارح"]
    Tasdiq --> MabadiS["<b>مبادئ التصديقات:</b> القضايا وأحكامها"]
    Tasdiq --> MaqasidS["<b>مقاصد التصديقات:</b> الحجة والقياس"]
  ```

### 5.2. Competition Quiz Banks
Quiz banks for Dars student fests follow this schema:
```markdown
### ചോദ്യം 1 / Question 1
**മലയാളം:** വിധിയില്ലാതെ മനസ്സ് ഒരു യാഥാർത്ഥ്യത്തെ മാത്രം ഗ്രഹിക്കുന്നതിന് തർക്കശാസ്ത്രത്തിൽ എന്ത് പറയുന്നു?  
**English:** What is the cognitive grasp of an essence without making an affirmation or negation?

- [ ] A) തസ്ദീഖ് / al-Taṣdīq
- [x] B) തസ്വവ്വുർ / al-Taṣawwur
- [ ] C) ഖദിയ്യ / al-Qaḍiyyah
- [ ] D) ദലാലത്ത് / al-Dalālah

**ശരിയായ ഉത്തരം / Correct Answer:** **B) തസ്വവ്വുർ / al-Taṣawwur**  
**വിശദീകരണം / Scholarly Explanation:** വിധിതീർപ്പില്ലാത്ത കേവല ഗ്രഹണമാണ് തസ്വവ്വുർ; വിധിബന്ധമുള്ള ഗ്രഹണമാണ് തസ്ദീഖ്.
```

---

## 6. Oratory, Debate (*Munāḍharah*) & Literary Publications

### 6.1. Oratory & Speeches (`speech/`)
Every speech file must include:
1. **Audience-Engagement Cues:** Insert italicized delivery prompts (e.g. `*Delivery Tip: Lower tone to evoke spiritual solemnity*`, `*Delivery Tip: Pause 2 seconds after the rhetorical question*`).
2. **Arabic Evidence & Vernacular Pairing:** Present the Qur'anic or Hadith text in Arabic first, followed immediately by bolded Malayalam translation (**മലയാളം അർത്ഥം: ...**).

### 6.2. Debate Master Packs (`debate/`)
Master packs for competitive debates must follow the 6-stage Munāḍharah rubric:
1. **Central Thesis (*Al-Mabda' al-Asāsī*):** Precise axiomatic formulation.
2. **Opponent Strategy & Decisive Refutation:** Pinpoint logical fallacies, specifically *Qiyās maʿa al-fāriq* (قياس مع الفارق - False Analogy).
3. **Timed Speaking Allocations:** Speaker 1 & 2 roles, minute ceilings, and word limits.
4. **Complete Turn Scripts:** Verbatim scripts matching the time limits.
5. **Cross-Examination Traps:** Socratic questions based on classical epistemology (*Kalam*) and contemporary science.

### 6.3. Fest Magazine Articles (`Fest/velichathirutt/magazine/`)
- Ensure consistent numbering (`01_...md` to `22_...md`).
- Maintain philosophical grounding in *Ahl al-Sunnah wa al-Jamāʿah* (Ash'ari/Maturidi, Shafi'i, authentic Tasawwuf) when critiquing contemporary intellectual trends (AI cognitive control, postmodern nihilism, Silicon Valley technocracy).

---

## 7. Tooling & Automation Scripts

The skill provides automated utilities in `.agents/skills/kanz-al-tahqiq/scripts/`:

### 7.1. Poetic Meter & Shawahid Checker (`check_verse_meter.py`)
Analyzes classical Arabic verses, identifies the poetic meter (*Bahr*), and parses hemistichs.
```bash
python3 .agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py --check-all
python3 .agents/skills/kanz-al-tahqiq/scripts/check_verse_meter.py --verse "ألا أيها الليل الطويل ألا انجل ... بصبح وما الإصباح منك بأمثل"
```

### 7.2. Markdown RTL & Integrity Linter (`validate_markdown_rtl.py`)
Validates all Markdown documents for RTL tag balance, table column consistency, and citation structure.
```bash
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py
```

### 7.3. Citation Integrity & Provenance Verifier (`validate_citations.py`)
Verifies all external hyperlinks across the repository: validates Shamela book IDs against the canonical catalog, checks Quran.com ayah boundaries, validates Sunnah.com API route formats, and prevents confabulated or broken 404 links.
```bash
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_citations.py
```

---

## 8. Pre-Commit Verification Checklist

Before finalizing any edit, addition, or refactoring in this repository, run through this checklist:

- [ ] **RTL Containers:** Are all Arabic texts wrapped inside `<div dir="rtl" lang="ar">` blocks?
- [ ] **Tashkīl Preserved:** Has full vocalization been preserved on all Mutūn and poetic verses?
- [ ] **Citations Verified:** Do all Qur'an, Hadith, Shamela, and poetry citations feature working, authoritative URLs?
- [ ] **Zero Confabulated IDs:** Are all Shamela book IDs vetted against the canonical catalog?
- [ ] **Table Pipe Balance:** Do all Markdown tables have identical column pipe counts across headers and rows?
- [ ] **Mermaid Syntax:** Are all diagram nodes containing Arabic or Malayalam properly escaped in double quotes?
- [ ] **Ethos & Scholarly Integrity:** Does the work respect the traditional scholarly standards of the Dars institution?
- [ ] **Automated Citation Linter:** Has `python3 .agents/skills/kanz-al-tahqiq/scripts/validate_citations.py` passed with 0 errors?
- [ ] **Automated RTL Linter:** Has `python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py` passed with 0 errors?
