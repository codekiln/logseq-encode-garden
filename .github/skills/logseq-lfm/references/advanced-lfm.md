# Advanced LFM formatting

Baseline LFM (bullets, headings-as-bullets, TAB nesting, no blank lines, protected `tags::`, namespaces, no self-links, no ordered lists) lives in `logseq-core`. This file covers the finer points.

## Special Formatting
- **Bold:** `**bold text**`
- *Italic:* `*italic text*`
- `Inline code:` `` `code` ``
- Blockquotes: `> Quote`
- Code Blocks:
  ```markdown
  ~~~
  $> git describe --tags
  ~~~
  ```

## Bold and inline code (monospace)

- In **body LFM** (especially answers under `[[AI/Response]]`), do **not** wrap inline monospaced spans in bold by placing `**` immediately outside the backticks — avoid `**`:example`**` and avoid titles like `**Troubleshooting — **`:cmd`**` (nested `**` + backticks). Logseq's parser does not treat that combination as reliable Markdown.
- Prefer **labels or prose in bold**, with commands/options in plain backticks beside them: e.g. **Ex check:** `:set clipboard?` or **Run** `:checkhealth`.
- Avoid opening `**` before a troubleshooting lead-in if the same fragment immediately continues into `` `...` `` on the same line unless you have verified rendering; split the label from the command (command in backticks only).

<CORRECT_✅>
~~~markdown
- **Read the option:** run `:set clipboard?` (or `:echo &clipboard`).
- **Troubleshooting — no echo:** `:messages` after `:set clipboard?`.
~~~
</CORRECT_✅>

<INCORRECT_❌>
~~~markdown
- Run **`:set clipboard?`** to inspect the value.
- **Troubleshooting — **`:registers`** flashes:** …
~~~
</INCORRECT_❌>

## Fenced Code Blocks Rule

- When nesting fenced code blocks in markdown, avoid using triple-backticks inside another triple-backtick block.
- Use triple-backticks for the outer markdown block and triple-tilde (`~~~`) for inner code blocks.
- This prevents rendering issues and aligns with the CommonMark spec.

**Example:**

```markdown
- Here's an example of the code:
  ~~~
  $> git describe --tags
  ~~~
```

## Footnotes

- Footnotes in Logseq should use markdown footnote syntax such as `[^1]`
- Footnote definitions should appear in a `Footnotes` section when collected at the end of a page
- Footnote definitions should use URL-only style when citing sources: `[^1]: https://example.com`
- When multiple footnote references appear inline next to each other, always separate them with spaces
- Correct inline format: `[^4] [^5]`
- Incorrect inline format: `[^4][^5]`
- Do not concatenate adjacent footnote markers, because some renderers visually collapse them into misleading numbers such as `45` or `145`
- Ensure footnote definitions are nested properly under bullet points when used in LFM

## Page-level attributes (recap)

Page-level attributes / Logseq frontmatter:
- MUST occur as the first lines in the file before any unordered list item
- MUST use kebab-case
- Separate key and value with `:: `
- The `tags::` item specifically MUST NOT be modified, added, or removed under any circumstances. Other page-level attributes may be modified when explicitly instructed.
