---
name: lv4ad-3-enrich-links
description: >-
  Add wikilinks from an already-formatted LV4AD chapter page (from
  lv4ad-2-format-chapter) out to other entities already in the garden —
  tools, commands, people, GitHub repos, concepts like RSI — following
  logseq-link-hygiene. Use when the user asks to link up, enrich, or connect
  an [[LV4AD/Ch/...]] page after it's already been formatted into blockquote
  + [[My Note]] shape. Only adds links to existing or clearly-warranted stub
  pages; never rewrites highlight/note text or heading structure.
targets: ["*"]
codexcli:
  short-description: Link an LV4AD chapter page to other garden entities
---

# LV4AD 3: Enrich with entity links

Final pass on an already-formatted `[[LV4AD/Ch/<NN Title>]]` page: wikilink
mentions of tools, commands, people, and concepts to the rest of the garden.
Structure and wording from `lv4ad-2-format-chapter` do not change.

## Steps

1. **Scan the page** for backticked commands/tools, proper nouns, and concepts
   worth linking: CLI tools (`ed`, `sed`, `ex`, `lazygit`, `ripgrep`, `fd`),
   plugins/projects (`lazy.nvim`), people (the author, tool creators), health/
   ergonomics concepts (RSI), and other book-specific terms (e.g. `vim/:/Tutor`
   for the `:Tutor` command).
2. **Check before linking or creating**, per `logseq-link-hygiene`: grep
   `pages/` and `journals/` for the term first.
   - If a page already exists (even as a logical page referenced elsewhere,
     not just a `.md` file), link to it as-is — don't recreate it.
   - If it doesn't exist and is a genuinely reusable concept/tool/person (not
     a one-off phrase), it's fine to link it as a new stub `[[Term]]` and
     create a minimal one- or two-line stub page for it, mirroring how `[[Ed]]`,
     `[[sed]]`, and `[[RSI]]` were stubbed out for this book — short, factual,
     no book-import narration (`logseq-core` no-agent-taint applies).
   - Don't invent namespaces speculatively; use existing person/GitHub
     conventions (e.g. `[[Person/<Name>/GitHub/<repo>]]`) when linking a
     repository mentioned in a highlight, e.g. `dusty-phillips/dotfiles`
     becomes `[[Person/Dusty Phillips/GitHub/dotfiles]]` if that person hub
     already exists — check first rather than assuming.
3. **Link inline, in place** — turn existing backticked/plain mentions into
   `[[Wikilink]]`s (or `` `code` `` + `[[Link]]` combos when the source used
   code formatting for a tool name) without altering the surrounding
   quote/note text otherwise.
4. **Don't touch** `[[My Note]]` bullets' own leading link or the heading
   links back to the book site — only add links for *newly recognized*
   entities inside the prose.
5. **Record any new stub pages** in today's `[[Filed]]` journal entry per
   `[[Logseq/Journal]]`, alongside (or merged into) the chapter's existing
   journal entry from `lv4ad-1-import-chapter`.

## Guardrails

- Never link a page to itself.
- Never modify the protected `tags::` frontmatter on any page you touch,
  including new stubs.
- If uncertain whether a mention deserves a link (too generic, too one-off),
  leave it unlinked rather than guessing.
