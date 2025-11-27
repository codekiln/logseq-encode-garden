# Result<T, E>
	- A fundamental [[Programming/Enum]] in [[Rust]] used for error handling, representing either success or failure
	- Part of [[Rust/prelude]], so it's automatically imported
	- Defined in `std::result::Result`
	- ## Definition
		- ~~~rust
		  enum Result<T, E> {
		      Ok(T),
		      Err(E),
		  }
		  ~~~
		- `T` - the type of the value in the `Ok` variant
		- `E` - the type of the error in the `Err` variant
	- ## Variants
		- ### Ok(T)
			- Represents a successful operation
			- Contains the successful value of type `T`
		- ### Err(E)
			- Represents a failed operation
			- Contains error information of type `E`
	- ## Common Methods
		- ### Checking Variants
			- `is_ok()` - returns `true` if the result is `Ok`
			- `is_err()` - returns `true` if the result is `Err`
		- ### Transforming Values
			- `map<U, F>(self, op: F) -> Result<U, E>` - maps a `Result<T, E>` to `Result<U, E>` by applying a function to the contained `Ok` value
			- `map_err<F, O>(self, op: O) -> Result<T, F>` - maps a `Result<T, E>` to `Result<T, F>` by applying a function to the contained `Err` value
		- ### Chaining Operations
			- `and_then<U, F>(self, op: F) -> Result<U, E>` - calls `op` if the result is `Ok`, otherwise returns the `Err` value
			- `or_else<F, O>(self, op: O) -> Result<T, F>` - calls `op` if the result is `Err`, otherwise returns the `Ok` value
		- ### Unwrapping
			- `unwrap()` - returns the value if `Ok`, panics if `Err`
			- `unwrap_or(default: T) -> T` - returns the value if `Ok`, otherwise returns `default`
			- `unwrap_or_else<F>(op: F) -> T` - returns the value if `Ok`, otherwise calls `op` with the error
			- `expect(msg: &str) -> T` - returns the value if `Ok`, panics with `msg` if `Err`
	- ## Usage Patterns
		- ### Pattern Matching
			- Use `match` to handle both variants:
				- ~~~rust
				  match result {
				      Ok(value) => println!("Success: {:?}", value),
				      Err(error) => println!("Error: {:?}", error),
				  }
				  ~~~
		- ### The `?` Operator
			- Propagates errors up the call stack
			- If `Result` is `Err`, returns early with the error
			- If `Result` is `Ok`, unwraps the value
			- Can only be used in functions that return `Result`
		- ### Example Function
			- ~~~rust
			  fn parse_version(header: &[u8]) -> Result<Version, &'static str> {
			      match header.get(0) {
			          None => Err("invalid header length"),
			          Some(&1) => Ok(Version::Version1),
			          Some(&2) => Ok(Version::Version2),
			          Some(_) => Err("invalid version"),
			      }
			  }
			  ~~~
	- They call each option of enum a `variant`
	- ## Related
		- [[Rust/prelude]] - Result is automatically imported
		- [[Rust/Option<T>]] - Similar enum for nullable values
		- Error handling in Rust typically uses Result for recoverable errors