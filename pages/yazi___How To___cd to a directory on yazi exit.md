- via https://yazi-rs.github.io/docs/quick-start#shell-wrapper
	- > We suggest using this `y` shell wrapper that provides the ability to change the current working directory when exiting Yazi.
	- add this to [[zsh/.zshrc]]
		- ```zsh
		  function y() {
		  	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
		  	command yazi "$@" --cwd-file="$tmp"
		  	IFS= read -r -d '' cwd < "$tmp"
		  	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd"
		  	rm -f -- "$tmp"
		  }
		  ```
	- > Then use `y` instead of `yazi` to start, and press q to quit, you'll see the CWD changed. Sometimes, you don't want to change, press `Q` to quit.
	- [[My Notes]]
		- they have sample setups for [[Shell]]s including:
			- [[Bash]]
			- [[zsh]]
			- [[Nushell]]
			- [[POSIX]]
			- [[PowerShell]]
			- [[Windows/Command/Prompt]]
			- [[Xonsh]]
		- I've only recently started hearing about [[Nushell]], and this is the first time I've ever heard of [[Xonsh]].