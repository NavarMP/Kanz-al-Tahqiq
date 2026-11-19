---
name: kanz-vocal-arts
description: >-
  Studio audio production and vocal engineering assistant for the Kanz al-Taḥqīq library.
  Use this skill whenever generating, synthesizing, or mastering professional audio files
  for any oral or literary art form: oratorical speeches (Khuṭbah/Waʿẓ), formal debates (Munāḍharah),
  classical poetry (Shiʿr/Qasīdah/Mappila Pāṭṭu), and Dars fest manuals across Malayalam, English,
  Arabic, and multilingual code-switching blends.
---

# Kanz Vocal Arts: Digital Studio & Audio Engineering Skill

Welcome to **Kanz Vocal Arts** (كنز الفنون الصوتية), the dedicated audio production engine of the Kanz al-Taḥqīq library.

📖 **Comprehensive User Manual:** For complete step-by-step playbooks, CLI references, and genre guides, consult the [Master Production Guide (HOW_TO_USE.md)](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/HOW_TO_USE.md).

This skill equips the agent with a complete digital audio workstation (DAW) pipeline directly within the repository. It transforms written speeches, debates, songs, and poetry into broadcast-ready, award-winning master audio files across Malayalam, Arabic, English, Urdu, and multilingual blends.

---

## 1. Quick Reference & Unified CLI

The entire pipeline can be executed in a single command using the unified CLI runner:

```bash
# Generate complete studio master for any speech, debate, or poem
python3 .agents/skills/kanz-vocal-arts/scripts/produce_art.py \
  path/to/script.md \
  --genre speech \
  --title "Speech Title" \
  --artist "Kanz al-Taḥqīq" \
  --album "ADSA Mehrajan’26" \
  --year "2026"
```

### Outputs Produced:
- **`*_master.wav`**: Lossless 24-bit 48kHz archival studio master.
- **`*_broadcast_320k.mp3`**: Pristine 320kbps MP3 with embedded ID3 metadata and complete text transcript.
- **`*.m4a`**: 256kbps streaming AAC file for web and mobile devices.

---

## 2. Pipeline Architecture

```
[Markdown Source Text]
         │
         ▼
1. clean_and_annotate.py ───> Strips URLs/brackets, fixes typos, segments by language
         │
         ▼
2. synthesize_voice.py ─────> Neural synthesis via Edge-TTS (or ElevenLabs/OpenAI),
                              inserts precise micro-pauses between sentences
         │
         ▼
3. master_audio.py ─────────> FFmpeg studio DSP chain:
                              • 80Hz Low-Cut (rumble elimination)
                              • 4-Band Sculpting EQ (warmth, notch, presence, air)
                              • Dynamic Compression (broadcast punch)
                              • Spatial Reverb (sacred lecture hall acoustics)
                              • Dynamic Sidechained Ambience (optional bed)
                              • EBU R128 Loudness Normalization (-16 LUFS, -1 dBTP)
         │
         ▼
4. package_release.py ──────> Encoders produce WAV Master, 320k MP3 + ID3 tags, and M4A
```

---

## 3. Supported Art Forms & Archetypes

See the comprehensive [Oral Arts Taxonomy Guide](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/references/oral_arts_taxonomy.md) for detailed structural breakdowns:

1. **Oratorical Speeches (*Khuṭbah / Waʿẓ / Fest Oratory*):**
   - Measured cadence (105–125 WPM), solemn exordium, sacred Arabic Quran/Hadith pauses, and gradual rhetorical crescendo.
2. **Formal Debates (*Munāḍharah*):**
   - Fast, persuasive cadence (135–155 WPM), sharp premise punching, integrated 4:00 warning bell and 5:00 termination buzzer sound effects.
3. **Metric Poetry (*Shiʿr / Qasīdah / Mappila Pāṭṭu*):**
   - Meter-guided recitation (*Bahr / Vṛttam*), mid-verse caesura (*ʿArūḍ*) halts (600ms), and subtle melodic drone underscoring.
4. **Dars Fest Manuals & Regulations:**
   - Dry, crisp, maximum-clarity articulation with item-number pauses.

---

## 4. Multilingual & Code-Switching Standards

See the full [Voice Casting Matrix](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/references/voice_casting_matrix.md) for available voices:

- **English Oratory:** `en-GB-RyanNeural` (prestigious scholarly orator) or `en-US-ChristopherNeural` (authoritative debater).
- **Arabic Invocations & Shawāhid:** `ar-SA-HamedNeural` (reverent classical *Khaṭīb*) or `ar-AE-HamdanNeural` (Hadith/Tajwīd).
- **Malayalam Stage Delivery:** `ml-IN-MidhunNeural` (Dars orator) or `ml-IN-SobhanaNeural` (poetic reciter).
- **Trilingual Hybrid Routing:** The cleaner automatically detects Arabic verses and Malayalam festival phrases within English texts, routing each clause to its native neural voice model and stitching them seamlessly.

---

## 5. Reference Documentation

- [Voice Casting Matrix](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/references/voice_casting_matrix.md)
- [Oral Arts Taxonomy](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/references/oral_arts_taxonomy.md)
- [Audio Mastering Standards](file:///Users/apple/Desktop/docs:books/Kanz-al-Tahqiq/.agents/skills/kanz-vocal-arts/references/mastering_standards.md)
