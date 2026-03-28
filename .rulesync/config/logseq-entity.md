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

The garden may eventually model many entity types. Types with Logseq-native SOP pages (authoritative):

- software-project — see `[[Logseq/Entity/software-project]]`
- color-theme — see `[[Logseq/Entity/color-theme]]`
- company — see `[[Logseq/Entity/company]]`
- question — see `[[Logseq/Entity/question]]`

Other entity types may be added here later without changing the skill itself. Prefer the `[[Logseq/Entity/<Type>]]` pages over this file when both exist.

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
- Use `created-by:: [[Person/<personname>]]` or `created-by:: [[CompanyName]]` (company page with `logseq-entity:: [[Logseq/Entity/company]]`) only when that entity page already exists.
- Add `alias:: [[Person/<personname>/GitHub/<projectname>]]` when appropriate and when that person page already exists.

### Page Shape

- Disk filename: `pages/<CanonicalName>.md`
- Link shape: `[[<CanonicalName>]]`
- First block should be an H1 reference link to the project
- Keep the initial page lean: title link plus a few descriptive bullets

### Creation Blockers

- If the creator is clear and a person page does not yet exist, create the person page so the software entity can link to it. If the creator is clearly an organization, create a company entity page first when using `created-by::` to that org.
- If it is not clear who the creator is, do not guess. Ask the human what should be done (e.g. create the software page without creator metadata, create the entity page first, or skip until the identity is clarified).

### Source-Block Handling

- By default, do not move source blocks from the journal or source page.
- Only move or transplant source blocks when the user explicitly asks.

## Entity Type: color-theme

Authoritative documentation: `[[Logseq/Entity/color-theme]]`. This section is bootstrap-only.

### Recognition

Strong signals:

- Named palette family with official style guide or shared flavor names across ports
- Official org or repo listing many app-specific themes (terminal, editor, tmux, etc.)

### Canonical Naming

- Short top-level page name when unambiguous (e.g. `[[Catppuccin]]`).
- Optional hierarchical `alias::` (e.g. `[[UI/Color/Theme/Catppuccin]]`) for namespace visibility.

### Frontmatter

- `logseq-entity:: [[Logseq/Entity/color-theme]]` on instances.
- Never modify `tags::` on existing pages without explicit human instruction.

### Page Shape

- Hub page: identity, flavors, palette link, stack matrix linking to app pages (e.g. [[Ghostty]], [[Neovim]], [[tmux]], [[yazi]]).

## Entity Type: company

Authoritative documentation: `[[Logseq/Entity/company]]`. This section is bootstrap-only.

### Recognition

Strong signals: official company or product site, stable brand name, GitHub org representing the vendor, repeated references to “who makes” multiple tools.

### Canonical Naming

- Short top-level page name (e.g. `[[Charm]]`) with `alias::` for alternate names (e.g. GitHub org label).

### Frontmatter

- `logseq-entity:: [[Logseq/Entity/company]]` on instances.
- Never modify `tags::` on existing pages without explicit human instruction.

### Page Shape

- Lean hub: H1 link to primary site, one-line positioning, links to notable software entities.

## Entity Type: question

Authoritative documentation: `[[Logseq/Entity/question]]`. This section is bootstrap-only.

### Recognition

Strong signals:

- A single answerable question stored under a topic namespace with a `/Q/` segment in the page title
- On disk: `pages/*___Q___*.md` between topic prefix and question slug

### Search And Dedup

Prefer `rg`. Search in this order unless the type page specifies otherwise:

1. Exact expected filepath / title under the topic namespace
2. Normalized question text and key phrases in `pages/**___Q___*.md`
3. Namespace-scoped glob (topic + `___Q___`)
4. H1 and opening blocks; allow minor rephrasing

Classify as: `existing`, `similar`, `new`, or `blocked`. Full process: see the logseq-entity skill reference `entity-search-and-dedup.md`.

### Frontmatter

- `logseq-entity:: [[Logseq/Entity/question]]` on new instances.
- Optional `see-also:: [[Page1]], [[Page2]], ...` for internal “see also” pages (**strongest tie first**). Prefer over a `## Related` section that only lists internal links. Do not list parent namespace pages whose only role is restating context already implied by the page title. External URLs stay in the body (e.g. under Answer).
- Optional `via:: [[Page1]], ...` **only** for what **prompted** adding the page (journal/import/session stub)—not for general related reading.
- Never modify `tags::` on existing pages. For new pages, optional `tags::` may mirror sibling question pages in the same topic (often `[[Q]]` plus a topic tag); see the type page.
- `alias::` optional when it matches local question-page patterns.

### Page Shape

- Link: `[[Topic/Q/Question text]]` (multi-segment topics allowed).
- File: `pages/Topic___Q___Question text.md`; use `%3F` for `?` in filenames when needed.
- Body: LFM; H1 is the question; optional `## Answer`, `## My Notes`. Use `see-also::` instead of `## Related` when appropriate for internal links.

### Legacy

- Older question pages may omit `logseq-entity::`. Do not bulk-edit unless the author requests migration.

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
