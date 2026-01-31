#!/usr/bin/env python3
"""
Generate search index for Bhagavad Gita verses.

Creates a search.json file with all verse content for client-side search.
"""

import os
import json
import yaml
from pathlib import Path

# Paths
VERSES_DIR = Path(__file__).parent.parent / "_verses"
OUTPUT_FILE = Path(__file__).parent.parent / "data" / "search.json"

def extract_yaml_frontmatter(file_path):
    """Extract YAML front matter from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return None

    end_idx = content.find('---', 3)
    if end_idx == -1:
        return None

    yaml_content = content[3:end_idx].strip()
    return yaml.safe_load(yaml_content)

def build_search_entry(verse_data, file_name):
    """Build search index entry for a verse."""
    chapter = verse_data.get('chapter', 0)
    verse_num = verse_data.get('verse_number', verse_data.get('verse', 0))

    # Build URL
    url = f"/verses/{file_name.replace('.md', '')}/"

    # Extract searchable text
    entry = {
        'id': f"ch{chapter}_v{verse_num}",
        'chapter': chapter,
        'verse': verse_num,
        'url': url,
        'title_en': verse_data.get('title_en', ''),
        'title_hi': verse_data.get('title_hi', ''),
        'devanagari': verse_data.get('devanagari', ''),
        'transliteration': verse_data.get('transliteration', ''),
    }

    # Add translations
    if 'literal_translation' in verse_data:
        trans = verse_data['literal_translation']
        if isinstance(trans, dict):
            entry['translation_en'] = trans.get('en', '')
            entry['translation_hi'] = trans.get('hi', '')
        else:
            entry['translation_en'] = str(trans)

    if 'translation' in verse_data:
        trans = verse_data['translation']
        if isinstance(trans, dict):
            entry['translation_en'] = trans.get('en', entry.get('translation_en', ''))
            entry['translation_hi'] = trans.get('hi', entry.get('translation_hi', ''))

    # Add commentary/meaning
    if 'interpretive_meaning' in verse_data:
        meaning = verse_data['interpretive_meaning']
        if isinstance(meaning, dict):
            entry['meaning_en'] = meaning.get('en', '')
            entry['meaning_hi'] = meaning.get('hi', '')

    if 'commentary' in verse_data:
        comm = verse_data['commentary']
        if isinstance(comm, dict):
            entry['commentary_en'] = comm.get('en', '')
            entry['commentary_hi'] = comm.get('hi', '')

    # Add word meanings (concatenated for search)
    if 'word_meanings' in verse_data:
        words_en = []
        words_hi = []
        for item in verse_data['word_meanings']:
            if isinstance(item.get('meaning'), dict):
                words_en.append(f"{item.get('word', '')} - {item.get('meaning', {}).get('en', '')}")
                words_hi.append(f"{item.get('word', '')} - {item.get('meaning', {}).get('hi', '')}")
        entry['word_meanings_en'] = ' '.join(words_en)
        entry['word_meanings_hi'] = ' '.join(words_hi)

    return entry

def main():
    """Generate search index."""
    print("=" * 60)
    print("Bhagavad Gita Search Index Generator")
    print("=" * 60)
    print(f"Verses directory: {VERSES_DIR}")
    print(f"Output file: {OUTPUT_FILE}")
    print()

    if not VERSES_DIR.exists():
        print(f"Error: Verses directory not found: {VERSES_DIR}")
        return 1

    # Find all verse files
    verse_files = sorted(VERSES_DIR.glob("*.md"))
    print(f"Found {len(verse_files)} verse files")
    print()

    # Process all verses
    search_index = []

    for verse_file in verse_files:
        print(f"Processing {verse_file.name}...")
        verse_data = extract_yaml_frontmatter(verse_file)

        if verse_data:
            entry = build_search_entry(verse_data, verse_file.name)
            search_index.append(entry)
        else:
            print(f"  Warning: Could not extract YAML from {verse_file.name}")

    # Sort by chapter and verse
    search_index.sort(key=lambda x: (x.get('chapter', 0), x.get('verse', 0)))

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write to file
    print()
    print(f"Writing search index to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(search_index, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 60)
    print("Generation Complete!")
    print("=" * 60)
    print(f"Total verses indexed: {len(search_index)}")
    print(f"Output file size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print()

    return 0

if __name__ == '__main__':
    exit(main())
