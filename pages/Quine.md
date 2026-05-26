alias:: [[Quine (computing)]]
tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/concept]]
see-also:: [[Book/Gödel, Escher, Bach: an Eternal Golden Braid]], [[Person/Joe Armstrong/Blog]]
via:: [[Person/Joe Armstrong]]
- # Quine
	- ## Overview
		- A quine is a program that takes no input and prints its own source code as its only output.
		- The idea matters because it turns self-reference into something executable: the program is both the description and the thing being described.
	- ## Context
		- Quines are usually treated as exploratory or recreational programs rather than production techniques, but they are a sharp way to think about self-reference, interpretation, and fixed points in programming languages.
		- The term is associated with [[Book/Gödel, Escher, Bach: an Eternal Golden Braid]] and the broader tradition of indirect self-reference.
		- [[Person/Douglas Hofstadter]] [[Quote]]
			- > The name "quine" was coined by Douglas Hofstadter, in his popular 1979 science book Gödel, Escher, Bach, in honor of philosopher Willard Van Orman Quine (1908-2000), who made an extensive study of indirect self-reference, and in particular for the following paradox-producing expression, known as Quine's paradox:
			- > "Yields falsehood when preceded by its quotation" yields falsehood when preceded by its quotation.
	- ## Key Principles
		- A proper quine does not read its own source file, fetch hidden input, or otherwise "cheat" by relying on the surrounding filesystem.
		- The usual trick is to separate the program into printing logic and a textual representation of the whole program, then arrange for each part to emit the other.
		- Languages with strong quoting, reflection, or `eval` facilities can make quines shorter, but the underlying idea is still self-description plus re-emission.
	- ## Mechanism
		- Most quines keep a string or data structure that contains a printable representation of their own body.
		- The runtime prints the surrounding scaffolding, then a quoted or escaped form of that representation, then the remainder of the program.
		- In that sense, a quine is a fixed point of the execution environment: running it preserves the program text instead of transforming it into some unrelated result.
	- ## Examples
		- Quines are common programming puzzles in languages like Lisp, Python, Ruby, JavaScript, C, and shell, with the exact construction shaped by each language's quoting rules.
		- They are also a useful bridge between playful code-golf culture and deeper results such as recursion theorems and self-referential constructions.
	- ## Misconceptions
		- A program that simply copies its file from disk is related, but it is not usually considered a proper quine.
		- A quine does not need to be practically useful in product code to be conceptually useful; its value is mostly explanatory rather than operational.
