# Using verse-content-sdk

This project now uses the shared `verse-content-sdk` library for common functionality.

## Installation

```bash
# Install the SDK (includes all dependencies)
pip install -r scripts/requirements.txt
```

## Available Scripts

### SDK-based Scripts (Recommended)

- `generate_embeddings_sdk.py` - Generate verse embeddings using the SDK

### Usage

```bash
# Generate embeddings
python scripts/generate_embeddings_sdk.py

# The script will:
# 1. Read verses from _verses/ directory
# 2. Generate embeddings using sentence-transformers
# 3. Save to data/embeddings.json
```

### Legacy Scripts

Original standalone scripts (kept for reference):
- `generate_embeddings_local.py` - Original local embeddings
- `generate_embeddings_openai.py` - OpenAI embeddings

## SDK Benefits

1. **Shared codebase**: Same scripts across Hanuman Chalisa and Bhagavad Gita
2. **Easier maintenance**: Updates in one place benefit all projects
3. **Tested code**: Scripts are tried and tested from hanuman-chalisa
4. **Simpler**: Project scripts are thin wrappers (10 lines instead of 200+)

## SDK Repository

https://github.com/sanatan-learnings/verse-content-sdk

## Next Steps

More functionality will be migrated to the SDK:
- Audio generation
- Image generation
- Search index generation
- Deployment scripts
