#!/usr/bin/env python3
"""
clean_and_annotate.py - Text Sanitizer and Phonetic Annotator for Kanz Vocal Arts.

Cleans raw Markdown files (removing URLs, bracketed citations, and OCR/markup artifacts),
fixes known typos, annotates phonetics, detects language boundaries (Arabic, Urdu, Malayalam, English),
and outputs a structured JSON performance script.
"""

import re
import json
import argparse
from pathlib import Path

# Arabic Unicode range
ARABIC_PATTERN = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+')
# Urdu specific characters
URDU_SPECIFIC_PATTERN = re.compile(r'[ٹڈڑںےہھئےپچژگ]')
# Malayalam Unicode range
MALAYALAM_PATTERN = re.compile(r'[\u0D00-\u0D7F]+')

def clean_text(raw_markdown: str) -> str:
    """Removes URLs, markdown links, footnote citations, and known typos."""
    text = raw_markdown
    
    # Strip HTML wrappers but preserve content; mark urdu if lang="ur"
    text = re.sub(r'<div[^>]*lang="ur"[^>]*>(.*?)</div>', r'__URDU_START__\1__URDU_END__', text, flags=re.DOTALL)
    text = re.sub(r'<p\s+dir="rtl"\s+lang="ar">(.*?)</p>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<div[^>]*>(.*?)</div>', r'\1', text, flags=re.DOTALL)
    text = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', text, flags=re.DOTALL)
    
    # Locate speech starting point: if "## Speech" exists, start from there!
    if "## Speech" in text:
        text = text.split("## Speech", 1)[1]
    
    # Strip headers (# Title)
    text = re.sub(r'^#+\s*.*$', '', text, flags=re.MULTILINE)
    
    # Strip metadata lines (e.g. *ADSA Mehrajan’26 ... or lines with fest guidelines)
    text = re.sub(r'^\*?\s*ADSA\s+Mehrajan.*$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^\*+[^\n]*\*+$', '', text, flags=re.MULTILINE)
    
    # Remove markdown tables (lines starting and ending with |)
    text = re.sub(r'^\|.*\|$', '', text, flags=re.MULTILINE)
    
    # Remove citation links with URLs: ([Title](https://...)) or [Title](https://...)
    text = re.sub(r'\(\[[^\]]*\]\(https?://[^\)]+\)\)', '', text)
    text = re.sub(r'\[[^\]]*\]\(https?://[^\)]+\)', '', text)
    
    # Strip remaining bare URLs
    text = re.sub(r'https?://\S+', '', text)
    
    # Remove brackets around solitary references like ([Sahih Muslim 2593]) or ([Qur’an 21:107])
    text = re.sub(r'\(\[([^\]]+)\]\)', '', text)
    
    # Remove leftover empty parentheses like (; ) or (; ; ) or ()
    text = re.sub(r'\(\s*[;\s,]*\)', '', text)
    
    # Fix known typos
    text = re.sub(r'\bthe the\b', 'the', text, flags=re.IGNORECASE)
    text = re.sub(r'\btru beauty\b', 'true beauty', text, flags=re.IGNORECASE)
    
    # Normalize honorifics for spoken delivery
    text = text.replace('ﷺ', ', peace and blessings be upon him,')
    text = text.replace('˹O Prophet˺', 'O Prophet,')
    
    # Clean whitespace around punctuation
    text = re.sub(r'\s+,', ',', text)
    text = re.sub(r',\s*,+', ',', text)
    
    # Clean excessive whitespace and blank lines
    lines = [line.strip() for line in text.split('\n')]
    cleaned_lines = [l for l in lines if l and not l.startswith('---')]
    return '\n\n'.join(cleaned_lines)

def detect_segment_language(text: str) -> str:
    """Classifies a text block as 'arabic', 'urdu', 'malayalam', or 'english'."""
    stripped = text.strip()
    
    if '__URDU_START__' in stripped or URDU_SPECIFIC_PATTERN.search(stripped):
        return 'urdu'
        
    ar_chars = len(''.join(ARABIC_PATTERN.findall(stripped)))
    ml_chars = len(''.join(MALAYALAM_PATTERN.findall(stripped)))
    total_chars = max(len(stripped), 1)
    
    if ar_chars / total_chars > 0.35:
        # Check if contains Urdu specific letters
        if URDU_SPECIFIC_PATTERN.search(stripped):
            return 'urdu'
        return 'arabic'
    if ml_chars / total_chars > 0.35:
        return 'malayalam'
    return 'english'

