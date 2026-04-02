# Create a new Logseq flashcard page (general)

Use when the target is **not** a straight Keyshort create (for that, follow command `logseq-create-shortcut`), or when the user gives a **full page title** like `[[vim/Keyshort/Inspect/Setting Value]]` and source prose to turn into a card.

## Guardrails

- **LFM**: bullets for every line (including headings `- #`), TAB indentation, **no blank lines** between blocks.
- **Never** add, remove, or change `tags::` frontmatter on existing pages.
- **No self-link**: do not put `[[Current/Page/Title]]` in the body of that same page.
- **Dedup**: search `pages/` for an existing file or near-duplicate before creating.

## File and link mapping

- Page title `[[A/B/C]]` → file `pages/A___B___C.md`.
- Links in content use **slashes**: `[[A/B/C]]`, never `A___B___C` inside `[[...]]`.

## Page shape for `{{cards ...}}` inheritance

1. **Root parent block** — include enough namespace links so cards roll up to the intended `{{cards [[Root]]}}` query on the scope page (e.g. `pages/vim___Keyshort.md` uses `{{cards [[vim/Keyshort]] }}`).
   - Include the **full chain** from `[[Keyshort]]` (when applicable) through each namespace segment down to the page’s parent.
   - Example (vim nested under Keyshort/Inspect):

~~~markdown
- [[Keyshort]] [[vim/Keyshort]] [[vim/Keyshort/Inspect]]
	- **Card prompt text here** #card
~~~

2. **Card line** — one bullet with `#card`. Put the **SRS cue** in bold (question or recall hook); keep it short.

3. **Answer bullets** — children of the card line: shortcuts, definitions, contrasts, examples. Reformulate prose into scannable bullets.

4. **SRS properties** (optional) — as child properties of the `#card` block, aligned with sibling cards in the same graph, for example:

~~~text
  card-last-interval:: -1
  card-repeats:: 1
  card-ease-factor:: 2.5
  card-next-schedule:: ...
  card-last-reviewed:: ...
  card-last-score:: ...
~~~

Copy defaults from a recent similar card in the same scope if the user wants consistency; otherwise omit and let Logseq assign on first review.

5. **Typography** — prefer ASCII `'` and `"` in new content unless the garden already uses typographic quotes on that page.

## Journal

Per rule `journal-updates`: add the page link under **`[[Filed]]`** (new page) or **`[[Updated]]`** (edit) in today’s `journals/YYYY_MM_DD.md` — default is **link only** under that heading; optional one short child bullet for context if it helps the day’s narrative.

## Keyshort-only shortcut

If the user is creating `[[<Scope>/Keyshort/...]]` with shortcut + description, use command **`logseq-create-shortcut`** instead of re-deriving those conventions here.
