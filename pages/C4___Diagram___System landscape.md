logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/1 - System context]], [[C4/Diagram]]

- # **[System landscape diagram](https://c4model.com/diagrams/system-landscape)** (C4 diagram)
	- ## Overview
		- A **supporting** C4 diagram that zooms **out** from a single system: shows **multiple software systems** (each modeled as a [[C4/Abstraction/1 - Software System]]) and how they fit together across an **enterprise** or **product portfolio**.
		- Like an **interconnected set of context diagrams**—emphasis on **landscape**, not internals.
	- ## Context
		- Listed under “Supporting diagrams” on [[C4/Diagram]]; complements [[C4/Diagram/1 - System context]] when no single system is the sole focus.
	- ## Key principles
		- **Consistent notation** — Reuse the same shapes and relationship language as core C4 so readers do not context-switch.
		- **Strategic clarity** — Favour **stable** system boundaries over project-acronym soup.
	- ## Mechanism
		- Often maintained as a **workspace-level** or **portfolio-level** artefact in architecture-as-code repos.
	- ## Examples
		- All **customer-facing products** plus **shared platform** systems and major **SaaS dependencies**.
	- ## Misconceptions
		- “**Landscape replaces context**” — **No**; context still tells **one** system’s story—landscape shows **many**.
