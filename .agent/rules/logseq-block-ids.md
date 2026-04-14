---
trigger: always_on
---
# Logseq Block IDs: Permanent Graph-Wide Anchors

## What Block IDs Are

A block ID is an `id::` property that Logseq assigns to a block to uniquely identify it across the entire graph:

```
- This is a block with content
  id:: 699c68e4-078b-4e13-8559-2257d5a1ea27
```

Block IDs are UUIDs. They serve as stable anchors that other blocks can reference using the `((uuid))` syntax:

```
- See the note I wrote earlier: ((699c68e4-078b-4e13-8559-2257d5a1ea27))
```

Logseq renders `((uuid))` inline as an embedded copy of the referenced block.

## Critical Rules for Agents

### 1. Check for References Before Removing an `id::`

When editing a block that has an `id::` property, check whether any `((uuid))` references to it exist in the graph before removing it. If references exist, removing the `id::` would orphan them. If no references are found, removal is safe.

Wrong:
```
Before: - TODO Fix the login bug
          id:: abc123
          :LOGBOOK: ...

After:  - TODO Fix the login bug    ← id:: removed — breaks all ((abc123)) refs
```

Correct:
```
After:  - TODO Fix the login bug
          id:: abc123               ← id:: preserved
          :LOGBOOK: ...
```

### 2. The `id::` Must Travel With Its Block

When moving or copying a block to a new page or location, the `id::` line must move with it. Block refs resolve **graph-wide** — moving a block to a different file does not break existing `((uuid))` references, as long as the `id::` stays attached to the block.

Wrong:
```
# Moving a block to a new page
New page: - TODO Fix the login bug    ← id:: left behind or dropped
Old page: id:: abc123                 ← id:: orphaned or deleted
```

Correct:
```
New page: - TODO Fix the login bug
            id:: abc123              ← id:: travels with the block
Old page: (block removed entirely)
```

### 3. Adding New Block IDs

Logseq assigns `id::` values automatically when a user copies a block reference (right-click → Copy block ref). Agents may also add a new `id::` to a block that doesn't have one — for example, when creating a new `((ref))` to that block. Generate a random UUID v4 for this purpose.

Before removing an existing `id::`, search the graph for any `((uuid))` reference to it. If references exist, the `id::` must be preserved. If no references are found, removing the `id::` is safe.

### 4. Re-indexing After External File Edits

When files containing `id::` blocks are edited outside Logseq (e.g., via an agent or text editor), Logseq may need a moment to re-index before `((refs))` render correctly in the UI. This is **not data loss** — it is a normal re-indexing delay. The references will resolve once Logseq has scanned the updated files.

## Summary

| Situation | What to do |
|-----------|------------|
| Editing a block with `id::` | Keep it; only remove if no `((uuid))` refs exist in the graph |
| Moving a block to another page | Move the `id::` line with the block |
| Copying a block | Copy the `id::` line along with the content |
| Block has no `id::` and you need to ref it | Add a new UUID v4 as `id::` |
| `((refs))` not rendering after file edit | Wait for Logseq to re-index; not data loss |
