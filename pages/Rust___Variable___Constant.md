alias:: [[Rust/const]]

- `const`
- [[Example]]
	- ```rust
	  const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
	  ```
- required to have a [[Rust/Type/Annotation]]
- [[Naming Convention]]: all uppercase with underscores between words
- [[Rust/Expression/Constant]] [Rust Reference’s section on constant evaluation](https://doc.rust-lang.org/reference/const_eval.html)
	- There's a subset of expressions that can be used when creating a const. These are evaluated at [[Compile-time]].
- See also
	- [Variables and Mutability - The Rust Programming Language](https://rust-book.cs.brown.edu/ch03-01-variables-and-mutability.html)