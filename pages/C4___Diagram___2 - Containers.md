logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Abstraction/2 - Container]], [[C4/Diagram/1 - System context]], [[C4/Diagram/3 - Components]]

- # **[Container diagram](https://c4model.com/diagrams/container)** (C4 diagram)
	- ## Overview
		- **Level 2** static-structure view: **inside** one [[C4/Abstraction/1 - Software System]], showing the **containers** at the [[C4/Abstraction/2 - Container]] level—web apps, APIs, workers, databases, file stores, etc.—and **how they communicate**.
		- Answers *what **ships** or **runs*** and *which **protocols** connect the pieces*.
	- ## Context
		- Central “**as-built runtime**” picture for many teams; bridges executives’ [[C4/Diagram/1 - System context]] with developers’ [[C4/Diagram/3 - Components]].
	- ## Key principles
		- **Technology honesty** — Name stacks where it aids comprehension (“PostgreSQL”, “Kotlin service”, …).
		- **Communication edges** — Prefer labelled relationships over a spaghetti of anonymous lines.
	- ## Mechanism
		- **Zoom in** on a single container to produce [[C4/Diagram/3 - Components]] for that boundary.
	- ## Examples
		- **Browser SPA** → **BFF API** → **domain services** → **OLTP database** + **object store** for attachments.
	- ## Misconceptions
		- “**One box per repo**” — **Heuristic at best**; some repos host **multiple** containers, or **one** container spans repos—model **runtimes**, not git topology.
		- “**Same as deployment diagram**” — **Different question**; [[C4/Diagram/Deployment]] maps software to **infrastructure**, not only logical containers.
