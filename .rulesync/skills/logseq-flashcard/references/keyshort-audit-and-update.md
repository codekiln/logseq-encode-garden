# Keyshort flashcards: audit and update

Canonical workflow ported from command `logseq-manage-shortcut-flashcards`. Use when the user wants to **audit** or **fix** `#card` blocks on **Keyshort** pages only.

## Variables

- **Scope** – Optional: restrict to one scope (e.g. `VSCode`, `Lazygit`, `tmux`).
- **Subscope** – Optional: narrow further (e.g. `Git`, `Pane`).
- **Mode** – **Required**: `audit` or `update`.

## Conventions

- **Pages**:
  - `pages/<Scope>___Keyshort___<Action>.md`
  - `pages/<Scope>___Keyshort___<Subscope>___<Action>.md`
- **Ancestry tags** (parent block of the cards):
  - Include `[[Keyshort]]` and `[[<Scope>]]`.
  - Include `[[<Scope>/Keyshort]]` and `[[<Scope>/Keyshort/<Subscope>]]` when applicable.
- **Flashcards**:
  - Use `#card` blocks only.
  - Do not add `Question :: Answer` blocks.
- **Frontmatter**:
  - Do not add or remove `tags::` on existing pages.

## Workflow

### Step 1: Discover Keyshort pages

- If Scope is provided, search `pages/<Scope>___Keyshort___*.md`.
- If Scope is omitted, search all `pages/*___Keyshort___*.md`.

### Step 2: Audit each page

Check for:

- Parent block containing `[[Keyshort]]` and `[[<Scope>]]`.
- `[[<Scope>/Keyshort]]` (and `[[<Scope>/Keyshort/<Subscope>]]` if the path implies subscope).
- `#card` blocks as **children** of that parent block.
- Any "Flashcard Questions" sections or `Question :: Answer` blocks (flag for removal or refactor).

### Step 3: Apply updates (only in `update` mode)

- Add missing ancestry links to the parent block without altering unrelated content.
- If shortcut content exists but has no `#card`, wrap or convert the relevant block into a `#card` block.
- If `Question :: Answer` blocks exist, convert to `#card` or remove the section (ask if ambiguous).

### Step 4: Summarize

- List pages audited.
- For updates, summarize changes per page.

## Related project rules and commands

- rule: `logseq-page-naming-reference`
- rule: `logseq-flavored-markdown`
- command: `logseq-create-shortcut`
