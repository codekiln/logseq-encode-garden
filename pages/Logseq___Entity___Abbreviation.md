logseq-entity:: [[Logseq/Entity/Definition]]
see-also:: [[Logseq/Entity/Term]]

- # Abbreviation
	- In this garden, **Abbreviation** pages model shortened forms of words or phrases — initialism, acronym, or contraction — where the abbreviated form is the primary lookup key.
	- ## Examples in this garden
		- [[IPC]] — Inter-Process Communication
		- [[SMB]] — Server Message Block
		- [[Keyshort]] — Keyboard Shortcut
	- ## When we treat something as an abbreviation entity
		- Strong signals: the page title is the abbreviated form; the full phrase expands it in the body; readers look up the short form, not the long one.
		- Good fit: protocol initials, technical acronyms, contracted terms.
		- Not an abbreviation entity: pages where the full phrase is the primary title (use [[Logseq/Entity/Term]] directly).
	- ## Relationship to Term
		- Abbreviation is a specialization of [[Logseq/Entity/Term]]. Pages that are abbreviation entities should also declare [[Logseq/Entity/Term]] as a secondary entity type.
	- ## Frontmatter
		- Set **`logseq-entity::`** to list this entity-type page (primary) then [[Logseq/Entity/Term]] (secondary): `logseq-entity:: [[Logseq/Entity/Abbreviation]], [[Logseq/Entity/Term]]`.
		- Use **`alias::`** for the expanded full phrase when it is a useful lookup surface.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- Use Logseq Flavored Markdown.
		- H1 is the abbreviated form.
		- Body: expansion in bold, followed by a short definition sentence. Link out to concept pages for deeper treatment.
