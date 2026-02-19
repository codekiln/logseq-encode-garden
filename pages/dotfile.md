alias:: [[dotfiles]]

- Files or directories that begin with a dot are typically configuration files for [[CLI/Tool]]s or developer tools
	- [[Examples]]
		- [[Bash/.bashrc]]
		- [[zsh/.zshrc]]
	- Sometimes config files will be called "dotfiles" even if they don't begin with a dot,
		- particularly if they are namespaced to a directory with a dot, e.g. [[mise/Config/mise.toml]]
- Many times, these will be put in source code version control tools like [[git]] in a file called `dotfiles`; see [[dotfile/dotfiles repo]]