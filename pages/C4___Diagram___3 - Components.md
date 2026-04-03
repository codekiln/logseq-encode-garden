logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Abstraction/3 - Component]], [[C4/Diagram/2 - Containers]], [[C4/Diagram/4 - Code]]

- # **[Component diagram](https://c4model.com/diagrams/component)** (C4 diagram)
	- ## Overview
		- **Level 3** static-structure view: **inside** a single [[C4/Abstraction/2 - Container]], showing major **components** at the [[C4/Abstraction/3 - Component]] level—groupings of related behaviour behind interfaces—and their dependencies.
		- Answers *how is **this deployable** structured **logically*** without naming every class.
	- ## Context
		- Most useful when the container is **large enough** that a flat list of technologies (from the container diagram) no longer explains **seams** and **ownership** inside the process.
	- ## Key principles
		- **Cohesion** — Each component should represent a **story** you can explain in one breath.
		- **Acyclic clarity** — Highlight **allowed** dependencies; call out **forbidden** ones if the diagram is a governance artefact.
	- ## Mechanism
		- Optional **deeper** step: [[C4/Diagram/4 - Code]] for implementation detail—often skipped or generated.
	- ## Examples
		- Inside a monolithic web container: **controllers**, **application services**, **domain core**, **integration adapters**, **repositories**.
	- ## Misconceptions
		- “**Must mirror the folder tree**” — **No**; components are **architectural** slices, not directory listings.
		- “**Every class is a component**” — **Opposite of C4 intent**; components **aggregate** [[C4/Abstraction/4 - Code]].
