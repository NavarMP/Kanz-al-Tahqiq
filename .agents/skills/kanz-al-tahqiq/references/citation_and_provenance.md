# Scholarly Citation & Provenance Standards

This reference guide specifies the uniform citation schemas, permalink conventions, and digital repository identifiers used in **Kanz al-Taḥqīq**.

---

## 1. The Holy Qur'an

### Syntax Standard:
Always format Qur'anic quotations using standard Islamic typographical brackets `﴿ ... ﴾`, followed by Surah name, Ayah number, and direct link to Quran.com.

```markdown
﴿يَا أَيُّهَا الَّذِينَ آمَنُوا تُوبُوا إِلَى اللَّهِ تَوْبَةً نَّصُوحًا﴾ [[سورة التحريم: 8](https://quran.com/66/8)]
```

### Surah URL Mapping:
- Base URL: `https://quran.com/<surah_number>/<ayah_number>`
- Surah Al-Fatihah: `https://quran.com/1/1`
- Surah Al-Baqarah: `https://quran.com/2/255`
- Surah Al-Ikhlas: `https://quran.com/112/1`

---

## 2. Prophetic Hadith Collections

### Syntax Standard:
Quote the matn (text) in Arabic, mention the primary collection (*Ṣaḥīḥ al-Bukhārī*, *Ṣaḥīḥ Muslim*, *Sunan Abī Dāwūd*, *Jāmiʿ al-Tirmidhī*), and provide a permalink to [Sunnah.com](https://sunnah.com).

```markdown
«يَا أَيُّهَا النَّاسُ تُوبُوا إِلَى اللَّهِ، فَإِنِّي أَتُوبُ فِي الْيَوْمِ إِلَيْهِ مِائَةَ مَرَّةٍ»  
*رواه مسلم في صحيحه ([صحيح مسلم: 2702](https://sunnah.com/muslim:2702))*
```

### Key Sunnah.com Collection URL Prefixes:
- **Sahih al-Bukhari:** `https://sunnah.com/bukhari:<number>`
- **Sahih Muslim:** `https://sunnah.com/muslim:<number>`
- **Sunan Abi Dawud:** `https://sunnah.com/abudawud:<number>`
- **Jami` at-Tirmidhi:** `https://sunnah.com/tirmidhi:<number>`
- **Sunan an-Nasa'i:** `https://sunnah.com/nasai:<number>`
- **Sunan Ibn Majah:** `https://sunnah.com/ibnmajah:<number>`
- **Riyad as-Salihin:** `https://sunnah.com/riyadussalihin:<number>`

---

## 3. Classical Texts in Maktaba Shamela (المكتبة الشاملة)

For source texts (*Mutūn*), commentaries (*Shurūḥ*), and biographical dictionaries (*Kutub al-Tarājim*), cite the official Shamela book ID:

```markdown
- **Fatḥ al-Muʿīn bi-Sharḥ Qurrat al-ʿAyn:** [المكتبة الشاملة: 11327](https://shamela.ws/book/11327)
- **Sharḥ Ibn ʿAqīl ʿalā Alfiyyat Ibn Mālik:** [المكتبة الشاملة: 11846](https://shamela.ws/book/11846)
- **Tafsīr al-Ṭabarī (Jāmiʿ al-Bayān):** [المكتبة الشاملة: 43](https://shamela.ws/book/43)
- **Tafsīr Ibn Kathīr:** [المكتبة الشاملة: 8180](https://shamela.ws/book/8180)
```

---

## 4. Arabic Poetic Shawāhid (الشواهد الشعرية)

When documenting poetic evidence in grammar (*Naḥw*), rhetoric (*Balāghah*), or literature:
1. Identify the poet (*al-Shāʿir*).
2. Identify the poetic meter (*al-Baḥr*).
3. Link to [Al-Diwan](https://www.aldiwan.net/) or [AdabWorld](https://adabworld.com/).

```markdown
> فإن يك بعض الناس سيفا لدولة ... ففي الناس بوقات لها وطبول
> — **أبو الطيب المتنبي** · **بحر الطويل** · [[ديوان المتنبي](https://www.aldiwan.net/cat-poet-al-mutanabbi)]
```

---

## 5. Comparative Philosophy & Western References

For cross-disciplinary studies in logic, epistemology, and metaphysics (especially in `Texts/Mantiq/tasrih-al-mantiq/Notes/`):
- Link to the **Stanford Encyclopedia of Philosophy (SEP)**:
  - Medieval Theories of the Syllogism: `https://plato.stanford.edu/entries/medieval-syllogism/`
  - Ibn Sina (Avicenna): `https://plato.stanford.edu/entries/ibn-sina/`
  - Porphyry: `https://plato.stanford.edu/entries/porphyry/`
  - Aristotle's Logic: `https://plato.stanford.edu/entries/aristotle-logic/`
- Literary and cultural references:
  - Shakespeare: Folger Shakespeare Library (`https://www.folger.edu/`)
  - Poetry Foundation (`https://www.poetryfoundation.org/`)
