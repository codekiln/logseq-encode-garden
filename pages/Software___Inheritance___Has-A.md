logseq-entity:: [[Logseq/Entity/Concept]]
- # Has-a relationship
	- ## Overview
		- A has-a relationship says that one object contains, owns, or uses another as a collaborator. A `Bicycle` has a `Wheel`; it can delegate wheel-related work to that part without becoming a kind of wheel.
	- ## In software
		- [[Software/Composition]] assembles an object from parts with distinct responsibilities. The containing object can expose a stable interface while changing or replacing a collaborator behind it.
		- Ownership is not implied by the phrase alone: a field may own its component, share it, or merely hold a reference. Lifetime and replacement rules belong to the particular design.
	- ## Distinction
		- [[Software/Inheritance/Is-A]] makes a substitutability claim about a specialized kind. A has-a link says how behavior is assembled, not that the containing object is a subtype of its component; [[Software/Subtyping]] explains that separate relationship.
