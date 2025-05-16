tags:: [[Py/Lib]], [[Framework]] 
alias:: [[pre-commit]]

- # [pre-commit](https://pre-commit.com/)
	- [[Py/Lib/pre-commit/GitHub/pre-commit]] [pre-commit/pre-commit: A framework for managing and maintaining multi-language pre-commit hooks.](https://github.com/pre-commit/pre-commit)
	- ## [[My Notes]]
		- [[2025-05-16 Fri]]
			- I started using this to actually manage installation of locally defined git hooks in a way that can extend to hooks written in any language.
			- #Thought This #Framework for multi-language pre-commit hooks is part of a class of tools that work across any [[Programming Language]].
			- Uses [[yaml]] for  [[Py/Lib/pre-commit/.pre-commit-config.yaml]]. The way they document the valid parameters is intuitive but not one I've seen before; first they list a table of top-level attributes, then they list tables for nested attributes and their valid values.
			- [[Core Developers]] work at [[Reddit]]
				- [[Person/Ken Struys/GitHub]] [struys (Ken Struys)](https://github.com/struys)
				- [[Person/Chris Kuehl/GitHub]] [chriskuehl (Chris Kuehl)](https://github.com/chriskuehl)
	- ## Intro
		- ### Impetus
			- > Some ... linters are written in languages that you do not ... have installed on your machine ... For example `scss-lint` is ... in [[Ruby]] ... you should be able to use [[scss-lint]] as a [[Git pre-commit hook]] without adding a [[Ruby/Gemfile]] to your project or understanding how to get [[scss-lint]]
			- > a multi-language package manager for pre-commit hooks. You specify a list of hooks you want and `pre-commit` manages the installation and execution of any [[Git Hook]] written in any language before every commit
	- ## [[Py/Lib/pre-commit/Installation]]
		- ### 1 - install the library
			- `pip install pre-commit`
		- ### 2 - create a [[Py/Lib/pre-commit/.pre-commit-config.yaml]]
			- you can generate a very basic configuration using the [[CLI]] with   [`pre-commit sample-config`](https://pre-commit.com/#pre-commit-sample-config)
			- #Example with [[Py/Lib/black]] the [[Programming/Language/Formatter]]
				- ```yaml
				  repos:
				  -   repo: https://github.com/pre-commit/pre-commit-hooks
				      rev: v2.3.0
				      hooks:
				      -   id: check-yaml
				      -   id: end-of-file-fixer
				      -   id: trailing-whitespace
				  -   repo: https://github.com/psf/black
				      rev: 22.10.0
				      hooks:
				      -   id: black
				  ```
					- You just list [[GitHub/Repos]] that are written as plugins
		- ### 3 - install [[Git Hooks]]
			- `pre-commit install` - [[Py/Lib/pre-commit/CLI/install]]
		- ### - 4 - optional - run against all files
			- `pre-commit run --all-files` [[Py/Lib/pre-commit/CLI/run/--all-files]]
			-
			-
		-