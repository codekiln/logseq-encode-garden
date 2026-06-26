# Logseq Entity Configuration

Repo-side support for the **logseq-entity** skill. **Per-type rules** (recognition, naming, dedup, frontmatter, page shape, blockers) live on **`[[Logseq/Entity]]`** and **`[[Logseq/Entity/<Type>]]`** in the active graph—**not** in this file.

## Resolution order

Agents read configuration in this order and stop relying on lower layers once the graph answers the question:

1. **`[[Logseq/Entity]]`** — shared, garden-agnostic conceptual model: terms, how instances are marked (`logseq-entity::`), and naming rules. It does **not** catalog the types; the set of `Logseq/Entity/<Type>` pages is that list.
2. **`[[Logseq/Entity/<Type>]]`** — entity definition for that entity (whatever titles appear under `Logseq/Entity/` in this garden). Each is itself marked `logseq-entity:: [[Logseq/Entity/Definition]]`; that meta page holds the shape of a type page, and its backlinks are the queryable list of types.
3. **`[[Logseq/Frontmatter]]`** — shared page-level attribute conventions (`tags::`, `alias::`, `see-also::`, `via::`, `date-created::`, etc.).
4. **`[[Logseq/Pref]]`** (and children such as **`[[Logseq/Pref/Page/Name]]`**) — optional encode-wide preferences when present (page naming, editorial defaults).
5. **This file** — only when those pages are missing, incomplete, or the workspace has no graph copy yet.

## Garden intent (shared)

- Personal Logseq knowledge garden; page names follow gardening practice, not external site layout alone.
- Prefer short stable page titles when a topic will grow sub-namespaces; use `alias::` for contextual paths.
- Keep graph entity definition pages self-contained. Do not write Rulesync, skill, slash-command, generated-file, repo-path, or agent-workflow references into Logseq pages.
- Keep actual `[[Page]]` links clickable in graph pages; do not put them inside backticks.
- New entity type page names should be singular where natural; **multi-word types** use **nested Title Case namespace segments** under `Logseq/Entity/` (for example **`Software/Project`**); plural or contextual surfaces belong in `alias::`. The set of **`Logseq/Entity/<Type>`** pages is authoritative for which types exist.
- **Never** modify, add, or remove **`tags::`** on existing pages unless a human explicitly overrides garden rules.

## When the graph has no entity pages yet

- Inspect existing `pages/` and journals for repeated patterns (namespaces, frontmatter, hub shapes).
- Propose or create **`[[Logseq/Entity]]`**, **`[[Logseq/Entity/<Type>]]`**, and **`[[Logseq/Frontmatter]]`** pages the author wants—**do not** recreate long per-type catalogs in this file.
- If conventions cannot be inferred safely, ask the human before bulk-creating pages.

## Reporting contract

After entity work from source material (e.g. a journal), report:

- entities found
- entities already present
- entities created
- entities inferred aggressively (call these out)
- blocked cases that need a human decision

## Notes for other gardens

Copy patterns from this repo’s skill under **`.rulesync/skills/logseq-entity/`**; keep **this** file short and graph-first. Type-specific detail belongs in the graph’s **`Logseq/Entity/...`** pages for that garden.
