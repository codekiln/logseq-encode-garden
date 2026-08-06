---
name: logseq-import-chatgpt-deep-research
description: >-
  Import a ChatGPT Deep Research report into the Logseq garden from its PDF and
  optional Markdown export. Use when the user gives a Deep Research PDF or asks
  to import/file a Deep Research report with preserved URL footnotes, source
  assets, Logseq-Flavored Markdown, existing-page links, and today's journal
  summary. This skill is the entrypoint for that import workflow.
targets: ["*"]
codexcli:
  short-description: Import ChatGPT Deep Research PDFs with Logseq footnotes
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
4. Link copied assets with skill **logseq-asset-linker**.
5. Resolve only intentional wikilinks with skill **logseq-link-hygiene**.
6. Add a concise `[[Filed]]` journal entry for today's date.
7. Run the checks in [references/validation.md](./references/validation.md).

## Hard Guardrail

Do not silently strip Deep Research citation markers. If the source contains
`cite` markers, the imported page must contain Logseq footnotes backed by URLs
extracted from the PDF, or the import is blocked.

## References

- Full workflow: [references/import-workflow.md](./references/import-workflow.md)
- Validation checklist: [references/validation.md](./references/validation.md)
- Citation helper: [scripts/restore_deep_research_footnotes.py](./scripts/restore_deep_research_footnotes.py)
