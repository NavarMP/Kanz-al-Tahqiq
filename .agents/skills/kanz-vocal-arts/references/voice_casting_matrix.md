# Voice Casting Matrix: Multilingual Oral Arts

This reference guide provides definitive neural voice mappings across Microsoft Edge Neural, ElevenLabs, and OpenAI Audio engines for traditional Islamic oratory, *Munāḍharah* (debates), classical poetry, and Dars fest announcements.

---

## 1. Trilingual Neural Voice Matrix

| Language | Tone / Archetype | Edge-TTS Model (Free / Local) | ElevenLabs Equivalent | Recommended Genre & Context |
| :--- | :--- | :--- | :--- | :--- |
| **English** | Classical Academic / Orator | `en-GB-RyanNeural` | Brian / Marcus | Speeches, Comparative Philosophy, Fest Keynotes |
| **English** | Dynamic Authority / Debater | `en-US-ChristopherNeural` | Adam / Antoni | Munāḍharah, Rebuttals, Fast Delivery |
| **English** | Contemplative / Warm Scholar | `en-US-AndrewMultilingualNeural` | Charlie / George | Spiritual Reflections, Tazkiyah Lectures |
| **English** | Sophisticated Female Orator | `en-GB-SoniaNeural` | Sarah / Alice | Panel Presentations, Academic Readings |
| **Arabic** | Classical *Khaṭīb* / Scholar | `ar-SA-HamedNeural` | Tariq / Khalid | Friday Sermons (*Khuṭab*), Dars Lectures |
| **Arabic** | Qur'anic / Hadith Reverence | `ar-AE-HamdanNeural` | Omar | Poetic *Shawāhid*, Hadith Citations, Tajwīd |
| **Arabic** | Classical Reciter (Female) | `ar-SA-ZariyahNeural` | Amina | Vernacular Hymns, Classical *Muʿallaqāt* |
| **Malayalam** | Dars Fest Orator (Male) | `ml-IN-MidhunNeural` | Custom Dars Cloned Voice | Fest Speeches, Dars Munāḍharah, Stage Delivery |
| **Malayalam** | Melodic / Poetic (Female) | `ml-IN-SobhanaNeural` | Custom Cloned Vocalist | Mappila Pāṭṭu, Metrical Poems (*Kāvya*) |
| **Urdu** | Resonant Orator (*Khaṭīb*) | `ur-PK-AsadNeural` | Hamza | Subcontinental Dars Oratory, Munāẓarah |
| **Hindi** | Formal Academic | `hi-IN-MadhurNeural` | Kabir | Inter-Faith Dialogues, Regional Conferences |

---

## 2. Code-Switching & Hybrid Synthesis Rules

When producing speeches or debates with mixed languages (e.g. English speech quoting Arabic Qur'an and Malayalam fest themes):
1. **Never force an English voice to read Arabic diacritics or Malayalam Malayalam script:** English models produce garbled or broken phonetics when encountering non-Latin Unicode scripts.
2. **Segment at script boundaries:** Use `clean_and_annotate.py` to carve out Arabic and Malayalam segments.
3. **Cross-Fade & Level Matching:** Spliced segments must match average RMS levels to prevent sudden volume drops or leaps across language transitions.
4. **Pacing Rules:**
   - Arabic sacred verses (*Ayahs* / Hadiths): Slow down by `-10%` to `-15%` to allow full resonance of *Makhārij* and Tajwīd pauses.
   - Malayalam cultural phrases: Deliver at natural speech rate (`-5%` to `0%`).
   - English oratorical prose: Maintain measured cadence (`-5%`, ~110–120 WPM).
