# Image Generation Guide for Bhagavad Gita

This guide explains how to generate AI-powered images for Bhagavad Gita verses using DALL-E 3.

## Overview

The image generation system:
- Uses OpenAI's DALL-E 3 API to generate images
- Combines scene descriptions with visual style themes
- Supports **chapter-based format** (Bhagavad Gita: Chapter X, Verse Y)
- Also works with **simple verse format** (Hanuman Chalisa: Verse X)
- Generates high-quality portrait images (1024x1792, cropped to 1024x1536)

## Setup

### 1. Install the SDK

The verse-content-sdk is already installed from the local directory:

```bash
# Already done:
pip install -e ~/workspaces/verse-content-sdk/
```

### 2. Configure API Key

Make sure your `.env` file contains your OpenAI API key:

```bash
OPENAI_API_KEY=your-key-here
```

✅ **Status**: API key is already configured in your `.env` file

### 3. Project Structure

```
bhagavad-gita/
├── docs/
│   ├── image-prompts.md        # Scene descriptions for each verse
│   └── themes/
│       └── modern-minimalist.yml  # Theme configuration
├── images/                     # Generated images go here
│   └── modern-minimalist/      # One folder per theme
│       ├── chapter-01-verse-01.png
│       ├── chapter-01-verse-02.png
│       └── ...
└── _verses/                    # Your verse content files
```

✅ **Status**: Structure is already set up

## How to Generate Images

### Quick Test (Free - No API Calls)

Test that everything is configured correctly:

```bash
python3 test-parse-prompts.py
```

This verifies:
- ✅ The docs/image-prompts.md file is readable
- ✅ Scene descriptions are correctly formatted
- ✅ Filenames will be generated correctly (chapter-XX-verse-YY.png)

### Generate a Single Image

To generate just the first verse image (costs ~$0.04):

```bash
verse-images --theme-name modern-minimalist
```

This will generate `images/modern-minimalist/chapter-01-verse-01.png`

### Generate Multiple Images

To generate all verses with scene descriptions:

```bash
verse-images --theme-name modern-minimalist
```

**Important**:
- Only verses with scene descriptions in `docs/image-prompts.md` will be generated
- The script skips already-generated images (so you can resume if interrupted)
- Each image costs approximately $0.04 (standard quality) or $0.08 (HD quality)

### Resume from a Specific Verse

If generation is interrupted, resume from where you left off:

```bash
verse-images --theme-name modern-minimalist --start-from chapter-01-verse-05.png
```

## Adding Scene Descriptions

### For Bhagavad Gita (Chapter-based)

Edit `docs/image-prompts.md` and add verses using this format:

```markdown
### Chapter 1, Verse 1

**Scene Description**:
A vast battlefield at Kurukshetra stretches endlessly under a dramatic sky...
[3-5 sentences describing the visual scene]

---

### Chapter 1, Verse 2

**Scene Description**:
[Your scene description here]

---
```

### Important Notes

1. **Format**: Must be exactly `### Chapter X, Verse Y` (with capital C, comma, and space)
2. **Scene Description**: Must start with `**Scene Description**:` on its own line
3. **Separator**: Use `---` to separate verses
4. **Length**: Keep descriptions to 3-5 sentences for best results
5. **Visual Focus**: Describe concrete visual elements (not abstract concepts)

### What Makes a Good Scene Description?

✅ **Good**: "A vast battlefield at Kurukshetra stretches endlessly under a dramatic sky. Two massive armies face each other with thousands of warriors, chariots, and elephants. In the foreground, blind King Dhritarashtra sits on his throne..."

❌ **Bad**: "This verse represents the beginning of the spiritual journey and the conflict between good and evil."

**Tips**:
- Include setting, characters, poses, expressions
- Specify lighting (golden hour, divine rays, ethereal glow)
- Mention colors and mood
- Translate abstract spiritual concepts into visual metaphors
- Think like a movie director describing a scene

