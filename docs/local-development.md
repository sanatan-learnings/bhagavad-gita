# Local Development Guide

This guide will help you set up the Bhagavad Gita project on your local machine for development.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Running the Site Locally](#running-the-site-locally)
4. [Working with Embeddings](#working-with-embeddings)
5. [Adding Content](#adding-content)
6. [Testing Changes](#testing-changes)
7. [Deploying](#deploying)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

#### 1. Ruby (3.x or higher)
**Check if installed:**
```bash
ruby --version
```

**Install on macOS:**
```bash
brew install ruby
```

**Install on Ubuntu/Debian:**
```bash
sudo apt-get install ruby-full build-essential zlib1g-dev
```

**Install on Windows:**
- Download from [RubyInstaller](https://rubyinstaller.org/)
- Choose version 3.x with DevKit

#### 2. Bundler (Ruby package manager)
```bash
gem install bundler
```

#### 3. Python (3.8 or higher)
**Check if installed:**
```bash
python3 --version
```

**Install on macOS:**
```bash
brew install python3
```

**Install on Ubuntu/Debian:**
```bash
sudo apt-get install python3 python3-pip python3-venv
```

**Install on Windows:**
- Download from [Python.org](https://www.python.org/downloads/)

#### 4. Git
**Check if installed:**
```bash
git --version
```

**Install:**
- macOS: `brew install git`
- Ubuntu: `sudo apt-get install git`
- Windows: Download from [git-scm.com](https://git-scm.com/)

## Initial Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sanatan-learnings/bhagavad-gita.git
cd bhagavad-gita
```

### 2. Install Ruby Dependencies

```bash
bundle install
```

This installs:
- Jekyll (static site generator)
- github-pages gem (GitHub Pages compatibility)
- jekyll-seo-tag (SEO optimization)
- webrick (development server)

**Troubleshooting:**
- If `bundle install` fails, try: `bundle update`
- On macOS with Apple Silicon, you may need: `bundle config set --local force_ruby_platform true`

### 3. Set Up Python Environment

#### Create Virtual Environment
```bash
python3 -m venv venv
```

#### Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

#### Install Python Dependencies
```bash
pip install -r scripts/requirements.txt
```

This installs:
- `openai`: OpenAI API client
- `sentence-transformers`: Local embeddings (optional)
- `python-dotenv`: Environment variable management
- `PyYAML`: YAML file parsing
- Other utilities

### 4. Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys
# Use any text editor (nano, vim, VS Code, etc.)
nano .env
```

**Required variables:**
```bash
# OpenAI API Key (get from: https://platform.openai.com/api-keys)
OPENAI_API_KEY=sk-proj-...

# Cloudflare (optional, only needed for deploying the worker)
CLOUDFLARE_ACCOUNT_ID=your_account_id
CLOUDFLARE_API_TOKEN=your_api_token
```

**Note:** The `.env` file is gitignored and will never be committed.

## Running the Site Locally

### Start the Jekyll Development Server

```bash
bundle exec jekyll serve
```

**Options:**
```bash
# Run with live reload (watches for file changes)
bundle exec jekyll serve --livereload

# Run on a different port
bundle exec jekyll serve --port 4001

# Show drafts
bundle exec jekyll serve --drafts

# Verbose output for debugging
bundle exec jekyll serve --verbose
```

### View the Site

Open your browser and navigate to:
```
http://localhost:4000/bhagavad-gita
```

**Note:** The `/bhagavad-gita` path matches the `baseurl` in `_config.yml`

### Stop the Server

Press `Ctrl+C` in the terminal

## Working with Embeddings

Embeddings are required for the AI-powered spiritual guidance feature.

### Option 1: Generate with OpenAI (Recommended)

**Prerequisites:**
- OpenAI API key in `.env`
- Python environment activated

**Generate:**
```bash
python scripts/generate_embeddings_openai.py
```

**Output:**
- Creates `data/embeddings.json`
- File size: ~500KB-1MB (depending on verse count)
- Cost: ~$0.10 for full Gita

**What it does:**
1. Reads all verse files from `_verses/`
2. Extracts YAML front matter
3. Combines content into semantic documents
4. Generates embeddings via OpenAI API
5. Saves both English and Hindi embeddings

### Option 2: Generate Locally (Free)

**Prerequisites:**
- Python environment activated
- No API key required

**Generate:**
```bash
python scripts/generate_embeddings_local.py
```

**Output:**
- Creates `data/embeddings.json`
- Uses sentence-transformers model
- 100% free, runs on your machine
- May take 2-5 minutes on first run (downloads model)

### Verify Embeddings

```bash
# Check if file was created
ls -lh data/embeddings.json

# View first few lines
head -n 20 data/embeddings.json
```

## Adding Content

### Adding a New Verse

#### 1. Create Verse File

Create a new file in `_verses/` directory:
```bash
# Example: Chapter 1, Verse 1
touch _verses/chapter_01_verse_01.md
```

**Naming convention:**
- `chapter_XX_verse_YY.md`
- Use zero-padding (01, 02, etc.)

#### 2. Add Verse Content

Use this template:

```yaml
---
layout: verse
title_en: "Chapter 1, Verse 1: Dhritarashtra's Question"
title_hi: "अध्याय 1, श्लोक 1: धृतराष्ट्र का प्रश्न"
chapter: 1
verse: 1
previous_verse: null  # or link to previous
next_verse: /verses/chapter_01_verse_02/

chapter_info:
  number: 1
  name_en: "Arjuna's Dilemma"
  name_hi: "अर्जुन विषाद योग"

# Sanskrit (Devanagari script)
devanagari: |
  धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः।
  मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय॥

# Transliteration (IAST)
transliteration: |
  dharma-kṣetre kuru-kṣetre
  samavetā yuyutsavaḥ
  māmakāḥ pāṇḍavāś caiva
  kim akurvata sañjaya

# Word-by-word meanings
word_meanings:
  - word: "धर्मक्षेत्रे"
    roman: "dharma-kṣetre"
    meaning:
      en: "in the place of dharma"
      hi: "धर्म के क्षेत्र में"
  - word: "कुरुक्षेत्रे"
    roman: "kuru-kṣetre"
    meaning:
      en: "in the land of Kurus"
      hi: "कुरु क्षेत्र में"
  # Add more word meanings...

# Literal translation
translation:
  en: |
    What did my sons and the sons of Pandu do, O Sanjaya,
    when they assembled together on the holy field of Kurukshetra,
    eager for battle?
  hi: |
    हे संजय! धर्मभूमि कुरुक्षेत्र में एकत्रित हुए,
    युद्ध की इच्छा रखने वाले मेरे और पाण्डु के पुत्रों ने
    क्या किया?

# Commentary and explanation
commentary:
  en: |
    This opening verse sets the stage for the entire Bhagavad Gita.
    King Dhritarashtra asks his minister Sanjaya about the events
    on the battlefield of Kurukshetra...
  hi: |
    यह प्रारंभिक श्लोक संपूर्ण भगवद् गीता की पृष्ठभूमि तैयार करता है।
    राजा धृतराष्ट्र अपने मंत्री संजय से कुरुक्षेत्र के युद्धक्षेत्र में
    घटित घटनाओं के बारे में पूछते हैं...

# Practical application
practical_application:
  en: |
    When facing difficult decisions, we must recognize the battlefield
    within ourselves - the conflict between dharma and personal desires.
  hi: |
    कठिन निर्णयों का सामना करते समय, हमें अपने भीतर के युद्धक्षेत्र को
    पहचानना चाहिए - धर्म और व्यक्तिगत इच्छाओं के बीच का संघर्ष।

# Keywords for search
keywords:
  en: [dharma, Kurukshetra, battlefield, Dhritarashtra, beginning]
  hi: [धर्म, कुरुक्षेत्र, युद्धक्षेत्र, धृतराष्ट्र, प्रारंभ]
---

<!-- Optional: Additional content can go here -->
```

#### 3. Test Locally

```bash
# Rebuild the site
bundle exec jekyll serve

# Visit the verse page
# http://localhost:4000/bhagavad-gita/verses/chapter_01_verse_01/
```

#### 4. Regenerate Embeddings

After adding new verses:
```bash
# Activate Python environment
source venv/bin/activate

# Regenerate embeddings
python scripts/generate_embeddings_openai.py
```

### Adding Translations

Edit `_data/translations/en.yml` or `hi.yml`:

```yaml
# _data/translations/en.yml
navigation:
  home: "Home"
  search: "Search"
  guidance: "Spiritual Guidance"
  full_text: "Full Gita"
```

## Testing Changes

### Check for Build Errors

```bash
# Build without serving
bundle exec jekyll build

# Check for errors in output
echo $?  # Should output 0 if successful
```

### Validate YAML Front Matter

```bash
# Test YAML parsing with Python
python3 -c "
import yaml
with open('_verses/chapter_01_verse_01.md') as f:
    content = f.read()
    yaml_content = content.split('---')[1]
    data = yaml.safe_load(yaml_content)
    print('Valid YAML')
"
```

### Test Embeddings

```bash
# Check embeddings file
python3 -c "
import json
with open('data/embeddings.json') as f:
    data = json.load(f)
    print(f\"Model: {data['model']}\")
    print(f\"Verses (EN): {len(data['verses']['en'])}\")
    print(f\"Verses (HI): {len(data['verses']['hi'])}\")
"
```

### Preview on Different Devices

```bash
# Find your local IP
ifconfig | grep "inet "  # macOS/Linux
ipconfig  # Windows

# Access from mobile device
# http://YOUR_LOCAL_IP:4000/bhagavad-gita
```

## Deploying

### Deploy to GitHub Pages

#### 1. Commit Your Changes

```bash
git add .
git status  # Review changes
git commit -m "Add Chapter 1 verses"
```

#### 2. Push to GitHub

```bash
git push origin main
```

#### 3. Wait for GitHub Actions

- Go to: https://github.com/sanatan-learnings/bhagavad-gita/actions
- Watch the workflow run
- Typically takes 1-2 minutes

#### 4. View Live Site

```
https://sanatan-learnings.github.io/bhagavad-gita
```

### Deploy Cloudflare Worker (Optional)

Only needed if you're setting up the spiritual guidance API:

```bash
# Install Wrangler CLI
npm install -g wrangler

# Authenticate
wrangler login

# Set OpenAI API key secret
wrangler secret put OPENAI_API_KEY

# Deploy
wrangler deploy

# Test
curl https://your-worker.workers.dev/health
```

## Troubleshooting

### Jekyll Won't Start

**Error:** `Could not find gem 'github-pages'`

**Solution:**
```bash
bundle install
# or
bundle update
```

**Error:** `Port 4000 already in use`

**Solution:**
```bash
# Kill existing process
lsof -ti:4000 | xargs kill -9

# Or use a different port
bundle exec jekyll serve --port 4001
```

### Python Issues

**Error:** `ModuleNotFoundError: No module named 'openai'`

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r scripts/requirements.txt
```

**Error:** `OPENAI_API_KEY not found`

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify content
cat .env

# Make sure it's loaded
python3 -c "
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv('OPENAI_API_KEY'))
"
```

### Embeddings Generation Fails

**Error:** `Error: Verses directory not found`

**Solution:**
```bash
# Make sure you're in the project root
pwd
# Should end with: /bhagavad-gita

# Check _verses directory exists
ls _verses/
```

**Error:** `OpenAI API rate limit exceeded`

**Solution:**
- Wait a few seconds and retry
- Use local embeddings instead: `python scripts/generate_embeddings_local.py`

### Site Looks Broken

**Check baseurl:**
- Local: `http://localhost:4000/bhagavad-gita` (with baseurl)
- Don't use: `http://localhost:4000` (without baseurl)

**Clear Jekyll cache:**
```bash
rm -rf _site .jekyll-cache
bundle exec jekyll serve
```

**Check browser console:**
- Open DevTools (F12)
- Look for JavaScript errors
- Check Network tab for failed requests

### Changes Not Appearing

**Solution:**
```bash
# Hard refresh in browser
# Mac: Cmd + Shift + R
# Windows/Linux: Ctrl + Shift + R

# Or clear Jekyll cache
rm -rf _site .jekyll-cache
bundle exec jekyll serve
```

## Development Tips

### Speed Up Development

1. **Use LiveReload:**
   ```bash
   bundle exec jekyll serve --livereload
   ```

2. **Limit builds during testing:**
   ```bash
   # Only build specific collection
   bundle exec jekyll serve --watch
   ```

3. **Exclude large files:**
   Edit `_config.yml`:
   ```yaml
   exclude:
     - data/embeddings.json  # Temporarily during dev
   ```

### Debug Layout Issues

Add to your layout file:
```html
<!-- Debug info -->
{{ page | inspect }}
```

### Check Site Performance

```bash
# Build for production
JEKYLL_ENV=production bundle exec jekyll build

# Check file sizes
du -sh _site/*
```

## Next Steps

- Read [tech-stack.md](tech-stack.md) to understand the architecture
- Check [README.md](../README.md) for contribution guidelines
- Explore `_layouts/` to understand page structure
- Review `assets/js/` for frontend functionality

## Getting Help

- [GitHub Issues](https://github.com/sanatan-learnings/bhagavad-gita/issues)
- [GitHub Discussions](https://github.com/sanatan-learnings/bhagavad-gita/discussions)
- Jekyll Docs: https://jekyllrb.com/docs/
