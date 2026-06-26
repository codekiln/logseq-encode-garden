---
name: logseq-link-hygiene
description: >-
  Check, resolve, and normalize Logseq wikilinks before or after editing graph
  pages. Use when adding links, importing notes, creating pages, reviewing
  unresolved references, preventing accidental stub pages, or replacing newly
  invented wikilinks with existing pages or aliases. Applies to all
  Logseq graph work, not only entity pages.
targets: ["*"]
---

# Logseq Link Hygiene

Use this skill whenever graph edits add, change, or review `[[wikilinks]]`.

## Default path

1. Identify newly added or proposed `[[wikilinks]]` in the edited graph pages.
2. Resolve each link against the existing graph before leaving it as a wikilink:
   - exact page title
   - `alias::` values
   - case-folded title
   - punctuation/spacing variants
   - slash namespace variants
   - garden-accepted structural links such as date links
3. If one clear page exists, use that `[[Page/Title]]`.
4. If multiple plausible pages exist, leave the current text alone and report the ambiguity.
5. If no page exists and the link target is not being intentionally created now, use plain text instead of a wikilink.
6. Only leave a new unresolved wikilink when the user explicitly wants a placeholder or when this workflow creates the target page in the same turn.

## Scripted check

When the edit is non-trivial or contains several links, run the checker from the repo root:

```sh
nbb-logseq .rulesync/skills/logseq-link-hygiene/scripts/resolve-wikilinks.cljs --changed <file>...
```

Trust the script's status categories, then apply human judgment to `ambiguous` and `unresolved` results.

If `nbb-logseq` is unavailable, assume global tools are managed by `mise` and install it with:

```sh
mise use -g npm:@logseq/nbb-logseq@latest
```

If installation is not appropriate for the current task, use shell search with the same resolution rules from `./references/link-resolution.md`.

## When to read references

- Read `./references/link-resolution.md` for matching rules, examples, and unresolved-link policy.
- Read `./references/nbb-logseq.md` before changing the script or setting up the `nbb-logseq` dependency.

## Reporting

In the final answer, mention:

- link replacements made
- unresolved links intentionally left as plain text
- ambiguous links needing human judgment
