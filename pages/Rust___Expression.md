- via [Functions - The Rust Programming Language](https://rust-book.cs.brown.edu/ch03-03-how-functions-work.html)
	- > Expressions **evaluate to a value** ... Consider a math operation, such as `5 + 6`, which is an expression that evaluates to the value `11`. Expressions can be part of statements: ... the `6` in the [[Rust/Statement]] `let y = 6;` is an expression that evaluates to the value `6`. **Calling a [[Rust/Function]] is an expression**. Calling a [[Rust/Macro]] is an expression. A new scope block created with curly brackets is an expression, for example:
		- ```rust
		  fn main() {
		      let y = {
		          let x = 3;
		          x + 1
		      };
		  
		      println!("The value of y is: {y}");
		  }
		  ```
		- the expression
			- ```rust
			  {
			      let x = 3;
			      x + 1
			  }
			  ```
			- doesn't have semicolon; it just returns 4.
	-