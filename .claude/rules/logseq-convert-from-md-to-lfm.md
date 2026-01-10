---
paths: '{journals,pages}/*.md'
---
# Converting from Standard Markdown to Logseq Flavored Markdown (LFM)

This guide provides a checklist for exceptional tasks that may require specific attention when converting standard markdown (particularly from ChatGPT or similar sources) to Logseq Flavored Markdown (LFM). For standard LFM rules, see the logseq-flavored-markdown rule.

## Conversion Checklist

### 1. Links Requiring Special Attention
- [ ] For any link without descriptive text (e.g., `[github.com](url)`), visit the destination to get its actual title/content
- [ ] Replace generic link text with meaningful descriptions from the destination
- [ ] Example: Convert `[github.com](https://github.com/pytest-dev/pytest/commit/9335a0b)` to `[Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b)`

### 2. Code Block Formatting
- [ ] Ensure code blocks are properly nested inside bullet points (not as separate bullet points)
- [ ] Example of correct format:
  ```
  - ~~~python
    your code here
    ~~~
  ```
  Not:
  ```
  - ~~~python
  - your code here
  - ~~~
  ```

### 3. Horizontal Rules
- [ ] Remove any lines with only horizontal separators (`---`) as they're not needed in LFM
- [ ] Use proper heading hierarchy and indentation to indicate section breaks instead

### 4. Tables
- [ ] Convert any markdown tables with more than two columns to bullet points with label-value pairs. If it has two columns, it's okay to keep it as a table, but it must be appropriately put inside of a markdown unordered list item (`-`). 
- [ ] Example:
<EXAMPLE_FROM>
| Label | Value |
|-------|-------|
| A     | B     |
</EXAMPLE_FROM>
<EXAMPLE_TO>
  - A: B
<EXAMPLE_TO>
or
<EXAMPLE_TO>
- | Label | Value |
  |-------|-------|
  | A     | B     |
</EXAMPLE_TO>

### 5. Heading Nesting Levels
- [ ] Ensure headings use the correct level for their indentation:
  - `#` (H1) only at root level (no indent)
  - `##` (H2) only at first indent (one TAB)
  - `###` (H3) only at second indent (two TABs)
- [ ] Example:
  ```
  - # Main Topic
    - ## Subtopic
      - ### Detail
  ```

### 6. Footnotes
- [ ] Convert footnote definitions to proper Logseq format
- [ ] Change section title from "References" to "Footnotes" 
- [ ] Format footnotes as `[^1]: url` (not `[^1]: [descriptive text](url)`)
- [ ] Remove descriptive link text from footnote definitions - Logseq footnotes should contain URLs directly
- [ ] Ensure footnotes are properly nested under bullet points
- [ ] Reference: See [Logseq___How To___Create a Markdown Footnote.md](../pages/Logseq___How To___Create a Markdown Footnote.md) for details
- [ ] Example conversion:
  ```
  FROM: [^1]: [Free tokens extended through April 30, 2025](https://example.com)
  TO:   [^1]: https://example.com
  ```

## Common Pitfalls That Required Correction

1. Code blocks being treated as separate bullet points instead of being nested inside them
2. Links using generic text like "github.com" instead of descriptive content from the destination
3. Horizontal rules being used for section breaks
4. Tables being left in markdown format instead of being converted to bullet points
5. Headings not matching their indentation level (e.g., using `##` at root level or `#` at indented level)
6. Footnotes formatted with descriptive link text instead of direct URLs (e.g., `[^1]: [text](url)` instead of `[^1]: url`)

## Example of Required Changes

From ChatGPT-style markdown:
<EXAMPLE_INPUT>
[github.com](https://github.com/pytest-dev/pytest/commit/9335a0b)

---

| Warning | Source |
|---------|--------|
| ast.Str | pytest |

```python
code here
```
</EXAMPLE_INPUT>

To LFM:
<EXAMPLE_OUTPUT>
- [Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b)
- ## Warning Details
	- Warning: ast.Str
	- Source: pytest
- ~~~
  code here
  ~~~
</EXAMPLE_OUTPUT>
or
<EXAMPLE_OUTPUT>
- [Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b)
- ## Warning Details
	- | Warning | Source |
	  |---------|--------|
      | ast.Str | pytest |
- ~~~
  code here
  ~~~
</EXAMPLE_OUTPUT>

## Related Rules
- logseq-flavored-markdown rule - Standard LFM rules
- logseq-naming-conventions rule - Tag and namespace conventions
- logseq-overview rule - General Logseq concepts
