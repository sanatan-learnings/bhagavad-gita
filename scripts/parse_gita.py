#!/usr/bin/env python3
"""
Parse complete Bhagavad Gita text and generate YAML entries.
Usage:
    python parse_gita.py < input.txt > output.yaml
    python parse_gita.py input.txt > output.yaml
"""

import re
import sys
from pathlib import Path

def devanagari_to_arabic(dev_num):
    """Convert Devanagari numerals to Arabic"""
    mapping = {
        '०': '0', '१': '1', '२': '2', '३': '3', '४': '4',
        '५': '5', '६': '6', '७': '7', '८': '8', '९': '9'
    }
    result = ''
    for char in dev_num:
        result += mapping.get(char, char)
    return result

def parse_verse_number(marker):
    """Parse verse marker like ॥ १-१॥ to (1, 1)"""
    # Remove ॥ markers and whitespace
    marker = marker.strip('॥ ')
    # Split by dash
    parts = marker.split('-')
    if len(parts) == 2:
        chapter = devanagari_to_arabic(parts[0].strip())
        verse = devanagari_to_arabic(parts[1].strip())
        return int(chapter), int(verse)
    return None, None

def parse_gita_text(input_text):
    """Parse Gita text and extract verses"""
    verses = []
    current_verse_lines = []
    chapter_names = {}  # Store chapter names
    chapter_colophons = {}  # Store chapter colophons
    current_chapter_name = None
    started = False  # Flag to skip preamble

    # Split into lines
    lines = input_text.strip().split('\n')

    for line in lines:
        line = line.strip()

        # Skip empty lines
        if not line:
            continue

        # Extract chapter headers (but skip them from verse text)
        if line.startswith('अथ') and 'ध्यायः' in line:
            started = True  # Now we've started the actual Gita text
            # Extract chapter name after the ।
            parts = line.split('।')
            if len(parts) > 1:
                current_chapter_name = parts[1].strip()
            # Reset accumulated lines when starting a new chapter
            current_verse_lines = []
            continue

        # Skip everything before the first chapter header
        if not started:
            continue

        # Check if line ends with chapter colophon marker (just chapter number)
        # Format: ॥ १॥, ॥ २॥, etc. (not verse markers like ॥ १-१॥)
        colophon_match = re.search(r'॥\s*[०-९]+\s*॥$', line)
        if colophon_match:
            # Extract chapter number from colophon marker
            marker = colophon_match.group()
            marker_clean = marker.strip('॥ ')
            chapter_num_str = devanagari_to_arabic(marker_clean)
            chapter_num = int(chapter_num_str)

            # Combine accumulated lines with current line (keep marker)
            colophon_text = line.strip()
            current_verse_lines.append(colophon_text)
            full_colophon = ' '.join(current_verse_lines)

            # Clean up the text
            full_colophon = full_colophon.replace(' ।', '।')
            full_colophon = re.sub(r'\s+', ' ', full_colophon).strip()

            # Store the colophon
            chapter_colophons[chapter_num] = full_colophon

            # Reset accumulated lines
            current_verse_lines = []
            continue

        # Check if line ends with verse marker (chapter-verse format)
        marker_match = re.search(r'॥\s*[०-९]+-[०-९]+\s*॥', line)

        if marker_match:
            # Extract the marker
            marker = marker_match.group()
            # Keep the entire line including the marker
            verse_text = line.strip()
            # Remove any parenthetical variants after the marker
            verse_text = re.sub(r'॥\s*\([^)]+\)\s*$', '॥', verse_text).strip()

            # Parse chapter and verse number
            ch, vs = parse_verse_number(marker)

            if ch and vs:
                # Combine with any previous lines
                current_verse_lines.append(verse_text)
                full_text = ' '.join(current_verse_lines)

                # Clean up the text
                full_text = full_text.replace(' ।', '।')
                full_text = re.sub(r'\s+', ' ', full_text).strip()

                verses.append({
                    'chapter': ch,
                    'verse': vs,
                    'text': full_text
                })

                # Store chapter name if we have one
                if current_chapter_name and ch not in chapter_names:
                    chapter_names[ch] = current_chapter_name

                # Reset for next verse
                current_verse_lines = []
        else:
            # This line is part of a verse (not yet complete)
            # Include speaker declarations and all other text
            if line:
                current_verse_lines.append(line)

    return verses, chapter_names, chapter_colophons

