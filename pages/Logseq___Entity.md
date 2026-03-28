alias:: [[Logseq Entities]]

- # Logseq Entity
	- This page defines the conceptual model for entities in this knowledge garden and lists the entity types the garden models.
	- ## Terms
		- **Entity** — a single thing that has its own page in the garden: one person, one software project, one book, etc. Each entity is an instance of exactly one entity type.
		- **Entity type** — a category of entities that share the same modeling rules. For example, "software-project" is a type; each individual tool or library (e.g. Neovim, Yamtrack) is an entity of that type. This page is the registry of entity types; each type has its own documentation page that describes how to recognize, name, and create entities of that type.
	- ## How we mark a page as an entity of a given type
		- In the page’s frontmatter, add `logseq-entity::` with a link to the entity-type page that documents that kind of entity. Example: `logseq-entity:: [[Logseq/Entity/software-project]]`. One such link per page. Why: the type page then gets backlinks to all pages that declare it, so the type page doubles as an index of instances and we can see at a glance which pages follow which SOP.
	- ## Cross-links without a `## Related` section (`see-also::`)
		- Optional frontmatter: **`see-also:: [[Page A]], [[Page B]], ...`** for **garden pages** that are useful “see also” context—same role as a tail **`## Related`** list of internal links, but kept in frontmatter. Order **strongest tie first**. Do **not** include links whose only role is **parent namespace** context; the page title’s hierarchy already implies that in Logseq. External URLs still belong inline in the body (e.g. under **Answer**). Applies garden-wide; especially handy for **question** pages.
	- ## Provenance — what went into the garden (`via::`)
		- Optional frontmatter: **`via:: [[Page A]], ...`** only for **what made this page exist here** (e.g. a journal day that prompted it, a specific import or chat deep-research stub, a session note you are filing from). **Not** for general related reading—use **`see-also::`** for that. **Not** for parent namespace context. Multiple entries: strongest causal tie first.
	- ## Entity types in this garden
		- **software-project** — Tools, editors, libraries, apps, CLIs, servers. Conventions (naming, dedup, page shape, creator handling) are documented on the software-project type page. Fallback when type pages are missing: `.rulesync/config/logseq-entity.md`.
		- **color-theme** — Coordinated palette families reused across apps (terminals, editors, TUIs). Conventions are on the color-theme type page. Fallback/bootstrap notes: `.rulesync/config/logseq-entity.md` (section **color-theme**).
		- **company** — Organizations or brands you track as first-class pages (e.g. vendors with multiple tools). Conventions are on the company type page.
		- **question** — Topic-scoped research questions using a `/Q/` segment in the page title (`*___Q___*` on disk). Conventions are on the question type page. Fallback/bootstrap notes: `.rulesync/config/logseq-entity.md` (section **question**).
		- Deferred for follow-up: other types (e.g. person, book) may be added later as dedicated entity-type pages when needed.