def parse_into_performance_segments(
    cleaned_text: str,
    default_english_voice="en-GB-RyanNeural",
    default_arabic_voice="ar-SA-HamedNeural",
    default_malayalam_voice="ml-IN-MidhunNeural",
    default_urdu_voice="ur-PK-AsadNeural"
) -> list:
    """Parses text into discrete, voiced performance segments with timing and pause cues."""
    paragraphs = cleaned_text.split('\n\n')
    segments = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Check for explicit Urdu marker
        is_marked_urdu = False
        if '__URDU_START__' in para:
            is_marked_urdu = True
            para = para.replace('__URDU_START__', '').replace('__URDU_END__', '').strip()
            
        lang = "urdu" if is_marked_urdu else detect_segment_language(para)
        
        if lang == 'urdu':
            segments.append({
                "language": "urdu",
                "voice": default_urdu_voice,
                "text": para,
                "rate": "-5%",
                "pitch": "+0Hz",
                "pause_after_ms": 750
            })
            continue
            
        if lang == 'arabic':
            pause = 1000 if "الرَّحْمَٰنِ الرَّحِيمِ" in para else 800
            segments.append({
                "language": "arabic",
                "voice": default_arabic_voice,
                "text": para,
                "rate": "-10%",
                "pitch": "+0Hz",
                "pause_after_ms": pause
            })
            continue
        
        # Check for Arabic closing salām at the end of speech
        if "Assalamu Alaikum wa Rahmatullahi wa Barakatuh" in para:
            before, _ = para.rsplit("Assalamu Alaikum wa Rahmatullahi wa Barakatuh", 1)
            if before.strip():
                clean_before = re.sub(r'\*+', '', before.strip()).strip()
                if clean_before:
                    segments.append({
                        "language": "english",
                        "voice": default_english_voice,
                        "text": clean_before,
                        "rate": "-5%",
                        "pitch": "+0Hz",
                        "pause_after_ms": 600
                    })
            segments.append({
                "language": "arabic",
                "voice": default_arabic_voice,
                "text": "السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ وَبَرَكَاتُهُ",
                "rate": "-8%",
                "pitch": "+0Hz",
                "pause_after_ms": 1200
            })
            continue
        
        # Check for embedded Arabic, Urdu, or Malayalam phrases
        token_pattern = re.compile(r'([\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\s،؛ـ]+|[\u0D00-\u0D7F]+|[^\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\u0D00-\u0D7F]+)')
        parts = token_pattern.findall(para)
        
        for part in parts:
            p_strip = part.strip()
            if not p_strip:
                continue
            
            p_lang = detect_segment_language(p_strip)
            if p_lang == 'urdu':
                segments.append({
                    "language": "urdu",
                    "voice": default_urdu_voice,
                    "text": p_strip,
                    "rate": "-5%",
                    "pitch": "+0Hz",
                    "pause_after_ms": 700
                })
            elif p_lang == 'arabic':
                segments.append({
                    "language": "arabic",
                    "voice": default_arabic_voice,
                    "text": p_strip,
                    "rate": "-10%",
                    "pitch": "+0Hz",
                    "pause_after_ms": 750
                })
            elif p_lang == 'malayalam' or any(c in p_strip for c in "വെളിച്ചത്തിരുട്ട്"):
                clean_ml = re.sub(r'[“”"]', '', p_strip)
                segments.append({
                    "language": "malayalam",
                    "voice": default_malayalam_voice,
                    "text": clean_ml,
                    "rate": "-5%",
                    "pitch": "+0Hz",
                    "pause_after_ms": 250
                })
            else:
                pause = 500
                if p_strip.endswith('.') or p_strip.endswith('!') or p_strip.endswith('?'):
                    pause = 750
                elif p_strip.endswith(','):
                    pause = 350
                elif p_strip.endswith(';'):
                    pause = 450
                elif p_strip.lower() == 'at':
                    pause = 200
                
                p_clean = re.sub(r'\*+', '', p_strip).strip()
                p_clean = re.sub(r'^[“"”’‘,\s]+', '', p_clean)
                p_clean = re.sub(r'[“"”’‘\s]+$', '', p_clean)
                p_clean = re.sub(r',\s*,+', ',', p_clean)
                
                if p_clean:
                    segments.append({
                        "language": "english",
                        "voice": default_english_voice,
                        "text": p_clean,
                        "rate": "-5%",
                        "pitch": "+0Hz",
                        "pause_after_ms": pause
                    })
    
    return segments

def main():
    parser = argparse.ArgumentParser(description="Clean and annotate a markdown file into an audio performance script.")
    parser.add_argument("input_file", help="Path to input markdown file")
    parser.add_argument("--output", "-o", help="Path to output JSON file", default=None)
    parser.add_argument("--en-voice", default="en-GB-RyanNeural", help="Default English neural voice")
    parser.add_argument("--ar-voice", default="ar-SA-HamedNeural", help="Default Arabic neural voice")
    parser.add_argument("--ml-voice", default="ml-IN-MidhunNeural", help="Default Malayalam neural voice")
    parser.add_argument("--ur-voice", default="ur-PK-AsadNeural", help="Default Urdu neural voice")
    
    args = parser.parse_args()
    input_path = Path(args.input_file)
    if not input_path.exists():
        print(f"Error: {input_path} does not exist.")
        exit(1)
        
    raw_content = input_path.read_text(encoding="utf-8")
    cleaned = clean_text(raw_content)
    segments = parse_into_performance_segments(
        cleaned,
        default_english_voice=args.en_voice,
        default_arabic_voice=args.ar_voice,
        default_malayalam_voice=args.ml_voice,
        default_urdu_voice=args.ur_voice
    )
    
    output_path = Path(args.output) if args.output else input_path.with_suffix('.performance.json')
    output_path.write_text(json.dumps({
        "source": str(input_path),
        "total_segments": len(segments),
        "segments": segments
    }, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print(f"Performance script successfully generated: {output_path} ({len(segments)} segments)")

if __name__ == "__main__":
    main()