def generate_yaml_output(verses, chapter_names, chapter_colophons):
    """Generate YAML output for the verses"""
    # Group by chapter
    chapters = {}
    for v in verses:
        if v['chapter'] not in chapters:
            chapters[v['chapter']] = []
        chapters[v['chapter']].append(v)

    # Generate output
    output_lines = []
    output_lines.append("# Bhagavad Gita - Canonical Devanagari Text")
    output_lines.append("# Format: chapter-XX-shloka-YY")
    output_lines.append("")
    output_lines.append("# Sequence of all verses")
    output_lines.append("sequence:")

    for ch in sorted(chapters.keys()):
        output_lines.append(f"  chapter_{ch:02d}:")
        for v in sorted(chapters[ch], key=lambda x: x['verse']):
            output_lines.append(f"    - chapter-{ch:02d}-shloka-{v['verse']:02d}")

    output_lines.append("")
    output_lines.append("# Verse Data")
    output_lines.append("")

    for ch in sorted(chapters.keys()):
        # Add chapter comment with name and verse count
        chapter_name = chapter_names.get(ch, f"Chapter {ch}")
        verse_count = len(chapters[ch])
        output_lines.append(f"# Chapter {ch}: {chapter_name}")
        output_lines.append(f"# Total shlokas in chapter: {verse_count}")
        output_lines.append("")

        # Add chapter name as a field (at the beginning of chapter)
        if ch in chapter_names:
            name_key = f"chapter_{ch:02d}_name"
            output_lines.append(f"{name_key}: '{chapter_names[ch]}'")
            output_lines.append("")

        # Add all verses for this chapter
        for v in sorted(chapters[ch], key=lambda x: x['verse']):
            key = f"chapter-{ch:02d}-shloka-{v['verse']:02d}"
            output_lines.append(f"{key}:")
            output_lines.append(f"  devanagari: '{v['text']}'")
            output_lines.append("")

        # Add chapter colophon at the end if available
        if ch in chapter_colophons:
            colophon_key = f"chapter_{ch:02d}_colophon"
            output_lines.append(f"{colophon_key}: '{chapter_colophons[ch]}'")
            output_lines.append("")

    return '\n'.join(output_lines)

def main():
    # Read input
    if len(sys.argv) > 1:
        # Read from file
        input_file = Path(sys.argv[1])
        if not input_file.exists():
            print(f"Error: File {input_file} not found", file=sys.stderr)
            sys.exit(1)
        input_text = input_file.read_text(encoding='utf-8')
    else:
        # Read from stdin
        input_text = sys.stdin.read()

    # Parse verses
    verses, chapter_names, chapter_colophons = parse_gita_text(input_text)

    # Generate YAML output
    yaml_output = generate_yaml_output(verses, chapter_names, chapter_colophons)

    # Print output
    print(yaml_output)

    # Print statistics to stderr
    print(f"\n# Statistics (to stderr):", file=sys.stderr)
    print(f"# Total verses parsed: {len(verses)}", file=sys.stderr)

    # Count by chapter
    chapters = {}
    for v in verses:
        chapters[v['chapter']] = chapters.get(v['chapter'], 0) + 1

    print(f"# Verses by chapter:", file=sys.stderr)
    for ch in sorted(chapters.keys()):
        print(f"#   Chapter {ch}: {chapters[ch]} verses", file=sys.stderr)

if __name__ == "__main__":
    main()
