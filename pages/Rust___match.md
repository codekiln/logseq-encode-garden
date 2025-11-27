- [`match`](https://rust-book.cs.brown.edu/ch06-02-match.html) expressions do [[Programming/Pattern Matching]]
	- consists of "arms"
	- example
		- ```rust
		  match guess.cmp(&secret_number) {
		          Ordering::Less => println!("Too small!"),
		          Ordering::Greater => println!("Too big!"),
		          Ordering::Equal => println!("You win!"),
		      }
		  ```