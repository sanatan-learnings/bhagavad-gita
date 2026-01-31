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
- Python 3.8+ (for embeddings generation)
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanatan-learnings/bhagavad-gita.git
   cd bhagavad-gita
   ```

2. **Install Ruby dependencies**
   ```bash
   gem install bundler
   bundle install
   ```

3. **Run Jekyll locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open http://localhost:4000/bhagavad-gita in your browser

### Generate Embeddings (for RAG System)

1. **Set up Python environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r scripts/requirements.txt
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key (for OpenAI embeddings)
   ```

3. **Generate embeddings**

   **Option A: OpenAI embeddings (Recommended for better quality)**
   ```bash
   python scripts/generate_embeddings_openai.py
   ```

   **Option B: Local embeddings (Free, no API key needed)**
   ```bash
   python scripts/generate_embeddings_local.py
   ```

This creates `data/embeddings.json` needed for the spiritual guidance feature.

## 📖 Adding Content

### Adding Verses

Create a new file in `_verses/` following this naming convention:
- `chapter_01_verse_01.md` through `chapter_01_verse_47.md` (Chapter 1)
- `chapter_02_verse_01.md` through `chapter_02_verse_72.md` (Chapter 2)

Use the existing sample verses as templates. Each verse file should include:

```yaml
---
layout: verse
title_en: "Chapter X, Verse Y"
title_hi: "अध्याय X, श्लोक Y"
chapter: X
verse_number: Y
previous_verse: /verses/chapter_XX_verse_YY/
next_verse: /verses/chapter_XX_verse_YY/
chapter_info:
  number: X
  name_en: "Chapter Name"
  name_hi: "अध्याय का नाम"

devanagari: |
  Sanskrit text here

transliteration: |
  Romanized text here

word_meanings:
  - word: "संस्कृत"
    roman: "sanskrit"
    meaning:
      en: "English meaning"
      hi: "हिंदी अर्थ"

literal_translation:
  en: "English translation"
  hi: "हिंदी अनुवाद"

interpretive_meaning:
  en: "Detailed explanation in English"
  hi: "हिंदी में विस्तृत व्याख्या"

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
   python scripts/generate_embeddings_local.py
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
│   ├── generate_embeddings_local.py
│   └── requirements.txt
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
