- main thing is that statements get semicolons.
- it's possible to have something which doesn't compile because the last line in the function actually has or doesn't have a semicolon.
	- It needs to have a semicolon if the last line is a statement.
	- It needs to NOT have a semicolon if the last line is a [[Rust/Expression]].
		- ```rust
		  fn main() {
		      let x = plus_one(5);
		  
		      println!("The value of x is: {x}");
		  }
		  
		  fn plus_one(x: i32) -> i32 {
		      x + 1; // <- will not compile
		  }
		  ```
- examples
	- `let y = 1;`
-