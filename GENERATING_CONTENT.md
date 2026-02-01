# Generating Content for New Verses

This guide shows how to use the `verse-generate` command to create content for Bhagavad Gita verses.

## Prerequisites

1. **API Keys**: Make sure your `.env` file contains:
   ```
   OPENAI_API_KEY=your_openai_key
   ELEVENLABS_API_KEY=your_elevenlabs_key
   ```

2. **Sanskrit Text**: Have the Sanskrit verse in Devanagari script ready

## Automated Generation (Recommended)

Generate everything with one command:

```bash
verse-generate --chapter 3 --verse 5 --all \
  --sanskrit "न हि कश्चित्क्षणमपि जातु तिष्ठत्यकर्मकृत्।
कार्यते ह्यवशः कर्म सर्वः प्रकृतिजैर्गुणैः।।" \
  --chapter-name-en "Karma Yoga" \
  --chapter-name-hi "कर्म योग"
```

**Note:** If `verse-generate` is not in your PATH, use the full path:
```bash
/Users/arungupta/Library/Python/3.13/bin/verse-generate --chapter 3 --verse 5 --all ...
```

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
verse-generate --chapter 3 --verse 5 --prompt \
  --sanskrit "न हि कश्चित्क्षणमपि जातु तिष्ठत्यकर्मकृत्।
कार्यते ह्यवशः कर्म सर्वः प्रकृतिजैर्गुणैः।।"
```

### Generate Only Verse File

```bash
verse-generate --chapter 3 --verse 5 --text \
  --sanskrit "न हि कश्चित्क्षणमपि जातु तिष्ठत्यकर्मकृत्।
कार्यते ह्यवशः कर्म सर्वः प्रकृतिजैर्गुणैः।।" \
  --chapter-name-en "Karma Yoga" \
  --chapter-name-hi "कर्म योग"
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

## Chapter Names Reference

| Chapter | English Name | Hindi Name |
|---------|--------------|------------|
| 1 | Arjuna's Dilemma | अर्जुन विषाद योग |
| 2 | The Yoga of Knowledge | सांख्य योग |
| 3 | Karma Yoga | कर्म योग |
| 4 | The Yoga of Wisdom | ज्ञान योग |
| 5 | Karma Sannyasa Yoga | कर्म संन्यास योग |
| 6 | Dhyana Yoga | ध्यान योग |
| 7 | Jnana Vijnana Yoga | ज्ञान विज्ञान योग |
| 8 | Akshara Brahma Yoga | अक्षर ब्रह्म योग |
| 9 | Raja Vidya Raja Guhya Yoga | राज विद्या राज गुह्य योग |
| 10 | Vibhuti Yoga | विभूति योग |
| 11 | Vishvarupa Darshana Yoga | विश्वरूप दर्शन योग |
| 12 | Bhakti Yoga | भक्ति योग |
| 13 | Kshetra Kshetragna Vibhaga Yoga | क्षेत्र क्षेत्रज्ञ विभाग योग |
| 14 | Gunatraya Vibhaga Yoga | गुणत्रय विभाग योग |
| 15 | Purushottama Yoga | पुरुषोत्तम योग |
| 16 | Daivasura Sampad Vibhaga Yoga | दैवासुर सम्पद् विभाग योग |
| 17 | Shraddhatraya Vibhaga Yoga | श्रद्धात्रय विभाग योग |
| 18 | Moksha Sannyasa Yoga | मोक्ष संन्यास योग |

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

- **API Costs**:
  - GPT-4: ~$0.01-0.03 per verse (text + prompt generation)
  - DALL-E 3: ~$0.04 per image
  - ElevenLabs: ~200-300 characters per verse (~0.002 credits)

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
