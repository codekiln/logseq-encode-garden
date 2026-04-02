logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Software/Paradigm/Object-Oriented]]
see-also:: [[Programming/Language/Func]], [[Programming/Language/General Purpose]]

- # Object-oriented programming
	- Canonical on-disk page under **[[Programming/Language/Concept/Object-Oriented]]**; **[[Software/Paradigm/Object-Oriented]]** is an **`alias::`** so paradigm-oriented links resolve here without a separate `Software/Paradigm/` file.
	- ## Overview
		- Object-oriented programming (OOP) organizes programs around **objects**: bundles of **state** (fields) and **behavior** (methods or messages), grouped by **classes** or prototypes, with **polymorphism** so the same interface can name different implementations.
		- It matters because many problem domains map naturally to “things” with lifecycles (UI widgets, accounts, documents); OOP supports **encapsulation** (hide invariants behind interfaces) and **substitutability** (program to abstractions).
	- ## Context
		- Historical roots include **Simula** and **Smalltalk**; mainstream adoption through **C++**, **Java**, **C#**, **Python**, **Ruby**, **JS** (prototype-based), etc.
		- OOP often coexists with **imperative** mutation and, in modern languages, with **functional** features (lambdas, immutable collections).
		- Contrast with **[[Programming/Language/Func]]** (expression-oriented, immutability-first, minimal shared mutable state) while noting many teams use **both** on the same codebase.
	- ## Key Principles
		- **Encapsulation** — Keep internal representation private; expose a stable contract.
		- **Abstraction** — Types or protocols describe *what* clients may rely on, not every implementation detail.
		- **Polymorphism** — Call the same interface on different concrete types (subtyping, interfaces, protocols, duck typing).
		- **Inheritance vs composition** — Class-based OOP offers **implementation inheritance**; modern guidance often prefers **composition** and small interfaces over deep hierarchies.
	- ## Mechanism
		- **Class-based** languages (Java, C#, Python) define objects from class templates; **prototype-based** JavaScript historically used delegation chains.
		- **Message passing** (Smalltalk-style): objects communicate by **sending messages**; the receiver decides how to handle them—contrast with purely static dispatch in some systems.
		- **Dynamic dispatch** — Method resolution at runtime based on the actual object type; static languages approximate with `virtual` methods, interfaces, or generics with bounds.
	- ## Examples
		- **Smalltalk** and **Ruby** emphasize message passing and open classes; **Java** and **C#** emphasize interfaces and class hierarchies with controlled extension.
		- **GUI toolkits** and **game entities** are classic OOP-shaped domains; **domain-driven design** often expresses aggregates as objects.
	- ## Misconceptions
		- “OOP = always good modeling” — **False**; anemic domain models and god objects are common failure modes; design discipline still required.
		- “Everything must be an object” — **False**; many successful hybrids use plain data (structs, records) plus behavior only where it earns its keep.
		- “OOP and FP are opposites” — **Oversimplified**; immutability, first-class functions, and objects coexist in **multi-paradigm** languages.
