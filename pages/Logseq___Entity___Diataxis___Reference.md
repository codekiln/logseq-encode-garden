logseq-entity:: [[Logseq/Entity/Definition]]
logseq-entity-hierarchy-type:: [[Logseq/Entity/Hierarchy/Frontmatter/Type/extends]]
alias:: [[Reference Page]], [[Diataxis Reference Page]]

- # Diataxis Reference
	- In this garden, **Diataxis Reference** pages model neutral technical descriptions of a thing and how it works — the source of truth a reader consults while working. They inform **cognition** and serve theoretical knowledge, the information quadrant of [[Diataxis]].
	- ## Inherited rules
		- Choosing between the four children, marking an instance, `see-also::` and shared frontmatter follow [[Logseq/Entity/Diataxis]].
	- ## What counts as an instance
		- A page led by the structure of what it describes rather than by a reader's task: specifications, parameters, components, constraints, laid out systematically.
		- Not an instance: a page that instructs — [[Logseq/Entity/Diataxis/How To]] or [[Logseq/Entity/Diataxis/Tutorial]]. A page that argues or gives background — [[Logseq/Entity/Diataxis/Explanation]].
	- ## Naming and links
		- Namespace pattern: `Topic/Subtopic/Ref/Specific Subject`.
		- `[[API/Endpoints/Ref/Authentication]]` → `pages/API___Endpoints___Ref___Authentication.md`; `[[Unicode/Block/Ref/Symbols for Legacy Computing]]` → `pages/Unicode___Block___Ref___Symbols for Legacy Computing.md`.
	- ## Frontmatter
		- **`tags::`** — new pages of this kind carry `[[Diataxis/Reference]]` alongside their topic tags.
	- ## Page shape
		- `- # <Topic Name> Reference`
			- `## Overview` — a brief factual description, with the scope and its boundaries.
			- `## Structure` — how the reference is organized and what conventions it uses.
			- `## Core Components` — `### Component` headings, each with a precise description, its specifications, its parameters, and a usage example.
			- `## Technical Details` — constraints, requirements, versions, dependencies.
		- The arrangement mirrors the logical structure of the thing described, so reader and subject can be navigated in parallel.
	- ## Writing an instance
		- **Describe and only describe.** Neutral description is the imperative. No opinion, speculation, interpretation or marketing.
		- **Adopt standard patterns.** Put information where the reader expects it, in a format they recognize; consistency is what makes reference trustworthy.
		- **Provide examples** that illustrate usage without sliding into instruction or explanation.
		- **Be austere and authoritative.** Reference is consulted, not read through, so it must be unambiguous and complete enough to stand on.
		- **Language:** objective, present tense, precise. Avoid *do this* and *follow these steps* — link to a how-to instead.
		- Update the page when the thing it describes changes; a stale reference is worse than none.
	- ## Relationship to other entities
		- **[[Diataxis/Reference]]** — the framework concept page this entity implements.
