#!/usr/bin/env python3
"""
synthesize_debate.py - Multi-Character Heated Debate Audio Synthesizer for Kanz Vocal Arts.

Features:
- Parses 1v1 multi-speaker debate stage scripts with speaker tags:
  [SPEAKER: MODERATOR], [SPEAKER: FOR], [SPEAKER: AGAINST]
- Generates procedural sound effects:
  [SFX: GAVEL], [SFX: BELL_WARN], [SFX: BELL_STOP], [SFX: APPLAUSE]
- Applies speaker-specific acoustic modulation:
  • FOR: ml-IN-MidhunNeural, rate=+8%, pitch=+5Hz, Panned Left (-25%)
  • AGAINST: ml-IN-MidhunNeural, rate=+0%, pitch=-5Hz, Panned Right (+25%)
  • MODERATOR: ml-IN-MidhunNeural, rate=-2%, pitch=+1Hz, Center Pan
  • Embedded Arabic Hadith/Quran: ar-SA-HamedNeural, rate=-8%
- Concatenates with realistic debate stage pacing and micro-pauses.
- Triggers mastering and packaging pipeline for complete release deliverables.
"""

import os
import sys
import re
import json
import asyncio
import argparse
import subprocess
from pathlib import Path
import edge_tts

ARABIC_PATTERN = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')

def generate_procedural_sfx(sfx_type: str, output_path: Path):
    """Generates procedural sound effects via FFmpeg lavfi filters."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if sfx_type == "GAVEL":
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "anoisesrc=d=0.08:c=pink:r=48000,lowpass=f=800,afade=t=out:st=0.01:d=0.07,volume=3.5",
            "-f", "lavfi", "-i", "anullsrc=d=0.12:r=48000",
            "-f", "lavfi", "-i", "anoisesrc=d=0.12:c=pink:r=48000,lowpass=f=800,afade=t=out:st=0.01:d=0.11,volume=4.0",
            "-filter_complex", "[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]",
            "-map", "[out]",
            "-ar", "48000", "-c:a", "pcm_s16le",
            str(output_path)
        ]
    elif sfx_type == "BELL_WARN":
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "sine=f=1174.66:d=1.8:r=48000,afade=t=out:st=0.1:d=1.7,volume=0.8",
            "-ar", "48000", "-c:a", "pcm_s16le",
            str(output_path)
        ]
    elif sfx_type == "BELL_STOP":
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "sine=f=1318.51:d=0.35:r=48000,afade=t=out:st=0.05:d=0.30,volume=0.8",
            "-f", "lavfi", "-i", "anullsrc=d=0.15:r=48000",
            "-f", "lavfi", "-i", "sine=f=1318.51:d=1.5:r=48000,afade=t=out:st=0.05:d=1.45,volume=0.8",
            "-filter_complex", "[0:a][1:a][2:a]concat=n=3:v=0:a=1[out]",
            "-map", "[out]",
            "-ar", "48000", "-c:a", "pcm_s16le",
            str(output_path)
        ]
    elif sfx_type == "APPLAUSE":
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", "anoisesrc=d=3.2:c=pink:r=48000,lowpass=f=1100,afade=t=in:st=0:d=0.5,afade=t=out:st=2.2:d=1.0,volume=1.1",
            "-ar", "48000", "-c:a", "pcm_s16le",
            str(output_path)
        ]
    else:
        raise ValueError(f"Unknown SFX type: {sfx_type}")

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def create_silence_wav(duration_ms: int, output_path: Path):
    """Generates silent audio segment of exact duration."""
    duration_s = max(duration_ms, 50) / 1000.0
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo",
        "-t", f"{duration_s:.3f}",
        "-c:a", "pcm_s16le",
        str(output_path)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def convert_and_pan(input_audio: Path, output_wav: Path, pan_filter: str):
    """Converts audio to 48kHz stereo WAV with directional stereo panning."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_audio),
        "-af", pan_filter,
        "-ar", "48000",
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(output_wav)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def synthesize_chunk(text: str, voice: str, rate: str, pitch: str, output_path: Path):
    """Synthesizes text via edge-tts."""
    comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await comm.save(str(output_path))

