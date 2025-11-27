- # Pattern Matching
	- A fundamental concept in programming that enables the examination and deconstruction of data structures based on their form
	- Allows developers to specify patterns to which data should conform
	- Facilitates concise and readable code for data extraction, transformation, and control flow
	- ## Definition
		- Involves checking a given sequence of tokens or data structures for the presence of constituents of some pattern
		- Unlike pattern recognition, which may allow approximate matches, pattern matching typically requires an exact match
		- Patterns can take the form of sequences or tree structures
	- ## Key Capabilities
		- **Locating patterns within data**: Finding specific structures or values
		- **Extracting components**: Destructuring data structures to access their parts
		- **Substituting matching patterns**: Replacing matched patterns with other sequences
		- **Control flow**: Directing program execution based on data structure
	- ## Language Implementations
		- ### Functional Languages
			- **Haskell, ML, Scala**: Use pattern matching extensively to destructure data types and control program flow
			- Pattern matching is often used in function definitions
			- Example (Haskell):
				- ~~~haskell
				  factorial 0 = 1
				  factorial n = n * factorial (n - 1)
				  ~~~
		- ### Object-Oriented Languages
			- **C#**: Introduced pattern matching in C# 7.0 for switch statements and expressions
			- **Java**: Added pattern matching features to enhance type checking and data extraction
		- ### Systems Languages
			- **Rust**: Uses pattern matching extensively with `match` expressions for safe data handling
			- **Swift**: Incorporates pattern matching for safer and more expressive code constructs
		- ### Scripting Languages
			- **Python**: Python 3.10 introduced structural pattern matching with `match`/`case` statements
			- Example (Python):
				- ~~~python
				  match command:
				      case ["move", x, y]:
				          move_to(x, y)
				      case ["draw", shape]:
				          draw_shape(shape)
				      case _:
				          print("Unknown command")
				  ~~~
	- ## Historical Context
		- **Early Implementations**: Languages like SNOBOL (1962) and COMIT (1957) were among the first to introduce pattern matching, primarily for string manipulation
		- **Functional Programming**: The ML language (1973) and its successors integrated pattern matching as a core feature
		- **Modern Developments**: Many modern languages have incorporated pattern matching to provide safer and more expressive code constructs
	- ## Common Use Cases
		- **Destructuring**: Extracting values from complex data structures (tuples, structs, enums)
		- **Type checking**: Handling different types or variants in a type-safe manner
		- **Control flow**: Replacing if-else chains or switch statements with more expressive pattern-based logic
		- **Error handling**: Matching on error types and success cases
		- **Data transformation**: Converting between different data representations
	- ## Related
		- [[Rust/match]] - Pattern matching in Rust using `match` expressions
		- [[Programming/Enum]] - Enums are often used with pattern matching
		- [[Programming/Language/Feature]] - Pattern matching as a language feature
		- Functional programming concepts

