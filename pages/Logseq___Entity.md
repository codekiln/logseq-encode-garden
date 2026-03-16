alias:: [[Logseq Entities]]

- # Logseq Entity
	- This page defines the conceptual model for entities in this knowledge garden and lists the entity types the garden models.
	- ## Terms
		- **Entity** — a single thing that has its own page in the garden: one person, one software project, one book, etc. Each entity is an instance of exactly one entity type.
		- **Entity type** — a category of entities that share the same modeling rules. For example, "software-project" is a type; each individual tool or library (e.g. Neovim, Yamtrack) is an entity of that type. This page is the registry of entity types; each type has its own documentation page that describes how to recognize, name, and create entities of that type.
	- ## How we mark a page as an entity of a given type
		- In the page’s frontmatter, add `logseq-entity::` with a link to the entity-type page that documents that kind of entity. Example: `logseq-entity:: [[Logseq/Entity/software-project]]`. One such link per page. Why: the type page then gets backlinks to all pages that declare it, so the type page doubles as an index of instances and we can see at a glance which pages follow which SOP.
	- ## Entity types in this garden
		- **software-project** — Tools, editors, libraries, apps, CLIs, servers. Conventions (naming, dedup, page shape, creator handling) are documented on the software-project type page. Fallback when type pages are missing: `.rulesync/config/logseq-entity.md`.
		- Deferred for follow-up: other types (e.g. person, book) may be added later; not yet documented as entity-type pages in this garden.
