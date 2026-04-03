logseq-entity:: [[Logseq/Entity/concept]]
alias:: [[Software Architecture]], [[Software/Architecture]]
see-also:: [[C4]], [[Architecture/Decision/Record]], [[Structurizr]]

- # Software architecture
	- ## Overview
		- **Software architecture** names the **major structures** of a software system—the **parts**, their **responsibilities**, and the **rules** governing how they relate—so that the system stays **understandable**, **evolvable**, and **fit for its quality goals** (performance, security, operability, cost, etc.).
		- It is not only **diagrams**; it is the set of **decisions** that are costly to reverse plus the **shared mental model** a team uses when changing the system.
	- ## Context
		- Sits between **product intent** and **implementation detail**: narrower than “everything about the system,” broader than a single module or framework choice.
		- Overlaps with **design** and **engineering leadership**; in many organisations, “architecture” highlights **cross-cutting** or **long-lived** choices (integration, data ownership, deployment shape, failure modes).
		- Common **views** and notations include the **[[C4]]** model, ADRs (**[[Architecture/Decision/Record]]**), and architecture-as-code tools such as **[[Structurizr]]**—each answers different audiences and lifecycles.
	- ## Key principles
		- **Stakeholder fit** — Architecture is **good** only relative to stated **drivers** (latency, compliance, team topology, time-to-market); there is no universal “best” shape.
		- **Constraints and trade-offs** — Prefer explicit **trade-off** language over buzzwords; every important gain usually costs something elsewhere.
		- **Integrity over time** — Guard **boundaries**, **interfaces**, and **invariants** so incremental work does not silently erode the model.
	- ## Mechanism
		- Practitioners capture architecture through **models** (structural, deployment, runtime), **records** (ADRs, RFCs), **reviews**, and **linting or validation** in code when possible.
		- **Refactoring** and **strangling** legacy areas are architecture work as much as greenfield diagrams.
	- ## Examples
		- Choosing **sync vs async** integration between bounded areas; defining **service** or **module** boundaries aligned with team ownership.
		- Publishing a **container-level** diagram for onboarding and incident response; using **C4** context + container views as the default communication set.
	- ## Misconceptions
		- “**Architecture = ivory tower before coding**” — **Often false**; healthy architecture is **continuously** refined as the system and risks become visible.
		- “**One UML diagram is enough**” — **Usually insufficient**; different stakeholders need **different abstractions** (see **[[C4/Diagram]]** for a structured split).
		- “**Microservices = good architecture**” — **Oversimplified**; distribution is a **cost** you pay for specific scaling or organisational goals, not a quality in itself.
