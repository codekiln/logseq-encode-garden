# `{{cards …}}` and Logseq’s query languages

Distilled from upstream **logseq-docs** (`pages/Flashcards.md`, `pages/Queries.md`, `pages/Advanced Queries.md`). Official hub: [Flashcards](https://docs.logseq.com/#/page/flashcards), [Queries](https://docs.logseq.com/#/page/queries), [Advanced Queries](https://docs.logseq.com/#/page/advanced%20queries).

## Which language drives card lookup?

- The **Cards** command (`/cards`) inserts a **`{{cards …}}`** macro. Logseq documents this as a **query that returns cards matching criteria**, in the same family as **simple queries** (`{{query …}}`): review subsets of cards via the **Queries** (simple query) expression language — not the full advanced-query map by itself.
- **Simple queries** (`{{query expr}}` / `{{cards expr}}`): parenthesized **filters** and **`and` / `or` / `not`**, page links as `[[Page title]]`, created with `/query` or `/cards` as appropriate.
- **Advanced queries** (`#+BEGIN_QUERY` … `{:title … :query …}`): **Datalog** over Logseq’s **Datascript** graph. The `:query` value can be either a **Datascript query** *or*, in supported cases, a **simple query expression** embedded inside the map (see “Advanced + simple” below).

For this encode garden’s workflows, **`{{cards [[Some/Page]]}}`** and ancestry on parent blocks are what make scoped decks work; see [create-flashcard-page.md](./create-flashcard-page.md) and [keyshort-audit-and-update.md](./keyshort-audit-and-update.md).

## Simple query shape (shared by `{{query}}` and `{{cards}}`)

- **Combinators** (wrap any filters):
  - `(and [[page 1]] [[page 2]])`
  - `(or [[page 1]] [[page 2]])`
  - `(not [[page 1]] [[page 2]])` — docs show `not` taking multiple inner filters in the example form; combine with `and` for “has A but not B”.
- **Bare page link** in `{{query [[tag1]]}}` means blocks **containing** that page reference. Same idea applies when you think about what blocks a card expression would consider **tagged** or linked.

### Documented `{{cards}}` examples (Flashcards)

- All cards under / related to a page: `{{cards [[Logseq]]}}`
- All cards **except** those matching a tag: `{{cards (not [[Logseq]])}}`

### Block vs page filters (important)

From **Queries** docs: most filters apply to **blocks**. Some apply only to **pages**. **Do not mix** page-only filters with block filters in one query:

- **Page-only** (must not mix with block filters): `page`, `page-property`, `page-tags`, `all-page-tags`

### Block-oriented filters (Queries reference)

| Filter | Role (high level) |
|--------|-------------------|
| `(between start end)` | Journal blocks in a date range; supports `today` / `yesterday` / `tomorrow` / `now` and offsets like `+7d`, `-2w` |
| `(page "term/alias")` | Page-level: match page |
| `(property name value)` | Match blocks/pages with property values (pages or `#tags` in values per docs) |
| `(task now)` / `(task now later)` … | TODO markers |
| `(priority a)` … | Priorities |
| `(page-property key "value")` | Page-level property |
| `(page-tags tag)` | Pages with tag |
| `(all-page-tags)` | Page tags listing |
| `(sort-by property-name order)` | Default sort; `order` is `desc` or `asc` (omit → `desc`); `created-at` / `updated-at` page-only |

### Typical composition patterns

- Both tags: `(and [[tag1]] [[tag2]])`
- Either tag: `(or [[tag1]] [[tag2]])`
- Tag2 but not tag1: `(and [[tag2]] (not [[tag1]]))`

These patterns are the same whether the macro is `query` or `cards`; **cards** additionally requires blocks to behave as **cards** (`#card` / `[[card]]` in stock Logseq — this garden standardizes on **`#card`** only).

## Advanced queries (when simple expressions are not enough)

- Shape is a **map**: `:title`, `:query`, optional `:inputs`, `:view`, `:result-transform`, `:collapsed?`, `:group-by-page?`, `:remove-block-children?`, `:rules`, etc.
- `:query` is **either** a Datascript **`:find` / `:where`** query **or** a **simple query** expression (documented example: “DOING tasks with priority A” as `(and (todo DOING) (priority A))`).
- **Tips** (from Advanced Queries docs, for Datalog paths):
  - `?b` / `?p` are conventional symbols for blocks and pages.
  - **Page names** in the DB are **lower case** (sanitized).
  - Many simple-query operators are available as **`:rules`** for reuse inside Datalog.

Beginner links from upstream docs: [Learn Datalog Today](https://www.learndatalogtoday.org/), Datascript / Datomic query references linked from the Advanced Queries page.

## Practical notes for agents (encode garden)

1. **Scope deck**: A page like `[[vim/Keyshort]]` that embeds `{{cards [[vim/Keyshort]]}}` only picks up `#card` blocks whose **ancestors** include that link (and siblings’ inheritance rules follow Logseq’s block tree). Fixing ancestry is an **editorial/graph** task, not a query-syntax change — see Keyshort references.
2. **Negation**: `(not [[X]])` is documented for cards; use **`(and … (not …))`** when you need “must match A and must not match B”.
3. **Escalation**: If the user needs card sets that **simple expressions cannot express**, consider an **advanced query** whose `:query` is still a simple expression, or full Datalog for block pulls — then map results to review UX separately (cards UI vs query table differ in product).

## Source map (local clone)

If `logseq-docs` is cloned, primary pages are:

- `pages/Flashcards.md` — `/cards`, `{{cards …}}`, link to Queries
- `pages/Queries.md` — simple query operators and examples
- `pages/Advanced Queries.md` — map shape, `:inputs`, simple query inside `:query`, Datalog tips
