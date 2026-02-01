# Content Sourcing Guide for Bhagavad Gita Verses

This guide helps you find authentic, reliable sources for Sanskrit text, translations, and commentary for the Bhagavad Gita.

## Recommended Primary Sources

### 1. **Gita Supersite** (Most Comprehensive)
- **URL**: https://www.gitasupersite.iitk.ac.in/
- **Maintained by**: IIT Kanpur
- **Features**:
  - Sanskrit text in Devanagari
  - IAST transliteration
  - Word-by-word meanings
  - Multiple commentaries (Shankaracharya, Ramanujacharya, etc.)
  - English translations from multiple scholars
- **Usage**: Best for complete, authentic content
- **License**: Generally public domain for classical texts

### 2. **Bhagavad Gita As It Is**
- **URL**: https://vedabase.io/en/library/bg/
- **Author**: A.C. Bhaktivedanta Swami Prabhupada
- **Features**:
  - Sanskrit with Devanagari
  - Transliteration
  - Word-for-word meanings
  - Translation
  - Detailed purports (commentary)
- **Usage**: Excellent for devotional perspective
- **License**: Check International Society for Krishna Consciousness (ISKCON) terms

### 3. **Sanskrit Documents**
- **URL**: http://sanskritdocuments.org/
- **Features**:
  - Pure Sanskrit text
  - Multiple scripts (Devanagari, IAST, etc.)
  - No translation (use for authentic Sanskrit)
- **Usage**: Best for verifying Sanskrit accuracy
- **License**: Generally public domain

### 4. **Sacred Texts**
- **URL**: https://sacred-texts.com/hin/gita/
- **Features**:
  - Multiple translations available
  - Public domain translations
  - Historical translations (Edwin Arnold, etc.)
- **Usage**: Good for English translations
- **License**: Public domain

### 5. **Bhagavad Gita Online**
- **URL**: https://www.holy-bhagavad-gita.org/
- **Features**:
  - Simple interface
  - Multiple commentaries
  - Verse-by-verse navigation
- **Usage**: Easy reference for quick lookups

## Recommended Translators

### Classical/Scholarly
1. **Swami Sivananda** - Clear, accessible
2. **Swami Gambhirananda** - Scholarly, Advaita perspective
3. **S. Radhakrishnan** - Philosophical, academic
4. **Eknath Easwaran** - Modern, practical

### Devotional
1. **Swami Prabhupada** - ISKCON/Vaishnava tradition
2. **Swami Chinmayananda** - Vedanta perspective
3. **Paramahansa Yogananda** - Kriya Yoga tradition

### Academic
1. **Barbara Stoler Miller** - Sanskrit scholar
2. **Winthrop Sargeant** - Detailed word-for-word analysis

## Content Structure Guidelines

### Minimum Required Fields

For each verse, ensure you have:

1. **Devanagari** - Sanskrit in Devanagari script
2. **Transliteration** - IAST or Harvard-Kyoto scheme
3. **Literal Translation** - Word-for-word or close translation
4. **Interpretive Meaning** - Commentary explaining deeper meaning
5. **Word Meanings** - Key Sanskrit terms with meanings

### Optional But Recommended

1. **Pronunciation Notes** - For difficult Sanskrit words
2. **Story/Context** - Background from Mahabharata
3. **Practical Application** - Modern life relevance
4. **Keywords** - For search optimization

## Workflow for Adding Verses

### Automated Workflow (Recommended)

Use the `verse-generate` command to automatically generate complete verse content using GPT-4:

```bash
# Generate everything (text, scene, image, audio) for a verse
verse-generate --chapter 3 --verse 5 --all \
  --chapter-name-en "Karma Yoga" \
  --chapter-name-hi "कर्म योग"
```

This automatically:
1. Fetches Sanskrit text from GPT-4
2. Generates transliteration (IAST)
3. Generates word-by-word meanings (English & Hindi)
4. Generates literal translation (English & Hindi)
5. Generates interpretive meaning with commentary
6. Generates story/context
7. Generates practical application
8. Creates scene description for image
9. Generates image using DALL-E 3
10. Generates audio pronunciation using ElevenLabs

**Important**: AI-generated content requires **manual review and editing** for accuracy. Use the sources below to verify.

### Manual Workflow (Traditional)

If you prefer to create content manually:

#### Step 1: Source Content
For each verse:
1. Visit Gita Supersite for verse number
2. Copy Sanskrit Devanagari text
3. Copy IAST transliteration
4. Get word meanings
5. Select translation you prefer (or combine multiple)
6. Write practical application in your own words

#### Step 2: Create Verse File
Use `verse-generate` to create the verse file with your Sanskrit text:

```bash
verse-generate --chapter 3 --verse 5 --text \
  --sanskrit "न हि कश्चित्क्षणमपि जातु तिष्ठत्यकर्मकृत्।
कार्यते ह्यवशः कर्म सर्वः प्रकृतिजैर्गुणैः।।" \
  --chapter-name-en "Karma Yoga"
```

Then edit `_verses/chapter_03_verse_05.md` to refine the AI-generated content.

#### Step 3: Verify Accuracy
- Cross-reference with 2-3 sources listed above
- Ensure Sanskrit is accurate
- Check transliteration follows IAST standard
- Verify meanings are contextually appropriate
- Refine AI-generated commentary with authentic sources

