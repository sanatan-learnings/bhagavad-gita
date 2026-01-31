#!/usr/bin/env python3
"""
Generate verse template files for Bhagavad Gita chapters.

Creates properly structured markdown files with YAML front matter
that you can fill in with actual verse content.
"""

import os
from pathlib import Path

def create_verse_template(chapter, verse_num, total_verses, chapter_name_en, chapter_name_hi):
    """Create a verse template with proper structure."""

    # Determine previous and next verse
    # Note: Jekyll converts underscores to hyphens in URLs, so we use hyphens here
    if verse_num == 1:
        prev_verse = "null"
    else:
        prev_verse = f"/verses/chapter-{chapter:02d}-verse-{verse_num-1:02d}/"

    if verse_num == total_verses:
        next_verse = "null"  # Or link to next chapter's first verse
    else:
        next_verse = f"/verses/chapter-{chapter:02d}-verse-{verse_num+1:02d}/"

    template = f"""---
layout: verse
title_en: "Chapter {chapter}, Verse {verse_num}"
title_hi: "अध्याय {chapter}, श्लोक {verse_num}"
chapter: {chapter}
verse_number: {verse_num}
previous_verse: {prev_verse}
next_verse: {next_verse}
chapter_info:
  number: {chapter}
  name_en: "{chapter_name_en}"
  name_hi: "{chapter_name_hi}"

# Sanskrit text in Devanagari script
devanagari: |
  [Add Sanskrit text here]

# Roman transliteration (IAST standard)
transliteration: |
  [Add transliteration here]

# Optional pronunciation notes for difficult words
phonetic_notes:
  - word: "[Sanskrit word]"
    note: "[pronunciation guide]"

# Word-by-word meanings
word_meanings:
  - word: "[Sanskrit word]"
    roman: "[romanized]"
    meaning:
      en: "[English meaning]"
      hi: "[Hindi meaning]"

# Literal translation
literal_translation:
  en: |
    [Add English literal translation here]
  hi: |
    [Add Hindi literal translation here]

# Interpretive meaning with spiritual context
interpretive_meaning:
  en: |
    [Add English commentary/interpretation here]
  hi: |
    [Add Hindi commentary/interpretation here]

# Story and context from Mahabharata (optional)
story:
  en: |
    [Add English context/story here]
  hi: |
    [Add Hindi context/story here]

# Practical application for modern life
practical_application:
  en: |
    [Add English practical guidance here]
  hi: |
    [Add Hindi practical guidance here]

# Optional: Keywords for search
keywords:
  en: [keyword1, keyword2, keyword3]
  hi: [शब्द1, शब्द2, शब्द3]
---

<!-- Optional: Additional notes or content can be added here in Markdown -->
"""
    return template

def generate_chapter_verses(chapter, total_verses, chapter_name_en, chapter_name_hi, output_dir):
    """Generate all verse files for a chapter."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Generating {total_verses} verse templates for Chapter {chapter}...")
    print(f"Output directory: {output_path}")
    print()

    for verse_num in range(1, total_verses + 1):
        filename = f"chapter_{chapter:02d}_verse_{verse_num:02d}.md"
        filepath = output_path / filename

        # Skip if file already exists (don't overwrite existing verses)
        if filepath.exists():
            print(f"  ⏭️  Skipping {filename} (already exists)")
            continue

        template = create_verse_template(chapter, verse_num, total_verses, chapter_name_en, chapter_name_hi)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)

        print(f"  ✓ Created {filename}")

    print()
    print(f"✓ Generated {total_verses} verse templates for Chapter {chapter}")
    print()

def main():
    print("=" * 70)
    print("Bhagavad Gita Verse Template Generator")
    print("=" * 70)
    print()

    # Configuration for each chapter
    chapters = [
        {
            "number": 1,
            "total_verses": 47,
            "name_en": "Arjuna's Dilemma",
            "name_hi": "अर्जुन विषाद योग"
        },
        {
            "number": 2,
            "total_verses": 72,
            "name_en": "The Yoga of Knowledge",
            "name_hi": "सांख्य योग"
        },
        # Add more chapters as needed
    ]

    output_dir = Path(__file__).parent.parent / "_verses"

    print(f"Output directory: {output_dir}")
    print()

    # Prompt user for which chapter to generate
    print("Available chapters:")
    for ch in chapters:
        print(f"  {ch['number']}. {ch['name_en']} ({ch['total_verses']} verses)")
    print()

    choice = input("Enter chapter number to generate (or 'all' for all chapters): ").strip()
    print()

    if choice.lower() == 'all':
        for chapter in chapters:
            generate_chapter_verses(
                chapter['number'],
                chapter['total_verses'],
                chapter['name_en'],
                chapter['name_hi'],
                output_dir
            )
    else:
        try:
            chapter_num = int(choice)
            chapter = next((ch for ch in chapters if ch['number'] == chapter_num), None)
            if chapter:
                generate_chapter_verses(
                    chapter['number'],
                    chapter['total_verses'],
                    chapter['name_en'],
                    chapter['name_hi'],
                    output_dir
                )
            else:
                print(f"Chapter {chapter_num} not found in configuration.")
        except ValueError:
            print("Invalid input. Please enter a number or 'all'.")

    print("=" * 70)
    print("Template generation complete!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("1. Fill in verse content using authentic sources")
    print("2. See docs/content-sourcing-guide.md for resources")
    print("3. Use existing sample verses as reference")
    print("4. Run: python3 scripts/generate_embeddings_openai.py")
    print("5. Run: python3 scripts/generate_search_index.py")
    print()

if __name__ == '__main__':
    main()
