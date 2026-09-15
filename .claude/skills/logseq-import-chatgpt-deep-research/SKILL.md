---
name: logseq-import-chatgpt-deep-research
description: >-
  Convert a ChatGPT Deep Research report into a Logseq-Flavored Markdown page,
  from its PDF and optional Markdown export. Use when the user gives a Deep
  Research PDF or asks to import/file a Deep Research report with preserved URL
  footnotes, Logseq-Flavored Markdown, existing-page links, and today's journal
  summary. This skill converts the report into a page; it does not archive the
  original PDF/Markdown export as a binary asset in the repo. This skill is the
  entrypoint for that import workflow.
---
# Import ChatGPT Deep Research

Use this skill for ChatGPT Deep Research reports, especially when the user
provides both `.pdf` and `.md` exports. The **PDF is the source of truth for
citations**; the Markdown export is only a structure/text convenience.

## Happy Path

1. Read and follow [references/import-workflow.md](./references/import-workflow.md).
2. Restore citations before LFM conversion:
   - Run `python3 .rulesync/skills/logseq-import-chatgpt-deep-research/scripts/restore_deep_research_footnotes.py --pdf <report.pdf> --markdown <report.md> --output /tmp/report-with-footnotes.md`.
   - If the script fails, stop and fix the citation extraction issue before importing.
3. Convert the footnoted Markdown to LFM with skill **logseq-convert-md-to-lfm**.
4. Resolve only intentional wikilinks with skill **logseq-link-hygiene**.
5. Add a concise `[[Filed]]` journal entry for today's date.
6. Run the checks in [references/validation.md](./references/validation.md).

## No Binary Assets

This skill converts a Deep Research report into a Logseq page. It does **not**
copy the original PDF or Markdown export into `assets/`, and it does not add
`source-pdf::`/`source-md::` frontmatter pointing at a copied binary. Read the
source files from wherever the user provided them (e.g. `~/Downloads`, `/tmp`)
and leave them there.

## Hard Guardrail

Do not silently strip Deep Research citation markers. If the source contains
`cite` markers, the imported page must contain Logseq footnotes backed by URLs
extracted from the PDF, or the import is blocked.

## References

- Full workflow: [references/import-workflow.md](./references/import-workflow.md)
- Validation checklist: [references/validation.md](./references/validation.md)
- Citation helper: [scripts/restore_deep_research_footnotes.py](./scripts/restore_deep_research_footnotes.py)
