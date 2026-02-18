#!/usr/bin/env python3
"""
Fix bhagavad-gita.yaml format to use _meta structure
"""
import yaml
from pathlib import Path

# Read current YAML
yaml_file = Path(__file__).parent.parent / "data/verses/bhagavad-gita.yaml"
with open(yaml_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Extract nested sequence and flatten it
flat_sequence = []
if 'sequence' in data:
    nested_seq = data.pop('sequence')
    for chapter_key in sorted(nested_seq.keys()):
        flat_sequence.extend(nested_seq[chapter_key])

# Create new structure with _meta
new_data = {
    '_meta': {
        'collection': 'bhagavad-gita',
        'source': 'Bhagavad Gita from sanskritdocuments.org',
        'description': 'Complete Bhagavad Gita with 701 shlokas across 18 chapters in canonical Devanagari text',
        'sequence': flat_sequence
    }
}

# Add all other data (verses, chapter names, colophons)
for key, value in data.items():
    new_data[key] = value

# Write back to file
with open(yaml_file, 'w', encoding='utf-8') as f:
    # Write header comment
    f.write("# Bhagavad Gita - Canonical Devanagari Text\n")
    f.write("# Format: chapter-XX-shloka-YY\n")
    f.write("\n")

    # Write YAML with proper formatting
    yaml.dump(new_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print(f"✓ Updated {yaml_file}")
print(f"✓ Flattened sequence with {len(flat_sequence)} verses")
