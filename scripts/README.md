# Bhagavad Gita Scripts

This directory contains project-specific scripts for the Bhagavad Gita site.

## Setup

Install the verse-content-sdk which provides all common functionality:

```bash
pip install -r scripts/requirements.txt
```

This installs the SDK and provides command-line tools:
- `verse-generate` - Unified command for generating complete verses (text, images, audio)
- `verse-embeddings` - Generate embeddings (OpenAI or local)
- `verse-audio` - Generate audio pronunciations
- `verse-images` - Generate theme images
- `verse-deploy` - Deploy Cloudflare Worker

## Content Generation

For detailed instructions on generating verse content, see **[GENERATING_CONTENT.md](../GENERATING_CONTENT.md)** in the project root.

### Quick Start

Generate everything for a verse (Sanskrit auto-fetched from GPT-4):

```bash
verse-generate --chapter 3 --verse 5 --all \
  --chapter-name-en "Karma Yoga" \
  --chapter-name-hi "कर्म योग"
```

**Note:** Commands are installed at `/Users/YOUR_USERNAME/Library/Python/3.13/bin/`.
Add to PATH or use full path to run them.

## Other Tasks

### Generate Embeddings

```bash
# Using OpenAI (default, requires OPENAI_API_KEY in .env)
verse-embeddings --verses-dir _verses --output data/embeddings.json

# Using local models (free, no API key needed)
verse-embeddings --verses-dir _verses --output data/embeddings.json --provider huggingface
```

### Deploy Cloudflare Worker
```bash
# Deploy the semantic search worker
verse-deploy
```

## Legacy Scripts

Legacy standalone scripts have been moved to `scripts/legacy/` for reference.

## More Information

- SDK Repository: https://github.com/sanatan-learnings/verse-content-sdk
- SDK provides shared functionality across all Sanatan Learnings projects
