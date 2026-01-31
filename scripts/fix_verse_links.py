#!/usr/bin/env python3
"""
Fix verse navigation links to use hyphens instead of underscores.
Jekyll converts underscores in filenames to hyphens in URLs.
"""

import os
import re
from pathlib import Path

def fix_verse_links_in_file(filepath):
    """Update previous_verse and next_verse links to use hyphens."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace underscores with hyphens in verse links
    # Match patterns like: /verses/chapter_01_verse_02/
    original = content
    content = re.sub(
        r'/verses/(chapter_\d+_verse_\d+)/',
        lambda m: '/verses/' + m.group(1).replace('_', '-') + '/',
        content
    )

    # Only write if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 70)
    print("Fix Verse Navigation Links")
    print("=" * 70)
    print()

    verses_dir = Path(__file__).parent.parent / "_verses"

    if not verses_dir.exists():
        print(f"Error: Verses directory not found: {verses_dir}")
        return

    print(f"Verses directory: {verses_dir}")
    print()

    verse_files = sorted(verses_dir.glob("chapter_*.md"))
    updated_count = 0

    for verse_file in verse_files:
        if fix_verse_links_in_file(verse_file):
            print(f"  ✓ Updated {verse_file.name}")
            updated_count += 1
        else:
            print(f"  - No changes needed for {verse_file.name}")

    print()
    print("=" * 70)
    print(f"Complete! Updated {updated_count} files")
    print("=" * 70)

if __name__ == '__main__':
    main()
