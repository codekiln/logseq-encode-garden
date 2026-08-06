# Validation Checklist

Run these checks before committing an imported Deep Research report.

## Citation Checks

- No Deep Research glyph markers remain:
  ```bash
  rg -n '|filecite|turn[0-9]+(search|view|file)' pages/<report>.md
  ```
- Every inline `[^n]` has exactly one definition.
- Every footnote definition is URL-only:
  ```markdown
  - [^1]: https://example.com
  ```
- Adjacent footnotes are separated by spaces.
- Duplicate URLs are consolidated to the lowest footnote number.

## LFM Checks

- No blank lines:
  ```bash
  awk 'length($0)==0 { print FILENAME ":" NR }' pages/<report>.md journals/YYYY_MM_DD.md
  ```
- No raw top-level Markdown tables or fences:
  ```bash
  rg -n '^```|^\|' pages/<report>.md
  ```
- `git diff --check` passes for changed files.

## Link Checks

- Run link hygiene on the report and journal:
  ```bash
  nbb-logseq .rulesync/skills/logseq-link-hygiene/scripts/resolve-wikilinks.cljs --changed pages/<report>.md journals/YYYY_MM_DD.md
  ```
- Known journal conventions like `[[Filed]]` and `[[Updated]]` may report as
  unresolved or alias matches. New topical links should be canonical,
  alias-matched, or intentionally created in the same workflow.
