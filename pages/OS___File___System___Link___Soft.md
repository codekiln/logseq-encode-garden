logseq-entity:: [[Logseq/Entity/term]]
alias:: [[Symlink]], [[Symlinks]], [[Symbolic Link]], [[Symbolic Links]], [[Soft Link]], [[Soft Links]]
tags:: [[Term]]
wikipedia-link:: https://en.wikipedia.org/wiki/Symbolic_link
see-also:: [[OS/File/System/Link/Hard]], [[OS/File/System/Link/Concept/Comparison of Different Types]], [[OS/File/System/Link]]
- # Symbolic link (soft link)
	- A **symbolic link** (also **symlink** or **soft link**) is a file whose contents point to another file or directory by storing a path to the target.
	- Unlike a [[OS/File/System/Link/Hard]], a symbolic link is its own file-system object. When a program follows it, the operating system resolves the stored path and continues at the target.
	- ## Advantages
		- **Cross-boundary references** - A symbolic link can point across file systems and, on Unix-like systems, commonly to directories.
		- **Clear indirection** - Tools can usually identify the symlink itself and inspect the stored target path.
		- **Flexible organization** - Symlinks are useful for config files, tool shims, shared project rules, and compatibility paths where one name should lead somewhere else.
	- ## Disadvantages
		- **Dangling links** - If the target path is moved or deleted, the symlink remains but no longer resolves.
		- **Path sensitivity** - Relative symlinks depend on their location; absolute symlinks depend on the same absolute path existing on the current machine.
		- **Traversal complexity** - Programs and security checks must decide when to follow symlinks and when to operate on the link itself.
