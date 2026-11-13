<div align="center">
  <img src="assets/kanz-al-tahqiq-hero.jpg" alt="An illuminated open manuscript resting beneath warm light on a dark teal desk" width="100%" />

  <h1>Kanz al-Taḥqīq · كنز التحقيق</h1>
  <p><strong>A carefully arranged study library for classical texts, translations, notes, and teaching materials.</strong></p>
  <p>العربية · English · മലയാളം</p>

  <p>
    <a href="#the-collection">Explore the collection</a> ·
    <a href="#contribute">Contribute</a> ·
    <a href="#sources-and-editorial-notes">Sources &amp; editorial notes</a>
  </p>

  <p>
    <a href="https://github.com/NavarMP/Kanz-al-Tahqiq"><img alt="GitHub stars" src="https://img.shields.io/github/stars/NavarMP/Kanz-al-Tahqiq?style=flat-square&amp;logo=github&amp;label=stars"></a>
    <a href="https://github.com/NavarMP/Kanz-al-Tahqiq/network/members"><img alt="GitHub forks" src="https://img.shields.io/github/forks/NavarMP/Kanz-al-Tahqiq?style=flat-square&amp;label=forks"></a>
    <a href="https://github.com/NavarMP/Kanz-al-Tahqiq/watchers"><img alt="GitHub watchers" src="https://img.shields.io/github/watchers/NavarMP/Kanz-al-Tahqiq?style=flat-square&amp;label=watchers"></a>
    <a href="https://github.com/NavarMP/Kanz-al-Tahqiq/commits/main"><img alt="Latest commit" src="https://img.shields.io/github/last-commit/NavarMP/Kanz-al-Tahqiq?style=flat-square&amp;label=updated"></a>
    <a href="https://github.com/NavarMP/Kanz-al-Tahqiq/issues"><img alt="Open issues" src="https://img.shields.io/github/issues/NavarMP/Kanz-al-Tahqiq?style=flat-square&amp;label=issues"></a>
  </p>
</div>

> **In brief:** Kanz al-Taḥqīq is a public, growing collection of classical Islamic study texts and related learning materials. It brings together Arabic originals, translations, structured study notes, and speeches in lightweight files that readers can search, copy, compare, and improve.

<p align="center"><em>Preserve the text. Make the path through it clearer. Keep the sources close.</em></p>

## Contents

