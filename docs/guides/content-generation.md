# Generating Content for New Verses

This guide shows how to use the `verse-generate` command to create content for Bhagavad Gita verses.

## Prerequisites

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **API Keys**: Make sure your `.env` file contains:
   ```
   OPENAI_API_KEY=your_openai_key
   ELEVENLABS_API_KEY=your_elevenlabs_key
   ```

## Automated Generation (Recommended)

Generate everything with one command:

```bash
verse-generate --collection bhagavad-gita --verse 5 --all
```

This automatically:
- Generates image from scene description (DALL-E 3)
- Generates audio pronunciation (ElevenLabs - full + slow speeds)
- Updates embeddings for search

**Note:** Verse position 5 = Chapter 1, Verse 5 (sequential numbering 1-700)

## What Gets Generated

Running the command above will:

1. **Generate Image** (`images/bhagavad-gita/modern-minimalist/chapter-01-shloka-05.png`)
   - Uses DALL-E 3 to create artwork
   - Based on scene description from `data/scenes/bhagavad-gita.yml`
   - Portrait format (1024x1792)
   - Default theme: modern-minimalist (use `--theme` to change)

2. **Generate Audio** (`audio/bhagavad-gita/chapter-01-shloka-05-full.mp3` and `-slow.mp3`)
   - Uses ElevenLabs for Sanskrit pronunciation
   - Creates two versions: full speed and slow speed
   - Based on Devanagari text from `data/verses/bhagavad-gita.yaml`

3. **Update Embeddings** (`data/embeddings.json`)
   - Updates vector embeddings for semantic search
   - Automatically included (use `--no-update-embeddings` to skip)

**Note:** Shloka markdown files (`_verses/bhagavad-gita/chapter-XX-shloka-YY.md`) must be created manually or regenerated with `--regenerate-content` flag.

## Step-by-Step Options

### Generate Only Image (requires scene description)

```bash
verse-generate --collection bhagavad-gita --verse 5 --image
```

### Generate Only Audio (requires verse file with Devanagari text)

```bash
verse-generate --collection bhagavad-gita --verse 5 --audio
```

### Generate Image and Audio (default behavior)

```bash
verse-generate --collection bhagavad-gita --verse 5 --all
# or simply:
verse-generate --collection bhagavad-gita --verse 5
```

### Regenerate Verse Content

```bash
verse-generate --collection bhagavad-gita --verse 5 --regenerate-content
```

Creates/updates verse markdown file with AI-generated translations and commentary.

## After Generation

1. **Review Shloka File**: Check `_verses/bhagavad-gita/chapter-01-shloka-05.md`
   - Verify translations and interpretations
   - Ensure proper frontmatter and formatting
   - See `_verses/bhagavad-gita/chapter-02-shloka-47.md` as a reference

2. **Review Scene Description**: Check `data/scenes/bhagavad-gita.yml`
   - Verify the scene description captures the shloka essence
   - Edit if needed before regenerating image

3. **Review Generated Files**:
   ```bash
   ls -lh images/bhagavad-gita/modern-minimalist/chapter-01-shloka-05.png
   ls -lh audio/bhagavad-gita/chapter-01-shloka-05-*.mp3
   ls -lh _verses/bhagavad-gita/chapter-01-shloka-05.md
   ```

4. **Test Locally**:
   ```bash
   bundle exec jekyll serve
   # Navigate to http://localhost:4000/bhagavad-gita/
   ```

5. **Commit and Push**:
   ```bash
   git add _verses/bhagavad-gita/chapter-01-shloka-05.md \
           data/scenes/bhagavad-gita.yml \
           images/bhagavad-gita/modern-minimalist/chapter-01-shloka-05.png \
           audio/bhagavad-gita/chapter-01-shloka-05-*.mp3
   git commit -m "Add Chapter 1, Shloka 5 with multimedia content"
   git push
   ```

## Tips

- **Review AI Content**: Always review and edit AI-generated translations and interpretations for accuracy

- **Scene Descriptions**: More specific scene descriptions lead to better images

- **Regeneration**: Use individual flags to regenerate only specific components

## Troubleshooting

**"Error: OPENAI_API_KEY not set"**
- Check `.env` file exists and contains valid API key

**"Scene description not found"** (warning only)
- Add scene to `data/scenes/bhagavad-gita.yml`
- Or use `--auto-generate-scene` to generate with AI

**"Shloka not found in data file"**
- Add shloka to `data/verses/bhagavad-gita.yaml` with Devanagari text
- Or use `--regenerate-content` to generate shloka file

## Full Documentation

For complete SDK documentation, see:
- [sanatan-verse-sdk README](https://github.com/sanatan-learnings/sanatan-verse-sdk)
- Run `verse-help` for comprehensive CLI documentation
- Run `verse-generate --help` for detailed command options
