# Import Workflow

This workflow replaces the deprecated `logseq-import-chatgpt-deep-research`
command.

## Inputs

- Required: ChatGPT Deep Research PDF.
- Recommended: matching ChatGPT Deep Research Markdown export.
- Optional: target Logseq page name and ChatGPT conversation URL.

If the Markdown export is missing, extract text from the PDF with `pdftotext`
and expect more manual cleanup. If the PDF is missing, do not claim citations
are preserved.

## Steps

1. **Choose the target page**
   - Use a namespaced report page, usually under the topic being researched.
   - On disk, convert `/` to `___`.
   - Check for an existing page before creating one.

2. **Copy source assets**
   - Copy the PDF into `assets/` under a namespace-shaped folder matching the
     target page.
   - Copy the original Markdown export into the same folder when provided.
   - Add `source-pdf::` and `source-md::` frontmatter links to the page.

3. **Restore citations from the PDF**
   - Run the helper script:
     ```bash
     python3 .rulesync/skills/logseq-import-chatgpt-deep-research/scripts/restore_deep_research_footnotes.py \
       --pdf path/to/report.pdf \
       --markdown path/to/report.md \
       --output /tmp/report-with-footnotes.md
     ```
   - The script extracts PDF hyperlinks with `pdftohtml -xml`, maps web
     `cite` markers in Markdown order to PDF anchors, deduplicates URLs using
     the lowest PDF footnote number, strips local `filecite` markers, and
     appends URL-only Markdown footnote definitions.
   - Treat `filecite` markers as local provenance. Represent them with
     `source-*::`, `see-also::`, or normal garden links, not fake URL footnotes.

4. **Convert to LFM**
   - Use skill **logseq-convert-md-to-lfm**.
   - Preserve headings as bullet-prefixed headings.
   - Convert wide tables to label-value bullets unless the table is genuinely
     clearer as a wrapped Markdown table.
   - Nest code fences inside bullets.
   - Remove blank lines and horizontal rules.

5. **Link existing entities selectively**
   - Use skill **logseq-link-hygiene**.
   - Link only clear existing pages that improve navigation.
   - Do not create new entity pages as a side effect of an import.

6. **Update today's journal**
   - Add the report under `[[Filed]]` if the page is new.
   - Keep the entry link-first, with at most one short child sentence that
     summarizes the result.

7. **Report back**
   - Name the target page.
   - Report the number of unique URL footnotes.
   - Mention any stripped local file citations and how they were represented.
   - Mention validation results.

## Failure Modes

- If `pdftohtml` is unavailable, install or locate Poppler before importing.
- If web citation markers exist but PDF anchors are missing or fewer than the
  citation groups, stop. Do not import a citation-stripped page.
- If URLs cannot be extracted from the PDF, ask for the original Deep Research
  PDF/export or the source list.
