#!/usr/bin/env python3
"""
Sort scenes in bhagavad-gita.yml by chapter and verse number
"""
import yaml
from pathlib import Path

# Custom YAML representer to avoid weird formatting
class literal_str(str): pass
def literal_str_representer(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(literal_str, literal_str_representer)

# Read current YAML preserving string formats
yaml_file = Path(__file__).parent.parent / "data/scenes/bhagavad-gita.yml"
with open(yaml_file, 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# Extract scenes and sort them
if 'scenes' in data:
    scenes = data['scenes']

    # Sort by extracting chapter and verse numbers
    def sort_key(scene_id):
        # Extract numbers from "chapter-XX-shloka-YY"
        parts = scene_id.split('-')
        chapter = int(parts[1])
        verse = int(parts[3])
        return (chapter, verse)

    sorted_scene_keys = sorted(scenes.keys(), key=sort_key)

    # Rebuild scenes dict in sorted order
    sorted_scenes = {}
    for key in sorted_scene_keys:
        scene = scenes[key]
        # Preserve multiline strings
        if 'description' in scene and '\n' not in scene['description']:
            scene['description'] = literal_str(scene['description'])
        sorted_scenes[key] = scene

    data['scenes'] = sorted_scenes

# Write back to file with better formatting
with open(yaml_file, 'w', encoding='utf-8') as f:
    yaml.dump(data, f,
              default_flow_style=False,
              allow_unicode=True,
              sort_keys=False,
              width=1000,
              indent=2)

print(f"✓ Sorted {len(sorted_scenes)} scenes in {yaml_file}")
