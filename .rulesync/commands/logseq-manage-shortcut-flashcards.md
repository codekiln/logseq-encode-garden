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
- **Ancestry links**:
  - The review prompt or a parent block includes `[[Keyshort]]` and the scope links used by the intended `{{cards}}` queries.
  - New general-purpose Keyshort pages normally include `[[<Scope>]]` and `[[<Scope>/Keyshort]]`, plus `[[<Scope>/Keyshort/<Subscope>]]` when applicable.
  - A more specific source link may supply the review scope, such as `[[tmux/session/Picker]]` on a picker-only card.
- **Flashcards**:
  - New or migrated review cards use `[[Card]]`; preserve existing `#card` and `[[card]]` markers unless migration is requested.
  - Do not add `Question :: Answer` blocks.
- **Frontmatter**:
  - Keyshort pages use `logseq-entity:: [[Logseq/Entity/Keyshort]]`.
  - Reviewable Keyshort pages also include `[[Logseq/Entity/Card]]` after the Keyshort type.

## Workflow

### Step 1: Discover Keyshort pages

- If Scope is provided, search for:
  - `pages/<Scope>___Keyshort___*.md`
- If Scope is not provided, search for all `pages/*___Keyshort___*.md`.

### Step 2: Audit each page

Check for:
- `logseq-entity::` containing `[[Logseq/Entity/Keyshort]]`, followed by `[[Logseq/Entity/Card]]` when the page contains review cards.
- Review prompt or parent block containing `[[Keyshort]]` and the intended review-scope links.
- `[[Card]]`, `#card`, or `[[card]]` on the review prompt, with the binding and description in child blocks.
- Any "Flashcard Questions" sections or `Question :: Answer` blocks (flag these for removal or refactor).

### Step 3: Apply updates (only in `update` mode)

- Add a missing `[[Logseq/Entity/Keyshort]]` marker to `logseq-entity::`; add `[[Logseq/Entity/Card]]` after it when the page contains review cards.
- Add missing ancestry links to the review prompt or its parent block without altering existing content.
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

- skill: `logseq-flashcard` – Home for this workflow; prefer the skill for agents
- rule: `logseq-core` – File naming and link conventions (detail: skill `logseq-lfm`)
- rule: `logseq-core` – LFM formatting rules (advanced detail: skill `logseq-lfm`)
- command: `logseq-create-shortcut` – Create new Keyshort pages
