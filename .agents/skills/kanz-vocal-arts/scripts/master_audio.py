#!/usr/bin/env python3
"""
master_audio.py - Studio Audio Engineering & Mastering Suite for Kanz Vocal Arts.

Applies high-end broadcast DSP chain via FFmpeg:
1. High-Pass Filter (80Hz low-cut)
2. Parametric EQ (Body warmth, boxiness notch, intelligibility presence, air shelf)
3. Dynamic Broadcast Compression
4. Spatial Sanctuary/Lecture Hall Reverberation
5. Optional Ambient Bed with Dynamic Sidechain Ducking
6. ITU-R BS.1770 / EBU R128 Loudness Normalization (-16 LUFS, -1.0 dBTP)
"""

import sys
import argparse
import subprocess
from pathlib import Path

def master_audio(
    vocal_dry_path: Path,
    output_path: Path,
    ambient_bed_path: Path = None,
    target_lufs: float = -16.0,
    true_peak: float = -1.0,
    room_reverb: bool = True
):
    """Executes the complete FFmpeg audio mastering chain."""
    vocal_dry_path = Path(vocal_dry_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Base vocal DSP chain
    eq_filters = [
        "highpass=f=80:p=2",
        "equalizer=f=220:t=q:w=1.2:g=1.5",
        "equalizer=f=750:t=q:w=2.0:g=-2.0",
        "equalizer=f=3800:t=q:w=1.0:g=2.8",
        "equalizer=f=11000:t=h:w=1.0:g=1.8",
        "acompressor=threshold=-18dB:ratio=3.5:attack=15:release=120:makeup=3.5dB"
    ]
    
    if room_reverb:
        # Subtle sanctuary/lecture hall acoustic depth
        eq_filters.append("aecho=0.8:0.88:35|55:0.22|0.15")
        
    vocal_filter = ",".join(eq_filters)
    
    if ambient_bed_path and Path(ambient_bed_path).exists():
        print(f"Mastering with ambient soundscape: {ambient_bed_path}")
        # Build complex filter with sidechain ducking
        filter_complex = (
            f"[0:a]{vocal_filter},asplit=2[vox_main][vox_sc];"
            f"[1:a]volume=-24dB,aloop=loop=-1:size=2e+09[bg];"
            f"[bg][vox_sc]sidechaincompress=threshold=0.08:ratio=4:attack=50:release=400[ducked_bg];"
            f"[vox_main][ducked_bg]amix=inputs=2:duration=first:dropout_transition=2[mixed];"
            f"[mixed]loudnorm=I={target_lufs}:TP={true_peak}:LRA=9[out]"
        )
        cmd = [
            "ffmpeg", "-y",
            "-i", str(vocal_dry_path),
            "-i", str(ambient_bed_path),
            "-filter_complex", filter_complex,
            "-map", "[out]",
            "-ar", "48000",
            "-c:a", "pcm_s24le",
            str(output_path)
        ]
    else:
        print("Mastering pure vocal track (Studio Competition Standard)...")
        filter_str = f"{vocal_filter},loudnorm=I={target_lufs}:TP={true_peak}:LRA=9"
        cmd = [
            "ffmpeg", "-y",
            "-i", str(vocal_dry_path),
            "-af", filter_str,
            "-ar", "48000",
            "-c:a", "pcm_s24le",
            str(output_path)
        ]
        
    print(f"Running FFmpeg mastering pipeline -> {output_path}...")
    subprocess.run(cmd, check=True)
    print("Mastering completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="Master dry vocal into studio-grade audio.")
    parser.add_argument("vocal_input", help="Path to raw dry vocal WAV")
    parser.add_argument("--output", "-o", required=True, help="Path to output mastered 24-bit WAV")
    parser.add_argument("--ambient", help="Optional path to ambient background track", default=None)
    parser.add_argument("--lufs", type=float, default=-16.0, help="Target integrated LUFS (default: -16.0)")
    parser.add_argument("--peak", type=float, default=-1.0, help="Target True Peak in dBTP (default: -1.0)")
    parser.add_argument("--no-reverb", action="store_true", help="Disable spatial hall reverb")
    
    args = parser.parse_args()
    master_audio(
        args.vocal_input,
        args.output,
        ambient_bed_path=args.ambient,
        target_lufs=args.lufs,
        true_peak=args.peak,
        room_reverb=not args.no_reverb
    )

if __name__ == "__main__":
    main()
