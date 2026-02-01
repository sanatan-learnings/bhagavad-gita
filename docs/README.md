# Documentation

This directory contains documentation and configuration files for the Bhagavad Gita website.

## Files

- **image-prompts.md** - Scene descriptions for generating verse images using DALL-E 3
- **themes/** - Visual style configurations for image generation
- **cloudflare-worker-setup.md** - Instructions for setting up the Cloudflare Worker API proxy

## Content Generation

For documentation on generating multimedia content (text, images, audio) for verses, see the verse-content-sdk documentation:

👉 [Content Generation Guide](https://github.com/sanatan-learnings/verse-content-sdk/blob/main/docs/content-generation-guide.md)

## Quick Reference

### Generate content for a verse
```bash
verse-generate --chapter 2 --verse 47 --image --audio
```

### Commands
- `verse-generate` - Unified command for generating text, images, and audio
- `verse-images` - Generate images using DALL-E 3
- `verse-audio` - Generate audio using ElevenLabs
- `verse-embeddings` - Generate embeddings for semantic search
- `verse-deploy` - Deploy Cloudflare Worker

See the [verse-content-sdk README](https://github.com/sanatan-learnings/verse-content-sdk) for full documentation.
