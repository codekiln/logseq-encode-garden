- # Destructuring
	- Also known as: unpacking, destructuring assignment
	- A programming concept that allows unpacking values from data structures (arrays, objects, tuples, structs) into distinct variables
	- Simplifies the extraction of multiple values and enhances code readability
	- ## Overview
		- Enables developers to extract multiple values from data structures in a concise and readable manner
		- Particularly useful when dealing with complex data structures or when functions return multiple values
		- Reduces boilerplate code when accessing multiple properties or elements
	- ## Language Implementations
		- ### JavaScript
			- Destructuring assignment allows unpacking values from arrays or properties from objects
			- Array destructuring:
				- ~~~javascript
				  const [first, second] = [1, 2];
				  ~~~
			- Object destructuring:
				- ~~~javascript
				  const { name, age } = { name: 'Alice', age: 25 };
				  ~~~
		- ### Python
			- Tuple unpacking enables assigning values from tuples or lists to variables
			- Tuple unpacking:
				- ~~~python
				  first, second = (1, 2)
				  ~~~
			- Dictionary unpacking (using unpacking operator):
				- ~~~python
				  person = {'name': 'Alice', 'age': 25}
				  name, age = person['name'], person['age']
				  # Or with unpacking:
				  {name, age} = person  # Python 3.8+
				  ~~~
		- ### Rust
			- Pattern matching facilitates destructuring of tuples, structs, and enums
			- Tuple destructuring:
				- ~~~rust
				  let (x, y) = (1, 2);
				  ~~~
			- Struct destructuring:
				- ~~~rust
				  struct Point { x: i32, y: i32 }
				  let point = Point { x: 3, y: 4 };
				  let Point { x, y } = point;
				  ~~~
	- ## Benefits
		- ### Improved Readability
			- Provides a clear and concise way to extract values
			- Makes code easier to understand
		- ### Reduced Boilerplate
			- Eliminates the need for repetitive code when accessing multiple properties or elements
			- Reduces verbosity in variable assignments
		- ### Enhanced Maintainability
			- Simplifies variable assignments
			- Makes code maintenance more straightforward
	- ## Advanced Features
		- ### Default Values
			- Some languages allow setting default values during destructuring to handle undefined or missing properties
			- Example (JavaScript):
				- ~~~javascript
				  const { name = 'Unknown', age = 0 } = person;
				  ~~~
		- ### Nested Destructuring
			- Can be applied to nested data structures
			- May increase complexity and reduce readability if overused
			- Example (JavaScript):
				- ~~~javascript
				  const { user: { name, email } } = data;
				  ~~~
		- ### Rest/Spread Patterns
			- Some languages support collecting remaining elements
			- Example (JavaScript):
				- ~~~javascript
				  const [first, ...rest] = [1, 2, 3, 4];
				  ~~~
	- ## Related
		- [[Programming/Pattern Matching]] - Destructuring is often used with pattern matching
		- [[Rust/Variable/Type/Compound/Tuple]] - Tuple destructuring in Rust
		- Variable assignment and binding

