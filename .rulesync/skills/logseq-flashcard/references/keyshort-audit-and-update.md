# Keyshort flashcards: audit and update

Workflow ported from command `logseq-manage-shortcut-flashcards`. Use when the user wants to **audit** or **fix** review-card blocks on **Keyshort** pages only.

## Variables

- **Scope** – Optional: restrict to one scope (e.g. `VSCode`, `Lazygit`, `tmux`).
- **Subscope** – Optional: narrow further (e.g. `Git`, `Pane`).
- **Mode** – **Required**: `audit` or `update`.

## Conventions

- **Pages**:
  - `pages/<Scope>___Keyshort___<Action>.md`
  - `pages/<Scope>___Keyshort___<Subscope>___<Action>.md`
- **Ancestry links** (on the review prompt or a parent block):
  - Include `[[Keyshort]]` and the scope links used by the intended `{{cards}}` queries.
  - New general-purpose Keyshort pages normally include `[[<Scope>]]` and `[[<Scope>/Keyshort]]`, plus `[[<Scope>/Keyshort/<Subscope>]]` when applicable.
  - A more specific source link may supply the review scope, such as `[[tmux/session/Picker]]` on a picker-only card.
- **Flashcards**:
  - New or migrated Keyshort review cards use `[[Card]]`.
  - Existing `#card` or `[[card]]` blocks are legacy review cards; preserve them unless the task is to migrate them.
  - Do not add `Question :: Answer` blocks.
- **Frontmatter**:
  - Keyshort pages use `logseq-entity:: [[Logseq/Entity/Keyshort]]`.
  - Reviewable Keyshort pages also include `[[Logseq/Entity/Card]]` after the Keyshort type.
  - `tags::` is protected per `logseq-core`.

## Workflow

### Step 1: Discover Keyshort pages

- If Scope is provided, search `pages/<Scope>___Keyshort___*.md`.
- If Scope is omitted, search all `pages/*___Keyshort___*.md`.

### Step 2: Audit each page

Check for:

- `logseq-entity::` containing `[[Logseq/Entity/Keyshort]]`, followed by `[[Logseq/Entity/Card]]` when the page contains review cards.
- Review prompt or parent block containing `[[Keyshort]]` and the intended review-scope links.
- `[[Card]]`, `#card`, or `[[card]]` on the review prompt, with the binding and description in child blocks.
- Any "Flashcard Questions" sections or `Question :: Answer` blocks (flag for removal or refactor).

### Step 3: Apply updates (only in `update` mode)

- Add a missing `[[Logseq/Entity/Keyshort]]` marker to `logseq-entity::`; add `[[Logseq/Entity/Card]]` after it when the page contains review cards.
- Add missing ancestry links to the review prompt or its parent block without altering unrelated content.
- If shortcut content exists but has no review marker, wrap or convert the relevant block into a `[[Card]]` block.
- If `Question :: Answer` blocks exist, convert to `[[Card]]` or remove the section (ask if ambiguous).

### Step 4: Summarize

- List pages audited.
- For updates, summarize changes per page.

## Related project rules and commands

- rule: `logseq-core` (naming/paths; detail: skill `logseq-lfm`)
- rule: `logseq-core` (LFM; detail: skill `logseq-lfm`)
- command: `logseq-create-shortcut`
