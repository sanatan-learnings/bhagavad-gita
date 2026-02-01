# Content Verification Guide

This guide helps you verify AI-generated Bhagavad Gita verse content against authentic sources.

## Why Verify AI Content?

While `verse-generate` automates content creation using GPT-4, **human verification is essential** for:
- Ensuring Sanskrit text accuracy
- Validating translations against traditional interpretations
- Maintaining consistency with authoritative sources
- Respecting spiritual and scholarly standards

## Verification Sources

### 1. **Gita Supersite** (Primary Reference)
- **URL**: https://www.gitasupersite.iitk.ac.in/
- **Maintained by**: IIT Kanpur
- **Features**: Sanskrit, IAST transliteration, word-by-word meanings, multiple commentaries
- **Usage**: Best for complete content verification
- **License**: Public domain for classical texts

### 2. **Bhagavad Gita As It Is**
- **URL**: https://vedabase.io/en/library/bg/
- **Author**: A.C. Bhaktivedanta Swami Prabhupada
- **Features**: Sanskrit, transliteration, word meanings, detailed purports
- **Usage**: Excellent for devotional perspective

### 3. **Sanskrit Documents**
- **URL**: http://sanskritdocuments.org/
- **Usage**: Best for verifying Sanskrit text accuracy
- **License**: Public domain

### 4. **Sacred Texts**
- **URL**: https://sacred-texts.com/hin/gita/
- **Features**: Multiple public domain translations
- **Usage**: Good for English translations

### 5. **Bhagavad Gita Online**
- **URL**: https://www.holy-bhagavad-gita.org/
- **Usage**: Easy reference for quick lookups

## Verification Checklist

After generating content with `verse-generate --all`, verify each verse:

- [ ] **Sanskrit text** - Cross-reference with Gita Supersite or Sanskrit Documents
- [ ] **Transliteration** - Verify follows IAST standard
- [ ] **Word meanings** - Check against 2-3 trusted sources
- [ ] **Translations** - Compare with multiple scholarly translations
- [ ] **Commentary** - Ensure aligns with traditional teachings
- [ ] **Practical applications** - Verify appropriateness and relevance

## Verification Workflow

1. **Generate content:**
   ```bash
   verse-generate --chapter 3 --verse 5 --all
   ```

2. **Open generated verse file:**
   ```bash
   open _verses/chapter_03_verse_05.md
   ```

3. **Verify each section:**
   - Compare Sanskrit with Gita Supersite
   - Check translations against 2-3 authoritative sources
   - Validate commentary aligns with traditional interpretations

4. **Edit for accuracy:**
   - Fix any errors in Sanskrit text
   - Adjust translations if needed
   - Refine commentary for clarity

5. **Commit changes:**
   ```bash
   git add _verses/chapter_03_verse_05.md
   git commit -m "Verify Chapter 3, Verse 5 content"
   ```

## Recommended Translators

Use these translators as reference points for verification:

### Classical/Scholarly
- **Swami Sivananda** - Clear, accessible
- **Swami Gambhirananda** - Scholarly, Advaita perspective
- **S. Radhakrishnan** - Philosophical, academic
- **Eknath Easwaran** - Modern, practical

### Devotional
- **Swami Prabhupada** - ISKCON/Vaishnava tradition
- **Swami Chinmayananda** - Vedanta perspective
- **Paramahansa Yogananda** - Kriya Yoga tradition

### Academic
- **Barbara Stoler Miller** - Sanskrit scholar
- **Winthrop Sargeant** - Detailed word-for-word analysis

## Quality Standards

### Minimum Required Fields
1. **Devanagari** - Verse text in Devanagari script
2. **Transliteration** - IAST standard
3. **Word Meanings** - Key terms (English & Hindi)
4. **Literal Translation** - English & Hindi
5. **Interpretive Meaning** - Commentary with spiritual context

### Optional But Recommended
- **Pronunciation Notes** - For difficult words
- **Story/Context** - Background from Mahabharata
- **Practical Application** - Modern life relevance
- **Keywords** - For search optimization

## Common Issues to Check

- ❌ **Incorrect Sanskrit** - Verify diacritics and spelling
- ❌ **Wrong transliteration** - Stick to IAST standard
- ❌ **Incomplete translations** - Ensure both English and Hindi
- ❌ **Non-traditional commentary** - Compare with authoritative sources
- ❌ **Inconsistent formatting** - Follow existing verse structure
- ❌ **Copyright concerns** - Ensure synthesized from multiple sources

## Translation Permissions

### Public Domain (Safe to Use)
- Classical commentaries (Shankaracharya, etc.)
- Pre-1928 translations (Edwin Arnold, etc.)
- Government/educational resources (IIT Kanpur)

### Requires Permission/Attribution
- Modern translations (post-1928)
- Published books (Easwaran, Prabhupada)
- Commercial websites

### Best Practice
1. Use AI-generated content as starting point
2. Verify against multiple public domain sources
3. Synthesize into your own words
4. Provide attribution when using specific translations
5. Document sources in commit messages

## Resources Summary

| Source | Best For | URL |
|--------|----------|-----|
| Gita Supersite | Complete verification | gitasupersite.iitk.ac.in |
| Vedabase | Devotional translations | vedabase.io/en/library/bg/ |
| Sanskrit Documents | Sanskrit accuracy | sanskritdocuments.org |
| Sacred Texts | Public domain translations | sacred-texts.com/hin/gita/ |
| Holy Bhagavad Gita | Quick reference | holy-bhagavad-gita.org |

## Getting Help

- **Sanskrit accuracy**: Post in r/sanskrit on Reddit
- **Translation choices**: Consult multiple commentaries
- **Technical issues**: GitHub issues
- **Content decisions**: Reference existing verses as examples

## License Considerations

- **Sanskrit text**: Public domain
- **Your original commentary/translations**: Your copyright
- **Third-party translations**: Need proper licensing
- **Always attribute sources** in commit messages

---

**See Also:**
- [content-generation.md](content-generation.md) - How to generate verses with AI
- [Gita Supersite](https://www.gitasupersite.iitk.ac.in/) - Primary verification source
