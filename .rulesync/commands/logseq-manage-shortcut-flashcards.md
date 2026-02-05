---
targets:
  - '*'
description: Audit or update Logseq Keyshort pages to ensure #card flashcards and proper ancestry tags
argument-hint: Optional Scope (e.g., VSCode, Lazygit); optional Subscope; mode (audit or update)
---
# Manage Logseq Keyshort Flashcards

This command audits or updates Keyshort pages to ensure `#card` flashcards inherit the correct tags from parent blocks and are picked up by Logseq `{{cards ...}}` queries.

## Variables

- **Scope** – Optional: Restrict to a specific scope (e.g., `VSCode`, `Lazygit`, `tmux`).
- **Subscope** – Optional: Narrow further (e.g., `Git`, `Terminal`).
- **Mode** – **Required**: `audit` or `update`.

## Conventions

- **Pages**:
  - `pages/<Scope>___Keyshort___<Action>.md`
  - `pages/<Scope>___Keyshort___<Subscope>___<Action>.md`
- **Ancestry tags**:
  - Parent block must include `[[Keyshort]]` and `[[<Scope>]]`.
  - Include `[[<Scope>/Keyshort]]` and `[[<Scope>/Keyshort/<Subscope>]]` when applicable.
- **Flashcards**:
  - Use `#card` blocks only.
  - Do not add `Question :: Answer` blocks.
- **Frontmatter**:
  - Do not add or remove `tags::` on existing pages.

## Workflow

### Step 1: Discover Keyshort pages

- If Scope is provided, search for:
  - `pages/<Scope>___Keyshort___*.md`
- If Scope is not provided, search for all `pages/*___Keyshort___*.md`.

### Step 2: Audit each page

Check for:
- Presence of a parent block containing `[[Keyshort]]` and `[[<Scope>]]`.
- Presence of `[[<Scope>/Keyshort]]` (and `[[<Scope>/Keyshort/<Subscope>]]` if applicable).
- `#card` blocks as children of the tagged parent block.
- Any "Flashcard Questions" sections or `Question :: Answer` blocks (flag these for removal or refactor).

### Step 3: Apply updates (only in `update` mode)

- Add missing ancestry links to the parent block without altering existing content.
- If a page has shortcut content but no `#card`, wrap or convert the relevant block into a `#card` block.
- If `Question :: Answer` blocks exist, convert to `#card` blocks or remove the section (ask if ambiguous).

### Step 4: Summarize results

- List pages audited.
- For updates, summarize changes per page.

## Report

- Provide a concise audit summary, with any pages needing manual review.
- If updates were applied, list each updated page path.

## Related

Use the prefix that matches the type: `rule:` for rules, `command:` for commands, `skill:` for skills.

- rule: `logseq-page-naming-reference` – File naming and link conventions
- rule: `logseq-flavored-markdown` – LFM formatting rules
- command: `logseq-create-shortcut` – Create new Keyshort pages
