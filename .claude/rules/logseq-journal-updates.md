---
paths:
  - '*.md'
---
# Journal Updates for Page Changes

⚠️ **CRITICAL**: When creating or modifying pages in the Logseq knowledge garden, you MUST always add an entry to today's journal to record the change.

## Purpose

Treat each journal entry as a public-facing, fun-to-read snapshot of your technical life at this moment in time (a "now page" for the day), not as an audit log.

## Guidelines

1. **For New Pages** (REQUIRED):
   - ⚠️ **MUST** log under `[[Filed]]`
   - Default format is link-only: `- [[New/Page/Name]]`
   - Do **not** use repetitive boilerplate like `Imported [[...]]` or `Created [[...]]`
   - Do **not** add inline action text next to links in `[[Filed]]`

2. **For Updated Pages**:
   - Log under `[[Updated]]`
   - Default format is link-only: `- [[Existing/Page]]`
   - Do **not** use repetitive boilerplate like `Updated [[...]] with ...`
   - Do **not** add inline action text next to links in `[[Updated]]`

3. **Optional Context**:
   - Add context only when it materially improves the narrative snapshot
   - At most one sentence, attached to the page link as a child bullet
   - Keep it human and readable, not status narration

4. **Format**:
   - Use bullet points (Logseq format)
   - Use page links with double square brackets: `[[Page/Name]]`
   - Under `[[Filed]]` / `[[Updated]]`, each item should be a bare page link
   - Prefer short lists of links over prose activity logs

5. **Journal Location**:
   - Add to the current day's journal file in `journals/YYYY_MM_DD.md`
   - Place new entries at an appropriate position in the journal file

This rule keeps the journal legible and engaging for readers while still showing the evolution of the garden.

## Checklist for Page Creation
- [ ] Page created
- [ ] ⚠️ Journal entry added to today's date (YYYY_MM_DD.md)
- [ ] Page properly linked under `[[Filed]]` (or `[[Updated]]` for modifications)
