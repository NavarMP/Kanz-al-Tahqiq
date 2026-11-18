# Right-to-Left (RTL) Markdown & Typography Guidelines

This reference guide establishes the typographic and structural standards for handling Arabic script, bidirectional text, and multilingual Markdown files across **Kanz al-Taḥqīq**.

---

## 1. The Core RTL Rule

Markdown and browser renderers default to **Left-to-Right (LTR)** layout. Without explicit directionality tags, Arabic text suffers from:
- Punctuation flipping (periods, question marks, and parentheses appearing on the wrong side).
- Number reversal in bidirectional strings.
- Right-edge misalignment in headings, bullet lists, and paragraphs.

### Mandatory Container Tag:
Every Markdown file written primarily in Arabic, or any discrete Arabic section, must be wrapped in:

```html
<div dir="rtl" lang="ar">

# عنوان رئيسي

نص عربي فقري مع علامات الترقيم بشكل صحيح.

- النقطة الأولى
- النقطة الثانية

</div>
```

---

## 2. Mixed Bidirectional Text (Trilingual Documents)

When presenting English, Malayalam, and Arabic in the same document (e.g. in `speech/` or `Notes/*Glossary*.md`), use intentional isolation:

### Pattern A: Arabic Section with Vernacular Explanation
```markdown
<div dir="rtl" lang="ar">
إِخْوَتِي، إِنَّ الْإِنْسَانَ ضَعِيفٌ بِطَبْعِهِ، يُخْطِئُ وَيُذْنِبُ.
</div>

**മലയാളം അർത്ഥം:** സഹോദരങ്ങളെ, മനുഷ്യൻ പ്രകൃത്യാ ദുർബലനാണ്; അവൻ തെറ്റുകൾ ചെയ്യും.
```

### Pattern B: Inline Arabic within LTR Text
When quoting a short Arabic phrase in English or Malayalam prose:
```markdown
The concept of **Taṣawwur** (<span dir="rtl" lang="ar">التَّصَوُّر</span>) signifies simple apprehension without judgment.
```

---

## 3. Tables and Directionality

### LTR Tables with Arabic Headwords:
For glossaries where the column order is designed for English/Malayalam readers (`Arabic | Transliteration | English | Malayalam`), the outer document is LTR. In this case, ensure the Arabic headword cell explicitly includes proper vocalization and spans if necessary:

```markdown
| Arabic headword | Transliteration | English | മലയാളം | Meaning and usage |
|---|---|---|---|---|
| التَّصْدِيق | al-taṣdīq | Propositional Assent | തസ്ദീഖ്; വിധിതീർപ്പ് | **EN:** Grasping a relationship with judgment. **ML:** മൗദൂഇലും മഹ്മൂലിലുമുള്ള വിധിബന്ധം. |
```

### Purely Arabic Tables:
When the table itself is intended for Arabic readers, place the entire table inside `<div dir="rtl" lang="ar">`:

```html
<div dir="rtl" lang="ar">

| المبحث | عدد الفصول | النسبة المئوية |
|---|---:|---:|
| عالم التصورات | 7 | 29.2% |
| عالم التصديقات | 18 | 70.8% |

</div>
```

---

## 4. KaTeX Math and RTL Compatibility

Antigravity and standard GitHub Markdown renderers parse KaTeX math (`$...$` or `$$...$$`).
- **Never place mathematical formulas inside RTL HTML containers**, as KaTeX layout engines expect LTR directionality.
- If an Arabic document contains formulas or formal symbolic logic, place the math block outside the RTL div or wrap the formula in an LTR container:
  ```html
  <div dir="ltr" align="center">

  $$P \land Q \implies R$$

  </div>
  ```

---

## 5. Automated Verification

Always verify RTL tags before committing:
```bash
python3 .agents/skills/kanz-al-tahqiq/scripts/validate_markdown_rtl.py
```
