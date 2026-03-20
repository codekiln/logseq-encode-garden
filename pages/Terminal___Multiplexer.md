tags:: [[Terminal/Multiplexer]]
see-also:: [[Terminal/Comparison]], [[yazi]]

- # Terminal Multiplexer Comparison
	- Covers: [[tmux]], [[Zellij]], [[GNU Screen]]
	- Terminal multiplexers sit between the terminal emulator and the shell; they manage sessions, windows, and panes independently of the terminal itself
	- ## Platform Support
		- macOS, Linux, FreeBSD, and most Unix-like systems
			- [[tmux]], [[GNU Screen]]
		- macOS and Linux
			- [[Zellij]]
	- ## Implementation Language
		- C
			- [[tmux]], [[GNU Screen]]
		- [[Rust]]
			- [[Zellij]]
	- ## Image Protocol Handling
		- Relevant for tools like [[yazi]] that display inline images
		- Passthrough required — multiplexers intercept terminal escape sequences, so image protocols need explicit passthrough support
		- [[tmux]] — passthrough supported via `set -g allow-passthrough on`
			- Without this, [[iTerm2/Image/Protocol]] and [[Kitty/Graphics/Protocol]] are silently dropped
			- Must be set per pane or globally; some versions require `allow-passthrough all`
		- [[Zellij]] — experimental native support for [[Kitty/Graphics/Protocol]]
			- No passthrough config needed; rendered directly
		- [[GNU Screen]] — no image protocol support; images will not display
	- ## Nix Support
		- Idiomatic `programs.*` home-manager module
			- [[tmux]] via `programs.tmux` — very mature, supports plugins declaratively
				- ~~~nix
				  programs.tmux = {
				    enable = true;
				    keyMode = "vi";
				    terminal = "tmux-256color";
				    plugins = with pkgs.tmuxPlugins; [ sensible yank ];
				  };
				  ~~~
			- [[Zellij]] via `programs.zellij`
				- ~~~nix
				  programs.zellij = {
				    enable = true;
				    enableZshIntegration = true;
				  };
				  ~~~
		- Available in nixpkgs; no dedicated home-manager `programs.*` module
			- [[GNU Screen]]
	- ## Notable Creators
		- [[Person/Nicholas Marriott]] — [[tmux]] (original author)
		- [[Person/Aram Drevekenin]] — [[Zellij]] — also created [[Bandwhich]]
		- [[GNU Screen]] — originally by Juergen Weigert and Oliver Laumann (1987)
	- ## Approximate Age (as of 2026)
		- [[GNU Screen]] — ~39 years (1987)
		- [[tmux]] — ~19 years (2007)
		- [[Zellij]] — ~5 years (first stable release 2021)
	- ## Built-in Multiplexers (terminal-native)
		- Some terminal emulators include multiplexing without a separate process
		- [[WezTerm]] — built-in tabs, splits, and panes; also supports tmux multiplexer mode
		- [[Kitty]] — built-in windows and tabs via "OS windows" and "tab bar"
		- Trade-off: terminal-native multiplexing doesn't persist across terminal restarts the way tmux/zellij sessions do
