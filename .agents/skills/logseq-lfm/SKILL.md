---
name: logseq-lfm
description: >-
  Look up Logseq-Flavored Markdown details beyond the always-on core: footnote
  syntax, nested fenced code blocks, bold-vs-backtick rendering pitfalls, the
  singular/plural naming rationale and aliases, the file-name-vs-link reference
  table, and the logical-vs-on-disk page distinction. Use when formatting
  footnotes, debugging why a ref/inline-code renders wrong, deciding a page
  name, or checking whether a page exists before creating a file. Baseline LFM
  rules live in logseq-core.
metadata:
  short-description: 'Advanced LFM details (footnotes, naming, logical vs disk pages)'
---
# Logseq-Flavored Markdown (advanced)

`logseq-core` carries the always-on LFM guardrails (bullets, TAB nesting, protected `tags::`, namespaces, no blank lines). Load this skill for the deeper details.

## When to read which reference

- **Footnotes, nested ``` / `~~~` code fences, bold-next-to-backticks pitfalls, special formatting** → [references/advanced-lfm.md](./references/advanced-lfm.md).
- **Naming a page** (singular form, plural-via-alias, when *not* to apply the convention) and **file-name ↔ link translation** (`Namespace___Page.md` ↔ `[[Namespace/Page]]`, common mistakes) → [references/naming-and-paths.md](./references/naming-and-paths.md).
- **Does a page exist? Should I create a `.md` file?** (logical reference-only pages vs on-disk pages; grep before concluding "missing"; link without creating a file) → [references/logical-vs-disk-pages.md](./references/logical-vs-disk-pages.md).

## Never

- Modify, add, or remove existing `tags::` frontmatter (protected — see `logseq-core`).
- Invent `[[Pages]]` that don't exist; use the `logseq-link-hygiene` skill.
