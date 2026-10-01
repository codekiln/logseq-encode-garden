alias:: [[Multiple vs Single Inheritance Trade-Off]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Trade-Off]]
see-also:: [[Software/Composition/vs/Inheritance]], [[Software/Inheritance/Is-A]]

- # [[Software/Inheritance/Multiple]] vs Single Inheritance
	- ## Summary
		- Under single inheritance a class has one parent, so every inherited member traces up one chain. Under multiple inheritance a class may name several parents, which fits an object that really is several kinds of thing at once. The cost of the second is conflict: two parents can define the same member, or reach a shared ancestor by two paths, and the language needs a rule that decides which definition wins.
		- Languages draw the line in different places. C++ and Python allow several parent classes. Java allows one parent class and any number of interfaces, and since Java 8 an interface can carry default method bodies, so a class that inherits two conflicting defaults must override the method. Ruby modules and Scala traits are mixins: single inheritance for the main chain, with extra behavior mixed in.
	- ## The Trade-Off
		- ### [[Software/Inheritance/Multiple/vs/Single/Multiple]]
			- {{embed [[Software/Inheritance/Multiple/vs/Single/Multiple]]}}
		- ### [[Software/Inheritance/Multiple/vs/Single/Single]]
			- {{embed [[Software/Inheritance/Multiple/vs/Single/Single]]}}
	- ## How the balance is struck
		- Keep one main lineage and let extra parents add capabilities that do not overlap with it. Mixins and traits follow this pattern.
		- When parents can overlap, state the resolution order and keep it predictable. Python computes a method resolution order with the C3 linearization, so the order in which bases are listed decides which parent wins.
		- When the extra parent is something the class uses rather than something it is, [[Software/Composition]] fits better; [[Software/Composition/vs/Inheritance]] weighs that choice.
	- ## In this garden
		- [[Logseq/Entity]] lets one page declare several entity types, primary first, and the page satisfies the shape rules of each. That is multiple inheritance of page-shape rules, with the listed order as the resolution order. [[Logseq/Entity/Hierarchy/Discussion]] works out where its limits sit.
	- ## Sources
		- [Multiple Inheritance of State, Implementation, and Type](https://docs.oracle.com/javase/tutorial/java/IandI/multipleinheritance.html) in the Java Tutorials covers interfaces, default methods, and conflict rules.
