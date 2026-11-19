#!/usr/bin/env python3
"""
produce_art.py - Unified One-Command Vocal Arts Audio Producer.

Orchestrates the entire end-to-end production pipeline:
1. Cleans and annotates text into a performance script.
2. Synthesizes multilingual speech with neural voices.
3. Masters audio through studio-grade DSP (EQ, compression, spatial acoustics, LUFS).
4. Packages into release-ready Lossless WAV, 320k MP3 (with ID3 metadata), and M4A.
"""

import sys
import argparse
import subprocess
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = SKILL_DIR / "scripts"

def run_step(description: str, cmd: list):
    print(f"\n▶ {description}")
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"❌ Error during: {description}")
        sys.exit(res.returncode)

def main():
    parser = argparse.ArgumentParser(description="Produce studio-grade audio for any speech, debate, or poem.")
    parser.add_argument("input_file", help="Path to input markdown or text file")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory for generated audio deliverables")
    parser.add_argument("--genre", default="speech", choices=["speech", "debate", "poem", "manual"], help="Art form genre")
    parser.add_argument("--title", default=None, help="Title of the artwork (defaults to file stem)")
    parser.add_argument("--artist", default="Kanz al-Taḥqīq Vocal Arts", help="Artist name")
    parser.add_argument("--album", default="Dars Arts Vault", help="Album name")
    parser.add_argument("--year", default="2026", help="Production year")
    parser.add_argument("--ambient", help="Optional path to ambient background track", default=None)
    parser.add_argument("--en-voice", default="en-GB-RyanNeural", help="English neural voice")
    parser.add_argument("--ar-voice", default="ar-SA-HamedNeural", help="Arabic neural voice")
    parser.add_argument("--ml-voice", default="ml-IN-MidhunNeural", help="Malayalam neural voice")
    
    args = parser.parse_args()
    input_path = Path(args.input_file).resolve()
    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        sys.exit(1)
        
    out_dir = Path(args.output_dir).resolve() if args.output_dir else input_path.parent / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    title = args.title or input_path.stem.replace("-", " ").replace("_", " ").title()
    perf_json = out_dir / f"{input_path.stem}.performance.json"
    dry_wav = out_dir / f"{input_path.stem}_dry.wav"
    master_wav = out_dir / f"{input_path.stem}_master.wav"
    
    # Step 1: Clean and annotate
    run_step(
        f"Step 1: Generating annotated performance script from {input_path.name}",
        [
            sys.executable, str(SCRIPTS_DIR / "clean_and_annotate.py"),
            str(input_path),
            "-o", str(perf_json),
            "--en-voice", args.en_voice,
            "--ar-voice", args.ar_voice,
            "--ml-voice", args.ml_voice
        ]
    )
    
    # Step 2: Voice synthesis
    run_step(
        "Step 2: Synthesizing neural speech segments and timing cues",
        [
            sys.executable, str(SCRIPTS_DIR / "synthesize_voice.py"),
            str(perf_json),
            "-o", str(dry_wav),
            "--work-dir", str(out_dir / "temp_build")
        ]
    )
    
    # Step 3: Studio Mastering
    master_cmd = [
        sys.executable, str(SCRIPTS_DIR / "master_audio.py"),
        str(dry_wav),
        "-o", str(master_wav)
    ]
    if args.ambient:
        master_cmd.extend(["--ambient", str(args.ambient)])
    run_step("Step 3: Mastering audio through studio broadcast DSP chain", master_cmd)
    
    # Step 4: Release Packaging
    run_step(
        "Step 4: Packaging deliverables into 320k MP3 and streaming M4A with metadata",
        [
            sys.executable, str(SCRIPTS_DIR / "package_release.py"),
            str(master_wav),
            "--output-dir", str(out_dir),
            "--title", title,
            "--artist", args.artist,
            "--album", args.album,
            "--year", args.year,
            "--genre", args.genre.capitalize(),
            "--transcript", str(input_path)
        ]
    )
    
    # Clean up intermediate dry and temp build
    if (out_dir / "temp_build").exists():
        import shutil
        shutil.rmtree(out_dir / "temp_build", ignore_errors=True)
    if dry_wav.exists():
        dry_wav.unlink()
        
    print(f"\n🎉 Production completed successfully!")
    print(f"Deliverables located in: {out_dir}")

if __name__ == "__main__":
    main()
