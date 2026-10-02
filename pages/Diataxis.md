logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[Logseq/Entity/Definition]]

- # [Diátaxis](https://diataxis.fr/)
	- A framework by [[Person/Daniele Procida]] that sorts documentation by what the reader needs, rather than by subject. Its four types are distinct in purpose and should not be blended on one page.
	- ## The compass
		- Pick the type by the need, not by what is easiest to write. Each row is an entity in this garden.
		- | Content…              | serves the reader’s…   | Type                                      | Namespace                     | Tag                        |
		  |-----------------------|-------------------------|-------------------------------------------|-------------------------|----------------------------|
		  | informs **action**    | application of skill    | [[Logseq/Entity/Diataxis/How To]]         | `Topic/…/How To/Task`   | `[[Diataxis/How To]]`      |
		  | guides **learning**   | acquisition of skill    | [[Logseq/Entity/Diataxis/Tutorial]]       | `Topic/…/Tutorial/Goal` | `[[Diataxis/Tutorial]]`    |
		  | informs **cognition** | theoretical knowledge   | [[Logseq/Entity/Diataxis/Reference]]      | `Topic/…/Ref/Subject`   | `[[Diataxis/Reference]]`   |
		  | explains **why**      | understanding           | [[Logseq/Entity/Diataxis/Explanation]]    | per [[Logseq/Entity/Concept]] | `[[Diataxis/Concept]]` |
	- ## The four types in this garden
		- [[Diataxis/How To]], [[Diataxis/Tutorial]], [[Diataxis/Reference]] and [[Diataxis/Explanation]] hold the framework's own account of each type. The `Logseq/Entity/Diataxis/` pages beside them say how a page of that kind is named, tagged and shaped here.
	- ## Shared rules across the four
		- Add the quadrant tag when creating a page of that kind; never rewrite `tags::` on a page you did not create.
		- Prefer `see-also::` in frontmatter over a `## Related` section that only lists internal wikilinks.
