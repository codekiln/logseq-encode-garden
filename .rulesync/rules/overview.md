---
root: true
targets:
  - '*'
description: 'Logseq Encode Garden - Instructions for AI'
globs:
  - '**/*'
---
# Logseq Encode Garden - Instructions for AI

This repository is a personal Logseq knowledge graph (not a software project): personal notes, research, and thoughts in Logseq's hierarchical, block-centric structure. Logseq is a privacy-first, open-source platform; each block inherits its parents' tags, and pages use a special flavor of Markdown (LFM). It is not a software project — no `progress.md` files; don't treat it like an app codebase.

## Key directories
- `pages/*.md` — all non-journal pages. Namespaced pages use triple underscores on disk: `[[Project/Tasks]]` ↔ `pages/Project___Tasks.md`. Page file names must be unique across the whole graph. Do not create real subfolders for namespaces.
- `journals/YYYY_MM_DD.md` — daily journal entries.
- `assets/` — images, PDFs, and attachments referenced via relative links.
- `logseq/` — graph configuration (usually don't edit).
- `tools/` — utility scripts (gitignored; separate repos).
- `.rulesync/**/*.md` — AI instruction sources, compiled by [rulesync](https://github.com/dyoshikawa/rulesync) into per-tool configs.

## Canonical sources (hard rule for agents)
- Edit **only** files under `.rulesync/` (rules, skills, commands, subagents, config, and `rulesync.jsonc`). Never hand-edit the generated outputs under `.claude/`, `.cursor/`, `.github/`, `.codex/` — treat them as read-only compiled output.
- If a tool's copy looks wrong, fix the matching `.rulesync/` source and run `rulesync generate` (or `npx rulesync generate`) from the repo root. Commit both the source change and the tracked generated files.

## Editing the graph
- Every page/journal edit follows the always-on `logseq-core` rule (protected `tags::`, LFM basics, naming, no-agent-taint, journal updates, block-ref safety).
- Absence of a `.md` file ≠ absence of a page: a `[[Namespace/Page]]` referenced anywhere exists logically. `grep` before concluding a page is missing; linking is complete without creating a file.

## Skills index (task → skill; bodies load on demand)
- LFM details (footnotes, naming rationale, file↔link table, logical-vs-disk) → **logseq-lfm**
- Convert pasted/standard Markdown to LFM → **logseq-convert-md-to-lfm**
- Tables in LFM → **logseq-table-formatter**
- Diataxis how-to / tutorial / reference / concept pages → **diataxis-docs**
- AI model mentions and model pages → **logseq-ai-model**
- Asset / image / PDF links → **logseq-asset-linker**
- YouTube transcript notes → **logseq-youtube-notes**
- Slide decks → **logseq-slides**
- Forum post import → **logseq-forum-post**
- Block IDs / `((uuid))` refs → **logseq-block-ids**
- Entities (dedup, create/update, type pages, journal record) → **logseq-entity**; person hubs → **logseq-person** command; garden naming prefs → **logseq-pref**
- Wikilink resolution / stub prevention → **logseq-link-hygiene**
- Flashcards / Keyshort cards → **logseq-flashcard**
- Questions (`/Q/` pages) → **logseq-question**
- Weekly page setup → **logseq-update-week** command
- Journal editorial formatting → **logseq-format-journal** command
- Git staging/commits → **git-conventions**; end-of-session checkout → **landing-the-plane**
- Rulesync usage / authoring skills → **rulesync**, **rulesync-create-skill**
