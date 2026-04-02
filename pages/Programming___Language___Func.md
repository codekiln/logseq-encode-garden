logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Term]], [[Category]], [[Diataxis/Concept]]
alias:: [[Software/Paradigm/Functional]], [[Functional Programming Language]] 
see-also:: [[Software/Paradigm/Object-Oriented]], [[Programming/Language/General Purpose]], [[Declarative]]

- # Functional programming
	- This page is the canonical on-disk home for **functional programming** as both a **paradigm** and a **family of languages**. The title **[[Software/Paradigm/Functional]]** is an **`alias::`** of this page so paradigm-oriented links land here without a separate file under `Software/Paradigm/`.
	- ## Overview
		- Functional programming treats **computation as the evaluation of expressions** built from **pure functions**, **immutable data**, and **explicit composition** (higher-order functions, pipelines, recursion) rather than as sequences of statements that mutate shared state.
		- It matters because it narrows the space of what a program can do between observation points: fewer hidden side effects often yields **easier reasoning**, **safer concurrency**, and **more modular** reuse—at the cost of different idioms and sometimes different performance tradeoffs than imperative or object-oriented styles.
	- ## Context
		- Roots in the **lambda calculus** and early languages (e.g. Lisp family); strong modern lineages include **ML**, **Haskell**, **Erlang/Elixir**, **Clojure**, **F#**, and **Scala**’s functional subset.
		- Most **general-purpose** languages today are **multi-paradigm**: they borrow functional features (first-class functions, `map`/`filter`, immutability helpers) without being “purely” functional end to end.
		- Contrast with **[[Software/Paradigm/Object-Oriented]]** (objects, messages or methods, often mutable state) and with **imperative** programming (loops, assignment, stepwise mutation).
	- ## Key Principles
		- **First-class and higher-order functions** — Functions are values; functions can take and return functions (callbacks, combinators).
		- **Immutability by default** — New values instead of in-place mutation where the paradigm is taken seriously; persistent data structures are common in FP ecosystems.
		- **Referential transparency (ideal)** — In **pure** FP, an expression’s value depends only on its inputs; side effects are pushed to the edges (IO monad, effect systems, etc.) or accepted as pragmatic leaks.
		- **Declarative composition** — Express *what* to compute from *what* (pipelines, queries) more than *how* to mutate memory step by step—overlaps with [[Declarative]] style in places.
	- ## Mechanism
		- **Evaluation strategies** matter in language design: strict vs lazy, tail-call optimization for recursion, and how closures capture environment.
		- **Type systems** range from strong static typing with inference (ML/Haskell) to dynamic Lisps; **algebraic data types** and **pattern matching** often pair with FP.
		- **Runtime models**: garbage collection is typical; concurrent FP often uses **message passing** (Erlang) or **software transactional memory** and immutable sharing.
	- ## Examples
		- Representative **language-level** examples (see also each language page): [[Haskell]], [[Clojure]], [[Elixir]], [[OCaml]].
		- **Library or DSL flavor**: relational or logic query styles (e.g. Datalog-inspired APIs) often feel functional even inside OO hosts.
	- ## Misconceptions
		- “Functional = no side effects ever in the language” — **False** for most real languages; **pure** cores with controlled effects are a design choice, not a universal law.
		- “FP is always slower” — **Oversimplified**; immutability and allocation patterns matter, but compilers and specialized data structures close much of the gap; hot paths differ by domain.
		- “Objects and FP cannot coexist” — **False**; many systems mix **functional style** inside OO languages or use **functional languages** with object-like modules.