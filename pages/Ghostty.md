tags:: [[Terminal/Emulator]], [[Zig]]
created-by:: [[Person/Mitchell Hashimoto]]
date-created:: [[2024]]
see-also:: [[Terminal/Comparison]]

- [Ghostty](https://ghostty.org/) is a terminal emulator written in [[Zig]] that aims to be fast, feature-rich, and native on each platform
	- Created by [[Person/Mitchell Hashimoto]] and publicly released in December 2024
	- Notable for using platform-native UI toolkits (AppKit on macOS, GTK4 on Linux) rather than a cross-platform abstraction
	- ## Platform
		- macOS and Linux — no Windows support (intentional, at least initially)
	- ## Language
		- [[Zig]] for the core; platform-native UI (AppKit / GTK4)
	- ## Image Protocol
		- Supports the [[Kitty/Graphics/Protocol]]
		- Relevant for tools like [[yazi]] that display inline images
	- ## Nix
		- Not yet in the official nixpkgs channel (as of early 2026)
		- Official Nix flake provided in the Ghostty repo
			- Install: `ghostty.packages.${system}.default`
		- home-manager module available via the flake
			- ~~~nix
			  programs.ghostty = {
			    enable = true;
			    settings = {
			      font-family = "JetBrains Mono";
			      theme = "catppuccin-mocha";
			    };
			  };
			  ~~~
	- ## Notable Features
		- Native UI on each platform (not electron / cross-platform widget toolkit)
		- Built-in tabs and splits
		- Fast startup and rendering
		- Config format is a simple `key = value` text file
