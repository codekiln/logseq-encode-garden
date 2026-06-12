alias:: [[Zsh Init Files]]

- # [[Zsh]] Init File
	- [[Zsh]] reads a sequence of init files on startup. Which files are sourced depends on whether the shell is a **login shell**, an **interactive shell**, or both — and on the OS.
	- ## Load order
		- 1. `/etc/zshenv` → `~/.zshenv` — every shell invocation, including scripts; no exceptions
		- 2. `/etc/zprofile` → `~/.zprofile` — login shells only; on [[macOS]], `path_helper` runs here
		- 3. `/etc/zshrc` → `~/.zshrc` — interactive shells; aliases, prompt, plugins
		- 4. `/etc/zlogin` → `~/.zlogin` — login shells, after `.zshrc`; rarely used
		- On logout: `~/.zlogout` → `/etc/zlogout`
	- ## When to use each file
		- `~/.zshenv` — env vars that non-interactive shells and scripts need (e.g. `EDITOR`, `GOPATH`, `XDG_*`). Runs on every invocation; keep it minimal.
		- `~/.zprofile` — [[PATH]] additions and login-shell-only env setup. The right place on [[macOS]] because it runs *after* `path_helper`.
		- `~/.zshrc` — interactive-only config: aliases, functions, prompt, plugin managers ([[Zsh/OhMyZsh]], etc.). Not sourced by scripts.
		- `~/.zlogin` — deferred login-shell actions; prefer `.zprofile` for almost everything.
	- ## macOS notes
		- Terminal emulators (Terminal.app, [[iTerm2]], [[Warp]]) start **login shells** by default on [[macOS]], unlike most Linux distros.
		- `/etc/zprofile` runs `path_helper`, which reconstructs `$PATH` from `/etc/paths` and files in `/etc/paths.d/`. PATH additions placed in `~/.zshenv` are made *before* `path_helper` and may be reordered. Additions in `~/.zprofile` come *after* and stick at the front.
		- Implication: on macOS, put `export PATH="…:$PATH"` in `~/.zprofile`, not `~/.zshenv`.
	- ## Linux notes
		- Terminal emulators on most Linux distros start **non-login interactive** shells, so `.zprofile` is skipped entirely. Put PATH and env exports in `~/.zshenv` (for scripts) or `~/.zshrc` (for interactive use).
		- When managing dotfiles with [[chezmoi]], use template guards to keep the files correct on both systems:
			- ~~~zsh
			  {{- if eq .chezmoi.os "darwin" }}
			  export PATH="/some/mac/only/bin:$PATH"
			  {{- end }}
			  ~~~
