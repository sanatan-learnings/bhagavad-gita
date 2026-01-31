# Bhagavad Gita Scripts

This directory contains scripts for generating content for the Bhagavad Gita site.

## Current Scripts

### `generate_embeddings_sdk.py`
Generate verse embeddings using the verse-content-sdk (OpenAI by default).

```bash
# Make sure SDK is installed
pip install -r scripts/requirements.txt

# Generate embeddings
python scripts/generate_embeddings_sdk.py
```

### `generate_verse_templates.py`
Project-specific script to generate verse markdown templates.

## Legacy Scripts

Legacy standalone scripts have been moved to `scripts/legacy/` for reference.

## Dependencies

All common functionality (embeddings, audio, images) is now provided by the [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk).

Install with:
```bash
pip install -r scripts/requirements.txt
```
