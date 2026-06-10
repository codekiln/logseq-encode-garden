see-also:: [[My/Principle/Fewer is Better than Many]], [[Unix/Philosophy]], [[My/Principle/Simplify to Avoid Cognitive Load]]

- # what it means
	- [[API]]s and [[CLI]]s are better when they have **fewer responsibilities**
	- prefer a narrow, well-defined contract over a broad, multi-purpose one
	- ## [[Examples]]
		- ### [[CLI]] design
			- a tool that does one thing and accepts only the flags it needs is easier to compose with other tools
			- a tool that accumulates features over time becomes harder to test, document, and maintain
		- ### [[API]] design
			- an endpoint that returns only the fields the caller needs is easier to evolve without breaking clients
			- a function with one clear input contract is easier to mock and test
	- ## [[Why]]
		- smaller surface areas reduce the number of things that can break and the number of things callers must understand
		- every extra flag, field, or mode is a commitment to maintain and a source of unexpected interaction
		- personal application of [[Unix/Philosophy]]'s "do one thing and do it well" to API and [[CLI]] design choices
