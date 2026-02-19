- # `$VISUAL`
	- A [[POSIX]]-defined [[EnvVar]] that specifies the user's preferred **screen-oriented** (full-screen) text editor.
	- Defined in IEEE Std 1003.1 (POSIX.1), under the "Environment Variables" chapter.
	- ## Convention
		- Programs should check `$VISUAL` **before** [[EnvVar/EDITOR]]. The distinction dates back to when terminals could be either line-oriented (e.g., `ed`) or screen-oriented (e.g., `vi`).
		- Modern tools like [[chezmoi/edit]], [[tmux/oh-my-tmux]], and [[Claude Code]] all respect this variable.
	- ## Examples
		- Setting in [[Bash/.bashrc]] or [[Zsh/.zshrc]]:
		  ~~~bash
		  export VISUAL="nvim"
		  ~~~
	- ## See also
		- [[EnvVar/EDITOR]] - the companion variable for line-oriented editors
