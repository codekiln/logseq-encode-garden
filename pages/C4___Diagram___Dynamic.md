logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/2 - Containers]], [[C4/Diagram]]

- # **[Dynamic diagram](https://c4model.com/diagrams/dynamic)** (C4 diagram)
	- ## Overview
		- A **supporting** C4 diagram describing **runtime behaviour**—collaborations, **message flows**, **call sequences**—using the **same structural elements** (people, software systems, containers, components) as the static views.
		- Answers *what **happens over time*** or *how a **use case** traverses the architecture*.
	- ## Context
		- The core C4 static diagrams are **not** sequence charts; when **chronology** matters, the dynamic view is the intended supplement (see [[C4/Diagram]]).
	- ## Key principles
		- **Narrative** — Anchor on a **concrete scenario** (“checkout”, “password reset”) rather than abstract “data flows everywhere”.
		- **Scoped** — Keep participant sets **small**; explode into multiple diagrams if needed.
	- ## Mechanism
		- Often rendered as **numbered interactions** or UML-style **collaboration** idioms while preserving C4 element identities.
	- ## Examples
		- **OAuth** token exchange between **browser**, **BFF**, and **identity provider**; **async** saga steps across **containers**.
	- ## Misconceptions
		- “**Any arrow on a container diagram is dynamic**” — **Misleading**; static diagrams show **possible** relationships—dynamic diagrams show **ordered** interactions for a story.
		- “**Dynamic replaces integration tests**” — **False**; it **communicates** intent—tests still **verify** it.
