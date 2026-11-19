#!/usr/bin/env python3
"""
synthesize_voice.py - High-Fidelity Voice Synthesizer for Kanz Vocal Arts.

Renders segmented performance scripts using edge-tts neural voices,
generates precise micro-pauses with ffmpeg, and concatenates them into
a unified 48kHz studio-quality dry vocal WAV track.
"""

import os
import sys
import json
import asyncio
import argparse
import subprocess
from pathlib import Path
import edge_tts

async def synthesize_segment(text: str, voice: str, rate: str, pitch: str, output_path: Path):
    """Synthesizes a single text segment using edge-tts."""
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(str(output_path))

def create_silence_wav(duration_ms: int, output_path: Path, sample_rate=48000):
    """Generates a silent audio segment of exact duration using ffmpeg."""
    duration_s = max(duration_ms, 50) / 1000.0
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi",
        "-i", f"anullsrc=r={sample_rate}:cl=stereo",
        "-t", f"{duration_s:.3f}",
        "-c:a", "pcm_s16le",
        str(output_path)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def convert_to_wav(input_path: Path, output_path: Path, sample_rate=48000):
    """Converts an audio file to uncompressed 48kHz stereo WAV."""
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-ar", str(sample_rate),
        "-ac", "2",
        "-c:a", "pcm_s16le",
        str(output_path)
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def process_performance_script(script_path: Path, output_wav: Path, work_dir: Path):
    """Processes all segments in the performance JSON and concatenates into output_wav."""
    data = json.loads(script_path.read_text(encoding="utf-8"))
    segments = data.get("segments", [])
    if not segments:
        raise ValueError(f"No segments found in {script_path}")

    work_dir.mkdir(parents=True, exist_ok=True)
    concat_list = []
    
    print(f"Synthesizing {len(segments)} segments...")
    for idx, seg in enumerate(segments):
        lang = seg.get("language", "english")
        voice = seg.get("voice", "en-GB-RyanNeural")
        rate = seg.get("rate", "-5%")
        pitch = seg.get("pitch", "+0Hz")
        text = seg.get("text", "").strip()
        pause_ms = seg.get("pause_after_ms", 500)
        
        if not text:
            continue
            
        seg_mp3 = work_dir / f"seg_{idx:03d}_{lang}.mp3"
        seg_wav = work_dir / f"seg_{idx:03d}_{lang}.wav"
        pause_wav = work_dir / f"pause_{idx:03d}.wav"
        
        # 1. Synthesize audio
        print(f"  [{idx+1}/{len(segments)}] ({lang} - {voice}) {text[:45]}...")
        await synthesize_segment(text, voice, rate, pitch, seg_mp3)
        convert_to_wav(seg_mp3, seg_wav)
        concat_list.append(seg_wav)
        
        # 2. Add pause if > 0
        if pause_ms > 0:
            create_silence_wav(pause_ms, pause_wav)
            concat_list.append(pause_wav)
            
    # Write concat manifest
    manifest_path = work_dir / "concat_manifest.txt"
    with open(manifest_path, "w", encoding="utf-8") as f:
        for audio_file in concat_list:
            f.write(f"file '{audio_file.resolve()}'\n")
            
    print(f"Concatenating all segments into {output_wav}...")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(manifest_path),
        "-c:a", "pcm_s16le",
        "-ar", "48000",
        str(output_wav)
    ]
    subprocess.run(concat_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check=True)
    print(f"Raw vocal track successfully generated: {output_wav}")

def main():
    parser = argparse.ArgumentParser(description="Synthesize performance script into a dry vocal WAV.")
    parser.add_argument("script_path", help="Path to performance JSON script")
    parser.add_argument("--output", "-o", required=True, help="Path to output dry vocal WAV")
    parser.add_argument("--work-dir", default=None, help="Directory for temporary files")
    
    args = parser.parse_args()
    script_path = Path(args.script_path)
    output_wav = Path(args.output)
    work_dir = Path(args.work_dir) if args.work_dir else output_wav.parent / "temp_audio_build"
    
    asyncio.run(process_performance_script(script_path, output_wav, work_dir))

if __name__ == "__main__":
    main()