## Creating Custom Themes

### 1. Create a Theme Configuration

Create `docs/themes/your-theme-name.yml`:

```yaml
theme:
  name: "Your Theme Name"
  description: "Description of the visual style"

  generation:
    style_modifier: |
      Style: Your detailed style description here.
      Explain the visual aesthetic, color palette, artistic approach.
      This text gets appended to every scene description.

    dalle_params:
      size: "1024x1792"      # Portrait (recommended)
      quality: "standard"    # standard or hd (hd costs 2x)
      style: "natural"       # natural or vivid

  folder: "your-theme-name"
  default: false
```

### 2. Generate with Your Theme

```bash
verse-images --theme-name your-theme-name
```

### 3. Override Style on Command Line

```bash
verse-images --theme-name your-theme-name \
  --style "watercolor painting style with soft colors"
```

## Cost Estimation

| Quality | Per Image | 10 Images | 50 Images | 100 Images |
|---------|-----------|-----------|-----------|------------|
| Standard | $0.04 | $0.40 | $2.00 | $4.00 |
| HD | $0.08 | $0.80 | $4.00 | $8.00 |

**Bhagavad Gita**: 701 total verses across 18 chapters
- Standard quality: 701 × $0.04 = **$28.04**
- HD quality: 701 × $0.08 = **$56.08**

**Tip**: Start with standard quality, test a few verses, then decide if HD is worth the 2x cost.

## Example: Generate Chapter 1, Verse 1

1. **Verify the scene description**:
   ```bash
   python3 test-parse-prompts.py
   ```

2. **Generate the image**:
   ```bash
   verse-images --theme-name modern-minimalist
   ```

3. **Check the result**:
   ```bash
   open images/modern-minimalist/chapter-01-verse-01.png
   ```

4. **If satisfied, continue with more verses** by adding more scene descriptions to `docs/image-prompts.md`

## Current Status

✅ SDK installed and working
✅ API key configured
✅ Project structure created
✅ Example theme created (modern-minimalist)
✅ Sample scene description added (Chapter 1, Verse 1)
✅ Parsing verified (3 verses detected)

**Next Step**: Add more scene descriptions to `docs/image-prompts.md` and run generation!

## Compatibility with Hanuman Chalisa

The same SDK works for both projects:

**Bhagavad Gita format** (chapters):
```markdown
### Chapter 1, Verse 1
**Scene Description**: ...
```
→ Generates: `chapter-01-verse-01.png`

**Hanuman Chalisa format** (no chapters):
```markdown
### Verse 1:
**Scene Description**: ...
```
→ Generates: `verse-01.png`

The SDK automatically detects which format you're using and adjusts accordingly.

## Troubleshooting

### Error: "Prompts file not found"
- Make sure you're running the command from the project root directory
- Verify `docs/image-prompts.md` exists

### Error: "OpenAI API key not found"
- Check that `.env` file contains `OPENAI_API_KEY=your-key`
- Make sure the .env file is in the project root

### Images look wrong
- Review your scene descriptions - be more specific about visual details
- Try adjusting the theme's `style_modifier` in the YAML file
- Experiment with `--style` parameter to override the theme

### Rate limit errors
- DALL-E 3 has rate limits (typically 5-7 requests/minute)
- The script automatically retries with exponential backoff
- If you hit rate limits, just wait a few minutes and resume

## Advanced Options

### Change Image Size

```bash
verse-images --theme-name modern-minimalist --size 1024x1024  # Square
verse-images --theme-name modern-minimalist --size 1792x1024  # Landscape
```

### Use HD Quality

```bash
verse-images --theme-name modern-minimalist --quality hd
```

### Use Vivid Style

```bash
verse-images --theme-name modern-minimalist --style-type vivid
```

## Questions?

- Check the SDK documentation: `~/workspaces/verse-content-sdk/README.md`
- Review example themes in Hanuman Chalisa project
- Open an issue on the verse-content-sdk repository
