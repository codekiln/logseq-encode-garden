alias:: [[Programming/Language/Func/Nix]]

- # Nix language
	- A [[Programming/Language/DSL]] for the [[Nix]] ecosystem (store paths, derivations, configuration). Grouped under [[Programming/Language/Func]] in this garden.
	- ## Docs
		- Intro tutorial: [Nix language basics — nix.dev documentation](https://nix.dev/tutorials/nix-language)
		- Language reference: [Nix Language - Nix 2.28.6 Reference Manual](https://nix.dev/manual/nix/2.28/language/index.html)
	- ## How the manual characterizes the language
		- **[[Domain Specific Language]]** — [Built-in functions](https://nix.dev/manual/nix/2.28/language/builtins) connect expressions to the Nix store and declared derivations.
		- **[[Declarative]]** — Dependencies are expressed as data, not as an ordered sequence of execution steps.
		- **Pure** — Values do not change during evaluation; functions are deterministic for the same inputs (see [[Programming/Language/Func]]).
		- **Functional** — Functions are first-class values; they can be named, passed as arguments, and returned (see [[Programming/Language/Func]]).
		- **Lazy** — Expressions are evaluated when their values are needed—non-strict evaluation (see [[Programming/Language/Func]]).
		- **Dynamically typed** — Type mismatches surface when expressions are evaluated, not before (see [[Programming/Time/Run]], “Dynamically typed languages”).