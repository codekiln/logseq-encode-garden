---
name: logseq-pref
description: >-
  Load [[Logseq/Pref]] and linked pages for encode-wide garden preferences
  (page naming, namespaces, editorial defaults) before creating pages or entity
  types. Use when aligning new titles with [[Logseq/Pref/Page/Name]], refreshing
  prefs in-graph, or routing alongside logseq-entity for naming—not for per-type
  entity SOP (those stay on [[Logseq/Entity/<Type>]]).
targets: ["*"]
codexcli:
  short-description: Load Logseq/Pref hub for encode naming prefs before graph edits
---

# Logseq Pref

Use this skill when work touches **how** this encode garden titles pages and namespaces, independent of a single entity type.

## Default path

1. Open **`[[Logseq/Pref]]`** when the page exists.
2. Follow links to concrete preference pages—typically **`[[Logseq/Pref/Page/Name]]`** for singular Title Case segments and nested paths.
3. Do **not** invent prefs that are not on those pages; defer gaps to the human or to **`[[Logseq/Entity]]`** for entity-specific canon.

## Relationship to other skills

- **logseq-entity** covers registry, dedupe, instances, and **`[[Logseq/Entity/<Type>]]`** SOPs. Load **logseq-pref** first when naming **new** type pages or choosing canonical paths so prefs and registry stay aligned.

## References

- Encode registry (which entity paths exist): **`[[Logseq/Entity]]`**
- Alias strategy: **`[[Logseq/Frontmatter/alias]]`**
