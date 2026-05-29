logseq-entity:: [[Logseq/Entity/question]]

- # In [[yazi]], if I navigate to a directory, is there a way to exit yazi into that directory?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- Yes — use the official **shell wrapper** function (conventionally named `y`). It launches yazi with `--cwd-file`, which makes yazi write its working directory to a temp file on exit. The wrapper then reads that file and `cd`s your shell to it.
			- **Setup (bash/zsh):** add this function to `~/.bashrc` or `~/.zshrc`:
				- ~~~bash
				  function y() {
				    local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
				    yazi "$@" --cwd-file="$tmp"
				    if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
				      builtin cd -- "$cwd"
				    fi
				    rm -f -- "$tmp"
				  }
				  ~~~
			- **Usage:** type `y` instead of `yazi` to launch. Press `q` to quit and land in the current directory; press `Q` to quit without changing directory.
			- Fish, Nushell, PowerShell, and Windows CMD variants are documented on [Quick Start | Yazi](https://yazi-rs.github.io/docs/quick-start/).
