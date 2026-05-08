tags:: [[dotfiles]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Matan Kushner]]
via:: https://github.com/matchai/dotfiles

- # [matchai/dotfiles](https://github.com/matchai/dotfiles)
	- ## [[My Notes]]
		- Clear, minimal directory structure.
	- ## [./files](https://github.com/matchai/dotfiles/tree/main/files)
		- [dotfiles/files/git-message](https://github.com/matchai/dotfiles/blob/main/files/git-message)
		- [dotfiles/files/instructions.md](https://github.com/matchai/dotfiles/blob/main/files/instructions.md) - a minimal [[git/commit/message/template]]
			- these are Matan's instructions to [[AI/LLM]]s on how to think of him; it's basically it's a personal context portfolio.
			- I appreciate the rhetoric. short, clear, to the point. explains himself the way he would to another engineer.
			- of note
				- privacy
					- > Never reference internal projects, tools, or services in commits/PRs to external or OSS repositories
				- git; avoid merge conflicts and don't rewrite history
					- > Never amend commits. Always create new commits to fix issues
				- code style
					- > Left align the happy path. Early returns over nesting
				- tooling
					- [[find]] -> [[fd]]
					- [[grep]] -> [[ripgrep]]
					- Use  [[Context7]]  for code generation and library documentation
					- Use  [[gh/grep]]  to search code examples from github
					- Never browse [[node_modules]] to read dependency source code. Instead, use [[opensrc]]
						- `opensrc path <pkg>` fetches the actual repo at the installed version with full source, tests, and docs. `node_modules` often contains transpiled/bundled output that's harder to reason about
						- When investigating how a dependency works internally, load the `opensrc` skill first. Never read files under node_modules, vendor, or similar dependency directories
				-