tags:: [[Term]]
alias:: [[Interface]]
see-also:: [[Programming/Language/Concept/Type/Nominal]], [[Programming/Language/Concept/Type/Structural]]

- # Interface (programming language)
	- An **interface** is a **named contract**: operations callers may rely on without fixing one implementation. **Program to an interface, not an implementation.**
	- The name stabilizes vocabulary: **`Vehicle`**, **`PaymentMethod`**, **`UserRepository`**, with many concrete types behind it (`Car`, `Truck`, …).
	- ## Nominal and structural
		- **Nominal typing** — the type **declares** the relationship (`class Car implements Vehicle`, `extends`, `impl Vehicle for Car`, explicit protocol conformance).
		- **Structural typing** — the value **matches** the interface type **without** a declaration if its **shape** fits. [[Typescript]] and [[Go]] are the everyday examples.
		- **Interface** names the boundary; **nominal vs structural** names how the checker enforces it.
	- ## Narrowing
		- A parameter typed to a **smaller** contract **hides** extra methods on the concrete value. Callers only see what **`Vehicle`** promises, even if **`Car`** also has `openTrunk()`:
		- ~~~
		  def planRoute(v: Vehicle) = ...
		  ~~~
		- Related vocabulary: **interface narrowing**, **upcasting**, **capability typing**, **information hiding** at the type boundary.
		- Any static language with subtyping or interface types supports this; it is **discipline** about which type you **expose**, not a separate type system.
	- ## Keywords by ecosystem
		- **[[Java]] / [[Kotlin]] / [[C#]]** — `interface`.
		- **[[Scala]] / [[Rust]]** — `trait`. In [[Rust]] the same keyword covers methods on `self` and generic bounds.
		- **[[Swift]]** — `protocol`.
		- **[[Typescript]]** — `interface` and `type`; the checker is **structural**.
		- **[[Go]]** — `interface`; satisfaction is **implicit** when methods match.
	- ## Interfaces and type classes
		- **Nominal vs structural** is one axis. Another is **where the operations live**:
		- ~~~
		  Where does the behavior live?

		  on the value (methods)     vs     outside the value (instances / dictionaries)
		  interface / trait methods          type class / given / instance
		  ~~~
		- **Interface / trait** — `car.honk()`; behavior on the **receiver**.
		- **Type class constraints** — evidence that operations exist **for** `T`, often passed separately. Example types: **`Car`** with `honk` mediated by a type-class instance:
			- **[[Scala]] 3**
				- ~~~
				  trait Honks[T] {
				    def honk(t: T): String
				  }

				  def inGarage[T](t: T)(using h: Honks[T]) = h.honk(t)
				  ~~~
			- **[[Haskell]]**
				- ~~~
				  class Honks a where
				    honk :: a -> String
				  ~~~
			- **[[Rust]]**
				- ~~~
				  trait Honks {
				      fn honk(&self) -> String;
				  }

				  fn use_vehicle<T: Honks>(v: T) -> String {
				      v.honk()
				  }
				  ~~~
				- The bound still depends on an `impl Honks for …` somewhere.
		- Advanced [[Scala]] / FP also encodes “has these operations” with **traits + generics**, **tagless final**, and similar; those designs **overlap** type classes and compete with plain [[Java]]-style interfaces.
	- ## [[Scala]]
		- Nominal trait: `def f(v: Vehicle)` with `Car extends Vehicle` in scope.
		- Structural: `def f(v: { def honk(): String }) = …` when you want anything with `honk` without a shared trait.
		- Type-class style: behavior via **givens** / implicits, e.g. evidence for **`Honks[Car]`**, not only methods on `v`.
	- ## Terminology
		- **Nominal interface** — conformance declared by name (`implements`, `extends`, `impl … for …`).
		- **Structural typing** — conformance when members match the expected shape.
		- **Capability / narrowing** — smallest useful parameter type.
		- **Type classes** — ad-hoc polymorphism; behavior **for** a type, often **beside** the value.
