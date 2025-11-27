- # Enum
	- Also known as: enumeration, enumerated type
	- A distinct data type that consists of a set of named constants, representing a collection of related values
	- Each named constant is called a `variant` (in some languages) or `enumerator`
	- ## Key Benefits
		- ### Improved Readability and Maintainability
			- Using descriptive names instead of arbitrary numbers or strings makes code more self-explanatory
			- Example: `Color.RED` is clearer than using `0` to represent a color
		- ### Type Safety
			- Restricts variables to predefined values, reducing the risk of invalid assignments
			- Ensures only valid, expected values are used, preventing bugs
		- ### Encapsulation
			- Groups related constants within a single data type
			- Organizes code more effectively and reduces errors from using unrelated constants
	- ## Common Use Cases
		- **State Management**: Representing discrete states (e.g., `PENDING`, `IN_PROGRESS`, `COMPLETED`)
		- **Configuration Options**: Defining sets of options or modes (e.g., logging levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`)
		- **Control Flow**: Using enums in `switch` or `case` statements to handle different scenarios
		- **Error Handling**: Representing success/failure states (e.g., `Result<T, E>` in Rust)
		- **Nullable Values**: Representing optional values (e.g., `Option<T>` in Rust, `Optional<T>` in Java)
	- ## Language Implementations
		- ### C
			- Declared using the `enum` keyword
			- Creates a set of named integer constants
			- By default, values start at 0 and increment
			- ~~~c
			  enum Color { RED, GREEN, BLUE };
			  // RED = 0, GREEN = 1, BLUE = 2
			  ~~~
		- ### C++
			- Supports unscoped enums (similar to C)
			- C++11 introduced scoped enums with `enum class` for better type safety
			- Prevents implicit conversions
			- ~~~cpp
			  enum class Color { RED, GREEN, BLUE };
			  // Access: Color::RED
			  ~~~
		- ### Java
			- More robust enums that can have methods and fields
			- Can implement interfaces
			- Each enumerator is an instance of the enum type
			- ~~~java
			  public enum Day {
			      SUNDAY, MONDAY, TUESDAY, WEDNESDAY, 
			      THURSDAY, FRIDAY, SATURDAY;
			  }
			  ~~~
		- ### Python
			- Provided by the `enum` module
			- Enumerators can have custom values
			- Supports iteration
			- ~~~python
			  from enum import Enum
			  
			  class Color(Enum):
			      RED = 1
			      GREEN = 2
			      BLUE = 3
			  ~~~
		- ### Rust
			- Powerful enums that can hold data (sum types / tagged unions)
			- Each variant can have associated data
			- Used extensively for error handling and optional values
			- ~~~rust
			  enum Result<T, E> {
			      Ok(T),
			      Err(E),
			  }
			  ~~~
	- ## Considerations
		- ### Serialization
			- When storing or transmitting enum values, ensure consistent representation (integer, string, etc.)
			- All parts of the system must understand the chosen representation
		- ### Extensibility
			- Adding new values can affect existing code
			- `switch` or `match` statements without default cases may need updates
			- Plan for potential extensions to avoid maintenance challenges
	- ## Related
		- [[Rust/std/result/Result]] - Example of a powerful enum in Rust
		- [[Programming/Language/Feature]] - Language features in general
		- Type safety and type systems
		- Sum types / Tagged unions (in functional programming languages)

