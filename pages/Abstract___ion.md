tags:: [[Term]]
alias:: [[Abstraction]]
see-also:: [[Declarative]], [[Imperative]]

- # Abstraction
	- Hiding complexity behind an interface so that higher-level reasoning can proceed without knowledge of lower-level details.
	- ## Levels
		- Abstraction works in layers: each level exposes a simplified model and conceals its implementation beneath it.
		- 1. A function abstracts a sequence of steps.
		- 2. A module abstracts a set of functions.
		- 3. An API abstracts an entire system.
	- ## Key Properties
		- **Interface vs. implementation**: the caller sees *what* something does; the abstraction decides *how*.
		- **Information hiding**: irrelevant detail is suppressed, not just renamed.
		- **Composability**: abstractions can be stacked — each layer need only understand the one immediately below it.
	- ## Relation to Declarative Style
		- Abstraction makes [[Declarative]] programming possible: to declare *what* should happen, there must be a layer that handles *how*.
		- [[Imperative]] code is often the implementation layer that a good abstraction hides.
	- ## Leaky Abstractions
		- An abstraction leaks when hidden implementation details escape into the interface — forcing callers to know things the abstraction was supposed to conceal.
