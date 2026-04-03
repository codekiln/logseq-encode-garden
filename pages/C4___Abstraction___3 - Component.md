logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/3 - Components]], [[C4/Abstraction/2 - Container]], [[C4/Abstraction/4 - Code]]

- # **[Component](https://c4model.com/abstractions/component)** (C4 abstraction)
	- ## Overview
		- In C4, a **component** is a **grouping of related functionality** behind a **well-defined interface**—deliberately **not** “whatever your framework calls a component”.
		- Components are **not** separately deployable; the **container** is the deployable unit, and components share its **process space** (for typical interpretations).
	- ## Context
		- Third zoom level of [[C4]]: answers *how is **this container** structured internally*—services, modules, facades, bounded technical roles.
		- Stands **one level above** language-level [[C4/Abstraction/4 - Code]] (classes, modules, files).
	- ## Key principles
		- **Interface-backed** — Think in terms of responsibilities and contracts, not folder trees alone.
		- **Runtime partition** — Packaging (JARs, DLLs, folders) may or may not align; C4 cares about **logical structure inside a running container**.
	- ## Mechanism
		- Shown on [[C4/Diagram/3 - Components]]; often **reverse-engineered** from code for large systems (e.g. via [[Structurizr]] or similar tooling).
	- ## Examples
		- A **set of MVC controllers** plus a **service layer** and **repositories** might be refactored into named components (not every class is one).
	- ## Misconceptions
		- “**Every package / namespace / folder is a component**” — **Often false**; those are **organisational** units—components are **architectural** groupings.
		- “**Microservice = component**” — **Usually wrong**; a microservice is typically a **container** or even its **own software system**, depending on ownership and boundary.
