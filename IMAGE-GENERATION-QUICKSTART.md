# Image Generation Quick Start

## Setup Complete! ✅

Your Bhagavad Gita project is now ready to generate AI-powered verse images using DALL-E 3.

## What's Been Set Up

1. ✅ **SDK Installed**: verse-content-sdk from local directory
2. ✅ **API Key Configured**: OpenAI API key loaded from .env
3. ✅ **Project Structure**: docs/, themes/, and image directories created
4. ✅ **Example Theme**: modern-minimalist theme configured
5. ✅ **Sample Verse**: Chapter 1, Verse 1 scene description added
6. ✅ **Chapter Support**: SDK modified to support chapter-based verses

## Quick Test (Free - No API Calls)

```bash
python3 test-parse-prompts.py
```

Expected output:
```
✓ Successfully parsed 3 verses
Found the following verses:
  chapter-01-verse-01.png
  chapter-01-verse-02.png  (placeholder)
  chapter-01-verse-03.png  (placeholder)
```

## Generate Your First Image

**Cost**: ~$0.04 per image (standard quality)

```bash
# From project root directory:
/Users/arungupta/Library/Python/3.13/bin/verse-images --theme-name modern-minimalist
```

Or use the test script:
```bash
bash test-image-generation.sh
```

This will generate: `images/modern-minimalist/chapter-01-verse-01.png`

## Next Steps

1. **View the generated image**:
   ```bash
   open images/modern-minimalist/chapter-01-verse-01.png
   ```

2. **Add more scene descriptions** to `docs/image-prompts.md`:
   - Copy the format from Chapter 1, Verse 1
   - Write detailed visual descriptions (3-5 sentences)
   - Focus on concrete visual elements

3. **Generate more images**:
   ```bash
   verse-images --theme-name modern-minimalist
   ```
   (Only generates images for verses with scene descriptions)

## File Locations

- **Scene descriptions**: `docs/image-prompts.md`
- **Theme config**: `docs/themes/modern-minimalist.yml`
- **Generated images**: `images/modern-minimalist/`
- **Full guide**: `docs/image-generation-guide.md`

## Important Notes

- Images are **chapter-based**: `chapter-01-verse-01.png`
- Script **skips existing images** (safe to re-run)
- Use `--start-from` to resume if interrupted
- Standard quality ($0.04/image) vs HD ($0.08/image)

## Chapter Support

The SDK now supports **both formats**:

**Bhagavad Gita** (with chapters):
```markdown
### Chapter 1, Verse 1
**Scene Description**: ...
```
→ `chapter-01-verse-01.png`

**Hanuman Chalisa** (no chapters):
```markdown
### Verse 1:
**Scene Description**: ...
```
→ `verse-01.png`

## Example Scene Description

```markdown
### Chapter 1, Verse 1

**Scene Description**:
A vast battlefield at Kurukshetra stretches endlessly under a dramatic sky.
Two massive armies face each other - the Kauravas on one side and the
Pandavas on the other, with thousands of warriors, chariots, elephants, and
flags visible in organized formations. In the foreground, blind King
Dhritarashtra sits on his throne in his palace chamber, his face turned toward
his minister Sanjaya who stands beside him with eyes closed in divine
concentration. Sanjaya's posture suggests he is receiving visions from afar.
The scene should convey anticipation, the calm before the storm, and the weight
of destiny. The lighting is dramatic, with golden-hour sunlight casting long
shadows across the battlefield visible through a mystical window or divine
vision. The overall mood is solemn, epic, and spiritually charged, representing
the moment when the greatest spiritual dialogue in history is about to begin.

---
```

## Cost for Full Bhagavad Gita

- **Chapter 1**: 47 verses × $0.04 = $1.88
- **All 18 chapters**: 701 verses × $0.04 = $28.04 (standard)
- **HD quality**: 701 verses × $0.08 = $56.08

**Recommendation**: Start with Chapter 1 in standard quality, review results, then decide on HD.

## Troubleshooting

**"Prompts file not found"**
→ Run commands from project root directory

**"API key not found"**
→ Check `.env` file contains `OPENAI_API_KEY=...`

**Images look wrong**
→ Make scene descriptions more specific and visual

## Ready to Generate!

```bash
# Test (free):
python3 test-parse-prompts.py

# Generate first image (~$0.04):
verse-images --theme-name modern-minimalist
```

Read the full guide at: **docs/image-generation-guide.md**
