---
name: diataxis-docs
description: >-
  Author a Diataxis-style documentation page in the Logseq garden — tutorial
  (learning), how-to (task), reference (information), or explanation/concept
  (understanding). Use when the user asks to create or restructure a How To,
  Tutorial, Reference, or Concept/Explanation page, or asks which Diataxis type
  fits. Adds the right `[[Diataxis/...]]` tag and namespace. Do not use for
  non-doc pages or to edit existing protected `tags::`.
targets: ["*"]
codexcli:
  short-description: Author Diataxis tutorial/how-to/reference/explanation pages
---

# Diataxis docs in the garden

Pick the quadrant by the user's need, then follow that quadrant's reference.

## The compass

| Content… | serves the user's… | → type | namespace | tag |
|----------|--------------------|--------|-----------|-----|
| informs **action** | application of skill | **how-to** | `Topic/.../How To/Task` | `[[Diataxis/How To]]` |
| guides **learning** | acquisition of skill | **tutorial** | `Topic/.../Tutorial/Goal` | `[[Diataxis/Tutorial]]` |
| informs **cognition** | theoretical knowledge | **reference** | `Topic/.../Ref/Subject` | `[[Diataxis/Reference]]` |
| explains **why** | understanding | **explanation/concept** | per type page | `[[Diataxis/Concept]]` / `[[Diataxis/Explanation]]` |

Then read the matching reference:
- How-to → [references/how-to.md](./references/how-to.md)
- Tutorial → [references/tutorial.md](./references/tutorial.md)
- Reference → [references/reference.md](./references/reference.md)
- Explanation/Concept → [references/explanation.md](./references/explanation.md)

## Shared rules (all quadrants)

- **LFM**: bullets, headings as bullets (`- # Heading`), TAB nesting, no blank lines (see `logseq-core`).
- **Tags**: ADD the quadrant's `[[Diataxis/...]]` tag to new doc pages; **never remove or edit existing `tags::`** (protected).
- **Namespace ↔ file**: `[[A/B/How To/X]]` → `pages/A___B___How To___X.md` (triple underscore).
- **Related pages**: prefer `see-also::` in frontmatter over a `## Related` list of internal links, unless the author asks.
- Use `logseq-link-hygiene` before adding `[[...]]`; do not invent pages.
