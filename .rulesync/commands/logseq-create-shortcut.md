---
targets:
  - '*'
description: Create Logseq Keyshort pages with #card flashcards using the <Scope>/Keyshort/<Action> (and optional <Subscope>) format
argument-hint: Scope (required); Action (required); optional Subscope; Shortcut; Description; optional Grouped cards
---
# Create a Logseq Keyshort Page (with #card flashcards)

This command creates or updates Logseq Keyshort pages using the canonical `<Scope>/Keyshort/<Action>` format, with optional `<Subscope>` segments. It ensures `#card` flashcards are children of a parent block that carries the needed ancestry tags for Logseq's `{{cards ...}}` queries.

## Variables

- **Scope** – **Required**: The tool or domain (e.g., `VSCode`, `Lazygit`, `tmux`).
- **Action** – **Required**: The shortcut action (e.g., `Open the Source Control Panel`).
- **Subscope** – Optional: A subgroup within the scope (e.g., `Git`, `Terminal`, `Pane`).
- **Shortcut** – Optional: Key chord(s) for the action (e.g., `Cmd+Shift+P`).
- **Description** – Optional: Short explanation of what it does.
- **Grouped cards** – Optional: If multiple related shortcuts should live on one page (e.g., Next/Previous), list them.

## Conventions

- **Page naming**:
  - Without subscope: `pages/<Scope>___Keyshort___<Action>.md`
  - With subscope: `pages/<Scope>___Keyshort___<Subscope>___<Action>.md`
- **Link format**:
  - `[[<Scope>/Keyshort]]` and optionally `[[<Scope>/Keyshort/<Subscope>]]`
  - Always include `[[Keyshort]]` and `[[<Scope>]]` in the parent block.
- **Flashcards**:
  - Use `#card` blocks only.
  - Avoid `Question :: Answer` blocks and any "Flashcard Questions" section.
- **Frontmatter**:
  - Do not add or remove `tags::` on existing pages.

## Workflow

### Step 1: Normalize inputs

- Confirm Scope, Action, and optional Subscope.
- If shortcut or description is missing, ask for it (or leave placeholders if the user wants a stub).
- If grouped cards are requested, list each card's action, shortcut, and description.

### Step 2: Determine target page path

- If Subscope is provided, use: `pages/<Scope>___Keyshort___<Subscope>___<Action>.md`
- Otherwise, use: `pages/<Scope>___Keyshort___<Action>.md`

### Step 3: Check for existing pages (dedup)

- Search for existing pages matching the intended title and close variants.
- If a matching page exists, update it rather than creating a new page.

### Step 4: Create or update content (LFM)

- Use Logseq Flavored Markdown (bulleted blocks, no blank lines).
- Create a parent block that includes ancestry tags:
  - `[[Keyshort]] [[<Scope>]] [[<Scope>/Keyshort]]`
  - Add `[[<Scope>/Keyshort/<Subscope>]]` if applicable.
- Add `#card` blocks as children of that parent block.
- For grouped cards, place multiple `#card` blocks under the same tagged parent block.

#### Example (single card)

~~~markdown
- [[Keyshort]] [[VSCode]] [[VSCode/Keyshort]] [[VSCode/Keyshort/Git]]
	- **Open the Source Control Panel** #card
		- Shortcut: `Ctrl+Shift+G`
		- Description: Opens the Source Control panel.
~~~

#### Example (grouped cards)

~~~markdown
- [[Keyshort]] [[tmux]] [[tmux/Keyshort]] [[tmux/Keyshort/Pane]]
	- **Move Pane Up** #card
		- Shortcut: `<keys>`
		- Description: Moves the pane up.
	- **Move Pane Down** #card
		- Shortcut: `<keys>`
		- Description: Moves the pane down.
~~~

## Report

- Report the created/updated page path.
- Summarize the cards added or updated.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-page-naming-reference` – File naming and link conventions
- rule: `logseq-flavored-markdown` – LFM formatting rules
- command: `logseq-manage-shortcut-flashcards` – Audit and maintain Keyshort pages
