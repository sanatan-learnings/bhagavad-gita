# Bhagavad Gita: A Comprehensive Guide

An interactive web-based guide to the Bhagavad Gita featuring verse-by-verse analysis, bilingual translations, and AI-powered spiritual guidance.

🌐 **[View Live Site](https://sanatan-learnings.github.io/bhagavad-gita)**

## 🌟 Features

- **Comprehensive Verse Analysis**: Each verse includes:
  - Original Sanskrit (Devanagari script)
  - Roman transliteration
  - Word-by-word meanings
  - Literal translation (English & Hindi)
  - Interpretive meaning with spiritual context
  - Story and context from Mahabharata
  - Practical applications for modern life

- **Bilingual Support**: Full interface in English and Hindi with seamless language switching

- **AI-Powered Spiritual Guidance**: Ask questions about Gita teachings and receive contextual answers powered by:
  - OpenAI or Local embeddings (HuggingFace Transformers)
  - Semantic search (Retrieval Augmented Generation)
  - GPT-4o for thoughtful spiritual responses
  - Cloudflare Worker for secure API management

- **Full-Text Search**: Search across all verses, translations, and meanings

- **Responsive Design**: Mobile-friendly interface with keyboard navigation

- **Print-Friendly**: Generate custom books with selected chapters

## 📚 Current Status

**Chapters Included**: Chapters 1-2 (119 verses planned)

**Content Status**:
- ✅ Complete project structure
- ✅ Full bilingual UI
- ✅ RAG system with embeddings
- ⚠️ **Sample verses only** (2 verses implemented as examples)
- ⏳ Full verse content needs to be added

**Note**: This repository includes a complete working framework with 2 sample verses demonstrating the structure. Additional verses should follow the same YAML format in the `_verses/` directory.

## 🚀 Quick Start

### Prerequisites

- Ruby 3.x or higher
- Python 3.8+ (for content generation)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanatan-learnings/bhagavad-gita.git
   cd bhagavad-gita
   ```

2. **Install dependencies**
   ```bash
   # Ruby dependencies for Jekyll
   gem install bundler
   bundle install

   # Python virtual environment for content generation
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install verse-content-sdk
   ```

3. **Run Jekyll locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open http://localhost:4000/bhagavad-gita in your browser

### Generate Content & Embeddings

1. **Set up API keys**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys:
   # - OPENAI_API_KEY (for content generation and embeddings)
   # - ELEVENLABS_API_KEY (for audio pronunciation)
   ```

2. **Activate virtual environment**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Generate verse content** (fully automated)
   ```bash
   verse-generate --chapter 1 --verse 3 --all
   ```

   Creates complete verse with text, image, and audio. See **[docs/guides/content-generation.md](docs/guides/content-generation.md)** for details.

4. **Generate embeddings** (for AI guidance feature)

   **Option A: OpenAI embeddings (Recommended)**
   ```bash
   verse-embeddings --verses-dir _verses --output data/embeddings.json
   ```

   **Option B: Local embeddings (Free, no API key)**
   ```bash
   verse-embeddings --verses-dir _verses --output data/embeddings.json --provider huggingface
   ```

This creates `data/embeddings.json` needed for the spiritual guidance feature.

## 📖 Documentation

### Guides
- **[Local Development](docs/guides/local-development.md)** - Setup and running locally
- **[Content Generation](docs/guides/content-generation.md)** - Creating verses with AI
- **[Content Verification](docs/guides/content-verification-guide.md)** - Verifying AI-generated content
- **[Cloudflare Worker](docs/guides/cloudflare-worker-setup.md)** - API proxy deployment

### Reference
- **[Tech Stack](docs/reference/tech-stack.md)** - Technical architecture
- **[Image Prompts](docs/reference/image-prompts.md)** - Scene descriptions

### SDK
- **[verse-content-sdk](https://github.com/sanatan-learnings/verse-content-sdk)** - Full SDK documentation

## 📖 Adding Content

### Automated Content Generation (Recommended)

Generate complete verses with one command:

```bash
verse-generate --chapter 1 --verse 5 --all
```

This automatically creates:
- Complete verse file with AI-generated translations and commentary
- Scene description for the image
- DALL-E 3 generated artwork
- ElevenLabs audio pronunciation (full + slow speeds)

See **[docs/content-generation.md](docs/content-generation.md)** for complete instructions.

### Manual Content Creation (Advanced)

If you prefer manual creation, verse files follow this structure in `_verses/`:

story:
  en: "Context from Mahabharata"
  hi: "महाभारत से संदर्भ"

practical_application:
  en: "How to apply in daily life"
  hi: "दैनिक जीवन में कैसे लागू करें"
---
```

### After Adding Content

1. **Regenerate embeddings** if you added new verses:
   ```bash
   verse-embeddings --verses-dir _verses --output data/embeddings.json
   ```

2. **Test locally** to ensure everything renders correctly:
   ```bash
   bundle exec jekyll serve
   ```

3. **Commit and push** to deploy to GitHub Pages

## 🔧 Deploying the Spiritual Guidance API

The RAG-powered spiritual guidance feature requires a Cloudflare Worker:

1. **Install Wrangler** (Cloudflare CLI)
   ```bash
   npm install -g wrangler
   ```

2. **Authenticate with Cloudflare**
   ```bash
   wrangler login
   ```

3. **Set up OpenAI API key**
   ```bash
   wrangler secret put OPENAI_API_KEY
   ```
   Paste your OpenAI API key when prompted

4. **Deploy the worker**
   ```bash
   wrangler deploy
   ```

5. **Update guidance.js** with your worker URL

## 💰 Cost Breakdown

| Component | Cost | Notes |
|-----------|------|-------|
| GitHub Pages Hosting | FREE | Static site hosting |
| Embeddings Generation | FREE or ~$0.10 | FREE with local models OR ~$0.10 for OpenAI embeddings (one-time) |
| Cloudflare Worker | FREE | 100k requests/day free tier |
| OpenAI API (Guidance) | ~$0.01/query | Only when users ask questions |
| **Total Setup** | $0-$0.10 | One-time embedding cost if using OpenAI |
| **Monthly Operational** | ~$0 | Negligible unless heavy guidance usage |

## 📁 Project Structure

```
bhagavad-gita/
├── _verses/              # Verse content files (YAML)
├── _layouts/             # HTML templates
├── _data/
│   ├── translations/     # UI strings (en.yml, hi.yml)
│   └── themes.yml       # Image theme definitions
├── assets/
│   ├── css/             # Styling
│   └── js/              # Language, navigation, RAG system
├── data/
│   └── embeddings.json  # Generated embeddings for RAG
├── scripts/
│   ├── README.md         # Scripts documentation
│   └── requirements.txt  # Python dependencies
├── workers/
│   └── cloudflare-worker.js  # API proxy for spiritual guidance
├── docs/                # Documentation (to be added)
├── index.html           # Home page
├── full-gita.html       # Full text view
├── guidance.html        # AI guidance interface
├── search.html          # Search interface
└── _config.yml          # Jekyll configuration
```

## 🤝 Contributing

Contributions are welcome! Areas where help is needed:

1. **Content**: Adding verses for Chapters 1 and 2 (117 verses remaining)
2. **Translations**: Improving Hindi translations
3. **Documentation**: Adding guides and explanations
4. **Features**: Audio narration, image generation (future)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the [Hanuman Chalisa project](https://github.com/sanatan-learnings/hanuman-chalisa)
- Built with Jekyll and hosted on GitHub Pages
- AI features powered by HuggingFace, OpenAI, and Cloudflare Workers
- Sanskrit transliterations follow IAST standards

## 📞 Support

- [Report issues](https://github.com/sanatan-learnings/bhagavad-gita/issues)
- [Ask questions](https://github.com/sanatan-learnings/bhagavad-gita/discussions)

---

**Om Shanti Shanti Shanti** 🕉️
