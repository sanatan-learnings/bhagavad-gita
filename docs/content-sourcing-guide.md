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

### Step 1: Generate Templates
```bash
python3 scripts/generate_verse_templates.py
# Select Chapter 1
```

### Step 2: Source Content
For each verse file:
1. Visit Gita Supersite for verse number
2. Copy Sanskrit Devanagari text
3. Copy IAST transliteration
4. Get word meanings
5. Select translation you prefer (or combine multiple)
6. Write practical application in your own words

### Step 3: Fill Templates
Open verse file (e.g., `chapter_01_verse_02.md`):

```yaml
devanagari: |
  [Paste from source]

transliteration: |
  [Paste from source]

word_meanings:
  - word: "संजय"
    roman: "sañjaya"
    meaning:
      en: "Sanjaya (charioteer, narrator)"
      hi: "संजय (सारथी, वर्णनकर्ता)"
  [Add more words...]

literal_translation:
  en: |
    [Paste/adapt translation]
  hi: |
    [Add Hindi translation]

interpretive_meaning:
  en: |
    [Write commentary - can combine multiple sources]
  hi: |
    [Hindi commentary]
```

### Step 4: Verify Accuracy
- Cross-reference with 2-3 sources
- Ensure Sanskrit is accurate
- Check transliteration follows standard (IAST)
- Verify meanings are contextually appropriate

### Step 5: Regenerate Search/Embeddings
```bash
python3 scripts/generate_embeddings_openai.py
python3 scripts/generate_search_index.py
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

### Use AI Assistance Carefully

- ✅ **Good use**: Transliteration verification, Sanskrit word lookup
- ✅ **Good use**: Structuring your own commentary
- ⚠️ **Careful**: Translations (verify with sources)
- ❌ **Avoid**: Completely AI-generated content without verification

## Common Pitfalls to Avoid

1. **Mixing transliteration schemes** (stick to IAST)
2. **Incomplete word meanings** (add both languages)
3. **Copy-paste errors** in Sanskrit (verify diacritics)
4. **Inconsistent formatting** (follow template exactly)
5. **Copyright violations** (synthesize from multiple sources)

## Example Workflow

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
1. Run `python3 scripts/generate_verse_templates.py`
2. Start with verses 2-5 (sample verses provided)
3. Build up momentum verse by verse
4. Regenerate search/embeddings after batches
