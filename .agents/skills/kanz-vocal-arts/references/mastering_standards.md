# Audio Mastering Standards: Kanz Vocal Arts

This document defines the studio signal processing standards, loudness calibration, and format delivery specifications enforced across all vocal arts productions.

---

## 1. Loudness & Headroom Standards

All final masters must comply with international broadcast and streaming standards:

| Parameter | Standard Value | Tolerance | Purpose |
| :--- | :--- | :--- | :--- |
| **Integrated Loudness ($I$)** | **-16.0 LUFS** | $\pm 0.5$ LUFS | Podcast & Spoken Word optimum standard (Apple / Spotify / Broadcast). |
| **True Peak ($TP$)** | **-1.0 dBTP** | Maximum Ceiling | Prevents inter-sample clipping on digital DACs and lossy transcoding. |
| **Loudness Range ($LRA$)** | **8.0 – 12.0 LU** | Target | Preserves natural oratorical dynamics while preventing excessive quietness. |
| **Sample Rate** | **48.0 kHz** | Exact | Broadcast video and high-resolution digital audio standard. |
| **Bit Depth** | **24-bit PCM** | Exact | Maximum dynamic resolution for archival master WAVs. |

---

## 2. DSP Mastering Signal Chain

```
[Raw Vocal]
    │
    ▼
1. High-Pass Filter (80Hz, 12dB/octave) ──────────> Removes sub-bass stage rumble & handling noise
    │
    ▼
2. 4-Band Sculpting Parametric EQ:
   • 220 Hz (+1.5 dB, Q=1.2) ────────────────────> Low-mid vocal chest body & warmth
   • 750 Hz (-2.0 dB, Q=2.0) ────────────────────> Notches out hollow boxiness
   • 3.8 kHz (+2.8 dB, Q=1.0) ───────────────────> Speech presence & consonant diction clarity
   • 11.0 kHz (+1.8 dB, High Shelf) ─────────────> Silky broadcast air & acoustic shimmer
    │
    ▼
3. Dynamic Broadcast Compression:
   • Threshold: -18 dB
   • Ratio: 3.5:1
   • Attack: 15 ms
   • Release: 120 ms
   • Make-up Gain: +3.5 dB
    │
    ▼
4. Spatial Reverberation (Room Acoustics):
   • Primary Reflection: 35 ms (Gain: 0.22)
   • Secondary Reflection: 55 ms (Gain: 0.15)
   • Decay Envelope: ~1.2 s
    │
    ▼
5. Dynamic Sidechain Ducking (Optional Bed):
   • Bed base level: -24 dB to -26 dB
   • Ducking attenuation: -5 dB to -7 dB when speech detected
    │
    ▼
6. EBU R128 Normalizer (ITU-R BS.1770) ───────────> Enforces -16.0 LUFS / -1.0 dBTP
    │
    ▼
[Release Master]
```

---

## 3. Release Formats & Specifications

Every production produces three mandatory release deliverables:

1. **Studio Master WAV (`*_master.wav`):**
   - 24-bit PCM, 48 kHz, Stereo.
   - For archival preservation, radio broadcasting, and video dubbing.
2. **Broadcast MP3 (`*_broadcast_320k.mp3`):**
   - 320 kbps Constant Bitrate (CBR), LAME encoded, 48 kHz.
   - Embedded ID3v2.3 metadata: Title, Artist, Album, Year, Genre, Comment, and complete Synchronized/Unsynchronized Spoken Transcript (USLT).
3. **Streaming AAC / M4A (`*.m4a`):**
   - 256 kbps Variable/Constant Bitrate AAC, 48 kHz.
   - Optimized for mobile listening, Apple Music, and web streaming.
