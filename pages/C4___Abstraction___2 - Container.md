logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/2 - Containers]], [[C4/Abstraction/1 - Software System]], [[C4/Abstraction/3 - Component]]

- # **[Container](https://c4model.com/abstractions/container)** (C4 abstraction)
	- ## Overview
		- A **container** is an **application** or **data store**—something that must **run** (or be hosted) to exist: web apps, APIs, mobile apps, databases, file stores, browser clients, server processes, etc.
		- Containers are the **deployable / runnable** pieces that together implement a [[C4/Abstraction/1 - Software System]].
	- ## Context
		- The second zoom level of [[C4]]: answers *what major things **ship** or **run*** and *how they **communicate*** (protocols, sync/async).
		- **Inside** a container, structure is expressed with [[C4/Abstraction/3 - Component]] elements.
	- ## Key principles
		- **Independently runnable** — If it doesn’t start, listen, store, or render as a unit, it is probably not a container.
		- **Technology explicit enough to be useful** — e.g. “PostgreSQL”, “Spring Boot monolith”, “React SPA”—not a vague “layer”.
	- ## Mechanism
		- Rendered as the primary boxes on a [[C4/Diagram/2 - Containers]]; each container hosts one or more [[C4/Abstraction/3 - Component]] groupings in the next zoom level.
	- ## Examples
		- A **single-page web app**, a **GraphQL API service**, a **message consumer**, a **relational database**, an **object store**.
	- ## Misconceptions
		- “**Docker image = container** (C4 sense)” — **Confusing word collision**; a C4 container is an **architectural** runtime unit, not necessarily one Docker container.
		- “**Every JAR / npm package is a container**” — **Usually false**; packaging and modules often map to [[C4/Abstraction/3 - Component]] or [[C4/Abstraction/4 - Code]] instead.
