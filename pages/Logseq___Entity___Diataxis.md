logseq-entity:: [[Logseq/Entity/Definition]]
see-also:: [[Diataxis]]

- # Diataxis
	- In this garden, **Diataxis** pages model documentation written for one reader need from the [[Diataxis]] framework: doing a task, learning a skill, looking something up, or understanding why.
	- ## Child entities
		- Each child entity below extends this one. Pick the child by what the reader needs.
		- | Content…              | serves the reader’s…   | Entity                                 | Namespace                     | Tag                      |
		  |-----------------------|------------------------|----------------------------------------|-------------------------------|--------------------------|
		  | informs **action**    | application of skill   | [[Logseq/Entity/Diataxis/How To]]      | `Topic/…/How To/Task`         | `[[Diataxis/How To]]`    |
		  | guides **learning**   | acquisition of skill   | [[Logseq/Entity/Diataxis/Tutorial]]    | `Topic/…/Tutorial/Goal`       | `[[Diataxis/Tutorial]]`  |
		  | informs **cognition** | theoretical knowledge  | [[Logseq/Entity/Diataxis/Reference]]   | `Topic/…/Ref/Subject`         | `[[Diataxis/Reference]]` |
		  | explains **why**      | understanding          | [[Logseq/Entity/Diataxis/Explanation]] | per [[Logseq/Entity/Concept]] | `[[Diataxis/Concept]]`   |
	- ## What counts as an instance
		- A page that serves one of the four needs. A topic that needs two of them gets two pages, each linking to the other.
		- Each child definition page says what its own instances look like and which of its siblings a near miss belongs to.
	- ## Marking an instance
		- An instance carries its child entity alone: `logseq-entity:: [[Logseq/Entity/Diataxis/How To]]`. The child already says the page is a Diataxis page.
		- When the page is also another entity, that entity comes first and the Diataxis child follows it: `logseq-entity:: [[Logseq/Entity/CLI/Command]], [[Logseq/Entity/Diataxis/How To]]`.
	- ## Frontmatter
		- **`tags::`** — a new page carries its child's tag from the table above, alongside its topic tags.
		- **`see-also::`** — preferred over a `## Related` section that only lists internal wikilinks.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape and writing
		- Each child entity defines its own namespace, page shape and voice.
		- A page links out to its siblings when the reader needs them, so a how-to links to the explanation behind a step and leaves the explaining to that page.
