* # Question entity

* One of the most frequent entities in the garden, this entity models a Question I had at a particular time. Typically Questions are stored under a topic namespace with a dedicated `/Q/` segment so they stay findable and deduplicable.

  * ## Examples in this garden

         - Pages on disk match `pages/*___Q___*.md` (e.g. [[mise/Q/How do I remove a mise tool?]] → `mise___Q___How do I remove a mise tool%3F.md`).
         - In-graph titles use a slash path such as `Topic/Q/Question text` or `Topic/SubTopic/Q/Question text`.

  * ## When we treat something as a question entity

         - Strong signals: the page captures a single answerable question; the title uses a topic namespace plus a fixed **Q** segment before the question wording; the body holds an answer (human, AI, or both).
         - Not a question entity: general notes without the `/Q/` naming convention, dashboards, CLI command stubs, or long-running threads better modeled as non-Q pages.

  * ## Canonical naming and links

         - **Link shape:** `[[Topic/Q/Question text]]` or `[[Topic/SubTopic/Q/Question text]]` as needed.
         - **File shape:** `pages/Topic___Q___Question text.md` with triple underscores between namespace parts; encode `?` as `%3F` in the filename when present.
         - Use forward slashes in journal and body links; never triple underscores inside Logseq links.

  * ## Finding and deduplicating

         - Treat every new question as a question-entity candidate.
         - Practical search order for this type:
          - 1. Exact expected page title / filepath under the topic namespace.
          - 2. Grep normalized question text and key phrases across `pages/**___Q___*.md`.
          - 3. Namespace-restricted globs (e.g. topic prefix + `___Q___`).
          - 4. H1 and first blocks on candidate pages; allow for minor rephrasing.
         - Classify each candidate as: **existing**, **similar** (needs human judgment), **new**, or **blocked** (missing config or ambiguous topic).

  * ## Frontmatter

         - On **new** question pages, include `logseq-entity:: [[Logseq/Entity/Question]]` so this type page indexes instances.
         - **Card-backed questions:** when the H1 carries `[[card]]` and the page is a first-class review target, add a second entity marker: `logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]` (see [[Logseq/Entity/Card]]). Card-backed questions use the compact page shape — see **Card-backed page shape** under Page shape below.
         - [[Logseq/Frontmatter/see-also]]
          - **`see-also::`** — optional; extremely parsimonious list of 1-2 not obvious **garden pages** that are the best adjacent reading (**strongest tie first**). Do not put anything obvious in this list, do not restate parent-namespace context the title already encodes. Do not use `see-also::` for external URLs (put those in the answer body).
         - [[Logseq/Frontmatter/via]]
          - **`via::`** — optional; only for **what logseq page best represents the context in which the question appeared** - only useful when astonishing; be parsimonious and only use this when it's not obvious.
         - **`tags::` / `alias::`** — only when they match established patterns on sibling question pages in the same topic; never alter existing **`tags::`** on a page you did not create for tagging migration.
         - Shared frontmatter conventions live on [[Logseq/Frontmatter]].

  * ## Page shape (canonical)

         id:: 69cd1d51-7708-4021-8c21-f7e864ec017e
         - **H1** — the question text; link key terms to existing pages where it helps.
         - Optional inline `[[card]]` at the end of the H1 — **only when the human operator explicitly requests it**. Do not add `[[card]]` speculatively, even if the question seems like good SRS material.
         - **Section order** (omit empty sections):
          - `## [[My Answer]]` — optional; [[Human]] / [[Gard/en/er/Human]] working answer (steps, tables, `[[tldr]]`, verified command examples).
          - `## [[My Notes]]` — optional; do not create by default. Tangents and links that are not the direct answer.
          - `## [[AI Answer]]` — standard heading for AI-researched answers. Answer content is direct children of this block; do **not** add a `[[AI/Response]]` child wrapper.
           - `[[Answer/Official]]` (alias `[[Official Answer]]`) — used when the answer is from official documentation; include a markdown link inline: `[[Answer/Official]] from [Source Title](url)`.
           - Lead with **Short answer:** when useful.
           - Cite **external** docs with markdown links in the answer body.
           - Bold for labels; backticks for commands. Do not wrap `` `commands` `` in `**…**` (see [[Logseq/Flavored Markdown]]).
         - **Do not** add `## Related` solely to list internal wikilinks; use **`see-also::`** instead.
         - ### Card-backed page shape
          - When `logseq-entity::` includes [[Logseq/Entity/Card]] and the H1 ends with `[[card]]`, omit the `## Answer` section header and attribution block. The answer sits directly as a child bullet of the H1, as short as a card prompt requires:
           - ~~~
             logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]

             - # Question text linking [[Key/Concept]]? [[card]]
              - Terse answer, e.g. [[tmux/Keyshort/Prefix]] `w`
             ~~~
          - Use `==highlight==` to mark mnemonic cues in the answer (e.g. `==N==ext Window`).
          - Wikilink key terms in both the question and the answer to canonical entity pages.

  * ## Relationship to other types

         - **Card:** `[[card]]` on the H1 plus `[[Logseq/Entity/Card]]` in frontmatter when the question page itself is reviewable; distinct from factoring a prompt into a `/Card/` namespace page under [[Logseq/Entity/Card]].
         - **CLI commands / flags:** questions *about* commands link to [[Logseq/Entity/CLI/Command]] and [[Logseq/Entity/CLI/Flag]] instances; they are not substitutes for command reference stubs.

  * ## Legacy instances

         - Older `___Q___` pages may lack `logseq-entity::`, use `## Related` for internal links (use `see-also::` instead), or use `## [[AI/Response]]` as the section heading instead of the correct [[AI Answer]] form.
         - Do not bulk-migrate unless requested; new pages should follow the rules above.

