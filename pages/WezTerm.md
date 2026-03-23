tags:: [[Terminal/Emulator]], [[Rust]]
created-by:: [[Person/Wez Furlong]]
date-created:: [[2018]]
see-also:: [[Terminal/Comparison]]

- [WezTerm](https://wezfurlong.org/wezterm/) is a cross-platform GPU-accelerated terminal emulator written in [[Rust]]
	- Created and primarily maintained by [[Person/Wez Furlong]]
	- Known for exceptional image protocol support and a Lua-based configuration system
	- ## Platform
		- macOS, Linux, and Windows
	- ## Language
		- [[Rust]]
	- ## Image Protocol
		- Supports both [[iTerm2/Image/Protocol]] and [[Kitty/Graphics/Protocol]]
		- One of the most complete image protocol implementations of any terminal
		- Relevant for tools like [[yazi]] that display inline images
	- ## Nix
		- Available in nixpkgs as `pkgs.wezterm`
		- Idiomatic home-manager module: `programs.wezterm`
			- ~~~nix
			  programs.wezterm = {
			    enable = true;
			    extraConfig = ''
			      return {
			        font = wezterm.font("JetBrains Mono"),
			        color_scheme = "Catppuccin Mocha",
			      }
			    '';
			  };
			  ~~~
		- `color_scheme` uses [[Catppuccin]]; see [[Catppuccin]] for flavors and other tools.
	- ## Notable Features
		- Lua-based configuration (`.wezterm.lua`)
		- Built-in multiplexer (tabs, splits, panes) — no tmux required
		- SSH multiplexer support
		- Extensive image protocol support
		- Fallback fonts and font shaping via HarfBuzz
