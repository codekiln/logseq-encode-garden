alias:: [[Composition vs Inheritance Trade-Off]]
logseq-entity:: [[Logseq/Entity/Concept]], [[Logseq/Entity/Trade-Off]]
- # [[Software/Composition]] vs [[Software/Inheritance]]
	- ## Summary
		- Composition and inheritance are ways to reuse and vary software behavior. Composition places variation in replaceable collaborators; inheritance places it in a parent-child hierarchy. The choice affects coupling, extension, and how behavior is traced.
	- ## The Trade-Off
		- ### [[Software/Composition/vs/Inheritance/Composition]]
			- {{embed [[Software/Composition/vs/Inheritance/Composition]]}}
		- ### [[Software/Composition/vs/Inheritance/Inheritance]]
			- {{embed [[Software/Composition/vs/Inheritance/Inheritance]]}}
	- ## In practice
		- Composition often fits when behavior needs independent variation or collaborators can be replaced. Inheritance can fit when a subtype truly preserves the parent contract and the hierarchy represents that relationship.
		- The approaches can be combined: a subtype may itself use composition. A choice should follow the needed relationship and its costs.
