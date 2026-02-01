# Documentation

Documentation for the Bhagavad Gita website.

## Structure

```
docs/
├── guides/                      # Step-by-step how-to guides
│   ├── local-development.md     # Setup and running locally
│   ├── content-generation.md    # Creating verses with AI
│   ├── content-sourcing-guide.md # Authentic content sources
│   └── cloudflare-worker-setup.md # API proxy deployment
├── reference/                   # Reference material
│   ├── image-prompts.md         # Scene descriptions for images
│   └── tech-stack.md            # Technical architecture
└── themes/                      # Image theme configurations
```

## Quick Start

### Generate Content

```bash
# Generate everything for a verse
verse-generate --chapter 2 --verse 47 --all
```

### Commands

- `verse-generate` - Generate text, images, and audio
- `verse-images` - Generate images using DALL-E 3
- `verse-audio` - Generate audio using ElevenLabs
- `verse-embeddings` - Generate embeddings for semantic search
- `verse-deploy` - Deploy Cloudflare Worker

See [verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk) for full SDK documentation.

## Guides

- **[Local Development](guides/local-development.md)** - Setup and run locally
- **[Content Generation](guides/content-generation.md)** - Create verses with AI
- **[Content Verification](guides/content-verification-guide.md)** - Verify AI-generated content
- **[Cloudflare Worker](guides/cloudflare-worker-setup.md)** - Deploy API proxy

## Reference

- **[Image Prompts](reference/image-prompts.md)** - Scene descriptions
- **[Tech Stack](reference/tech-stack.md)** - Architecture overview
- **[Themes](themes/)** - Visual style configurations