def parse_debate_script(script_text: str):
    """Parses markdown text into ordered debate action items."""
    # Strip HTML comments
    script_text = re.sub(r'<!--.*?-->', '', script_text, flags=re.DOTALL)
    lines = script_text.split('\n')
    actions = []
    current_speaker = "MODERATOR"
    
    # Speaker config profiles
    speaker_profiles = {
        "MODERATOR": {
            "voice": "ml-IN-MidhunNeural",
            "rate": "-2%",
            "pitch": "+1Hz",
            "pan": "pan=stereo|c0=0.5*c0+0.5*c1|c1=0.5*c0+0.5*c1",
            "pause": 400
        },
        "FOR": {
            "voice": "ml-IN-MidhunNeural",
            "rate": "+8%",
            "pitch": "+5Hz",
            "pan": "pan=stereo|c0=0.85*c0|c1=0.35*c0", # Panned Left
            "pause": 300
        },
        "AGAINST": {
            "voice": "ml-IN-MidhunNeural",
            "rate": "+0%",
            "pitch": "-5Hz",
            "pan": "pan=stereo|c0=0.35*c0|c1=0.85*c0", # Panned Right
            "pause": 300
        }
    }
    
    current_text_buf = []

    def flush_text(speaker):
        nonlocal current_text_buf
        if not current_text_buf:
            return
        full_text = " ".join(current_text_buf).strip()
        current_text_buf = []
        if not full_text:
            return
            
        # Split text into manageable paragraphs/sentences
        # Check if contains Arabic quotes
        parts = re.split(r'([«»][^«»]+[«»]|[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\s،؛ـ]{10,})', full_text)
        for part in parts:
            p_strip = part.strip()
            if not p_strip:
                continue
            ar_count = len(''.join(ARABIC_PATTERN.findall(p_strip)))
            if ar_count > 6 and ar_count / max(len(p_strip), 1) > 0.4:
                # Arabic citation
                clean_ar = p_strip.replace('«', '').replace('»', '').strip()
                actions.append({
                    "type": "speech",
                    "speaker": speaker,
                    "language": "arabic",
                    "voice": "ar-SA-HamedNeural",
                    "rate": "-8%",
                    "pitch": "+0Hz",
                    "pan": speaker_profiles[speaker]["pan"],
                    "text": clean_ar,
                    "pause_after_ms": 750
                })
            else:
                # Spoken Malayalam
                # Normalize honorifics
                p_ml = p_strip.replace('ﷺ', 'സ്വല്ലല്ലാഹു അലൈഹിവസല്ലം')
                p_ml = p_ml.replace('«', '').replace('»', '')
                p_ml = re.sub(r'[*_#]+', '', p_ml).strip()
                if p_ml:
                    actions.append({
                        "type": "speech",
                        "speaker": speaker,
                        "language": "malayalam",
                        "voice": speaker_profiles[speaker]["voice"],
                        "rate": speaker_profiles[speaker]["rate"],
                        "pitch": speaker_profiles[speaker]["pitch"],
                        "pan": speaker_profiles[speaker]["pan"],
                        "text": p_ml,
                        "pause_after_ms": speaker_profiles[speaker]["pause"]
                    })

    for line in lines:
        line_s = line.strip()
        if not line_s or line_s.startswith('---') or line_s.startswith('#'):
            continue
            
        # Skip character list bullet points
        if line_s.startswith('- [SPEAKER:') or line_s.startswith('* [SPEAKER:'):
            continue

        # Check for SFX
        sfx_match = re.search(r'\[SFX:\s*(GAVEL|BELL_WARN|BELL_STOP|APPLAUSE)\]', line_s)
        if sfx_match:
            flush_text(current_speaker)
            sfx_type = sfx_match.group(1)
            actions.append({
                "type": "sfx",
                "sfx_type": sfx_type,
                "pause_after_ms": 400
            })
            continue
            
        # Check for Speaker tag
        spk_match = re.match(r'\[SPEAKER:\s*(MODERATOR|FOR|AGAINST)\]', line_s)
        if spk_match:
            flush_text(current_speaker)
            current_speaker = spk_match.group(1)
            continue
            
        # Ignore stage directions like [കഥാപാത്രങ്ങളും...] or [തടസ്സപ്പെടുത്തിക്കൊണ്ട്...]
        if line_s.startswith('[') and line_s.endswith(']'):
            continue
            
        current_text_buf.append(line_s)
        
    flush_text(current_speaker)
    return actions

