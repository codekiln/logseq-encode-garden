---
name: logseq-block-ids
description: >-
  Work safely with Logseq block IDs (`id::` properties) and `((uuid))` block
  references when moving, copying, or removing blocks across graph pages. Use
  when relocating a block that has an id::, creating a new ((ref)) to a block,
  deciding whether an id:: can be removed, or diagnosing refs that won't render.
  Baseline safety (never backtick a live ref/link; keep id:: with its block) is
  in logseq-core; this skill has the full move/copy/reindex procedures.
---
# Logseq block IDs

`id::` is a UUID Logseq assigns to a block as a stable, graph-wide anchor that other blocks embed via `((uuid))`.

## Core safety (also in logseq-core)

- Never wrap a live `((uuid))` or `[[Page]]` in backticks — that renders it as literal text instead of embedding/linking.
- Keep the `id::` line attached to its block when moving/copying. Refs resolve graph-wide, so moving a block to another file does not break `((uuid))` refs as long as `id::` travels with it.
- Before removing an `id::`, grep the graph for `((that-uuid))`; if refs exist, preserve it.

## When to read the reference

Read [references/block-id-operations.md](./references/block-id-operations.md) for: the move/copy worked examples, adding a new UUID v4 to a block you want to reference, the re-indexing-delay (not data loss) note, and the full summary table of situations → actions.
