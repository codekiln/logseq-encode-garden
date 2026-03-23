tags:: [[Terminal/Multiplexer]], [[Rust]]
created-by:: [[Person/Aram Drevekenin]]
date-created:: [[2021]]
see-also:: [[tmux]], [[Terminal/Multiplexer]]

- [Zellij](https://zellij.dev/) is a terminal multiplexer written in [[Rust]], designed to be more approachable than [[tmux]] while offering a modern plugin and layout system
	- Created by [[Person/Aram Drevekenin]]; first stable release in 2021
	- ## Platform
		- macOS and Linux
	- ## Language
		- [[Rust]]
	- ## Image Protocol
		- Experimental native support for [[Kitty/Graphics/Protocol]]
		- No passthrough configuration needed (unlike [[tmux]])
		- Relevant for tools like [[yazi]] that display inline images
	- ## Nix
		- Available in nixpkgs as `pkgs.zellij`
		- home-manager module: `programs.zellij`
			- ~~~nix
			  programs.zellij = {
			    enable = true;
			    enableZshIntegration = true;
			    settings = {
			      theme = "catppuccin-mocha";
			      default_layout = "compact";
			    };
			  };
			  ~~~
		- `theme` uses a [[Catppuccin]] flavor; see [[Catppuccin]] for palette details and other apps.
	- ## Notable Features
		- Layout system using KDL config files — define named layouts for projects
		- WebAssembly plugin system — plugins run sandboxed in WASM
		- Floating panes
		- More discoverable UX than tmux — keybindings shown in a persistent status bar
		- Sessions persist after disconnect (like tmux)
