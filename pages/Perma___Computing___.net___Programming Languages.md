## #notes
	- #[[Basic Idea]]
		- *principles of #[[Permaculture]] should compel one to consider the energy impact of programming language choice or even microchip choices*
		  id:: 67b45837-474d-48de-b42a-456660d090f5
- ## [programming languages](https://permacomputing.net/programming_languages/)
	- When assessing programming languages, we should pay attention to
		- How complex is the language? How long would it take to learn all the syntactical details? How long would it take to implement a compiler/interpreter from scratch?
		- Are there several alternative implementations of the language? (It is generally a good sign if there are)
		- What are the [software](../software/) characteristics of these implementations (e.g. disk and memory footprint and compilation speed)? How much resources would it take to [bootstrap](../bootstrapping/) them?
		- How fast and compact is the generated code? What are the overheads and mandatory dependencies like? Does the hello world require bytes, kilobytes, megabytes or gigabytes of memory if all the dependencies are included?
		- Asking "what is the most suitable programming language for permacomputing?" is akin to asking what is "the most suitable plant for permaculture". The entire question contradicts itself.
	- Not all software needs to last for decades, run efficiently or be ultra-secure. However, it is still good if the language does not prevent this.
	- See also
		- [Drew DeVault's blog post about benchmarking compilers by Hello world size](https://drewdevault.com/2020/01/04/Slow.html)
		- [Blog post about a research in energy efficiency of programming languages](https://www.sendung.de/2022-07-24/programming-languages-energy-efficiency/)