#### Step 4: Regenerate Search/Embeddings
```bash
verse-embeddings --verses-dir _verses --output data/embeddings.json
```

## Translation Permission Guidelines

### Public Domain (Safe to Use)
- Classical commentaries (Shankaracharya, etc.)
- Pre-1928 translations (Edwin Arnold, etc.)
- Government/educational institution resources (IIT Kanpur)

### Requires Permission/Attribution
- Modern translations (post-1928)
- Published books (Easwaran, Prabhupada, etc.)
- Commercial websites

### Best Practice
1. Use multiple public domain sources
2. Synthesize into your own words
3. Provide attribution when using specific translations
4. For Hindi translations, create your own or use public domain sources

## Quality Checklist

Before committing a verse, verify:

- [ ] Sanskrit text is accurate (checked against 2+ sources)
- [ ] Transliteration follows IAST standard
- [ ] Word meanings are contextually correct
- [ ] Translation flows naturally in English/Hindi
- [ ] Commentary adds spiritual insight
- [ ] Practical application is relevant to modern readers
- [ ] No copyright violations
- [ ] Consistent formatting with existing verses

## Batch Processing Tips

### For Faster Completion

1. **Focus on Sanskrit first**: Get all Sanskrit text and transliteration done
2. **Batch translations**: Do all English translations, then Hindi
3. **Word meanings**: Start with common words that repeat
4. **Commentary**: Can be briefer initially, expand later
5. **Practical applications**: Can add these last

### Using AI-Generated Content

The `verse-generate` command uses GPT-4 to generate verse content automatically.

**Benefits:**
- ✅ Fast: Generates complete verse in minutes
- ✅ Comprehensive: Includes all required fields
- ✅ Bilingual: Generates English and Hindi content
- ✅ Consistent: Follows standard format

**Important Considerations:**
- ⚠️ **Always verify**: AI may make errors in Sanskrit or interpretation
- ⚠️ **Cross-reference**: Check against authentic sources (Gita Supersite, etc.)
- ⚠️ **Edit for accuracy**: Refine translations and commentary
- ⚠️ **Spiritual authenticity**: Ensure interpretations align with traditional teachings
- ✅ **Use as starting point**: AI provides solid foundation for manual refinement

## Common Pitfalls to Avoid

1. **Mixing transliteration schemes** (stick to IAST)
2. **Incomplete word meanings** (add both languages)
3. **Copy-paste errors** in Sanskrit (verify diacritics)
4. **Inconsistent formatting** (follow template exactly)
5. **Copyright violations** (synthesize from multiple sources)

## Example Workflow

### Automated Workflow
**Time per verse**: ~5-10 minutes (generation + review)

1. Run verse-generate command (2 min)
   - Command generates all content via GPT-4
   - Creates verse file, scene description, image, audio
2. Review AI-generated content (3-5 min)
   - Open verse file in editor
   - Check Sanskrit text accuracy
   - Verify transliteration
   - Review translations and commentary
3. Refine content (3-5 min)
   - Cross-reference with Gita Supersite
   - Edit interpretations if needed
   - Adjust practical applications
4. Commit and push (1 min)

**For 46 verses**: ~4-8 hours total work (vs. 15-23 hours manual)

### Manual Workflow
**Time per verse**: ~20-30 minutes for quality content

1. Open Gita Supersite (5 min)
   - Copy Sanskrit, transliteration
   - Copy word meanings
2. Choose translation (5 min)
   - Read 2-3 translations
   - Select best or synthesize
3. Write commentary (10 min)
   - Combine insights from multiple sources
   - Add your interpretation
4. Practical application (5 min)
   - Think of modern relevance
   - Write brief guidance
5. Hindi translation (5 min)
   - Use Hindi source or translate

**For 46 verses**: ~15-23 hours total work

## Resources Summary

| Source | Best For | URL |
|--------|----------|-----|
| Gita Supersite | Complete content | gitasupersite.iitk.ac.in |
| Vedabase | Devotional translation | vedabase.io/en/library/bg/ |
| Sanskrit Documents | Authentic Sanskrit | sanskritdocuments.org |
| Sacred Texts | Public domain translations | sacred-texts.com/hin/gita/ |
| Holy Bhagavad Gita | Quick reference | holy-bhagavad-gita.org |

## Getting Help

If you have questions about:
- **Sanskrit accuracy**: Post in r/sanskrit on Reddit
- **Translation choices**: Consult multiple commentaries
- **Technical issues**: GitHub issues in this repo
- **Content decisions**: Reference existing verses as examples

## License Considerations

This project (code/structure) is MIT licensed. However:
- Sanskrit text is public domain
- Your original commentary/translations are yours
- Third-party translations need proper licensing
- Always attribute sources in commit messages

---

**Next Steps**:
1. See [GENERATING_CONTENT.md](../GENERATING_CONTENT.md) for detailed instructions
2. Use `verse-generate` command to create complete verse content
3. Review and refine AI-generated content using sources above
4. Regenerate embeddings: `verse-embeddings --verses-dir _verses --output data/embeddings.json`

For complete documentation, see: https://github.com/sanatan-learnings/verse-content-sdk
