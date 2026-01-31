# Local Development Setup Guide

This documentation provides a comprehensive walkthrough for establishing a development environment for the Bhagavad Gita project on macOS, Linux, and Windows.

## Core Purpose

Local development enables developers to see changes immediately without waiting for GitHub Actions, catch build errors before pushing, test the RAG system with actual embeddings, and validate verse formatting across languages.

## Prerequisites Installation

### macOS Setup

Ruby version management via rbenv provides the cleanest installation:

```bash
# Install rbenv and ruby-build
brew install rbenv ruby-build

# Initialize rbenv in your shell
echo 'eval "$(rbenv init -)"' >> ~/.zshrc
source ~/.zshrc

# Install Ruby 3.3.0
rbenv install 3.3.0
rbenv global 3.3.0

# Verify installation
ruby --version
```

Install Bundler and Python:
```bash
gem install bundler
brew install python3
```

### Linux (Ubuntu/Debian)

```bash
# Install Ruby and build tools
sudo apt-get update
sudo apt-get install ruby-full build-essential zlib1g-dev python3 python3-pip python3-venv

# Install Bundler
gem install bundler
```

### Windows

Download and install:
- Ruby 3.x from [RubyInstaller](https://rubyinstaller.org/) (with DevKit)
- Python 3.8+ from [Python.org](https://www.python.org/downloads/)

## Project Setup

Clone and install dependencies:

```bash
git clone https://github.com/sanatan-learnings/bhagavad-gita.git
cd bhagavad-gita

# Install Ruby dependencies
bundle install

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r scripts/requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Running the Development Server

The primary command launches a local Jekyll server with automatic file-watching:

```bash
bundle exec jekyll serve
```

Access the site at `http://localhost:4000/bhagavad-gita/`. The server automatically rebuilds when you edit files.

**Useful variations:**
```bash
# Live reload (auto-refresh browser)
bundle exec jekyll serve --livereload

# Different port
bundle exec jekyll serve --port 4001

# Verbose output for debugging
bundle exec jekyll serve --verbose
```

## Generating Embeddings

After adding or modifying verses, regenerate embeddings for the RAG system:

```bash
# Activate Python environment
source venv/bin/activate

# Generate with OpenAI (recommended)
python scripts/generate_embeddings_openai.py

# Or generate locally (free, no API key)
python scripts/generate_embeddings_local.py
```

The script reads all verse files from `_verses/`, generates embeddings, and outputs to `data/embeddings.json`.

## Development Workflow

### Adding New Verses

1. Create verse file in `_verses/` following naming convention: `chapter_XX_verse_YY.md`
2. Use existing verse files as templates for YAML structure
3. Include all required fields: devanagari, transliteration, translations, commentary
4. Test locally: `bundle exec jekyll serve`
5. Regenerate embeddings if needed
6. Commit and push changes

### Testing the RAG System

1. Ensure embeddings are generated: `ls -lh data/embeddings.json`
2. Start Jekyll server: `bundle exec jekyll serve`
3. Navigate to `/bhagavad-gita/guidance.html`
4. Enter your OpenAI API key (stored in browser localStorage)
5. Ask spiritual guidance questions
6. Verify relevant verses are retrieved
7. Check console for debugging info (F12 → Console tab)

## Troubleshooting Coverage

**Port already in use:**
```bash
# Find and kill process on port 4000
lsof -ti:4000 | xargs kill -9

# Or use different port
bundle exec jekyll serve --port 4001
```

**Bundle install fails:**
```bash
bundle update
# On Apple Silicon Macs:
bundle config set --local force_ruby_platform true
bundle install
```

**Python module errors:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate
pip install -r scripts/requirements.txt
```

**Changes not appearing:**
- Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Linux)
- Clear Jekyll cache: `rm -rf _site .jekyll-cache`
- Restart Jekyll server

**Embeddings generation fails:**
- Verify OpenAI API key in `.env`: `cat .env`
- Check API key has credits: https://platform.openai.com/account/usage
- Try local embeddings instead: `python scripts/generate_embeddings_local.py`

**YAML syntax errors:**
Validate verse YAML:
```bash
python3 -c "
import yaml
with open('_verses/chapter_01_verse_01.md') as f:
    content = f.read()
    yaml_content = content.split('---')[1]
    yaml.safe_load(yaml_content)
    print('Valid YAML')
"
```

## Validation Features

GitHub Actions automatically validates builds on push. Test locally before pushing:

```bash
# Build without serving
bundle exec jekyll build

# Check exit code
echo $?  # Should be 0 for success
```

## Workflow Recommendations

Development tasks include:
1. Edit verse files or site templates
2. Monitor terminal output for build errors
3. Refresh browser to see changes
4. Test navigation between verses
5. Verify language switching works
6. Test spiritual guidance with sample queries
7. Commit validated changes

## Related Documentation

- [tech-stack.md](tech-stack.md) - Technology architecture overview
- [README.md](../README.md) - Project overview and contribution guidelines

## Quick Reference

**Start development:**
```bash
bundle exec jekyll serve --livereload
```

**Generate embeddings:**
```bash
source venv/bin/activate && python scripts/generate_embeddings_openai.py
```

**Add new verse:**
```bash
touch _verses/chapter_02_verse_48.md
# Edit file with verse content
bundle exec jekyll serve
```

**Deploy to production:**
```bash
git add .
git commit -m "Add Chapter 2, Verse 48"
git push  # GitHub Actions deploys automatically
```
