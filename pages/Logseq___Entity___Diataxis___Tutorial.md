logseq-entity:: [[Logseq/Entity/Definition]]
logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
alias:: [[Tutorial Page]], [[Diataxis Tutorial Page]]

- # Diataxis Tutorial
	- In this garden, **Diataxis Tutorial** pages model learning-oriented, hands-on lessons that take a beginner through meaningful practical steps. They guide **learning** and serve the acquisition of a skill, the studying quadrant of [[Diataxis]].
	- ## Inherited rules
		- Choosing between the four children, marking an instance, `see-also::` and shared frontmatter follow [[Logseq/Entity/Diataxis]].
	- ## What counts as an instance
		- A page whose job is to teach by doing: the reader ends it able to do something they could not do before, having produced a visible result along the way.
		- Not an instance: a page for someone who already knows the goal and needs the route — that is [[Logseq/Entity/Diataxis/How To]]. A page that describes or explains rather than teaches — [[Logseq/Entity/Diataxis/Reference]] or [[Logseq/Entity/Diataxis/Explanation]].
	- ## Naming and links
		- Namespace pattern: `Topic/Subtopic/Tutorial/Learning Goal`.
		- `[[Programming/Python/Tutorial/Build Your First Web App]]` → `pages/Programming___Python___Tutorial___Build Your First Web App.md`.
	- ## Frontmatter
		- **`tags::`** — new pages of this kind carry `[[Diataxis/Tutorial]]` alongside their topic tags.
	- ## Page shape
		- `- # Tutorial: <Learning Goal>`
			- `## What You'll Create` — the end result in a sentence.
			- `## Prerequisites` — required tools or knowledge, and any setup.
			- `## Learning Goals` — the skills acquired, and what the reader can do afterward.
			- `## Steps` — `### 1. First Achievement` headings, each with concrete instructions, the expected result, and what to notice.
			- `## What You've Learned` — recap, then where to practice next.
	- ## Writing an instance
		- **Ensure success.** Every step must work reliably for every reader; the author takes full responsibility for that.
		- **Show early results.** Break the journey into small steps that each produce something visible.
		- **Minimize explanation.** Keep the focus on doing and link explanation elsewhere.
		- **Be concrete.** Specific examples, not abstractions.
		- **Language:** *we* for the shared journey — *We will create…*; *You will see…* to set expectations; *Notice that…* to direct attention. Present tense, active voice.
		- **Test it** by following your own instructions exactly, then cut the explanations that crept in and add the steps you skipped.
	- ## Relationship to other entities
		- **[[Diataxis/Tutorial]]** — the framework concept page this entity implements.
