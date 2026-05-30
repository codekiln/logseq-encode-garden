# `date-created::` frontmatter

The `date-created::` Logseq frontmatter property records **when the entity the page describes was created or published**, not when the page was added to the knowledge garden.

## Meaning
- **Entity** = the thing the page is about: a blog post, article, essay, book, piece of software, video, event, or other dated work.
- **date-created** = publication date, release date, or creation date of that entity.

## When to Set
- When creating or editing a page that represents a dated entity, set `date-created::` to that entity's date.
- Use a format consistent with the rest of the garden (e.g. `[[YY/MM]]`, `[[YYYY/MM/DD Day]]`, or `[[YYYY/MM]]` as appropriate).
- Do **not** use today's date (or the import date) unless the entity itself was created/published on that date.

## Examples
- Blog post published May 2021 → `date-created:: [[21/05]]` (or `[[2021/05]]` if that is the project convention).
- Book published in 2023 → `date-created:: [[2023]]` or `[[23]]` as appropriate.
- Article published 2026-02-10 → `date-created:: [[2026/02/10]]` or `[[26/02/10]]`.

## What Not to Do
- Do **not** set `date-created::` to the date you added or imported the page when the entity's actual creation/publication date is known or discoverable.
