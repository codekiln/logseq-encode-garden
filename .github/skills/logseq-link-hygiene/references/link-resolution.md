# Link Resolution

## Invariant

A Logseq wikilink is a graph edge and a page-creation affordance. Do not create one casually.

Before adding a new `[[wikilink]]`, classify it as:

- `canonical` - the exact page already exists
- `alias-match` - an existing page declares this link text as an alias
- `normalized-match` - one clear page matches after normalization
- `intentional-new` - the target page is created in the same workflow or explicitly requested
- `date-link` - a garden date link such as `[[2026/05/04]]`
- `ambiguous` - multiple existing pages could be intended
- `unresolved` - no existing page matches and no new page is intended

Only `canonical`, `alias-match`, `normalized-match`, `date-link`, and `intentional-new` should remain wikilinks without further explanation.

## Resolution order

1. Exact title: convert disk filenames under `pages/` from `___` to `/` and decode URL escapes when obvious.
2. Alias: parse `alias::` frontmatter values. Treat comma-separated `[[Page]]` values and bare alias strings as alternate names for the containing page.
3. Normalized title: lower case, remove punctuation, collapse whitespace, and compare.
4. Namespace variant: compare slash and space variants, including forms like `12 factor app` and `12factor/app`.
5. Body evidence: when still uncertain, search for the phrase and source context with `rg`.
6. Structural exceptions: date links in the garden's accepted shape are intentionally link-like even when the journal page does not exist yet.

## Replacement policy

- One clear match: replace the new link with the canonical page link.
- Multiple matches: do not choose silently; report candidates.
- No match: leave as plain text unless the user asked for a placeholder or the target page is created now.
- External reference only: use a Markdown URL link instead of a wikilink when the target is not meant to become a graph page.

## Examples

- Proposed `[[12 factor app]]`; existing page `[[12factor/app]]`: use `[[12factor/app]]`.
- Proposed `[[People/Jane Doe]]`; existing `[[Person/Jane Doe]]`: use the existing person page, unless graph rules explicitly define a `People/` namespace.
- Proposed `[[semantic versioning]]`; existing alias on `[[Semantic Versioning]]`: use the canonical page.
- Proposed `[[some memorable phrase]]` with no existing page and no creation request: leave `some memorable phrase` as plain text.

## Shell fallback

When the script cannot run:

```sh
rg -n "alias::|\\[\\[12 factor app\\]\\]|12 factor app|12factor/app" pages journals
rg --files pages | rg -i "12.*factor|factor.*app"
```

Adapt the query terms for the link being resolved.
