# Generating Content for New Verses

This guide shows how to use the `verse-generate` command to create content for Bhagavad Gita verses.

## Prerequisites

**API Keys**: Make sure your `.env` file contains:
```
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

## Automated Generation (Recommended)

Generate everything with one command:

```bash
verse-generate --chapter 3 --verse 5 --all
```

This automatically:
- Fetches Sanskrit text from GPT-4
- Fetches chapter names from GPT-4
- Generates all content (text, scene description, image, audio)

## What Gets Generated

Running the command above will:

1. **Generate Verse File** (`_verses/chapter_03_verse_05.md`)
   - Uses GPT-4 to analyze the Sanskrit verse
   - Creates transliteration, word meanings, translations
   - Generates interpretive meaning, story/context, practical application
   - Produces content in English and Hindi
   - ⚠️ Requires manual review and formatting

2. **Generate Scene Description** (`docs/image-prompts.md`)
   - Uses GPT-4 to create a vivid 3-5 sentence description
   - Describes visual elements for DALL-E 3
   - Appends to the existing file

3. **Generate Image** (`images/modern-minimalist/chapter-03-verse-05.png`)
   - Uses DALL-E 3 to create artwork
   - Based on the generated scene description
   - Portrait format (1024x1792)

4. **Generate Audio** (`audio/chapter_03_verse_05_*.mp3`)
   - Uses ElevenLabs for Sanskrit pronunciation
   - Creates two versions: full speed and slow speed
   - Based on the Devanagari text

## Step-by-Step Options

### Generate Only Scene Description

```bash
verse-generate --chapter 3 --verse 5 --prompt
```

### Generate Only Verse File

```bash
verse-generate --chapter 3 --verse 5 --text
```

### Generate Only Image (requires existing scene description)

```bash
verse-generate --chapter 3 --verse 5 --image
```

### Generate Only Audio (requires existing verse file)

```bash
verse-generate --chapter 3 --verse 5 --audio
```

### Generate Image and Audio

```bash
verse-generate --chapter 3 --verse 5 --image --audio
```

## After Generation

1. **Review Verse File**: Check `_verses/chapter_XX_verse_YY.md`
   - Verify translations and interpretations
   - Format the AI-generated content to match existing verse structure
   - See `_verses/chapter_02_verse_47.md` as a reference

2. **Review Scene Description**: Check `docs/image-prompts.md`
   - Verify the scene description captures the verse essence
   - Edit if needed before regenerating image

3. **Review Generated Files**:
   ```bash
   ls -lh images/modern-minimalist/chapter-03-verse-05.png
   ls -lh audio/chapter_03_verse_05_*.mp3
   ls -lh _verses/chapter_03_verse_05.md
   ```

4. **Test Locally**:
   ```bash
   bundle exec jekyll serve
   # Navigate to http://localhost:4000/bhagavad-gita/verses/chapter-03-verse-05/
   ```

5. **Commit and Push**:
   ```bash
   git add _verses/chapter_03_verse_05.md \
           docs/image-prompts.md \
           images/modern-minimalist/chapter-03-verse-05.png \
           audio/chapter_03_verse_05_*.mp3
   git commit -m "Add Chapter 3, Verse 5 with multimedia content"
   git push
   ```

## Tips

- **Review AI Content**: Always review and edit AI-generated translations and interpretations for accuracy

- **Scene Descriptions**: More specific scene descriptions lead to better images

- **Regeneration**: Use individual flags to regenerate only specific components

## Troubleshooting

**"Error: OPENAI_API_KEY not set"**
- Check `.env` file exists and contains valid API key

**"Error: Scene description not found"**
- Generate scene description first with `--prompt` flag
- Or add it manually to `docs/image-prompts.md`

**"Error: Verse file not found"**
- Generate verse file first with `--text` flag
- Or create it manually in `_verses/` directory

## Full Documentation

For complete SDK documentation, see:
- [verse-content-sdk README](https://github.com/sanatan-learnings/verse-content-sdk)
- [Content Generation Guide](https://github.com/sanatan-learnings/verse-content-sdk/blob/main/docs/content-generation-guide.md)
