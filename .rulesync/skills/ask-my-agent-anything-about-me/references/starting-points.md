# AMA starting points

Where to look first when answering questions about the owner. These are entry
points, not the whole graph — follow links outward from them.

## The owner's curated self-description (`My/*`)

The `[[My]]` namespace is the owner's own context portfolio, written for AI agents
and organized by progressive disclosure (descend into longer namespaces for more
detail). Start here:

- `[[My]]` — what the namespace is and how it is organized.
- `[[Person/codekiln]]` — the owner's person hub.
- `[[My/AI]]` and `[[My/AI/Rule]]` — how the owner thinks about and works with AI.
- `[[My/Pref/*]]` — concrete preferences (e.g. `My/Pref/Dev/*`, `My/Pref/Writing/*`).
- `[[My/Principle/*]]` — the owner's stated principles (e.g. `My/Principle/Dispel
  Ambiguity`, `My/Principle/Simplify`, `My/Principle/Declarative over Imperative`).
- `[[My/Repo]]` orientation, when present — how the owner's repos are catalogued.

Discover the current set quickly:

```bash
ls pages/My___*.md
```

`.../Discussion` pages explain the "why" behind the items immediately above them
in the namespace — read them when a visitor asks "why" the owner holds a view.

## What the owner is thinking about lately

- `journals/` (`YYYY_MM_DD.md`) — daily entries: questions, reading, and in-progress
  thinking. The most recent files show current interests; `[[Filed]]` / `[[Updated]]`
  sections list the pages touched each day.

## Topics and people

- `pages/` is namespaced with triple underscores on disk (`Topic___Sub.md` ↔
  `[[Topic/Sub]]`). Search broadly:

```bash
grep -rl "search term" pages/ journals/
```

- `[[Person/*]]` pages capture people the owner finds notable; `[[Book/*]]`,
  `[[AI/*]]`, and similar namespaces capture topics and references.

## Search before concluding

Linking is complete without a file, so a referenced page can exist with no `.md`.
Always `grep` across `pages/` and `journals/` before saying the garden is silent.
