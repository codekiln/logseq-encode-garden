logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Software/Paradigm/Declarative vs Imperative]], [[Declarative vs Imperative]]

- # [[Declarative]] vs [[Imperative]]
	- ## Overview
		- Programming paradigms can be broadly grouped by whether code describes ***what*** to compute or ***how*** to compute it.
		- **Declarative** code expresses the desired outcome or constraint, leaving the runtime or compiler to figure out the execution steps — SQL queries, HTML markup, and CSS rules are canonical examples.
		- **Imperative** code specifies an explicit sequence of commands that mutate state to arrive at a result — C, shell scripts, and most mainstream loops are imperative at their core.
		- The distinction matters because declarative code trades control over execution for **readability, correctness guarantees, and optimization opportunities**; imperative code trades those for **precise control over performance and side effects**.
	- ## Context
		- The terms come from linguistics: a declarative sentence states a fact; an imperative sentence issues a command. The analogy is apt — a SQL `SELECT` states what rows we want; a loop with conditionals commands how to find them.
		- Wikipedia characterizes declarative programming as *"a programming paradigm … that expresses the logic of a computation without describing its control flow"* ([Wikipedia: Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming)) and imperative programming as a paradigm that *"uses statements that change a program's state"* ([Wikipedia: Imperative programming](https://en.wikipedia.org/wiki/Imperative_programming)).
		- Most real languages are **multi-paradigm**: Python, JavaScript, and Kotlin support both styles; the question is usually which style dominates a given component or layer.
		- [[Software/Paradigm/Functional]] is often considered a subset of the declarative family, emphasizing pure functions and expressions over procedure sequences. [[Programming/Language/Concept/Object-Oriented]] blends with imperative style but is orthogonal to the declarative/imperative axis.
	- ## Key Principles
		- **What vs How** — Declarative: the program states what result is wanted; the runtime determines how. Imperative: the program specifies each step explicitly.
		- **State mutation** — Imperative programs typically read and write mutable state step by step. Declarative programs tend to avoid or hide mutation behind abstractions.
		- **Control flow ownership** — Imperative code owns control flow (loops, branches, exceptions). Declarative code delegates it to a runtime engine (query planner, reconciler, constraint solver).
		- **Referential transparency (declarative ideal)** — A sub-expression always yields the same result for the same inputs, enabling safe reuse and optimization.
	- ## Mechanism
		- **Declarative execution models**: query planners (SQL, Datalog), reactive rendering engines (React reconciler, CSS layout engine), logic unification (Prolog), constraint solvers (CSS flexbox, linear programming), and dependency-graph build systems (Make, Nix).
		- **Imperative execution models**: register-machine instruction sequences, stack-based bytecodes (JVM, CPython), shell pipelines (sequential commands with exit codes), and event-loop callbacks with mutable closures.
		- **Hybrid layers** are the norm in production code — React component trees are declarative (describe the UI), but event handlers inside them are often imperative (mutate refs, call APIs sequentially).
	- ## Examples
		- 1. **SQL** — `SELECT name FROM users WHERE active = true` is declarative; an equivalent Python loop iterating over rows and filtering is imperative.
		- 1. **HTML/CSS** — Setting `display: flex; justify-content: center` is declarative; computing pixel positions in JavaScript is imperative.
		- 1. **Nix/NixOS** — A Nix expression describes a system configuration; Nix decides how to build and link it. Contrast with shell-script provisioning.
		- 1. **Terraform / Kubernetes YAML** — Describe desired infrastructure state; the tool reconciles current reality to match the spec.
		- 1. **React JSX** — Describe what the UI should look like given current state; the reconciler figures out minimal DOM mutations.
	- ## Misconceptions
		- "Declarative is always better" — **False**; when execution semantics matter (performance, ordering, error recovery), declarative abstraction can hide costs or make them hard to diagnose. Imperative code gives more control.
		- "Functional = declarative" — **Mostly true** in spirit but not definitionally identical. Functional programming is a specific discipline (pure functions, immutability) that is highly declarative; declarative programming is the broader category (SQL is declarative but not functional).
		- "Imperative is lower-level" — **Oversimplified**; OOP is imperative in style but high-level in abstraction. The axis is about who controls flow, not about abstraction height.
		- "You must choose one" — **False**; most production systems layer declarative configuration over imperative business logic, or use a declarative DSL that compiles to imperative code.