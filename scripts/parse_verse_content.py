#!/usr/bin/env python3
"""
Parse AI-generated content from verse files and move it into YAML frontmatter.

This script fixes verse files where verse-generate left content in a code block
instead of properly parsing it into the frontmatter.
"""

import re
import yaml
from pathlib import Path


def parse_verse_file(file_path):
    """Parse a verse file and extract the generated YAML content."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if file has the TODO comment (indicates unparsed content)
    if '<!-- TODO: Parse and format the AI-generated content below -->' not in content:
        return None

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        print(f"⚠ Could not extract frontmatter from {file_path}")
        return None

    frontmatter_text = match.group(1)
    frontmatter = yaml.safe_load(frontmatter_text)

    # Extract generated YAML from code block
    code_block_match = re.search(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    if not code_block_match:
        print(f"⚠ Could not find YAML code block in {file_path}")
        return None

    generated_yaml_text = code_block_match.group(1)
    generated_data = yaml.safe_load(generated_yaml_text)

    if not generated_data or 'verse' not in generated_data:
        print(f"⚠ Invalid generated YAML in {file_path}")
        return None

    verse_data = generated_data['verse']

    # Merge generated content into frontmatter
    if 'transliteration' in generated_data:
        trans = generated_data['transliteration']
        if isinstance(trans, dict) and 'IAST' in trans:
            frontmatter['transliteration'] = trans['IAST'].strip()
        else:
            frontmatter['transliteration'] = str(trans).strip()

    if 'word_meanings' in generated_data:
        word_meanings = []
        for item in generated_data['word_meanings']:
            # Parse format: "संस्कृत (roman): english; hindi; description"
            sanskrit = item.get('संस्कृत', '')
            roman = item.get('roman', '')
            english = item.get('english', '')
            hindi = item.get('hindi', '')

            word_meanings.append({
                'word': sanskrit,
                'roman': roman,
                'meaning': {
                    'en': english,
                    'hi': hindi
                }
            })
        frontmatter['word_meanings'] = word_meanings

    if 'literal_translation' in generated_data:
        frontmatter['literal_translation'] = generated_data['literal_translation']

    if 'interpretive_meaning' in generated_data:
        frontmatter['interpretive_meaning'] = generated_data['interpretive_meaning']

    if 'story_context' in generated_data:
        frontmatter['story'] = generated_data['story_context']

    if 'practical_application' in generated_data:
        frontmatter['practical_application'] = generated_data['practical_application']

    return frontmatter


def write_verse_file(file_path, frontmatter):
    """Write the updated frontmatter to the verse file."""
    # Convert frontmatter to YAML
    yaml_content = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # Create complete file content
    content = f"---\n{yaml_content}---\n"

    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✓ Updated {file_path.name}")


def main():
    """Process all verse files."""
    verses_dir = Path(__file__).parent.parent / '_verses'

    if not verses_dir.exists():
        print(f"✗ Verses directory not found: {verses_dir}")
        return

    verse_files = list(verses_dir.glob('chapter_*.md'))
    print(f"Found {len(verse_files)} verse files\n")

    updated = 0
    for verse_file in sorted(verse_files):
        frontmatter = parse_verse_file(verse_file)
        if frontmatter:
            write_verse_file(verse_file, frontmatter)
            updated += 1

    print(f"\n✓ Updated {updated} verse files")


if __name__ == '__main__':
    main()
