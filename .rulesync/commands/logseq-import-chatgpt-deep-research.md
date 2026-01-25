---
targets:
  - '*'
description: Import ChatGPT Deep Research report PDFs into Logseq pages with proper formatting, footnotes, and entity linking
argument-hint: PDF file path (required), target page name (optional), journal date (optional, defaults to today)
---
# Import ChatGPT Deep Research Report PDF

This command imports a ChatGPT Deep Research report PDF into a Logseq page, converting it to Logseq Flavored Markdown (LFM) with proper formatting, footnotes with URLs, and optional entity linking to existing pages in the knowledge garden.

## Variables

- `{pdf_path}` - **Required**: Path to the PDF file to import
- `{target_page}` - **Optional**: Target page name in Logseq namespace format (e.g., `[[Namespace/Page]]`). If not provided, infer from PDF content or ask user.
- `{journal_date}` - **Optional**: Journal date in format `YYYY_MM_DD`. Defaults to today's date.

## Workflow

### Step 1: Extract PDF Content

- Extract text from the PDF using `pdftotext` command-line tool:
  ```bash
  pdftotext '{pdf_path}' -
  ```
- If `pdftotext` is not available, use Python with PyPDF2 or similar library
- Preserve document structure (headings, sections, tables) as much as possible

### Step 2: Determine Target Page

- **If `{target_page}` is provided**: Use that exact page
- **If `{target_page}` is not provided**:
  - Search for existing pages that might match the PDF content
  - Ask user to specify the target page name
- **Check if page exists**: Search for the page file (e.g., `pages/Namespace___Page.md`)
- **File naming**: Use triple underscores (`___`) for namespaces in filenames
- **Link format**: Use forward slashes (`/`) in links (e.g., `[[Namespace/Page]]`)

### Step 3: Convert to Logseq Flavored Markdown

Follow the logseq-convert-from-md-to-lfm rule:

- [ ] Convert all content to bullet-point structure with TAB indentation
- [ ] Ensure all headings are prefixed with bullet points (`-`)
- [ ] Maintain proper heading hierarchy (H1 at root, H2 at first indent, etc.)
- [ ] Convert tables appropriately:
  - 2-column tables can stay as markdown tables (nested in bullet points)
  - Multi-column comparison tables should be preserved when they provide clear value
- [ ] Remove horizontal rules (`---`)
- [ ] Ensure code blocks are properly nested inside bullet points
- [ ] **Preserve existing page content** if the page already exists - append or merge appropriately

### Step 4: Identify Existing Entities for Linking

- [ ] Search the knowledge garden for entities mentioned in the PDF that already exist as pages
- [ ] Common entities to check:
  - Technologies (e.g., `[[MCP]]`, `[[Python]]`, `[[TypeScript]]`)
  - Tools (e.g., `[[Toggl]]`, `[[GitHub]]`)
  - Concepts (e.g., `[[API]]`, `[[CLI]]`)
  - Protocols (e.g., `[[REST]]`, `[[GraphQL]]`)
- [ ] **Present findings to user**: List identified entities and ask which ones they want to link
  - Example: "I found these existing pages that could be linked: [[MCP]], [[Python]], [[CLI]]. Would you like me to link any of these?"
- [ ] **User guidance**:
  - Do NOT create new pages or tags
  - Do NOT replace every instance - be selective
  - Only link when it adds semantic value
  - Ask user for confirmation before linking

### Step 5: Extract and Format Footnotes

- [ ] Identify all numbered references in the PDF (typically superscript numbers or bracketed numbers like `1`, `2`, `[1]`, `[2]`)
- [ ] Convert these to Logseq footnote format: `[^1]`, `[^2]`, `[^3]`
- [ ] **Extract URLs from the PDF**: ChatGPT Deep Research reports should already contain URLs in the footnotes/references section. Extract these URLs directly from the PDF.
- [ ] **If URLs are missing or incomplete** (fallback only):
  - Search for actual URLs for each reference:
    - **GitHub repositories**: Search for `github username/repo-name` or project name
    - **npm packages**: Search for `@package-name` or package name on npm
    - **PyPI packages**: Search for `pypi package-name`
    - **NuGet packages**: Search for package name on NuGet
    - **Official documentation**: Search for `service-name API documentation` or `service-name docs`
    - **Blog posts**: Search for title or author + topic
    - **Protocols/Standards**: Search for official protocol documentation
- [ ] Format footnotes as `[^1]: https://url.com` (URL only, no descriptive text)
- [ ] Create a "Footnotes" section at the end of the document
- [ ] Ensure footnotes are properly nested under bullet points

### Step 6: Consolidate Duplicate Footnotes

- [ ] Identify footnotes that reference the same URL
- [ ] Map duplicate footnotes to a single footnote number (use the lowest number)
- [ ] Update all references in the document to use the consolidated footnote number
- [ ] Remove duplicate footnote definitions
- [ ] Ensure each unique URL appears only once in the footnotes section

**Example**: If `[^3]`, `[^4]`, `[^5]`, `[^6]` all point to the same URL, consolidate to `[^3]` and update all references.

### Step 7: Add Frontmatter

- [ ] **Preserve existing frontmatter** (especially `tags::`) - DO NOT modify existing `tags::` frontmatter
- [ ] Add `tags:: [[ChatGPT/Deep Research]]` if not already present
- [ ] **Ask user for ChatGPT conversation link**: "Please provide the ChatGPT conversation link for this Deep Research report"
- [ ] Add `chatgpt-link:: {link}` to frontmatter where `{link}` is the URL provided by the user
- [ ] Frontmatter format:
  ```markdown
  tags:: [[ChatGPT/Deep Research]]
  chatgpt-link:: https://chatgpt.com/c/...
  ```

### Step 8: Link from Journal Entry

- [ ] Determine journal date: Use `{journal_date}` if provided, otherwise use today's date (format: `YYYY_MM_DD`)
- [ ] Journal file path: `journals/{journal_date}.md`
- [ ] Add link to the page in the journal entry using namespace format: `[[Namespace/Page]]` (with forward slashes)
- [ ] Place the link at an appropriate location (typically near the top)

## Report

After completing the import, report:

- ✅ PDF extracted and converted to LFM
- ✅ Target page: `[[Namespace/Page]]` (created/updated)
- ✅ Footnotes added: {count} unique footnotes
- ✅ Entities linked: {list of linked entities} (if any)
- ✅ Journal entry updated: `journals/{date}.md`
- ✅ Frontmatter added: `tags:: [[ChatGPT/Deep Research]]`, `chatgpt-link:: {link}`

## Related Rules

- **logseq-convert-from-md-to-lfm** - Conversion checklist for markdown to LFM
- **logseq-flavored-markdown** - Standard LFM formatting rules
- **logseq-naming-conventions** - Page naming and namespace conventions
- **logseq-page-naming-reference** - File vs link format reference
- **logseq-journal-updates** - How to update journal entries

## Common Pitfalls

1. **Creating new pages when existing page should be used** - Always check for existing pages first
2. **Using wrong namespace format** - Remember: `___` in filenames, `/` in links
3. **Footnotes with descriptive text** - Use URL only: `[^1]: https://url.com` not `[^1]: [text](url)`
4. **Not consolidating duplicates** - Always deduplicate footnotes pointing to same URL
5. **Modifying frontmatter tags** - Never modify existing `tags::` frontmatter, only add if missing
6. **Missing footnote URLs** - All footnotes should have actual hyperlinks, not placeholder text
7. **Over-linking entities** - Only link when user confirms and when it adds semantic value
8. **Creating new pages for entities** - Only link to existing pages, never create new ones
