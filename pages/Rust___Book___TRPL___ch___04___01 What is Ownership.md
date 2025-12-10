- [What is Ownership? - The Rust Programming Language](https://rust-book.cs.brown.edu/ch04-01-what-is-ownership.html)
	- [[Rust/Variable]]s by live in the scope of function's [[Programming/Concept/Stack]], and are deallocated at the end of the function.
	- [[Rust/Box]]es, in contrast, live in the [[Programming/Concept/Heap]].
		- Internally, [[Rust/Collection]]s like [[Rust/Vec]] and [[Rust/String]] use `Box`es.
	- Rust is unique because it does not permit manual memory management.
	- [[Rust/Variable]]s cannot be used after being moved.
		- The following does not compile:
			- ```rust
			  fn main() {
			    let first = String::from("Ferris");
			    let full = add_suffix(first);
			    // does not compile, first has been moved!
			    println!("{full}, originally {first}"); 
			  }
			  ```
		- To get around this, you can clone the string so there are two copies.
	- [[Rust/Owner/ship]] comes into play in the difference between these two phrases:
		- **Box deallocation principle (almost correct):** if a variable **is bound to** a `Box`, when rust deallocates the variable's frame, then Rust deallocates the box's heap memory.
		- **Box deallocation principle (fully correct):** if a `Box` **is owned by** a variable, when Rust deallocates the variable's frame, then Rust deallocates the Box's heap's memory.
			- Here ownership refer s to how variables can fall out of scope.
		- None of the following example compile;
			- ```rust
			  // example 1 
			  let b = Box::new(0);
			  let b2 = b; // this is okay
			  move_a_box(b); // not okay: Box is not owned by b
			  
			  // example 2
			  let b = Box::new(0);
			  move_a_box(b); // Box passed to func. when done, rust deallocates its mem
			  println!("{}", b); // Box is not owned by b
			  
			  // example 3
			  let b = Box::new(0);
			  move_a_box(b); // Box passed to func. when done, rust deallocates its mem
			  let b2 = b; // box is not owned by b
			  ```
		- Here's an example of the compilation error for the first one:
			- code
				- ```rust
				  
				  fn move_a_box(b: Box<i32>) {
				      println!("b in move_a_box: {b}");
				  }
				  
				  fn main() {
				      let b = Box::new(0);
				      println!("b: {b}");
				      let b2 = b;
				      println!("b2: {b2}");
				      // works at this line
				      move_a_box(b2); 
				      // but if you include the next line, 
				      // this will cause compiler error
				      move_a_box(b); 
				  }
				  
				  ```
			- rust panic on compile if last line `move_a_box(b);` is kept in:
				- ```rust
				  error[E0382]: use of moved value: `b`
				    --> exercises/ch04-01-ownership/src/main.rs:12:16
				     |
				   7 |     let b = Box::new(0);
				     |         - move occurs because `b` has type `Box<i32>`, which does not implement the `Copy` trait
				   8 |     println!("b: {b}");
				   9 |     let b2 = b;
				     |              - value moved here
				  ...
				  12 |     move_a_box(b);
				     |                ^ value used here after move
				     |
				  help: consider cloning the value if the performance cost is acceptable
				     |
				   9 |     let b2 = b.clone();
				     |               ++++++++
				  
				  For more information about this error, try `rustc --explain E0382`.
				  error: could not compile `ch04-01-ownership` (bin "ch04-01-ownership") due to 1 previous error
				  ```
		- See [[Rust Ownership]] for a summary
	-
		-