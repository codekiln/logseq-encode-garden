- you can use [[Rust/Variable/let]] on the same var more than once. Subsequent or nested use "shadows" prior use, following traditional scoping rules in c-family languages. Technically this is just a new binding.
- ```rust
   let x = 5;
   println!("Initial x: {x}"); // 5
   let x = x + 1; // Shadowing
   println!("Shadowed x: {x}"); // 6
   {
       let x = x * 2; // Shadowing in inner scope
       println!("Inner scope x: {x}"); // 8
   }
   println!("Outer scope x: {x}"); // 6
  ```
- The rules of shadowing also work with [[Rust/mut]] - but mutations, in this case can only happen in the scope in which they are (re-)defined.
	- ```rust
	  let mut x = 20;
	  println!("Initial x: {x}"); // 20
	  {
	      let mut x = x;
	      x += 2;
	  }
	  println!("After mutation x: {x}"); // 20
	  ```