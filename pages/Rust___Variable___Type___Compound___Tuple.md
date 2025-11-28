- can use [[Programming/Destructuring]]
- can access elements with dot notation, e.g. `my_tuple.1` accesses the 2nd element in the [[Programming/Zero Indexing]] array
- [[Example]]
	- ```rust
	  let my_tuple = (1, 2.0, 'a');
	  let (a, b, c) = my_tuple;
	  println!("Tuple elements: {a}, {b}, {c}");
	  // Tuple elements: 1, 2, a
	  let two_point_zero = my_tuple.1;
	  println!("Accessed second element: {two_point_zero}");
	  // Accessed second element: 2
	  ```
- The tuple **without any values** is [[Rust/unit]]. This value and its corresponding type are both written `()` and represent an empty value or an **empty return type**. Expressions implicitly return the unit value if they don’t return any other value.
- Variables can use [[Rust/mut]] with [[Rust/Variable/let]] to make mutable tuples.
	- [[Example]]
		- ```rust
		  fn test_tuple_mutation() {
		      let mut x: (i32, i32) = (1, 2);
		      x.0 = 0;
		      x.1 += 5;
		  }
		  ```