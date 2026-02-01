# Content Sourcing Guide

This guide helps you find authentic sources for verifying and sourcing Bhagavad Gita verse content.

## Recommended Primary Sources

### 1. **Gita Supersite** (Most Comprehensive)
- **URL**: https://www.gitasupersite.iitk.ac.in/
- **Maintained by**: IIT Kanpur
- **Features**: Sanskrit, IAST transliteration, word-by-word meanings, multiple commentaries
- **Usage**: Best for complete, authentic content verification
- **License**: Public domain for classical texts

### 2. **Bhagavad Gita As It Is**
- **URL**: https://vedabase.io/en/library/bg/
- **Author**: A.C. Bhaktivedanta Swami Prabhupada
- **Features**: Sanskrit, transliteration, word meanings, detailed purports
- **Usage**: Excellent for devotional perspective
- **License**: Check ISKCON terms

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

## Recommended Translators

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

## Content Generation Workflow

The `verse-generate` command creates complete verse content automatically using GPT-4.

For complete generation instructions, see **[content-generation.md](content-generation.md)**.

## Verifying AI-Generated Content

AI-generated content requires **human verification** for accuracy:

### Verification Checklist

- [ ] **Sanskrit text** - Cross-reference with Gita Supersite or Sanskrit Documents
- [ ] **Transliteration** - Verify follows IAST standard
- [ ] **Word meanings** - Check against 2-3 trusted sources
- [ ] **Translations** - Compare with multiple scholarly translations
- [ ] **Commentary** - Ensure aligns with traditional teachings
- [ ] **Practical applications** - Verify appropriateness and relevance

### Recommended Verification Process

1. Generate content with `verse-generate`
2. Open generated verse file in `_verses/`
3. Cross-reference each section with sources above
4. Edit for accuracy and authenticity
5. Commit changes

## Translation Permission Guidelines

### Public Domain (Safe to Use)
- Classical commentaries (Shankaracharya, etc.)
- Pre-1928 translations (Edwin Arnold, etc.)
- Government/educational resources (IIT Kanpur)

### Requires Permission/Attribution
- Modern translations (post-1928)
- Published books (Easwaran, Prabhupada)
- Commercial websites

### Best Practice
1. Use multiple public domain sources
2. Synthesize into your own words
3. Provide attribution when using specific translations
4. For Hindi translations, create your own or use public domain sources

## Quality Standards

### Minimum Required Fields
1. **Devanagari** - Sanskrit in Devanagari script
2. **Transliteration** - IAST standard
3. **Word Meanings** - Key Sanskrit terms (English & Hindi)
4. **Literal Translation** - English & Hindi
5. **Interpretive Meaning** - Commentary with spiritual context

### Optional But Recommended
- **Pronunciation Notes** - For difficult words
- **Story/Context** - Background from Mahabharata
- **Practical Application** - Modern life relevance
- **Keywords** - For search optimization

## Common Pitfalls to Avoid

- ❌ Mixing transliteration schemes (stick to IAST)
- ❌ Incomplete word meanings (add both languages)
- ❌ Copy-paste errors in Sanskrit (verify diacritics)
- ❌ Inconsistent formatting (follow existing verses)
- ❌ Copyright violations (synthesize from multiple sources)
- ❌ Trusting AI output without verification

## Resources Summary

| Source | Best For | URL |
|--------|----------|-----|
| Gita Supersite | Complete content | gitasupersite.iitk.ac.in |
| Vedabase | Devotional translation | vedabase.io/en/library/bg/ |
| Sanskrit Documents | Authentic Sanskrit | sanskritdocuments.org |
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
- [content-generation.md](content-generation.md) - Complete generation workflow
- [Gita Supersite](https://www.gitasupersite.iitk.ac.in/) - Primary verification source
