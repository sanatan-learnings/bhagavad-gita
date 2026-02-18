#!/usr/bin/env python3
"""
Unwrap devanagari and colophon lines in bhagavad-gita.yaml
"""
import re
from pathlib import Path

yaml_file = Path(__file__).parent.parent / "data/verses/bhagavad-gita.yaml"

# Read file
with open(yaml_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process lines
output_lines = []
i = 0
while i < len(lines):
    line = lines[i]

    # Check if this is a devanagari or colophon line
    if re.match(r'  devanagari:', line) or re.match(r'chapter_\d+_colophon:', line):
        # Determine the indentation level
        indent_level = len(line) - len(line.lstrip())

        # Collect this line and any continuation lines
        collected = line.rstrip()
        i += 1

        # Collect continuation lines (indented more than the key)
        while i < len(lines):
            next_line = lines[i]
            next_indent = len(next_line) - len(next_line.lstrip())

            # Stop if we hit a line that's not more indented or is a comment
            if next_indent <= indent_level or next_line.strip().startswith('#') or not next_line.strip():
                break

            collected += ' ' + next_line.strip()
            i += 1

        # Write as single line
        output_lines.append(collected + '\n')
    else:
        output_lines.append(line)
        i += 1

# Write back
with open(yaml_file, 'w', encoding='utf-8') as f:
    f.writelines(output_lines)

print(f"✓ Unwrapped devanagari and colophon lines in {yaml_file}")
