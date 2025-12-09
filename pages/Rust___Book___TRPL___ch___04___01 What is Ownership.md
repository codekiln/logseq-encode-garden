- [What is Ownership? - The Rust Programming Language](https://rust-book.cs.brown.edu/ch04-01-what-is-ownership.html)
	- [[Rust/Variable]]s by live in the scope of function's stack, and are deallocated at the end of the function.
	- [[Rust/Box]]es, in contrast, live in the heap.
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
	- [[Rust/Ownership]] comes into play in the difference between these two phrases:
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
		-