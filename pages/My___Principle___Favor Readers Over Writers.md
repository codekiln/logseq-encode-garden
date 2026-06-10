see-also:: [[My/Principle/Create Uniform Interfaces]], [[My/Principle/Make Illegal States Unrepresentable]]

- # what it means
	- code is read far more often than it is written, so optimize for the reader's comprehension over the writer's convenience
	- prefer explicit over terse when explicitness aids understanding
	- ## [[Examples]]
		- ### naming
			- use descriptive variable and function names even when shorter names seem obvious in context
			- name functions for what the caller needs to understand, not for how the implementation works
		- ### structure
			- avoid clever one-liners that compress logic at the cost of readability
			- break a complex expression into named intermediate variables so each step is self-documenting
		- ### [[API]] design
			- surface intent in parameter names and types so callers don't need to read the implementation
	- ## [[Why]]
		- writing code is a one-time event; reading it happens dozens of times across many people and months
		- the cognitive cost of deciphering dense code compounds across every future reader
	- ## source
		- via [[@yminsky]] slide in [[Jane Street]] talk — see [[My/Principle]] for context
