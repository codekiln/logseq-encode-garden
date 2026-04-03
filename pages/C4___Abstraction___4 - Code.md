logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/4 - Code]], [[C4/Abstraction/3 - Component]]

- # **[Code](https://c4model.com/abstractions/code)** (C4 abstraction)
	- ## Overview
		- **Code** elements are the programming-language building blocks that implement a [[C4/Abstraction/3 - Component]]: **classes**, **interfaces**, **enums**, **functions**, **objects**, and similar constructs.
		- The **finest** C4 static zoom; many teams **skip** drawing it and rely on the IDE or generated UML instead.
	- ## Context
		- Fourth level of [[C4]]: answers *how is this **component** actually built*—often **too detailed** for stakeholder decks but useful for developers onboarding to a module.
	- ## Key principles
		- **Honest detail** — Show the **architecturally relevant** types and relationships, not every POJO or util class.
		- **Optional by value** — If the diagram adds no new insight, omit it.
	- ## Mechanism
		- Expressed in [[C4/Diagram/4 - Code]] views; frequently **auto-generated** from source when used at all.
	- ## Examples
		- A UML-style **class diagram** for a service’s core types; a **module dependency** sketch in lieu of full UML.
	- ## Misconceptions
		- “C4 **requires** code diagrams” — **False**; context + container often suffice per [[C4/Diagram]].
		- “**Code diagram = full class diagram of everything**” — **Usually noise**; C4 expects **selective** structure, not inventory.
