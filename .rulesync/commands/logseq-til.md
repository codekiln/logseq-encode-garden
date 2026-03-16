---
targets:
  - '*'
description: Log a "Today I Learned" item under the [[TIL]] block in today's day page, appending to an existing [[TIL]] block if one is present
argument-hint: TIL content (required); e.g. "that git rebase --onto can rebase a range of commits"
---
# Log a Today I Learned (TIL) Entry

This command adds a TIL item to the current day page under a `[[TIL]]` block. It avoids creating duplicate `[[TIL]]` blocks — if one already exists on the day page it appends to it; otherwise it creates one.

## Variables

- **TIL content** – **Required**: The thing learned, phrased naturally. Can start with "that", an action verb, or a noun phrase.

## Conventions

- There must be **at most one** `[[TIL]]` block per day page.
- If a `[[TIL]]` block already exists, append to it (do not create a second one).
- Each TIL item is a child bullet of the `[[TIL]]` block.
- Use Logseq Flavored Markdown (LFM): all content as bullets, TAB indentation, no blank lines.

## Workflow

### Step 1: Determine today's day page

Detect which day-page style this repo uses:

1. **Journal-style** (default): `journals/YYYY_MM_DD.md` — used when a `journals/` directory exists and contains dated files.
2. **Week/day-style**: `pages/YYYY___tT___wWW___dN.md` — used when the repo uses trimester/week/day page structure (e.g. `pages/2025___t1___w14___d2.md`). In this case determine today's page by matching today's date to the correct trimester, week number, and day number.

If the repo style is ambiguous, prefer the journal style.

### Step 2: Open today's day page

- Read the file for today's date.
- If the file does not exist yet, note that it will need to be created with minimal content before the TIL block is added.

### Step 3: Check for an existing [[TIL]] block

- Search the file for a line containing `[[TIL]]` at bullet level (e.g. `- [[TIL]]`).
- **If found**: identify the position; the new item will be appended as the last child bullet under that block.
- **If not found**: the `[[TIL]]` block will be created. Append it at the end of the file (or after the last top-level section, whichever is more natural for the existing structure).

### Step 4: Write the TIL item

Format the entry as a child bullet of `[[TIL]]`:

~~~markdown
- [[TIL]]
	- {TIL content}
~~~

If the `[[TIL]]` block already exists, append only the child bullet:

~~~markdown
	- {TIL content}
~~~

Keep the content concise. Link to relevant Logseq pages with `[[double brackets]]` only when a matching page is known to exist in the garden.

### Step 5: Report

- Confirm which day page was updated (file path and link form).
- State whether the `[[TIL]]` block already existed or was newly created.
- Show the final content of the `[[TIL]]` block as it now appears in the file.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-flavored-markdown` – Bullet structure, headings, LFM syntax
- rule: `logseq-typical-week-structure` – Week/day page naming for trimester-based repos
- rule: `logseq-journal-updates` – Journal entry conventions
