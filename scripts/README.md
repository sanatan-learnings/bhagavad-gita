# Bhagavad Gita Scripts

This directory contains project-specific scripts for the Bhagavad Gita site.

## Setup

Install the verse-content-sdk which provides all common functionality:

```bash
pip install -r scripts/requirements.txt
```

This installs the SDK and provides command-line tools:
- `verse-embeddings` - Generate embeddings (OpenAI or local)
- `verse-audio` - Generate audio pronunciations
- `verse-images` - Generate theme images

## Common Tasks

### Generate Embeddings

```bash
# Using OpenAI (default, requires OPENAI_API_KEY in .env)
verse-embeddings --verses-dir _verses --output data/embeddings.json

# Using local models (free, no API key needed)
verse-embeddings --verses-dir _verses --output data/embeddings.json --provider huggingface
```

### Generate Audio (Coming Soon)
```bash
verse-audio --verses-dir _verses --output-dir audio
```

### Generate Images (Coming Soon)
```bash
verse-images --verses-dir _verses --output-dir images
```

### Deploy Cloudflare Worker
```bash
# Deploy the semantic search worker
verse-deploy
```

## Project-Specific Scripts

### `generate_verse_templates.py`
Generate verse markdown templates specific to Bhagavad Gita structure.

```bash
python scripts/generate_verse_templates.py
```

## Legacy Scripts

Legacy standalone scripts have been moved to `scripts/legacy/` for reference.

## More Information

- SDK Repository: https://github.com/sanatan-learnings/verse-content-sdk
- SDK provides shared functionality across all Sanatan Learnings projects
