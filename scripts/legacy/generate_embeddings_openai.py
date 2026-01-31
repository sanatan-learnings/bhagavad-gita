#!/usr/bin/env python3
"""
Generate embeddings for Bhagavad Gita verses using OpenAI's API.

This script reads all verse markdown files, extracts YAML front matter,
combines fields into rich semantic documents, generates embeddings using
OpenAI's text-embedding-3-small model, and outputs embeddings.json.

Installation:
  pip install openai python-dotenv pyyaml

Usage:
  python scripts/generate_embeddings_openai.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
import yaml

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed")
    print("Please install it with: pip install openai")
    sys.exit(1)

# Load environment variables from .env file (optional, for local development)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not available (CI/CD environment), use environment variables directly
    pass

# Configuration
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSIONS = 1536
VERSES_DIR = Path(__file__).parent.parent / "_verses"
OUTPUT_FILE = Path(__file__).parent.parent / "data" / "embeddings.json"

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

def build_document(verse_data, lang='en'):
    """
    Build a rich semantic document from verse data.

    Combines multiple fields to capture full spiritual context:
    - Title (semantic anchor)
    - Sanskrit text (original terminology)
    - Translation (basic meaning)
    - Commentary (spiritual depth)
    - Practical Application (teachings and guidance)
    """
    parts = []

    # Title
    title_key = f'title_{lang}'
    if title_key in verse_data:
        parts.append(verse_data[title_key])

    # Sanskrit text (for English) or Devanagari (for Hindi)
    if lang == 'en' and 'transliteration' in verse_data:
        parts.append(f"Sanskrit: {verse_data['transliteration']}")
    elif lang == 'hi' and 'devanagari' in verse_data:
        parts.append(f"संस्कृत: {verse_data['devanagari']}")

    # Translation
    translation_key = 'translation'
    if translation_key in verse_data:
        trans_data = verse_data[translation_key]
        if isinstance(trans_data, dict) and lang in trans_data:
            parts.append(f"Translation: {trans_data[lang]}")

    # Commentary
    commentary_key = 'commentary'
    if commentary_key in verse_data:
        comm_data = verse_data[commentary_key]
        if isinstance(comm_data, dict) and lang in comm_data:
            parts.append(f"Commentary: {comm_data[lang]}")

    # Practical Application
    if 'practical_application' in verse_data:
        app_data = verse_data['practical_application']
        if isinstance(app_data, dict) and lang in app_data:
            parts.append(f"Practical Guidance: {app_data[lang]}")

    # Keywords for better semantic search
    if 'keywords' in verse_data:
        keywords = verse_data['keywords']
        if isinstance(keywords, dict) and lang in keywords:
            if isinstance(keywords[lang], list):
                parts.append(f"Keywords: {', '.join(keywords[lang])}")

    return "\n\n".join(parts)

def generate_verse_url(verse_data):
    """Generate URL path for verse page."""
    chapter = verse_data.get('chapter', 1)
    verse = verse_data.get('verse', 1)
    return f'/verses/chapter_{chapter:02d}_verse_{verse:02d}/'

def process_verse_file(file_path, client):
    """Process a single verse file and return metadata + embeddings."""
    print(f"Processing {file_path.name}...")

    verse_data = extract_yaml_frontmatter(file_path)
    if not verse_data:
        print(f"  Warning: Could not extract YAML from {file_path.name}")
        return None

    chapter = verse_data.get('chapter', 1)
    verse = verse_data.get('verse', 1)

    # Build documents for both languages
    doc_en = build_document(verse_data, 'en')
    doc_hi = build_document(verse_data, 'hi')

    # Get embeddings from OpenAI
    print(f"  Generating embeddings via OpenAI API...")
    try:
        response_en = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=doc_en
        )
        emb_en = response_en.data[0].embedding

        response_hi = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=doc_hi
        )
        emb_hi = response_hi.data[0].embedding
    except Exception as e:
        print(f"  Error generating embeddings: {e}")
        return None

    # Prepare result structure
    result = {
        'en': {
            'chapter': chapter,
            'verse': verse,
            'title': verse_data.get('title_en', ''),
            'url': generate_verse_url(verse_data),
            'embedding': emb_en,
            'metadata': {
                'devanagari': verse_data.get('devanagari', ''),
                'transliteration': verse_data.get('transliteration', ''),
                'translation': verse_data.get('translation', {}).get('en', '')
            }
        },
        'hi': {
            'chapter': chapter,
            'verse': verse,
            'title': verse_data.get('title_hi', ''),
            'url': generate_verse_url(verse_data),
            'embedding': emb_hi,
            'metadata': {
                'devanagari': verse_data.get('devanagari', ''),
                'transliteration': verse_data.get('transliteration', ''),
                'translation': verse_data.get('translation', {}).get('hi', '')
            }
        }
    }

    return result

def main():
    """Main execution flow."""
    print("=" * 60)
    print("Bhagavad Gita Embeddings Generator (OpenAI)")
    print("=" * 60)
    print(f"Model: {EMBEDDING_MODEL}")
    print(f"Dimensions: {EMBEDDING_DIMENSIONS}")
    print(f"Provider: OpenAI")
    print(f"Verses directory: {VERSES_DIR}")
    print(f"Output file: {OUTPUT_FILE}")
    print()

    # Check API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("Error: OPENAI_API_KEY not found in environment")
        print("Please set it in your .env file")
        sys.exit(1)

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Check verses directory
    if not VERSES_DIR.exists():
        print(f"Error: Verses directory not found: {VERSES_DIR}")
        sys.exit(1)

    # Find all verse files
    verse_files = sorted(VERSES_DIR.glob("*.md"))
    print(f"Found {len(verse_files)} verse files")
    print()

    # Process all verses
    verses_en = []
    verses_hi = []
    total_tokens = 0

    for verse_file in verse_files:
        result = process_verse_file(verse_file, client)
        if result:
            verses_en.append(result['en'])
            verses_hi.append(result['hi'])
        print()

    # Sort by chapter and verse
    sort_key = lambda v: (v.get('chapter', 0), v.get('verse', 0))
    verses_en.sort(key=sort_key)
    verses_hi.sort(key=sort_key)

    # Build output structure
    output = {
        'model': EMBEDDING_MODEL,
        'dimensions': EMBEDDING_DIMENSIONS,
        'provider': 'openai',
        'generated_at': datetime.now().isoformat(),
        'verses': {
            'en': verses_en,
            'hi': verses_hi
        }
    }

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Write to file
    print(f"Writing embeddings to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 60)
    print("Generation Complete!")
    print("=" * 60)
    print(f"Total verses processed: {len(verses_en)}")
    print(f"English embeddings: {len(verses_en)}")
    print(f"Hindi embeddings: {len(verses_hi)}")
    print(f"Output file size: {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")
    print()

if __name__ == '__main__':
    main()
