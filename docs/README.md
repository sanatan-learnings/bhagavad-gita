# Documentation

This directory contains documentation and configuration files for the Bhagavad Gita website.

## Files

- **content-generation.md** - Complete guide for generating verses with AI
- **content-sourcing-guide.md** - Sources and validation for verse content
- **image-prompts.md** - Scene descriptions for DALL-E 3 image generation
- **themes/** - Visual style configurations for image generation
- **cloudflare-worker-setup.md** - Cloudflare Worker API proxy setup
- **local-development.md** - Local development setup
- **tech-stack.md** - Technologies used in the project

## Content Generation

See **[content-generation.md](content-generation.md)** for the complete guide on generating verses with AI.

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
