see-also:: [[My/Principle/Favor Readers Over Writers]], [[My/Principle/Make Illegal States Unrepresentable]]

- # what it means
	- design [[API]]s, [[CLI]]s, and data models so all parts follow the same patterns and conventions
	- when one part of a system teaches the interface, every other part becomes immediately learnable
	- ## [[Examples]]
		- ### [[REST API]] design
			- all endpoints return the same error shape, the same pagination envelope, the same field naming convention
			- callers can apply knowledge from one endpoint to every other endpoint without consulting docs
		- ### [[CLI]] design
			- all subcommands accept `--dry-run` and `--verbose` with the same semantics
			- flag names for similar concepts (e.g. `--output`, `--format`) are spelled identically across commands
		- ### library design
			- a collection type exposes the same iteration, filtering, and mapping interface as built-in types
	- ## [[Why]]
		- consistent interfaces reduce the total interface surface a user must learn
		- when users can predict behavior from pattern-matching, they make fewer errors and need less documentation
		- see also [[My/Principle/Minimize Surface Area]] — uniformity is one way to keep surface area manageable
	- ## source
		- via [[@yminsky]] slide in [[Jane Street]] talk — see [[My/Principle]] for context
