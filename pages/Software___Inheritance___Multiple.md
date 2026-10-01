logseq-entity:: [[Logseq/Entity/Concept]]

- # Multiple inheritance
	- ## Overview
		- Multiple inheritance lets a class inherit from more than one parent. The class makes an [[Software/Inheritance/Is-A]] claim toward each of its parents at once.
	- ## Mechanism
		- When two parents define the same member, or both descend from a shared ancestor, the language needs a rule for which definition applies. Python orders the parents with the C3 linearization; C++ requires the call to name the parent and uses virtual inheritance to keep one copy of a shared ancestor.
		- Mixins and traits are a constrained form: one main parent, plus units of behavior added alongside it.
	- ## Trade-off
		- [[Software/Inheritance/Multiple/vs/Single]] weighs multiple inheritance against single inheritance.
