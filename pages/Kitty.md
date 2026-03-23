tags:: [[Terminal/Emulator]]
created-by:: [[Person/Kovid Goyal]]
date-created:: [[2017]]
see-also:: [[Terminal/Comparison]]

- [Kitty](https://sw.kovidgoyal.net/kitty/) is a fast, GPU-based terminal emulator for macOS and Linux
	- Not to be confused with the ProductHunt "Golden Kitty" awards — this is [[Person/Kovid Goyal]]'s terminal, not a product category
	- Created by [[Person/Kovid Goyal]], who also created [[Calibre]]
	- ## Platform
		- macOS and Linux — no Windows support
	- ## Language
		- Written primarily in Python and C
		- C handles the rendering-critical path; Python handles configuration and extension
	- ## Image Protocol
		- Invented the [[Kitty/Graphics/Protocol]], the most capable terminal image protocol
		- Supports full RGBA images, animations, and precise placement
		- Widely adopted by other terminals ([[WezTerm]], [[Alacritty]], [[Ghostty]])
		- Relevant for tools like [[yazi]] that display inline images
	- ## Nix
		- Available in nixpkgs as `pkgs.kitty`
		- Idiomatic home-manager module: `programs.kitty`
			- ~~~nix
			  programs.kitty = {
			    enable = true;
			    font.name = "JetBrains Mono";
			    theme = "Catppuccin-Mocha";
			    settings = {
			      window_padding_width = 8;
			    };
			  };
			  ~~~
		- `theme` uses [[Catppuccin]]; see [[Catppuccin]] for flavors and the rest of the stack.
	- ## Notable Features
		- GPU rendering via OpenGL/Metal
		- Built-in tabs and window splits ("windows" in Kitty terminology)
		- "Kittens" — small terminal programs built on Kitty's Python API
		- SSH kitten for seamless remote sessions with full local config
		- Extensible via Python
