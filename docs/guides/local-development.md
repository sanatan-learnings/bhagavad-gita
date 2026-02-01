# Local Development Guide

Quick setup guide for running the Bhagavad Gita site locally.

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

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install verse-content-sdk (for content generation)
pip install verse-content-sdk

# Configure environment variables
cp .env.example .env
# Edit .env and add your API keys:
# - OPENAI_API_KEY (for content generation and embeddings)
# - ELEVENLABS_API_KEY (for audio pronunciation)
```

**Note:** Always activate the virtual environment before running SDK commands:
```bash
source venv/bin/activate
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
# Generate with OpenAI (recommended)
verse-embeddings --verses-dir _verses --output data/embeddings.json

# Or generate locally (free, no API key)
verse-embeddings --verses-dir _verses --output data/embeddings.json --provider huggingface
```

See [verse-content-sdk USAGE.md](https://github.com/sanatan-learnings/verse-content-sdk/blob/main/docs/USAGE.md) for full documentation.

## Development Workflow

### Adding New Verses

Use the automated generation command (recommended):

```bash
verse-generate --chapter 2 --verse 48 --all
```

This creates complete verse with text, image, and audio in one step.

See **[content-generation.md](content-generation.md)** for full workflow details.

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

**Changes not appearing:**
- Hard refresh browser: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Linux)
- Clear Jekyll cache: `rm -rf _site .jekyll-cache`
- Restart Jekyll server

**Embeddings generation fails:**
- Verify OpenAI API key in `.env`: `cat .env`
- Check API key has credits: https://platform.openai.com/account/usage
- Try local embeddings instead: `verse-embeddings --verses-dir _verses --output data/embeddings.json --provider huggingface`

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

- [tech-stack.md](../reference/tech-stack.md) - Technology architecture overview
- [README.md](../README.md) - Project overview and contribution guidelines

## Quick Reference

**Start development:**
```bash
bundle exec jekyll serve --livereload
```

**Generate new verse:**
```bash
verse-generate --chapter 2 --verse 48 --all
```

**Regenerate embeddings:**
```bash
verse-embeddings --verses-dir _verses --output data/embeddings.json
```

**Deploy to production:**
```bash
git add .
git commit -m "Add Chapter 2, Verse 48"
git push  # GitHub Actions deploys automatically
```
