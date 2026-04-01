tags:: [[Flashcard]]

- [Card Format - repeater](https://shaankhosla.github.io/repeater/card-format.html)
	- they can be anywhere
		- ```
		  flashcards/
		    math.md
		    science/
		        physics.md
		        chemistry.md
		  
		  ```
	- `repeater` scans `.md` files for various [parsing signals](https://shaankhosla.github.io/repeater/card-format.html#parsing-logic)
		- lines that begin with `Q: ` and `A: ` so you can mix flashcards with your notes.
			- Basic Card format
				- ```
				  Q: What is Coulomb's constant?
				  A: The proportionality constant of the electric force.
				  ```
			- Multi Line format
				- ```
				  Q: List the SI base units.
				  A: meter (m)
				  kilogram (kg)
				  second (s)
				  
				  ```
		- lines that contain ` :: ` which it interprets as a "one liner" q and a format
			- ```
			  What is Coulomb's constant?::The proportionality constant of the electric force.
			  ```
		- [[Flashcard/Cloze]] lines that start with `C: ` and contain box brackets aka square brackets
			- ```
			  C: The [order] of a group is [the cardinality of its underlying set].
			  ```