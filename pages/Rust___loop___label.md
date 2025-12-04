- when loops are nested in rust, it's possible to lablel them. This is useful if you have to break out of one loop but the other.
- The syntax is `'loop_name: loop { ... break 'loop_name}`.
	- [[Confus/ing]]
		- Syntactically, the (`'identifier`) token shape appears elsewhere in [[Rust/Lifetime]]s, but there it serves a different purpose
		- | Context | Meaning |
		  | ---- | ---- | ---- |
		  | `'label:` before a loop | loop label |
		  | `'label` in `break 'label` | labeled control flow |
		  | `'a` in `&'a T` | lifetime parameter |
		  | `'static` | the static lifetime |
		  | `'_'` | anonymous lifetime |
		- So `'thing` is *not* “the same feature” being reused — it’s the same **token class** used in multiple grammar positions.
- [[Example]]
	- ```rust
	  fn loop_labels_to_disambiguate_multiple_loops() {
	      println!("Loop labels to disambiguate multiple loops:");
	      let mut count = 0;
	  
	      'counting_up: loop {
	          println!("count = {count}");
	          let mut remaining = 10;
	  
	          loop {
	              println!("remaining = {remaining}");
	              if remaining == 9 {
	                  break;
	              }
	              if count == 2 {
	                  break 'counting_up;
	              }
	              remaining -= 1;
	          }
	  
	          count += 1;
	      }
	      println!("End count = {count}");
	  }
	  ```