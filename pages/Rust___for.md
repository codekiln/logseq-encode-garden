- rust has a `for ... in` loop
- [[Example]] of [[Rust/for/in]] for collections
	- ```rust
	  fn looping_with_for() {
	      println!("Looping with for:");
	      let a = [10, 20, 30, 40, 50];
	  
	      for element in a {
	          println!("the value is: {element}");
	      }
	  }
	  ```
- [[Example]] of using [[Rust/range]] expression `(1..4)`
	- ```rust
	  fn main() {
	      for number in (1..4).rev() {
	          println!("{number}!");
	      }
	      println!("LIFTOFF!!!");
	  }
	  ```
	- output
		- ```
		  Looping with for and range:
		  3!
		  2!
		  1!
		  LIFTOFF!!!
		  ```