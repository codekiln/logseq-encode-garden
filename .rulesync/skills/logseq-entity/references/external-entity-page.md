# External entity pages

Many pages in this graph act as local proxy pages for internet pages, entities, projects, posts, documentation, and other external resources.

## Canonical URL placement

When creating a page whose main subject has a canonical external URL, prefer one Markdown H1 link as the first body block after any page-level frontmatter:

~~~markdown
- # [Entity Name](https://example.com/)
~~~

This H1 link is the page's primary external pointer. Do not add the same URL again as `source::`, `url::`, a separate "Open..." link, an embed, or a macro unless the user explicitly asks for that additional representation.

If existing page conventions for a specific entity type clearly use a different pattern, follow the local convention and still avoid duplicate representations of the same URL.

## No duplicate representations

Do not repeat the same URL, title, or entity fact in multiple blocks on a new page. Before finishing, scan the added page for duplicate representations of:
- the canonical URL
- the page title
- the external entity name
- the same short description
- the same source citation

Keep the single representation that best matches the graph's existing convention. Delete the redundant ones.

## Logseq macros

Do not invent Logseq macros. Only add a `{{...}}` macro when the macro name is already used in this graph or the user explicitly requests it. Known examples already present include `{{embed ...}}`, `{{video ...}}`, and `{{youtube-timestamp ...}}`. Do not add `{{iframe ...}}`; it is not an established macro in this graph and it duplicates a normal URL link.

## Examples

Bad:
~~~markdown
source:: https://example.com/roadmap
- # Entity Roadmap
	- [Open roadmap](https://example.com/roadmap)
	- {{iframe https://example.com/roadmap}}
~~~

Better:
~~~markdown
- # [Entity Roadmap](https://example.com/roadmap)
~~~
