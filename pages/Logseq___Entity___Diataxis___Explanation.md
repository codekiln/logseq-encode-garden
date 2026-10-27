logseq-entity:: [[Logseq/Entity/Definition]]
logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
alias:: [[Explanation Page]], [[Diataxis Explanation Page]], [[Diataxis Concept Page]]

- # Diataxis Explanation
	- In this garden, **Diataxis Explanation** pages model understanding-oriented writing: why something is the way it is, and how ideas fit together. They explain **why** and serve understanding, the reflective quadrant of [[Diataxis]].
	- ## Inherited rules
		- Choosing between the four children, marking an instance, `see-also::` and shared frontmatter follow [[Logseq/Entity/Diataxis]].
	- ## What counts as an instance
		- A page that gives background, weighs alternatives, or draws the connections between ideas, rather than instructing or cataloguing.
		- Not an instance: a page of steps — [[Logseq/Entity/Diataxis/How To]] or [[Logseq/Entity/Diataxis/Tutorial]]. A systematic description of a thing — [[Logseq/Entity/Diataxis/Reference]].
	- ## Relationship to [[Logseq/Entity/Concept]]
		- This quadrant overlaps the entity system almost entirely: an explanation-shaped page in this garden is normally a **concept** instance, and [[Logseq/Entity/Concept]] governs its frontmatter, its naming, and its body sections.
		- Read [[Logseq/Entity/Concept]] first, then this page for the Diataxis vocabulary and the tag. Where the two differ, the Concept page wins on shape and this page wins on which quadrant the writing belongs to.
		- **[[Logseq/Entity/Term]]** covers the narrower case of naming a thing rather than explaining it; a page can be both.
	- ## Naming and links
		- No namespace segment of its own — an explanation page is named for the idea it explains, wherever that idea naturally sits, per [[Logseq/Entity/Concept]].
	- ## Frontmatter
		- **`tags::`** — new pages of this kind carry `[[Diataxis/Concept]]` (or `[[Diataxis/Explanation]]`, the same cluster by alias).
	- ## Page shape
		- Per [[Logseq/Entity/Concept]]. This entity adds no shape of its own.
	- ## Writing an instance
		- Take a wider view than a task allows: the history, the alternatives that were not taken, the reasons behind a design.
		- Admit the disagreements. Explanation is the one quadrant where opinion belongs, provided it is marked as such.
		- Link out to the how-to, tutorial and reference pages rather than absorbing their jobs.
	- ## Relationship to other entities
		- **[[Diataxis/Explanation]]** — the framework concept page this entity implements.
		- **[[Logseq/Entity/Discussion]]** — a Discussion page that weighs alternatives also carries this entity, after Discussion in its `logseq-entity::` line. It takes its name, placement, shape and frontmatter from the Discussion definition, so an agent writing one leaves out the `[[Diataxis/Concept]]` tag that new Explanation pages otherwise carry.
