#!/usr/bin/env python3
"""
Generate embeddings for Bhagavad Gita using the verse-content-sdk.

This is a thin wrapper that uses the shared SDK for embedding generation.

Usage:
    python scripts/generate_embeddings_sdk.py
"""

from pathlib import Path
from verse_content_sdk.embeddings import generate_embeddings

# Project paths
PROJECT_DIR = Path(__file__).parent.parent
VERSES_DIR = PROJECT_DIR / "_verses"
OUTPUT_FILE = PROJECT_DIR / "data" / "embeddings.json"

if __name__ == '__main__':
    generate_embeddings(
        verses_dir=VERSES_DIR,
        output_file=OUTPUT_FILE
    )
