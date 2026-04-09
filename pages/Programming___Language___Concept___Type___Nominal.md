tags:: [[Term]]
alias:: [[Nominal Typing]]
see-also:: [[Programming/Language/Concept/Type/Structural]], [[Programming/Language/Concept/Interface]]

- # Nominal typing
	- **Nominal typing** assigns a type to a value because the type **was declared** to implement **Vehicle**, not merely because it has `wheelCount` and `honk`.
	- Shorthand: **you count as a `Vehicle` because you declared conformance.** Conformance is **name-based** and usually **explicit**.
	- That is the usual setup for **interface-style** abstractions in [[Java]]-like stacks: **`Car` implements `Vehicle`**, `extends` a trait, `impl Vehicle for Truck`, and similar.
	- ## Languages
		- ### [[Scala]]
			- A `trait` names the contract; the implementing type **declares** `extends`.
			- ~~~
			  trait Vehicle {
			    def wheelCount: Int
			    def honk(): String
			  }

			  def driveThroughCity(v: Vehicle) = v.honk()
			  ~~~
			- Conformance is explicit, e.g. `class Car extends Vehicle`.
		- ### [[Java]], [[C#]], [[Kotlin]]
			- `interface Vehicle` with `implements`: the concrete type **must** declare the relationship, e.g. `class Car implements Vehicle`.
		- ### [[Rust]]
			- `trait Vehicle` with explicit `impl Vehicle for Car`.
		- ### [[Swift]]
			- `protocol Vehicle`; types declare conformance, e.g. `extension Car: Vehicle`.
		- ### [[Typescript]]
			- `interface Vehicle` and `implements Vehicle` read like nominal code, but the checker still matches **structure** at the type level.
	- ## Nominal vs structural
		- ~~~
		  How do we know this value is allowed to “be a Vehicle”?

		  explicit declaration  <--------------------->  structural match
		       (nominal)                                    (shape)

		  Java / Scala trait              Go / TypeScript / Python Protocol
		  ~~~
		- Nominal systems sit on the **declaration-first** side of that axis.
	- ## Terminology
		- **Nominal interface** — `interface`, `trait`, `protocol` in [[Swift]], explicit `impl` in [[Rust]]; common in [[Scala]], [[Java]], [[Rust]], [[Swift]], [[Kotlin]], [[C#]].
