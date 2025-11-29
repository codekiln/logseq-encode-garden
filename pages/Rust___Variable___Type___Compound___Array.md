- unlike [[Rust/Variable/Type/Compound/Tuple]], every element must have the **same type**
	- in this aspec it's similar to [[Py/TypedDict]]
	- the type can use rust's type inference; you don't need to be explicit. In that sense it's perhaps a bit like python's type checking
	- ```rust
	  fn test_arrays() {
	      let a = [1, 2, 3, 4, 5]; 
	    	// rust analyzer will turn this into ...
	      let a: [i32; 5] = [1, 2, 3, 4, 5];
	    
	    	let months = ["January", "February", "March", "April", "May", "June", "July",
	                "August", "September", "October", "November", "December"];
	  
	  }
	  
	  
	  ```
- has a **fixed length**
-