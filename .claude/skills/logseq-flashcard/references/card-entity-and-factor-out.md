# Card entity pages and factor-out workflow

Use when a user asks to create a first-class flashcard/card page or factor cards out of an existing content page. Does not apply to Keyshort pages — see "When NOT to factor out" below.

## Authority

- Load `[[Logseq/Entity]]` and `[[Logseq/Entity/Card]]` before editing graph pages.
- New first-class card pages use `logseq-entity:: [[Logseq/Entity/Card]]`.
- New review prompts use `[[Card]]` as the Logseq card marker.
- Legacy `#card`, `[[card]]`, and inline card blocks are valid source material. Preserve them unless the task is to migrate or factor them out.

## Naming

- Page title shape: `[[Source/Page/Short Card Title]]`.
- File shape: `pages/Source___Page___Short Card Title.md`.
- The deprecated shape `[[Source/Page/Card/Short Card Title]]` (with an explicit `Card` namespace segment) still exists in the garden but is unmigrated; do not create new pages with it.
- Dedup before creating: exact title match, normalized prompt text in existing pages, then matching legacy inline card blocks.

## When NOT to factor out

- **Keyshort pages** (`Scope/Keyshort/Action`) are already card entities. They carry their `[[Card]]` blocks inline. Do not create a companion card page for a Keyshort page.

## Page shape

Use LFM: bullets for body lines, tab indentation, no blank body lines.

~~~markdown
logseq-entity:: [[Logseq/Entity/Card]]
- # Short Card Title
	- [[Scope]] [[Source/Page]]
		- **Prompt text?** [[Card]]
			- Answer bullet
			- Another answer bullet
~~~

- The ancestry parent block should include enough source/scope links for scoped `{{cards [[...]]}}` decks to pick up the card.
- Do not self-link the current card page in its own body.
- `tags::` is protected per `logseq-core`; do not alter it on existing pages.

## Factor-out workflow

1. Identify the smallest reviewable inline card block: prompt plus answer children.
2. Choose the target page as `[[Source/Page/Short Card Title]]`.
3. Create the card page with `logseq-entity:: [[Logseq/Entity/Card]]`, an H1, source/scope ancestry links, and a `[[Card]]` prompt block.
4. Replace the original inline card block with a page embed:

~~~markdown
- {{embed [[Source/Page/Short Card Title]]}}
~~~

5. Update today's journal per `journal-updates`: new card pages under `[[Filed]]`, existing source pages under `[[Updated]]` unless the source page is also new today.

## Example

Source page `[[mise/Architecture]]` with an inline card under `## System Overview` factors to `[[mise/Architecture/Jobs to be Done]]`; the original block becomes `{{embed [[mise/Architecture/Jobs to be Done]]}}`.

Note: the existing page `[[mise/Architecture/Card/Jobs to be Done]]` uses the deprecated `/Card/` shape and has not yet been migrated.
