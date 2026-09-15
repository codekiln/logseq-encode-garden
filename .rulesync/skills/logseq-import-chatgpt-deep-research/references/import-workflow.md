# Import Workflow

Use this workflow when importing ChatGPT Deep Research exports into the Logseq
garden.

## Inputs

- Required: ChatGPT Deep Research PDF.
- Recommended: matching ChatGPT Deep Research Markdown export.
- Optional: target Logseq page name and ChatGPT conversation URL.

If the Markdown export is missing, extract text from the PDF with `pdftotext`
and expect more manual cleanup. If the PDF is missing, do not claim citations
are preserved.

This skill converts a report into a Logseq page; it does not archive the
original PDF/Markdown export in the repo. Work with the source files from
wherever the user provided them and never copy them into `assets/`.

## Steps

1. **Choose the target page**
   - Use a namespaced report page, usually under the topic being researched.
   - On disk, convert `/` to `___`.
   - Check for an existing page before creating one.

2. **Do not commit the source files**
   - The point of this skill is to convert the report into a Logseq page, not
     to archive the original PDF/Markdown export as a binary asset in the
     repo. Read the PDF/Markdown from wherever the user provided them (e.g.
     `~/Downloads`, `/tmp`); do not copy them into `assets/`.
   - Do not add `source-pdf::`/`source-md::` frontmatter pointing at a copied
     asset. If provenance is worth recording, use a plain-text note (original
     filename, ChatGPT conversation URL if given) instead of a binary link.

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
   - Confirm no PDF/Markdown source file was copied into the repo.

## Failure Modes

- If `pdftohtml` is unavailable, install or locate Poppler before importing.
- If web citation markers exist but PDF anchors are missing or fewer than the
  citation groups, stop. Do not import a citation-stripped page.
- If URLs cannot be extracted from the PDF, ask for the original Deep Research
  PDF/export or the source list.