async def process_debate_pipeline(script_path: Path, output_dry_wav: Path, work_dir: Path):
    """Processes script, generates SFX & speeches, applies panning and concatenates."""
    work_dir.mkdir(parents=True, exist_ok=True)
    sfx_dir = work_dir / "sfx"
    sfx_dir.mkdir(exist_ok=True)
    
    script_content = script_path.read_text(encoding="utf-8")
    actions = parse_debate_script(script_content)
    print(f"Parsed {len(actions)} total stage actions from {script_path.name}.")
    
    # Pre-generate procedural SFX cache
    sfx_cache = {}
    for s_type in ["GAVEL", "BELL_WARN", "BELL_STOP", "APPLAUSE"]:
        sfx_path = sfx_dir / f"{s_type.lower()}.wav"
        if not sfx_path.exists():
            print(f"Generating procedural SFX: {s_type}...")
            generate_procedural_sfx(s_type, sfx_path)
        sfx_cache[s_type] = sfx_path
        
    concat_list = []
    
    for idx, act in enumerate(actions):
        act_type = act["type"]
        if act_type == "sfx":
            sfx_t = act["sfx_type"]
            sfx_file = sfx_cache[sfx_t]
            concat_list.append(sfx_file)
            print(f"  [{idx+1}/{len(actions)}] [SFX: {sfx_t}]")
            
            p_ms = act.get("pause_after_ms", 300)
            if p_ms > 0:
                p_file = work_dir / f"pause_{idx:03d}.wav"
                create_silence_wav(p_ms, p_file)
                concat_list.append(p_file)
                
        elif act_type == "speech":
            speaker = act["speaker"]
            text = act["text"]
            voice = act["voice"]
            rate = act["rate"]
            pitch = act["pitch"]
            pan = act["pan"]
            pause_ms = act["pause_after_ms"]
            
            raw_mp3 = work_dir / f"act_{idx:03d}_raw.mp3"
            panned_wav = work_dir / f"act_{idx:03d}_panned.wav"
            
            print(f"  [{idx+1}/{len(actions)}] [{speaker}] ({voice}, p={pitch}, r={rate}) {text[:45]}...")
            await synthesize_chunk(text, voice, rate, pitch, raw_mp3)
            convert_and_pan(raw_mp3, panned_wav, pan)
            concat_list.append(panned_wav)
            
            if pause_ms > 0:
                p_file = work_dir / f"pause_{idx:03d}.wav"
                create_silence_wav(pause_ms, p_file)
                concat_list.append(p_file)

    manifest_path = work_dir / "debate_concat_manifest.txt"
    with open(manifest_path, "w", encoding="utf-8") as f:
        for fpath in concat_list:
            f.write(f"file '{fpath.resolve()}'\n")
            
    print(f"\nConcatenating all {len(concat_list)} segments into {output_dry_wav}...")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(manifest_path),
        "-c:a", "pcm_s16le",
        "-ar", "48000",
        str(output_dry_wav)
    ]
    subprocess.run(concat_cmd, check=True)
    print(f"Dry vocal debate master successfully generated: {output_dry_wav}")

def main():
    parser = argparse.ArgumentParser(description="Multi-Character Heated Debate Audio Synthesizer.")
    parser.add_argument("script_file", help="Path to debate markdown script")
    parser.add_argument("--output-dir", "-o", default=None, help="Output deliverables directory")
    parser.add_argument("--title", default="AI: Blessing or Threat? - Heated Malayalam Debate Duel", help="Title")
    parser.add_argument("--album", default="ADSA Debate Mehrajan’26", help="Album")
    parser.add_argument("--artist", default="Kanz al-Taḥqīq Vocal Arts", help="Artist")
    parser.add_argument("--year", default="2026", help="Year")
    
    args = parser.parse_args()
    script_path = Path(args.script_file).resolve()
    if not script_path.exists():
        print(f"Error: {script_path} not found.")
        sys.exit(1)
        
    out_dir = Path(args.output_dir).resolve() if args.output_dir else script_path.parent / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    work_dir = out_dir / "temp_build"
    dry_wav = out_dir / f"{script_path.stem}_dry.wav"
    master_wav = out_dir / f"{script_path.stem}_master.wav"
    
    # 1. Synthesize dry debate audio
    asyncio.run(process_debate_pipeline(script_path, dry_wav, work_dir))
    
    # 2. Studio Broadcast DSP Mastering
    skill_dir = Path(__file__).resolve().parent.parent
    master_script = skill_dir / "scripts" / "master_audio.py"
    pkg_script = skill_dir / "scripts" / "package_release.py"
    
    print("\n▶ Studio Mastering through Broadcast DSP Chain (EQ, Compression, Spatial Reverb, EBU R128)...")
    subprocess.run([
        sys.executable, str(master_script),
        str(dry_wav),
        "-o", str(master_wav),
        "--lufs", "-16.0",
        "--peak", "-1.0"
    ], check=True)
    
    # 3. Multi-Format Release Packaging
    print("\n▶ Packaging Release Deliverables (320k MP3 + ID3 Metadata + M4A Streaming)...")
    subprocess.run([
        sys.executable, str(pkg_script),
        str(master_wav),
        "--output-dir", str(out_dir),
        "--title", args.title,
        "--artist", args.artist,
        "--album", args.album,
        "--year", args.year,
        "--genre", "Debate / Munāḍharah",
        "--transcript", str(script_path)
    ], check=True)
    
    print("\n🎉 COMPLETE HEATED DEBATE AUDIO PRODUCTION SUCCEEDED!")
    print(f"Deliverables directory: {out_dir}")

if __name__ == "__main__":
    main()
