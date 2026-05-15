tags:: [[mise/Commands]]

- # [mise activate | mise-en-place](https://mise.jdx.dev/cli/activate.html)
	- **Usage**: `mise activate [FLAGS] [SHELL_TYPE]`
	- **Source code**: [`src/cli/activate.rs`](https://github.com/jdx/mise/blob/main/src/cli/activate.rs)
	- Initializes mise in the current [[Shell]] session.
	- This should go in [[zsh/.zshrc]], [[Bash/.bashrc]], [[Bash/.bash_profile]], etc:
		- `eval "$(mise activate zsh)"`
	- ## What does [[mise/activate]] actually do? [[card]]
		- it makes it so that [every time the prompt is displayed](https://mise.jdx.dev/dev-tools/shims.html#overview),
			- it updates the [[mise/Environment]] declarations
			- it makes [[mise/Tool]]s available
		-