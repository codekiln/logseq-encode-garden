- # `$EDITOR`
	- A [[POSIX]]-defined [[EnvVar]] that specifies the user's preferred **line-oriented** text editor.
	- Defined in IEEE Std 1003.1 (POSIX.1), under the "Environment Variables" chapter.
	- ## Convention
		- Programs that need to open a text editor should check [[EnvVar/VISUAL]] first, then fall back to `$EDITOR`, then to a default (typically `vi`).
		- In practice, most users set both `$VISUAL` and `$EDITOR` to the same value (e.g., `vim`, `nvim`, `nano`).
	- ## Examples
		- Setting in [[Bash/.bashrc]] or [[Zsh/.zshrc]]:
		  ~~~bash
		  export EDITOR="vim"
		  ~~~
	- ## See also
		- [[EnvVar/VISUAL]] - the companion variable for screen-oriented editors
