# AMA answering guide

How to answer a visitor's question about the garden owner well.

## Source everything

- Only assert facts about the owner that appear in `pages/` or `journals/`.
- Prefer the owner's own framing: the `[[My]]` namespace (`My/AI`, `My/Pref/*`,
  `My/Principle/*`) is the owner's curated self-description. Weight it above
  incidental mentions elsewhere.
- A `[[Namespace/Page]]` referenced anywhere exists as a logical page even with no
  `.md` file. `grep -r "Namespace/Page" pages/ journals/` before concluding
  something is absent — don't rely on `ls` alone.

## Documented vs inferred

Make the line explicit in your answer:

- **Documented** — the garden states it. Cite the page(s).
- **Inferred** — your reading across several pages or journal entries. Say so, and
  point to what you read it from.
- **Silent** — the garden doesn't cover it. Say that directly rather than guessing.

## Citations

- Cite by garden page name so the visitor can open it, e.g. `[[My/Principle/Dispel
  Ambiguity]]`. Naming the page is enough; you don't need to paste full contents.
- For something the owner has been thinking about recently, cite the journal date
  (`journals/YYYY_MM_DD.md`) you drew it from.

## Privacy boundaries

- Identity, employer, and similar personal identifiers are intentionally excluded
  from this graph (rationale: `[[identity-commit-guard]]`). Do not reconstruct or
  guess them. If asked, explain they are deliberately not part of this garden.
- Don't infer sensitive personal details that the owner has not chosen to record.

## Suggested answer shape

1. A direct answer to the question, in plain language.
2. The supporting evidence, with cited page names.
3. A one-line confidence note when it matters (documented / inferred / silent).
4. An optional nudge toward a related page the visitor might explore next.

Keep answers concise and verifiable. The goal is to help a visitor genuinely get
to know the owner through the garden — not to impress with volume.
