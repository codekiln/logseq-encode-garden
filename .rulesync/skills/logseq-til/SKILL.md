---
name: logseq-til
description: >-
  Log a "Today I Learned" item on today's day page under a single [[TIL]]
  block, appending to the block already there instead of creating a second
  one. Use when the user says "TIL", "log a TIL", "add that to my TIL", or
  hands over something they just learned and wants it on today's page. Do not
  use for research questions (logseq-question) or for entity pages
  (logseq-entity).
targets: ["*"]
codexcli:
  short-description: Append a TIL item under the one [[TIL]] block on today's day page
---

# Log a TIL

The user supplies the thing learned, phrased naturally — it can start with "that", a verb, or a noun phrase.

## Workflow

### Find today's day page

This garden keeps day pages at `journals/YYYY_MM_DD.md`. A garden that instead uses trimester/week/day pages keeps them at `pages/YYYY___tT___wWW___dN.md`; match today's date to the trimester, week and day number to find the file. When both layouts are present, prefer the journal.

If the file does not exist, create it with minimal content before adding the TIL.

### Look for an existing [[TIL]] block

Search the file for a bullet containing `[[TIL]]`, such as `- [[TIL]]`. There is at most one per day page.

- Found: append the new item as the last child bullet under it.
- Not found: add the block at the end of the file, or after the last top-level section when that reads better with the existing structure.

### Write the item

~~~markdown
- [[TIL]]
	- {what was learned}
~~~

Keep it concise. Use `[[wikilinks]]` only for pages known to exist in the garden — see skill `logseq-link-hygiene`.

### Report

Name the day page by file path and link form, say whether the `[[TIL]]` block already existed, and show the block as it now reads.

## Related

- rule: `logseq-core` — bullet structure, headings, LFM syntax (detail: skill `logseq-lfm`)
- skill: `logseq-update-week` — week and day page naming for trimester-based gardens
- page: `[[Logseq/Journal]]` — journal format when editing `journals/*.md`
