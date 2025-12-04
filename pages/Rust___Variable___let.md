- [[Examples]]
	- ```rust
	  let foo = 1; // implicit typing
	  let foo: u32 = 1; // explicit typing
	  ```
- `let` can only be used in function local scope
- unlike `const`, it's not required to have a type annotation, but [[Rust/analyzer]] will likely make it difficult to create a new one without inserting the type, e.g. it will change `let foo = 1` to `let foo: u32 = 1`
- [[Rust/mut]] - `let mut count = FOUR;`
	- `mut` is a `let` suffix that makes the variable mutable
- ### comparison - [[Typescript]]'s `let` keyword vs Rust's `let` keyword
	- Typescript `let`
		- mutable by default
		- reassignment is always allowed:
			- ```ts
			  let x = 4;
			  x += 1;
			  console.log(`${x}`); // 5
			  ```
	- Rust `let`
		- immutable by default
		- reassignment is only allowed
			- 1 - if followed with [[Rust/mut]] keyword
				- ```rust
				  let mut x = 5;
				  ```
			- 2 - if `let` is redeclared, which is what rustacians call [[Rust/Variable/Shadowing]]
				- ```rust
				  let x = 5;
				  let x += 1;
				  println!("{x}"); // 6
				  ```
- ### doesn't need initialization
	- this compiles just fine:
		- ```rust
		  let x;
		  let cond: bool = false
		  if cond { x = 5; } else { x = 6; }
		  println!({x}); // 6
		  ```
		- Lesson: just because x is immutable by default doesn't mean it has to be initialized with a value. It can be a placeholder for something that's filled up later.