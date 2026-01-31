# Technology Stack

## Architecture Overview

The Bhagavad Gita project uses a **static site generation approach** combining Jekyll for build processes, GitHub Pages for hosting, and AI-powered embeddings for semantic search. The workflow flows from development through content management (YAML/Markdown) to automated deployment via GitHub Actions.

## Core Technologies

**Static Site Generation:**
- Jekyll v4.x serves as the Ruby-based site generator
- GitHub Pages provides free hosting with automatic builds via Actions
- Liquid templates power dynamic HTML rendering

**Frontend Stack:**
- HTML5 for semantic structure
- Custom CSS with responsive design and print-optimized layouts
- Vanilla JavaScript handles language switching, navigation, and RAG system without framework dependencies

**Content Organization:**
- YAML front matter structures all verse data (Devanagari, transliteration, translations, commentary)
- Each verse as separate markdown file in `_verses/` collection
- Multi-language support for English and Hindi with extensible architecture

## AI & Semantic Search

**Embeddings:**
OpenAI's text-embedding-3-small generates 1536-dimensional embeddings for all verses. Alternative local generation available via sentence-transformers (384 dimensions, free). One-time generation cost approximately $0.10 for complete Gita using OpenAI.

**Spiritual Guidance (RAG System):**
The guidance interface implements retrieval augmented generation combining semantic search via cosine similarity with GPT-4o for context-aware responses. Users query the Gita teachings, the system finds relevant verses through embedding similarity, then GPT-4o provides spiritual guidance grounded in actual scripture.

**API Architecture:**
Two deployment modes available: (1) User-provided OpenAI API key stored locally in browser localStorage, or (2) Cloudflare Worker proxy handling API requests securely without exposing credentials. Semantic search operates entirely client-side in JavaScript.

## Development Workflow

Content development emphasizes version control through Git. Verse files follow consistent YAML structure. Python scripts generate embeddings after content updates. Jekyll rebuilds site automatically. GitHub Actions deploys on push to main branch.

## Performance and Cost

Static site generation eliminates server overhead, achieving instant page loads via CDN. Pre-computed embeddings loaded once per session. GitHub Pages hosting remains perpetually free. OpenAI embedding generation costs ~$0.10 one-time, spiritual guidance queries cost ~$0.01 each. Cloudflare Workers free tier provides 100,000 requests daily.

## Technical Implementation Details

**Python Environment:**
- `openai>=1.0.0` for API access
- `python-dotenv` for environment management
- `PyYAML` for verse file parsing
- Optional: `sentence-transformers` for local embeddings

**Ruby Dependencies:**
- `github-pages` gem ensures compatibility
- `jekyll-seo-tag` for optimization
- `webrick` for local development server

**Data Flow:**
Verse markdown files → YAML extraction → Python embedding generation → JSON output → Client-side JavaScript loading → User query → Semantic search → GPT-4o guidance → Response display with verse citations

## Future Enhancements

Planned features include audio narration via ElevenLabs (Sanskrit recitation, Hindi commentary), chapter illustrations via DALL-E 3, full-text search with Lunr.js, progressive web app capabilities for offline access, and extended verse coverage beyond initial chapters.
