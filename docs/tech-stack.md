# Technology Stack

This document outlines the complete technology stack used in the Bhagavad Gita project.

## Frontend Technologies

### Static Site Generation
- **Jekyll 4.x**: Ruby-based static site generator
  - Powers the entire site build process
  - Handles collections, layouts, and includes
  - Processes YAML front matter in verse files
  - Built-in support for Markdown and Liquid templating

### Styling
- **CSS3**: Custom stylesheets for responsive design
  - Mobile-first responsive design
  - Print-optimized styles for book generation
  - Dark mode support (planned)

### JavaScript
- **Vanilla JavaScript**: No framework dependencies
  - Language switching functionality
  - Client-side search implementation
  - RAG (Retrieval Augmented Generation) system
  - Navigation and UI interactions

### UI Components
- **Custom Components**: Built from scratch
  - Bilingual language switcher
  - Verse navigation system
  - Search interface
  - Spiritual guidance chat interface

## Backend & Infrastructure

### Hosting
- **GitHub Pages**: Free static site hosting
  - Automatic deployment via GitHub Actions
  - Custom domain support
  - HTTPS enabled by default
  - CDN-backed for global performance

### CI/CD
- **GitHub Actions**: Automated build and deployment
  - Jekyll build pipeline
  - Automatic deployment to GitHub Pages
  - Triggered on push to main branch

### API & Edge Computing
- **Cloudflare Workers**: Serverless edge functions
  - Proxy for OpenAI API requests
  - Secure API key management
  - CORS handling
  - Request/response transformation
  - 100k free requests/day

## AI & Machine Learning

### Embeddings Generation

#### Option 1: OpenAI (Recommended)
- **Model**: `text-embedding-3-small`
- **Dimensions**: 1536
- **Use Case**: High-quality semantic embeddings
- **Cost**: ~$0.10 one-time for full Gita
- **Library**: `openai` Python package (v1.0+)

#### Option 2: Local Embeddings (Free)
- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Dimensions**: 384
- **Use Case**: Free alternative, no API required
- **Library**: `sentence-transformers` Python package
- **Runtime**: HuggingFace Transformers

### Semantic Search (RAG)
- **Vector Similarity**: Cosine similarity for embedding comparison
- **Implementation**: Client-side JavaScript
- **Storage**: Pre-computed embeddings in JSON

### AI Responses
- **Model**: GPT-4o (via OpenAI API)
- **Purpose**: Contextual spiritual guidance
- **Approach**: RAG (Retrieval Augmented Generation)
  1. User query → embedding
  2. Find similar verses via cosine similarity
  3. Send top verses as context to GPT-4o
  4. Return spiritually grounded response

## Data & Content

### Content Management
- **YAML Front Matter**: Structured verse data
  - Chapter and verse metadata
  - Sanskrit (Devanagari)
  - Roman transliteration
  - Word-by-word meanings
  - Translations (English & Hindi)
  - Commentary and practical applications

### Collections
- **Jekyll Collections**: `_verses` collection
  - Each verse as a separate Markdown file
  - Automatic page generation
  - Permalinks: `/verses/chapter_XX_verse_YY/`

### Data Files
- **YAML**: Configuration and translations
  - `_data/translations/en.yml`: English UI strings
  - `_data/translations/hi.yml`: Hindi UI strings
  - `_data/themes.yml`: Image theme definitions

- **JSON**: Generated data
  - `data/embeddings.json`: Vector embeddings for RAG
  - `data/search.json`: Search index (planned)

## Development Tools

### Version Control
- **Git**: Source control
- **GitHub**: Repository hosting, collaboration, and Pages

### Python Environment
- **Python 3.8+**: For embeddings generation
- **venv**: Virtual environment management
- **pip**: Package management

### Ruby Environment
- **Ruby 3.x+**: Jekyll runtime
- **Bundler**: Dependency management
- **RubyGems**: Package ecosystem

## Python Dependencies

