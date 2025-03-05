tags:: [[CLang/Lib]]

- # [Tree-sitter](https://tree-sitter.github.io/tree-sitter/)
	- Tree-sitter is a **parser generator** tool and an **incremental parsing library**. It can build a concrete **syntax tree** for a source file and **efficiently update the syntax tree** as **the source file is edited**. Tree-sitter aims to be:
		- General enough to parse any programming language
		- Fast enough to parse on every keystroke in a text editor
		- Robust enough to provide useful results even in the presence of syntax errors
		- Dependency-free so that the runtime library (which is written in pure [C11](https://github.com/tree-sitter/tree-sitter/tree/master/lib) - [[Programming/Language/C/11]]) can be embedded in any application