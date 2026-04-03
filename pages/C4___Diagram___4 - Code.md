logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Abstraction/4 - Code]], [[C4/Diagram/3 - Components]]

- # **[Code diagram](https://c4model.com/diagrams/code)** (C4 diagram)
	- ## Overview
		- **Level 4** static-structure view: **inside** a [[C4/Abstraction/3 - Component]], showing **language-level** elements—classes, interfaces, files, modules—and key relationships.
		- The **most detailed** C4 diagram; often **omitted** when IDEs and generators already answer the same question.
	- ## Context
		- Still **structural** (not a sequence chart); behavioural stories use [[C4/Diagram/Dynamic]] instead.
	- ## Key principles
		- **Selective projection** — Omit noise (simple DTOs, utilities) unless they carry architectural meaning.
		- **Maintainability** — Prefer **generated** or **tool-backed** views so the picture does not rot.
	- ## Mechanism
		- Feeds from reverse-engineering pipelines (e.g. Java/C# analysis) in tools like [[Structurizr]] for large codebases.
	- ## Examples
		- A **trimmed UML class diagram** for the core of one service; a **module graph** for a front-end bundle.
	- ## Misconceptions
		- “**C4 level 4 = mandatory**” — **False**; many successful C4 adoptions **stop** at container or component.
		- “**Code diagram replaces good naming in code**” — **Unwise**; the diagram should **echo** intentional module boundaries, not substitute for them.
