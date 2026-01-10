---
targets:
  - '*'
description: Import an "Energy" section from Treatise on Writing Acousmatic Music on Fixed Media into Logseq
argument-hint: URL to the energy page xhtml (e.g., https://sites.inagrm.com/avdg/activities/percussion-resonance.xhtml)
---

# Import ToWAMoFM Energy

This command imports an "Energy" section from the Treatise on Writing Acousmatic Music on Fixed Media (ToWAMoFM) into your Logseq knowledge garden. It fetches the content from the website, translates it to English, extracts keywords into the [[ToWAMoFM]] namespace, creates person pages for composers, and sets up sound example embeds.

## Variables

- `{url}` - The URL to the energy page xhtml file (e.g., `https://sites.inagrm.com/avdg/activities/percussion-resonance.xhtml`)

## Workflow

### Step 1: Fetch and Parse the Page

1. Navigate to the provided URL using the browser tools
2. Extract the page content, including:
   - Page title
   - All text content (sections, advice, commentary)
   - Sound examples with composer names and piece titles
   - Bibliography references
3. Monitor network requests to find the actual MP3 file URLs for sound examples

### Step 2: Determine Page Structure

1. Identify the energy type from the URL or page title (e.g., "percussion-resonance" → "Percussion-Resonance")
2. Determine the page number in the sequence (01, 02, 03, etc.) by checking existing pages in `pages/ToWAMoFM___01___01 Energy___**.md`
3. Determine the previous and next pages in the sequence:
   - Previous: The energy page with number one less (if not the first)
   - Next: The energy page with number one more (if not the last)

### Step 3: Translate and Simplify Content

1. Translate all French content to English
2. Simplify language to be accessible to teenaged musical experimenters:
   - Remove academic pretension
   - Use direct, conversational language
   - Explain technical terms in plain language
   - Keep it practical and hands-on
3. Break down complex concepts into digestible bullet points

### Step 4: Extract Keywords and Create Links

**CRITICAL: Follow Logseq Flavored Markdown (LFM) rules strictly. See the logseq-flavored-markdown rule for complete guidelines.**

1. **Identify key musical concepts and terms** from the content

2. **Replace angle bracket terms with Logseq page references:**
   - Find all terms in angle brackets (e.g., `<harmonic halo>`, `<dynamic>`, `<halo harmonique>`)
   - Convert these to proper Logseq page references following the workflow below
   - Example: `<harmonic halo>` → `[[Harmonic Halo]]`
   - Example: `<dynamic>` → `[[Dynamic]]`
   - Capitalize terms appropriately when converting (e.g., "harmonic halo" → "Harmonic Halo")

3. **For each term (including those from angle brackets), check if it already exists in the knowledge garden:**
   - Search for existing pages using `glob_file_search` or `grep`:
     - Search for `pages/**/*{Term}*.md` (various naming patterns)
     - Search for `[[Term]]` references in existing pages
     - Check if a page exists with the exact term name
   - **If the term already exists:**
     - Use the existing page reference exactly as it appears in the knowledge garden
     - Do NOT create a new page
     - Use the canonical page name (the actual filename) when referencing
   - **If the term does NOT exist:**
     - Create a new page at `pages/ToWAMoFM___{Term}.md` (which corresponds to `[[ToWAMoFM/{Term}]]`)
     - Add frontmatter with alias: `alias:: [[{Term}]]`
     - Example: For "Exciter", create `pages/ToWAMoFM___Exciter.md` with:
       ```markdown
       alias:: [[Exciter]]
       ```

4. **In the energy page content, always use the non-namespaced term reference:**
   - Use `[[Term]]` (not `[[ToWAMoFM/Term]]`) in the content
   - The alias system will resolve `[[Term]]` to `[[ToWAMoFM/Term]]` if needed
   - Example: Write `[[Exciter]]` in content, not `[[ToWAMoFM/Exciter]]`
   - Replace angle bracket terms in the original text: `<harmonic halo>` → `[[Harmonic Halo]]`

5. **Common terms to check/create:**
   - `[[Sound Body]]`, `[[Exciter]]`, `[[Resonator]]`, `[[Diffuser]]`
   - `[[ADSR]]`, `[[Attack]]`, `[[Decay]]`, `[[Sustain]]`, `[[Release]]`
   - `[[Percussion]]`, `[[Resonance]]`, `[[Harmonic Halo]]`
   - `[[Instrument]]`, `[[Microphones]]`, `[[Sound/Speaker]]`
   - Any other relevant musical concepts from the content
   - Terms found in angle brackets in the original French text

6. **Create person references for composers mentioned:**
   - Follow the logseq-person rule for person page creation
   - Search first to avoid duplicates
   - Use `[[Person/{Composer Name}]]` format

### Step 5: Create the Main Energy Page

1. Create the page file at `pages/ToWAMoFM___01___01 Energy___{NN} {Energy-Name}.md` where:
   - `{NN}` is the two-digit page number (01, 02, 03, etc.)
   - `{Energy-Name}` is the formatted energy name (e.g., "Percussion-Resonance")
2. Add frontmatter:
   - `alias:: [[ToWAMoFM/{Energy-Name}]]` (if appropriate)
   - `prev:: [[ToWAMoFM/01/01 Energy/{NN-1} {Previous-Name}]]` (if not first)
   - `next:: [[ToWAMoFM/01/01 Energy/{NN+1} {Next-Name}]]` (if not last)
3. Structure the content:
   - Main heading: `- # [{Energy-Name}]({url})`
   - Organize content into logical sections with `##` headings
   - Use bullet points with proper TAB indentation
   - Include a "Sound Examples" section at the end
   - Include a "Bibliography" section if present

### Step 6: Process Sound Examples

For each sound example:

1. Extract:
   - Composer name (e.g., "Ivo Malec")
   - Piece title (e.g., "Attaqua")
   - MP3 file URL from network requests

2. Create person page if needed:
   - Check if `pages/Person___{Composer Name}.md` exists
   - If not, create a basic person page following the **logseq-person rule** (see logseq-person command/rule for complete guidelines)

3. Create sound example embed page:
   - File: `pages/Person___{Composer Name}___{Piece Title}.md`
   - Content: Simple format with just the audio link:
     ```markdown
     - ![Piece Title](mp3-url)
     ```

4. Add embed to main energy page:
   - In the "Sound Examples" section, add: `{{embed [[Person/{Composer Name}/{Piece Title}]]}}`

### Step 7: Formatting Guidelines

1. **Follow Logseq Flavored Markdown (LFM) rules strictly:**
   - **CRITICAL: Refer to the logseq-flavored-markdown rule for complete guidelines**
   - All content must be in bullet points (`-`)
   - Use TAB indentation (not spaces) for nesting
   - No blank lines between content blocks
   - Headings must be prefixed with bullet points: `- # Heading Text`
   - Proper heading hierarchy: H2 (##) under H1 (#), H3 (###) under H2 (##), etc.
   - Never modify, add, or remove `tags::` frontmatter (if present)
   - Use triple tildes (`~~~`) for code blocks when nested in markdown

2. Language style:
   - Conversational and accessible
   - Avoid academic jargon
   - Use "we" and "you" to engage the reader
   - Include practical examples and analogies
   - Add personal notes or connections where helpful (marked with `[[My Note]]` or italicized)

3. Link formatting:
   - Use double square brackets for page references: `[[Page Name]]`
   - Use namespaces appropriately: `[[ToWAMoFM/Concept]]`, `[[Person/Name]]`
   - Create embeds for sound examples: `{{embed [[Person/Name/Piece]]}}`

### Step 8: Update Journal

1. Add an entry to today's journal file (`journals/YYYY_MM_DD.md`)
2. Link to the newly created energy page
3. Note what was imported

## Example

**Input:**
```
/logseq-ToWAMoFM-energy https://sites.inagrm.com/avdg/activities/percussion-resonance.xhtml
```

**Output:**
- Creates `pages/ToWAMoFM___01___01 Energy___01 Percussion-Resonance.md`
- Creates person pages for all composers - following the logseq-person rule
- Creates embed pages for each sound example
- Updates journal with entry

## Notes

- The command assumes pages are numbered sequentially (01, 02, 03, etc.)
- Sound example MP3 URLs are found by monitoring network requests when the page loads
- Person pages follow the logseq-person rule conventions
- All content is translated from French to accessible English
- The language is simplified for teenaged musical experimenters, not academic researchers (make it simple and unpretentious)