- [The project](#the-project)
- [Vision and mission](#vision-and-mission)
- [The collection](#the-collection)
- [How the materials are prepared](#how-the-materials-are-prepared)
- [Why Markdown](#why-markdown)
- [Repository map](#repository-map)
- [Contribute](#contribute)
- [Open collaboration and licensing](#open-collaboration-and-licensing)
- [Analytics](#analytics)
- [Sources and editorial notes](#sources-and-editorial-notes)
- [Maintainer](#maintainer)
- [Quick links](#quick-links)

## The project

Kanz al-Taḥqīq (كنز التحقيق) is a text-first study archive for readers who want to engage closely with classical works and the ideas around them. Its current collection spans **fiqh, logic, and Arabic grammar**, alongside explanatory notes, public-speaking material, and Malayalam articles. Arabic is kept central, with English and Malayalam editions where available.

The aim is practical: make useful material easier to find, read, search, quote, compare, teach, and revise. A source text, its translation, and a learner's commentary are different things; the repository keeps those layers identifiable and links to references wherever the records provide them.

This is a **digital study aid**, not a scholarly institution, a substitute for a qualified teacher, or a source of personal religious rulings. Some files are working translations or machine-assisted text and are labelled accordingly. Please read each document's own scope and source notes before relying on it.

## Vision and mission

### Vision

Build a dependable, multilingual study library where classical texts remain readable in their original form and become easier to approach through careful translation, explanation, and responsible digital organization.

### Mission

- Preserve and organize useful source texts in accessible, searchable formats.
- Place translations and study aids beside the works they explain, while keeping their status clear.
- Make editorial decisions and source references visible, so readers can verify rather than merely trust.
- Welcome careful contributions from students, translators, editors, teachers, and readers.
- Improve access without presenting an unfinished transcription or translation as a definitive edition.

### Future missions

These are directions for the project, not dated promises:

1. **Stronger provenance:** record author, edition, publisher, page references, source URL, and rights information for every text where these can be verified.
2. **Scholarly review:** invite qualified readers to review transcription, vocalization, translation, and teaching notes, and record review status in the documents.
3. **More connected study paths:** expand translations, glossaries, indexes, cross-references, and examples where source rights and review capacity permit.
4. **Better discovery:** make it easier to navigate the library by subject, work, language, and editorial status.
5. **Durable access:** keep the collection portable, accessible, and easy to reuse in teaching and research once licensing is clarified.

## The collection

The repository currently contains **24 Markdown documents** across **three study areas** and **three languages**. The collection is small enough to browse directly and organized so related files stay together.

| Area | Work and materials | Languages and notes |
|---|---|---|
| **Fiqh** | [Fatḥ al-Muʿīn — Arabic text](Texts/Fiqh/fath-al-muin/fath-al-muin.md), [Malayalam translation](Texts/Fiqh/fath-al-muin/fath-al-muin-ml.md), and [Arabic–Malayalam study notes](Texts/Fiqh/fath-al-muin/Notes/Fath-al-Muin-Study-Note-Ar-Ml.md) | The available text covers the introduction and prayer material through the funeral prayer. The Arabic vocalization is automatically generated; the Malayalam translation is marked as a preliminary machine translation. |
| **Logic** | [Taṣrīḥ al-Manṭiq — Arabic](Texts/Mantiq/tasrih-al-mantiq/Tasrih-al-mantiq.md), [English](Texts/Mantiq/tasrih-al-mantiq/Tasrih-al-Mantiq-En.md), and [Malayalam](Texts/Mantiq/tasrih-al-mantiq/Tasrih-al-Mantiq-ml.md), with [Arabic](Texts/Mantiq/tasrih-al-mantiq/Notes/tasrih-al-mantiq-note.md), [English](Texts/Mantiq/tasrih-al-mantiq/Notes/Tasrih-al-Mantiq-note-En.md), and [Malayalam](Texts/Mantiq/tasrih-al-mantiq/Notes/Tasrih-al-Mantiq-note-Ml.md) study guides | The guides map the text, explain its topics, and include tables, diagrams, and examples. The English guide describes how it compares the supplied text with a 2019 fourth edition from Jamia Islamia Hind. |
| **Arabic grammar** | [Alfiyyah Ibn Mālik](Texts/Nahw/alfiyyah/alfiyyah-ibn-malik.md) and a [study sheet and thematic index for *Sharḥ al-Khulāṣah al-Alfiyyah*](Texts/Nahw/alfiyyah/Sharh/Sharh-alfiyyah-by-makhdumayn.md) | The poem file has an Arabic chapter index. The study sheet summarizes a named printed edition; it is not a full transcription of the commentary. |
| **Articles — Malayalam** | [ഹദീസിലെ ശൈഖാനി](Articles/Malayalam/hadithile-sheikhani.md), [അല്ലാഹു മൊറാലിറ്റിക്കെതിരോ?](Articles/Malayalam/allahu-moralitykkethiro.md), [റിവേഴ്സ് ഗിയറിൽ ഓടുന്ന so-called ‘പുരോഗമനം’](Articles/Malayalam/reverse-gear-progress.md), and [ലോകകപ്പ്: ബഹിഷ്കരിക്കേണ്ടവർ തോളിലേറ്റുന്നു](Articles/Malayalam/world-cup-boycott.md) | The first and fourth articles link to their Darshanam Magazine publication pages. |
| **Speeches and essays** | [Spirituality Is Far from Wahhabism — English](speeches/English/spirituality-wahhabism.md), [group version](speeches/English/spirituality-wahabism-group.md), [AI-assisted draft](speeches/English/spirituality-wahhabism-chatgpt.md), [Sufism Is Love — Malayalam](speeches/Malayalam/sufism-is-love.md), [opening address](speeches/Malayalam/opening-speech-soul-pain-and-light.md), [Man is Not a Political Animal but a Spiritual One](speeches/Malayalam/manushyan-rashtreeya-jeeviyalla-aathmeeya-jeeviyanu.md), [Da'wah: Medium and Message](speeches/Malayalam/dawah-medium-and-message.md), [Nature and Spiritual Responsibility](speeches/Malayalam/prakrithi-duranthangalum-aatmeeya-bodhyavum.md), and [Tawbah Naṣūḥah — Arabic speech with Malayalam meanings](speeches/Arabic/tawbah-nasuhah.md) | Public-speaking and reflective material on spirituality, *taṣawwuf*, da'wah, and religious life. Citations appear in the individual pieces. |

### A study path

The materials are intended to support a simple sequence: read the text, consult a translation if available, use the notes to clarify structure and terminology, then follow the citations back to their sources.

```mermaid
flowchart LR
    accTitle: A study path through the collection
    accDescr: Read a source text, consult a translation and study notes, then check citations before teaching or improving the material.
    A[Source text] --> B[Translation, where available]
    B --> C[Study notes and examples]
    C --> D[Check citations and edition details]
    D --> E[Teach, discuss, and improve]
```

## How the materials are prepared

The repository brings together several kinds of work. They should not be read as though they all have the same editorial status.

| Layer | What it means here |
|---|---|
| **Source text** | A text transcribed or reproduced from a cited source where that source is recorded. Check the individual file for edition and completeness details. |
| **Translation** | A rendering into another language. A translation may be preliminary or machine-assisted; its document should say so. |
| **Study note** | Explanatory material that organizes terms, chapters, examples, and references. It is commentary for learning, not part of the classical text. |
| **Speech or essay** | A presentation or reflective draft. Its arguments and sources belong to that piece and should be assessed as such. |

Where a document does not yet identify an edition, translation method, or reviewer, that is a documentation gap—not a claim that the item has been verified. Corrections and source records are welcome through the contribution process below.

## Why Markdown

Markdown is the library's working format because it keeps the material light, portable, and easy to improve:

- **Readable as plain text:** works in GitHub, a browser, and ordinary text editors without special software.
- **Easy to search and copy:** readers can find a term, quote a passage, or extract a section without fighting a scanned page or locked document.
- **Good for Arabic and multilingual text:** UTF-8 text, headings, tables, links, and right-to-left HTML markers can live together in one editable file.
- **Clear structure:** headings and lists create a usable table of contents; tables and code blocks help organize examples and terminology.
- **Useful version history:** Git can show what changed, when, and why, making correction and review more transparent.
- **Friendly to research tools and AI agents:** plain text can be indexed and processed with less friction than image-only pages. This helps discovery; it does **not** make generated summaries or translations authoritative.
- **Flexible and low-overhead:** contributors can suggest small fixes as well as larger translations without needing a publishing platform.

Where Markdown has limits—complex page layout, print typography, or exact manuscript facsimiles—companion formats may still be useful. Markdown is a practical base layer, not a replacement for scholarly editions.

## Repository map

<details>
<summary>Expand the folder layout</summary>

```text
Texts/
├── Fiqh/fath-al-muin/
│   ├── fath-al-muin.md                 # Arabic text and source note
│   ├── fath-al-muin-ml.md              # Preliminary Malayalam translation
│   └── Notes/                           # Arabic–Malayalam study notes
├── Mantiq/tasrih-al-mantiq/
│   ├── Tasrih-al-mantiq.md              # Arabic text
│   ├── Tasrih-al-Mantiq-En.md           # English translation
│   ├── Tasrih-al-Mantiq-ml.md           # Malayalam translation
│   └── Notes/                           # Arabic, English, Malayalam guides
└── Nahw/alfiyyah/
    ├── alfiyyah-ibn-malik.md            # Arabic poem and chapter index
    └── Sharh/
        └── Sharh-alfiyyah-by-makhdumayn.md # Study sheet for a printed commentary

Articles/
└── Malayalam/                           # Malayalam articles

speeches/
├── Arabic/                              # Arabic speech scripts with Malayalam meanings
├── English/                             # Speech versions
└── Malayalam/                           # Malayalam speeches and scripts
```

</details>

## Contribute

Contributions can improve transcription, translation, references, formatting, navigation, and study notes. A careful correction with a clear source is more useful than a large untraceable rewrite.

1. **Look at the surrounding files.** Follow their folder structure, language labels, and source-note style.
2. **Open an issue for substantial work.** Describe the work, language, source or edition, and kind of review it needs. This helps avoid duplicated effort.
3. **Make a focused change.** Keep the original text, translation, and commentary distinguishable. Preserve Arabic spelling and right-to-left handling unless the change is specifically correcting them.
4. **Document provenance.** Include author, title, edition, publisher, page or section, and a stable URL where available. Say when a translation or vocalization is machine-assisted or still awaiting review.
5. **Check rights before submitting.** Do not add a modern edition, translation, scan, or other protected material unless you have permission or a clear legal basis to share it.
6. **Open a pull request.** Summarize what changed, cite the evidence, identify any uncertain readings, and note whether specialist review is still needed.

Small fixes—typos, broken links, missing metadata, and clear source corrections—can go straight to a pull request. Start with [GitHub Issues](https://github.com/NavarMP/Kanz-al-Tahqiq/issues/new).

### Useful contribution types

- Verify text against a named edition and record page references.
- Review Arabic transcription, vocalization, or Malayalam and English translations.
- Add a glossary, index, cross-reference, or carefully sourced example.
- Improve heading structure, accessibility, links, or right-to-left rendering.
- Report an error with the file path, passage, proposed correction, and source.

## Open collaboration and licensing

The repository is **public and open to contributions**. However, there is currently no `LICENSE` file. Public visibility on GitHub does not by itself grant permission to reuse or redistribute the repository's original material.

This collection includes historical works, edition-specific text, translations, notes, and speech drafts, and the rights can differ from one layer to another. Please check the source notes and do not assume a blanket reuse license. A formal open-source or open-content license should be added only after the maintainer has reviewed the rights for the material it would cover.

Until then, treat the repository as publicly viewable with reuse rights **not yet specified**. Contributors should include only material they have the right to share. If you can help document editions or rights, please open an issue.

## Analytics

### Repository activity

The badges at the top report live GitHub stars, forks, watchers, open issues, and the last commit. They update as GitHub records change; they are activity signals, not measures of scholarly quality or review.

### Collection snapshot

| Measure | Current snapshot |
|---|---:|
| Markdown documents (excluding this README) | 24 |
| Core study areas | 3 — fiqh, logic, Arabic grammar |
| Languages represented | 3 — Arabic, English, Malayalam |
| Main content groups | 3 — study texts, articles, and speeches |

Counts describe the current repository layout and will change as the collection grows. The next useful quality indicators are source coverage, review status, and the completeness of each item's edition record; these are not yet tracked centrally.

## Sources and editorial notes

Source information is recorded in the documents when known. The following references are explicitly used or described in the current collection:

### Texts and editions

- *Fatḥ al-Muʿīn*: [Shamela, book 11327](https://shamela.ws/book/11327). Its file identifies the base text of *Qurrat al-ʿAyn* using [Islamic Portal 360](https://fiqh.islamicportal360.com/en/book/9011327/).
- *Taṣrīḥ al-Manṭiq*: the English study guide says it compares the supplied Arabic text with the fourth edition from Jamia Islamia Hind, dated 15 May 2019. The supplied Arabic file itself does not include a full bibliographic record.
- *Alfiyyah Ibn Mālik*: the poem file does not yet identify a source edition. Its separate [study sheet for *Sharḥ al-Khulāṣah al-Alfiyyah*](Texts/Nahw/alfiyyah/Sharh/Sharh-alfiyyah-by-makhdumayn.md) identifies the commentary's shaykhs as Zayn al-Dīn al-Kabīr al-Makhdūmī and his son ʿAbd al-ʿAzīz al-Makhdūmī, and names a revised edition from Capital International Books, Calicut, compiled and arranged by Muḥammad Sālim al-Burhānī. Please help add a verified source record for the poem itself.

### Research and speech references

- The logic notes cite the *Stanford Encyclopedia of Philosophy* on [medieval theories of the syllogism](https://plato.stanford.edu/entries/medieval-syllogism/), [Porphyry](https://plato.stanford.edu/entries/porphyry/), and [Ibn Sina](https://plato.stanford.edu/entries/ibn-sina/).
- The speeches cite sources inline, including the [Qur'an](https://quran.com/), [Sunnah.com](https://sunnah.com/), [Ibn ʿAṭāʾ Allāh's *al-Ḥikam*](https://www.themathesontrust.org/papers/islam/ibnataallah-hikam.pdf), and literary sources such as [Folger Shakespeare Library](https://www.folger.edu/explore/shakespeares-works/the-merchant-of-venice/) and the [Poetry Foundation](https://www.poetryfoundation.org/poems/45536/ode-intimations-of-immortality-from-recollections-of-early-childhood).
- Prefer the references inside each document for passage-level citations, translation details, and context; this README is only an overview.

## Maintainer

**Muḥammed Navār** — founder and maintainer · [GitHub profile](https://github.com/NavarMP)

The repository history currently credits the project to this maintainer. Additional contributors are welcome and should be credited through GitHub's contribution history and document acknowledgements where appropriate.

## Quick links

- [Browse all files](https://github.com/NavarMP/Kanz-al-Tahqiq/tree/main)
- [Read the study texts](Texts/)
- [Read the articles](Articles/)
- [Read the speeches](speeches/)
- [Open an issue or suggest a source](https://github.com/NavarMP/Kanz-al-Tahqiq/issues/new)
- [View pull requests](https://github.com/NavarMP/Kanz-al-Tahqiq/pulls)
- [Project maintainer: Muḥammed Navār](https://github.com/NavarMP)
- **Telegram / other community channel:** no verified project channel is currently linked in this repository. If one is established, add its official URL here.

<div align="center">
  <sub>Careful texts. Visible sources. Shared study.</sub>
</div>
