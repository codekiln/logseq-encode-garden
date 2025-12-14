- # `format!` macro
	- The `format!` macro creates a formatted string by combining text with values
	- Part of Rust's standard library macro family for string formatting
	- ## Overview
		- Returns a `String` containing the formatted text
		- Uses the same formatting syntax as `println!` and `print!` macros
		- Evaluates at compile time where possible
	- ## Syntax
		- ```rust
		  format!(format_string, args...)
		  ```
		- `format_string`: A string literal containing format specifiers
		- `args...`: Values to be formatted and inserted into the string
	- ## Format Specifiers
		- `{}` - Default formatting (uses `Display` trait)
		- `{:?}` - Debug formatting (uses `Debug` trait)
		- `{:#?}` - Pretty-printed debug formatting
		- `{0}` - Positional argument (0-indexed)
		- `{name}` - Named argument
		- `{:width}` - Minimum width
		- `{:0width}` - Zero-padded with minimum width
		- `{:.precision}` - Floating-point precision
		- `{:x}` - Hexadecimal formatting (lowercase)
		- `{:X}` - Hexadecimal formatting (uppercase)
		- `{:o}` - Octal formatting
		- `{:b}` - Binary formatting
	- ## Examples
		- ### Basic Usage
			- ```rust
			  let name = "Alice";
			  let age = 30;
			  let message = format!("Hello, {}! You are {} years old.", name, age);
			  // message = "Hello, Alice! You are 30 years old."
			  ```
		- ### Positional Arguments
			- ```rust
			  let s = format!("{1} and {0}", "second", "first");
			  // s = "first and second"
			  ```
		- ### Named Arguments
			- ```rust
			  let s = format!("{name} is {age} years old", name = "Bob", age = 25);
			  // s = "Bob is 25 years old"
			  ```
		- ### Debug Formatting
			- ```rust
			  let vec = vec![1, 2, 3];
			  let s = format!("{:?}", vec);
			  // s = "[1, 2, 3]"
			  ```
		- ### Number Formatting
			- ```rust
			  let n = 42;
			  format!("{:04}", n);      // "0042" (zero-padded, width 4)
			  format!("{:x}", n);        // "2a" (hexadecimal)
			  format!("{:X}", n);        // "2A" (uppercase hex)
			  format!("{:b}", n);        // "101010" (binary)
			  ```
		- ### Floating-Point Precision
			- ```rust
			  let pi = 3.14159265359;
			  format!("{:.2}", pi);     // "3.14" (2 decimal places)
			  format!("{:.0}", pi);     // "3" (no decimal places)
			  ```
	- ## Related Macros
		- [[Rust/println]] - Print formatted text to stdout with newline
		- [[Rust/print]] - Print formatted text to stdout
		- [[Rust/eprintln]] - Print formatted text to stderr with newline
		- [[Rust/eprint]] - Print formatted text to stderr
		- [[Rust/write]] - Write formatted text to a writer
		- [[Rust/writeln]] - Write formatted text to a writer with newline
	- ## Traits Used
		- `Display` - Default formatting trait (`{}`)
		- `Debug` - Debug formatting trait (`{:?}`)
	- ## Performance
		- Allocates a new `String` on the heap
		- For string concatenation without formatting, consider `String::from()` or `to_string()` methods
		- Formatting is evaluated at compile time when possible
	- ## Related
		- [[Rust/Macro]] - General macro concept in Rust
		- [[Rust/String]] - String type in Rust
		- [[Rust/std/fmt]] - Formatting module in standard library
		- [[Rust/Book/TRPL]] - The Rust Programming Language book
