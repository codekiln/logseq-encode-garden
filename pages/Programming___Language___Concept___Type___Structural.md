tags:: [[Term]]
alias:: [[Structural Typing]]
see-also:: [[Programming/Language/Concept/Type/Nominal]], [[Programming/Language/Concept/Interface]]

- # Structural typing
	- **Structural typing** accepts a value wherever a **vehicle-shaped** type is expected **if it has the required methods or fields**, whether or not anyone wrote “implements **Vehicle**.”
	- Shorthand: **you count as a `Vehicle` because you match the shape.** The checker cares about members and their types.
	- Opposite pole: **nominal typing**.
	- ## Languages
		- ### [[Scala]]
		  collapsed:: true
			- Inline structural type when you want matching members without a shared nominal `trait Vehicle`:
			- ~~~
			  def driveAway(v: { def wheelCount: Int; def honk(): String }) = v.honk()
			  ~~~
			- **[[Scala]] 2** often uses **reflection** for this; many teams avoid it in hot code. **[[Scala]] 3** keeps structural types; idiomatic code still favors nominal `trait Vehicle` unless there is a concrete reason not to.
		- ### [[Typescript]]
		  collapsed:: true
			- Object types match **by structure**; `implements` is not required for the checker.
			- ~~~
			  type Vehicle = { wheelCount: number; honk(): string }
			  
			  function driveAway(v: Vehicle) {
			    return v.honk()
			  }
			  ~~~
		- ### [[Go]]
		  collapsed:: true
			- Any type with the right methods **satisfies** the `interface` with **no** declaration on the concrete type.
			- ~~~
			  type Vehicle interface {
			      WheelCount() int
			      Honk() string
			  }
			  ~~~
		- ### [[Python]]
		  collapsed:: true
			- `typing.Protocol` gives static checkers a **structural** protocol; at runtime, behavior remains duck typed.
			- ~~~
			  from typing import Protocol
			  
			  class Vehicle(Protocol):
			      def wheel_count(self) -> int: ...
			      def honk(self) -> str: ...
			  ~~~
		- ### [[OCaml]]
		  collapsed:: true
			- Record and object types often match **structurally**; syntax differs, idea is the same.
	- ## Duck typing
		- **Duck typing** is the runtime version: call the method if it exists; **no static proof** before execution.
		- ~~~
		  def driveAway(thing):
		      return thing.honk()
		  ~~~
		- [[Ruby]] and [[JS]] often follow the same idea. A **static** checker that enforces shape is **structural typing**; **duck typing** discovers failures when the call happens.
	- ## [[Scala]] refinements
		- A refinement type alias packages the same “has these members” idea under a name:
		- ~~~
		  type CarLike = {
		    def wheelCount: Int
		    def honk(): String
		  }
		  ~~~
		- `T <: Vehicle` constrains **generics** against a **nominal** trait; it is not the same as a freestanding structural bundle.
	- ## [[JS]] prototypes
		- Behavior is attached along the **prototype chain** at **runtime**:
		- ~~~
		  const car = { honk() { return "beep" } }
		  ~~~
		- Prototypes explain **runtime** lookup. **Structural typing** explains **static** acceptance. Both are shape-flavored; they solve different problems.
	- ## Nominal vs structural
		- ~~~
		  How do we know this value is allowed to “be a Vehicle”?
		  
		  explicit declaration  <--------------------->  structural match
		       (nominal)                                    (shape)
		  
		  Java / Scala trait              Go / TypeScript / Python Protocol
		  ~~~
		- Structural typing is the **shape-first** side of that axis.
	- ## Terminology
		- **Structural typing** — structural types, implicit interface satisfaction in [[Go]], [[Typescript]] object types, [[Scala]] refinements / structural types, [[Python]] `Protocol` for static checkers.