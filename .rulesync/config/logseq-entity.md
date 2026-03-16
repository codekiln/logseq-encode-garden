# Logseq Entity Configuration

This file stores fallback garden-specific configuration for the `logseq-entity` skill.

The skill should prefer `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` pages when they exist.

Use this file when those pages do not exist yet, are incomplete, or need bootstrap support.

## Bootstrap Role

- Treat this file as fallback/bootstrap configuration, not the primary ontology once `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` exist.
- During initialization, use this file to seed the first Logseq-native entity pages.
- Keep this file aligned enough to remain useful until the Logseq-native pages are complete.

## Garden Intent

- This is a personal Logseq knowledge garden.
- Canonical page names should follow knowledge-gardening principles rather than external site structure.
- If an entity is likely to develop sub-namespaces, prefer a short top-level canonical page name.
- Use aliases to situate entities within contextual namespaces.

## Enabled Entity Types

The garden may eventually model many entity types. For now, the highest-priority type for this garden is:

- software-project

Other entity types may be added here later without changing the skill itself.

## Entity Type: software-project

### Recognition

Strong signals:

- GitHub repository links
- official project homepages
- article or post titles that clearly name a software project
- surrounding notes that describe a tool, editor, library, app, CLI, or server

Aggressive inference is allowed, but the skill must tell the user what it inferred after the fact.

### Canonical Naming

- Prefer a top-level canonical page when the project is likely to grow in importance or gain sub-namespaces.
- Use the shortest stable project name that still clearly identifies the software.
- Do not default to `[[GitHub/owner/repo]]` as the canonical page title when a top-level entity page would be more garden-friendly.

Examples:

- `[[rust]]` may be canonical, with contextual aliases such as `[[Programming/Language/Rust]]`
- `[[rsvim]]` may be canonical even if discovered from `rsvim/rsvim`

### Search And Dedup

Search in this order:

1. exact canonical page name
2. exact alias match
3. partial title match
4. repo owner and repo name
5. page-body mentions of the same homepage, repo, or description

Classify results as:

- `existing`
- `similar`
- `new`
- `blocked`

### Frontmatter

- Never modify, add, or remove `tags::` in an existing document.
- For newly created pages, only add frontmatter that is actually known.
- Use `created-by:: [[Person/<personname>]]` only when the person page already exists.
- Add `alias:: [[Person/<personname>/GitHub/<projectname>]]` when appropriate and when that person page already exists.

### Page Shape

- Disk filename: `pages/<CanonicalName>.md`
- Link shape: `[[<CanonicalName>]]`
- First block should be an H1 reference link to the project
- Keep the initial page lean: title link plus a few descriptive bullets

### Creation Blockers

- If the creator is clear and a person page does not yet exist, create the person page so the software entity can link to it.
- If it is not clear who the creator is, do not guess. Ask the human what should be done (e.g. create the software page without creator metadata, create a person page first, or skip until the identity is clarified).

### Source-Block Handling

- By default, do not move source blocks from the journal or source page.
- Only move or transplant source blocks when the user explicitly asks.

## Reporting Contract

After running on a page such as a journal entry, report:

- entities found
- entities already present
- entities created
- entities inferred aggressively
- blocked cases that need a human decision

## Notes For Future Gardens

This config file is expected to vary from garden to garden.

The public `logseq-entity` skill should stay generic. Over time, this file should shrink as the garden's entity ontology moves into `[[Logseq/Entity]]` and `[[Logseq/Entity/<Type>]]` pages.
