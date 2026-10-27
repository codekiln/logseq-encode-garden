logseq-entity:: [[Logseq/Entity/Definition]]
logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
alias:: [[How To Page]], [[Diataxis How To Page]]

- # Diataxis How To
	- In this garden, **Diataxis How To** pages model goal-oriented directions that walk a competent reader through solving one specific problem. They inform **action** and serve the application of a skill, the practical quadrant of [[Diataxis]].
	- ## Inherited rules
		- Choosing between the four children, marking an instance, `see-also::` and shared frontmatter follow [[Logseq/Entity/Diataxis]].
	- ## What counts as an instance
		- A page addressing a real-world task the reader already knows they want to accomplish, written as a sequence of steps rather than as teaching or description.
		- Not an instance: a page that teaches a skill the reader does not yet have — that is [[Logseq/Entity/Diataxis/Tutorial]]. A page that describes what something *is* — that is [[Logseq/Entity/Diataxis/Reference]]. A page that explains *why* — that is [[Logseq/Entity/Diataxis/Explanation]].
	- ## Naming and links
		- Namespace pattern: `Topic/Subtopic/How To/Specific Task`, for example [[Diataxis/How To/Create a How To]].
		- The title states plainly what the guide accomplishes. `[[Programming/Python/How To/Set Up a Virtual Environment]]` → `pages/Programming___Python___How To___Set Up a Virtual Environment.md`.
	- ## Frontmatter
		- **`tags::`** — new pages of this kind carry `[[Diataxis/How To]]` alongside whatever topic tags they already have.
	- ## Page shape
		- `- # How To <Specific Task>`
			- `## Overview` — what the guide accomplishes, who it is for, when they would need it.
			- `## Prerequisites` — tools, knowledge or resources needed before starting.
			- `## Steps` — numbered `### 1. First Step` headings, each with its details beneath. The sequence flows in a meaningful order.
			- `## Troubleshooting` — common failures and their fixes.
		- Omit a section rather than padding it.
	- ## Writing an instance
		- **Assume competence.** The reader knows the goal; they need the route, not a lesson.
		- **No digressions.** Link out to explanation and reference pages instead of teaching inside the steps.
		- **Practical over complete.** Usability beats covering every possibility.
		- **Language:** conditional imperatives — *If you want X, do Y*. Open steps with an action verb — *Install*, *Configure*, *Create*. Present tense, active voice, concise.
		- When research is needed, add a `### Research` block with findings, flag what is uncertain, and settle scope with the human before writing the steps out.
	- ## Relationship to other entities
		- **[[Diataxis/How To]]** — the framework concept page this entity implements.
