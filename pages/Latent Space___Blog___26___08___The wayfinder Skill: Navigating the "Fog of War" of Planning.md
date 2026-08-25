created-by:: [[Latent Space]]
date-created:: [[2026/08/20]]
logseq-entity:: [[Logseq/Entity/Article]]
readwise-link:: https://read.readwise.io/read/01m0gfjwrjsf18vzchms81ep69

- # [The /wayfinder Skill: Navigating the "Fog of War" of Planning](https://www.latent.space/p/wayfinder-skill)
	- An interview with [[Person/Matt Pocock]] about the `/wayfinder` skill, for planning a piece of work too large to hold in one agent session.
	- ## Summary
		- Wayfinder writes the plan as a **map**: one issue on the repository’s tracker, with **decision tickets** hanging off it as child issues. Each ticket asks one question whose answer is a decision. A session picks up a ticket whose blockers are all closed, resolves it, and records the answer on the map. The plan is finished when nothing is left to decide.
		- Tickets come in four kinds. A **research** ticket reads documentation or a knowledge base. A **prototype** ticket makes something rough to react to. A **grilling** ticket is a conversation with a person. A **task** ticket is work a person has to finish before a decision can be made.
		- The **fog of war** is the part of the work that cannot be decided yet. Early decisions push the fog back, the way exploring a map in a strategy game reveals more of it.
		- [[Claude/Code/Skill/Grill Me]] covers the case where the whole piece of work fits in one session and the path is visible. Wayfinder covers the case where the path ahead is unclear.
		- Picking the words came first. Pocock calls **map**, **ticket** and **session** "leading words", a shared vocabulary between person and agent, and keeps the same vocabulary across every skill they publish.
	- ## Highlights
		- > Pocock recently released a new skill called **/wayfinder**. Its purpose is to help you and your agent figure out a project where the end state isn’t entirely clear. Or as Pocock put it in our interview, **/wayfinder helps you navigate “the fog of war,”** where you have a project but **“you can’t quite decide everything right at the start.”**
		- > I didn’t want to feel constrained in the planning stage anymore. I wanted an orchestrator layer that would basically say, okay, whatever you want to plan, I’m going to handle the planning sessions for you. I’m going to split this out into multiple different threads, do prototyping, do research and pull it all back together, so that you don’t feel constrained in the planning anymore.
	- ## Links
		- [wayfinder SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md), in [[Person/Matt Pocock/GitHub/skills]]
		- [wayfinder documentation](https://github.com/mattpocock/skills/blob/main/docs/engineering/wayfinder.md)
		- [[Person/Matt Pocock/YouTube/26/06/Building Great Agent Skills: The Missing Manual]]