### Core AI/ML Libraries
```
openai>=1.0.0           # OpenAI API client
sentence-transformers   # Local embeddings (HuggingFace)
```

### Utilities
```
python-dotenv>=1.0.0    # Environment variable management
PyYAML>=6.0.0          # YAML parsing
requests>=2.31.0       # HTTP requests
Pillow>=10.0.0         # Image processing (future)
```

### Future Features (Planned)
```
elevenlabs>=1.0.0      # Text-to-speech audio generation
```

## Ruby Dependencies

### Jekyll & Plugins
```
gem "github-pages"      # GitHub Pages compatible Jekyll
gem "jekyll-seo-tag"    # SEO optimization
gem "webrick"           # Local development server
```

## Environment Variables

### Required for Full Functionality
```bash
# OpenAI API (for embeddings and spiritual guidance)
OPENAI_API_KEY=sk-...

# Cloudflare (for worker deployment)
CLOUDFLARE_ACCOUNT_ID=...
CLOUDFLARE_API_TOKEN=...
```

## Architecture Patterns

### JAMstack
- **J**avaScript: Client-side functionality
- **A**PIs: Cloudflare Workers + OpenAI API
- **M**arkup: Jekyll-generated static HTML

### Static Site Generation (SSG)
- Pre-rendered HTML at build time
- No server-side rendering needed
- Fast page loads, excellent SEO

### Retrieval Augmented Generation (RAG)
- Semantic search over verse embeddings
- Context-aware AI responses
- Grounded in actual Gita content

### Serverless Architecture
- No traditional backend servers
- Edge functions for API calls
- Pay-per-use pricing model

## Performance Considerations

### Optimization Strategies
- Static HTML (instant page loads)
- Lazy loading for embeddings
- Client-side caching
- CDN distribution via GitHub Pages
- Minified CSS/JS (production)

### Scalability
- Static site scales infinitely
- Cloudflare Workers handle API load
- Embeddings computed once, used forever
- No database connections or backend overhead

## Security

### API Key Management
- Environment variables for secrets
- `.env` gitignored
- Cloudflare Workers proxy API calls
- No API keys exposed to client

### Content Security
- Static site (no server vulnerabilities)
- HTTPS by default
- No user data storage
- No authentication required

## Browser Compatibility

### Supported Browsers
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Chrome Mobile)
- Progressive enhancement approach

### JavaScript Requirements
- ES6+ features used
- Fetch API for network requests
- Local Storage for language preference

## Future Technology Additions

### Planned Features
1. **Audio Narration**
   - ElevenLabs API for Sanskrit recitation
   - Hindi commentary audio

2. **Image Generation**
   - DALL-E 3 for chapter illustrations
   - Scene visualizations

3. **Advanced Search**
   - Full-text search with Lunr.js
   - Fuzzy matching
   - Keyword highlighting

4. **Progressive Web App (PWA)**
   - Offline support
   - Mobile app experience
   - Install to home screen

## Cost Summary

| Component | Monthly Cost | Notes |
|-----------|--------------|-------|
| Hosting | $0 | GitHub Pages free tier |
| CI/CD | $0 | GitHub Actions free tier |
| Workers | $0 | Cloudflare free tier (100k req/day) |
| Embeddings | $0.10 | One-time (OpenAI) or $0 (local) |
| AI Guidance | Variable | ~$0.01 per user query |

**Total Monthly**: ~$0 for typical usage

## Development Philosophy

### Principles
1. **Keep It Simple**: No framework bloat
2. **User First**: Fast, accessible, mobile-friendly
3. **Free to Run**: Minimize operational costs
4. **Open Source**: MIT licensed, community-driven
5. **Content Quality**: Accuracy over quantity

### Technology Choices
- **Jekyll over React/Next.js**: Simpler, faster, no build complexity
- **Vanilla JS over frameworks**: Lightweight, no dependencies
- **Static over dynamic**: Better performance, lower cost
- **Edge functions over traditional backend**: Serverless, scalable
