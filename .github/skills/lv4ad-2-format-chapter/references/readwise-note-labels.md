# Labeling Readwise note segments

After **lv4ad-1-import-chapter**, each highlight may have zero or more **plain**
child bullets (note segments). This pass labels each segment `[[My Note]]` or
`[[AI Notes]]` and shapes nested content. The user also adds notes directly in
Logseq later — treat those the same way when reformatting.

## Already labeled?

If a child bullet already starts with `[[My Note]]` or `[[AI Notes]]`, keep the
label and only fix nesting/italics — do not relabel.

## Classifying an unlabeled segment

**Default to `[[My Note]]`** when uncertain.

### `[[AI Notes]]` — Readwise built-in AI answers

Typical signals (any one is enough):

- Opens with *The document* (e.g. *The document identifies…*, *The document
  does not explicitly define…*).
- Answers an implicit question about the highlighted passage (*Yes, the
  dashboard is the interface…*).
- References the selection in third person (*In the context of the nvim-spider
  configuration you selected:*).
- Offers general knowledge the book omitted (*so I will provide their meanings
  based on general Neovim knowledge*).

### `[[My Note]]` — reader's own notes

Typical signals:

- First person (*I really appreciate…*, *I still get distracted…*, *I wonder
  whether…*).
- Reader synthesis (*It sounds like the three places are…*, *Ok so this is the
  answer to my question…*).
- Short personal tags (*Useful context*).
- Missing-text reconstruction (*Some text is missing in Readwise:*, *Missing
  text:*) — including code or `###` sub-headings the reader pasted in.

### Post-`---` segments (special case)

Import splits Readwise `notes` on `\n---\n`. The **first** segment is almost
always `[[My Note]]`. For the **second** segment:

| Second segment looks like… | Action |
| --- | --- |
| AI answer (signals above) | `[[AI Notes]]` child under the highlight |
| Book prose after a *Missing text* / *Some text is missing* note | **Promote** to a sibling `- >` blockquote at section level — not a note |
| Ambiguous | `[[My Note]]` |

Example (Ch. 5, `disabled.lua` highlight): segment 1 is `[[My Note]]` with the
`return { … }` code fence; segment 2 (*In Lua, a table is like…*) becomes a
sibling blockquote because it is book text, not an AI answer.

Example (Ch. 5, `vim.uv.cwd()` highlight): segment 1 → `[[My Note]]`; segment 2
(*The document hasn't explicitly defined…*) → `[[AI Notes]]`.

## Notes added later in Logseq

The user sometimes adds `[[My Note]]` or `[[AI Notes]]` blocks while reading
after import. When reformatting an existing chapter page:

- Preserve every labeled note and its nesting.
- Plain unlabeled children under a highlight get classified with the rules above.
- Never drop a note because it is not in the latest Readwise export.
