logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
see-also:: [[C4/Diagram/1 - System context]], [[C4/Abstraction/2 - Container]]

- # **[Software system](https://c4model.com/abstractions/software-system)** (C4 abstraction)
	- ## Overview
		- The **highest** C4 abstraction: something that **delivers value** to its users (human or not), including the system you are modelling and **other** systems it depends on (or that depend on it).
		- Often aligned with what a **single team** builds, owns, and can change—sometimes approximated by one repo or a **single deploy boundary**, though organisations use different words (“application”, “product”, “service”, …).
	- ## Context
		- Sits at the top of the decomposition chain under [[C4]]; **not** the same as DDD **bounded contexts**, org **tribes**, or **feature teams**—those may slice reality differently.
		- The usual **zoom-in** target is **containers** inside this boundary ([[C4/Abstraction/2 - Container]]).
	- ## Key principles
		- **Value-oriented** — If it doesn’t plausibly “ship” as a coherent thing users or other systems rely on, it may not be a software system in C4 terms.
		- **Boundary discipline** — External collaborators appear as **other software systems** or **people** at the **context** view, not as vague blobs.
	- ## Mechanism
		- In diagrams, a software system is typically a **single major box** at [[C4/Diagram/1 - System context]]; opening it yields the [[C4/Diagram/2 - Containers]] view.
	- ## Examples
		- An internal **HR portal**, a **customer API platform**, or a **billing service** each might be one software system if teams and ownership match the C4 boundary.
	- ## Misconceptions
		- “**Every** bounded context is a software system” — **Often wrong**; contexts are a modelling tool, not identical to C4’s deploy/ownership box.
		- “**Microservice = software system**” — **Sometimes**; many systems contain **multiple** deployables—those are usually **containers**, not separate software systems, unless ownership and boundary truly differ.
