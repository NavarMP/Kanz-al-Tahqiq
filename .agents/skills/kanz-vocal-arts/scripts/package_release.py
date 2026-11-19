#!/usr/bin/env python3
"""
package_release.py - Multi-Format Release Packager and Tagging Suite for Kanz Vocal Arts.

Converts 24-bit WAV masters to:
- 320kbps CBR Broadcast MP3 with full ID3v2 metadata & embedded transcript
- 256kbps High-Fidelity AAC / M4A for mobile streaming
- Embeds metadata: Title, Artist, Album, Year, Genre, Track, and Spoken Script
"""

import sys
import argparse
import subprocess
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TDRC, TCON, COMM, USLT

def package_audio(
    wav_master_path: Path,
    output_dir: Path,
    title: str,
    artist: str = "Kanz al-Taḥqīq",
    album: str = "ADSA Mehrajan’26",
    year: str = "2026",
    genre: str = "Spoken Word",
    comment: str = "",
    lyrics: str = ""
):
    wav_master_path = Path(wav_master_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    stem = wav_master_path.stem.replace("_master", "")
    mp3_path = output_dir / f"{stem}_broadcast_320k.mp3"
    m4a_path = output_dir / f"{stem}.m4a"
    
    # 1. Encode 320kbps MP3
    print(f"Encoding broadcast 320kbps MP3 -> {mp3_path}...")
    cmd_mp3 = [
        "ffmpeg", "-y",
        "-i", str(wav_master_path),
        "-codec:a", "libmp3lame",
        "-b:a", "320k",
        "-ar", "48000",
        str(mp3_path)
    ]
    subprocess.run(cmd_mp3, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 2. Encode 256kbps M4A (AAC)
    print(f"Encoding streaming 256kbps M4A -> {m4a_path}...")
    cmd_m4a = [
        "ffmpeg", "-y",
        "-i", str(wav_master_path),
        "-codec:a", "aac",
        "-b:a", "256k",
        "-ar", "48000",
        str(m4a_path)
    ]
    subprocess.run(cmd_m4a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # 3. Embed ID3 Tags in MP3
    print(f"Embedding ID3v2 metadata in {mp3_path}...")
    audio = MP3(str(mp3_path), ID3=ID3)
    try:
        audio.add_tags()
    except Exception:
        pass
        
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.tags.add(TALB(encoding=3, text=album))
    audio.tags.add(TDRC(encoding=3, text=year))
    audio.tags.add(TCON(encoding=3, text=genre))
    if comment:
        audio.tags.add(COMM(encoding=3, lang='eng', desc='Description', text=comment))
    if lyrics:
        audio.tags.add(USLT(encoding=3, lang='eng', desc='Transcript', text=lyrics))
    audio.save()
    
    print("Release packaging completed successfully.")
    print(f"  • WAV Master: {wav_master_path}")
    print(f"  • Broadcast MP3: {mp3_path}")
    print(f"  • Streaming M4A: {m4a_path}")

def main():
    parser = argparse.ArgumentParser(description="Package master WAV into release-ready MP3 & M4A.")
    parser.add_argument("wav_master", help="Path to input master WAV")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory (default: same as input)")
    parser.add_argument("--title", required=True, help="Title of speech/poem/debate")
    parser.add_argument("--artist", default="Kanz al-Taḥqīq", help="Artist name")
    parser.add_argument("--album", default="ADSA Mehrajan’26", help="Album name")
    parser.add_argument("--year", default="2026", help="Release year")
    parser.add_argument("--genre", default="Spoken Word", help="Audio genre")
    parser.add_argument("--comment", default="", help="Comment / Fest Theme")
    parser.add_argument("--transcript", default=None, help="Path to text transcript to embed")
    
    args = parser.parse_args()
    wav_path = Path(args.wav_master)
    out_dir = Path(args.output_dir) if args.output_dir else wav_path.parent
    lyrics_text = Path(args.transcript).read_text(encoding="utf-8") if args.transcript and Path(args.transcript).exists() else ""
    
    package_audio(
        wav_path,
        out_dir,
        title=args.title,
        artist=args.artist,
        album=args.album,
        year=args.year,
        genre=args.genre,
        comment=args.comment,
        lyrics=lyrics_text
    )

if __name__ == "__main__":
    main()
