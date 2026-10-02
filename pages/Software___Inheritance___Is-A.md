logseq-entity:: [[Logseq/Entity/Concept]]
- # Is-a relationship
	- ## Overview
		- An is-a relationship says that every instance of a more specific kind can be treated as an instance of a more general kind. `MountainBike` is a `Bicycle` only if code written for bicycles can use mountain bikes without losing the behavior it relies on.
	- ## In software
		- [[Software/Inheritance/Class-Based]] often encodes an is-a claim with a subclass declaration. The declaration alone does not prove the claim: an override can break a promise made by the parent.
		- [[Software/Subtyping]] gives the claim a type-level form; behavioral subtyping asks whether substituting the specialized value preserves client expectations.
	- ## Distinction
		- [[Software/Inheritance/Has-A]] means an object contains or uses another object. A `Bicycle` has a `Wheel`, but a bicycle is not a wheel. [[Software/Composition]] commonly models this relationship.
		- The informal English test is useful for spotting a mistaken hierarchy, but behavior and contracts decide whether substitution is sound.
