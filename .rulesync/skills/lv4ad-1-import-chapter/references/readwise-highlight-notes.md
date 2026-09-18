# Readwise highlight notes (Reader API)

`reader-get-document-highlights --document-id <id> --json` returns one object per
highlight:

```json
{
  "id": "01m2f45ryywpgdrdzh6bvsbwqd",
  "content": "Others, such as flash.nvim and which-key provide…",
  "tags": [],
  "notes": "The document identifies flash.nvim as a pre-installed plugin…"
}
```

There is **no separate field** for Readwise's built-in AI answers — user notes,
AI replies, and (sometimes) recovered book text all land in the single `notes`
string.

## How notes combine

| Pattern | `notes` shape | Example (Ch. 5) |
| --- | --- | --- |
| User note only | Plain prose | *Ok so this is the answer to my question…* |
| AI answer only | Plain prose | *The document identifies flash.nvim…* |
| User + AI | User text, then `\n---\n`, then AI text | *Still getting to know lua…* / *The document hasn't explicitly defined…* |
| User reconstruction + stray book text | User text (often `Missing text:` or `Some text is missing in Readwise:`), then `\n---\n`, then book prose | `return { … }` block / *In Lua, a table is like…* |

The `---` divider is Readwise's convention when a highlight carries **both** a
user note and a follow-on block (usually an AI answer). In reconstruction notes
the post-`---` block can instead be **book text** that Readwise failed to
capture as its own highlight.

## Import rules (lv4ad-1)

1. Always pull highlights with
   `readwise reader-get-document-highlights --document-id <id> --json`.
   Resolve the document id from the chapter's `readwise-link::` permalink
   (`…/read/<id>`) or via `reader-search-documents`.
2. One flat bullet per highlight: `- > <content>` (exact `content` field).
3. When `notes` is non-null, add **one plain child bullet per segment**:
   - Split on `\n---\n` (trim whitespace on each segment).
   - Preserve segment text verbatim — no `[[My Note]]`, `[[AI Notes]]`, or
     italics yet.
   - Order: first segment first child, second segment second child, etc.
4. Notes added later in Logseq (not in the Readwise export) are out of scope
   for import — they appear when the user edits the page manually or re-runs
   a partial import.

Classification into `[[My Note]]` vs `[[AI Notes]]`, and promoting recovered
book text to blockquotes, happens in **lv4ad-2-format-chapter**.
