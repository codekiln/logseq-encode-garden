logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Game/Video/Dev/Entity Component System]], [[Entity Component System]]
see-also:: [[miniplex]], [[Programming/Language/Concept/Object-Oriented]]
- # Entity Component System
	- ## Overview
		- ECS models a simulation as **entities** (identities), **components** (data attached to those identities), and **systems** (logic that runs over entities matching a component shape).
		- It matters in game development because it helps organize many heterogeneous objects without forcing behavior into deep inheritance trees or monolithic object classes.
	- ## Context
		- ECS is common in game and simulation code where the same update loop needs to touch large sets of entities that share only some aspects: position, velocity, health, input state, render state, and so on.
		- It is often adopted as an alternative to class-heavy [[Programming/Language/Concept/Object-Oriented]] designs when composition starts to scale better than inheritance.
	- ## Key Principles
		- **Entities are identities** — an entity is mainly a handle for “this thing in the world,” not a bag of methods.
		- **Components are data** — components usually store state only; behavior emerges from how systems read and write that state.
		- **Systems are behavior** — systems iterate matching entities and apply one concern at a time: movement, AI, collision, rendering prep, cleanup.
		- **Composition beats inheritance** — adding or removing components changes what an entity can participate in, without reshaping a class hierarchy.
	- ## Mechanism
		- A world or store holds entities and supports queries such as “all entities with position and velocity.”
		- Systems run over those queries during the game loop and update only the component slices they care about.
		- Different ECS implementations make different tradeoffs around storage layout, scheduling, change tracking, and whether systems are first-class runtime objects or just ordinary functions.
	- ## Examples
		- [[miniplex]] is a lightweight example that keeps entities as ordinary JavaScript objects and lets the host app decide how systems are scheduled.
		- Archetype-based ECS engines push harder on cache locality and query performance, while lighter libraries often optimize for API clarity and ease of integration.
	- ## Misconceptions
		- “ECS is just OOP with different names” — not really; the important shift is separating identity, data, and behavior so systems compose across entity kinds.
		- “All ECS implementations look the same” — false; some emphasize data-oriented storage and schedulers, while others stay minimal and library-like.
		- “Using ECS automatically makes a game faster” — false; the payoff depends on the workload, data layout, and whether the architecture actually fits the problem.
