alias:: [[Rust Ownership]]

- [[Rust/Book/TRPL/ch/04/01 What is Ownership]]
	- Summary
		- all [[Programming/Concept/Heap]] data must be owned by exactly one variable
		- rust deallocates [[Programming/Concept/Heap]] data once its owner goes out of scope
		- ownership can be transferred with [[Rust/Owner/Move]]s, which happen in [[Rust/Variable]] assignments and [[Rust/Function]] calls
		- [[Programming/Concept/Heap]] data can only be accessed through the current owner, not previous owners
	-
	-