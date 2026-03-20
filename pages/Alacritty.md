tags:: [[Terminal/Emulator]], [[Rust]]
created-by:: [[Person/Joe Wilm]]
date-created:: [[2016]]
see-also:: [[Terminal/Comparison]]

- [Alacritty](https://alacritty.org/) is a cross-platform, GPU-accelerated terminal emulator written in [[Rust]]
	- Emphasizes simplicity and performance; intentionally minimal feature set
	- Originally authored by [[Person/Joe Wilm]]; now maintained by a community of contributors
	- ## Platform
		- macOS, Linux, Windows, and FreeBSD
	- ## Language
		- [[Rust]]
	- ## Image Protocol
		- Supports the [[Kitty/Graphics/Protocol]] (added ~2024)
		- Relevant for tools like [[yazi]] that display inline images
	- ## Nix
		- Available in nixpkgs as `pkgs.alacritty`
		- Idiomatic home-manager module: `programs.alacritty`
			- Supports generating `alacritty.toml` config declaratively
			- ~~~nix
			  programs.alacritty = {
			    enable = true;
			    settings = {
			      font.normal.family = "JetBrains Mono";
			      window.opacity = 0.95;
			    };
			  };
			  ~~~
	- ## Notable Features
		- GPU rendering via OpenGL/Metal
		- Vi mode for keyboard-driven selection and navigation
		- No tabs or splits built-in — intentional; delegates to tmux/zellij
		- Config via a single `alacritty.toml` file
