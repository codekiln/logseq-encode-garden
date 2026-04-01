tags:: [[Terminal/Emulator]], [[Zig]]
created-by:: [[Person/Mitchell Hashimoto]]
date-created:: [[2024]]
see-also:: [[Terminal/Comparison]]

- [Ghostty](https://ghostty.org/) is a terminal emulator written in [[Zig]] that aims to be fast, feature-rich, and native on each platform
	- Created by [[Person/Mitchell Hashimoto]] and publicly released in December 2024
	- [[Ghostty/GitHub/ghostty]]
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
		- [Binaries and Packages - Install](https://ghostty.org/docs/install/binary#nix-(macos-binary))
			- In Nixpkgs, Ghostty is available as a repackaging of the official `.dmg` under the package name `ghostty-bin`, not to be confused with `ghostty`, which is the GTK app [available for Nix on Linux](#nix).
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
		- `theme` uses a [[Catppuccin]] flavor; see [[Catppuccin]] for other flavors and wiring [[nvim]], [[tmux]], [[yazi]], and other terminals.
	- ## Notable Features
		- Native UI on each platform (not electron / cross-platform widget toolkit)
		- Built-in tabs and splits
		- Fast startup and rendering
		- Config format is a simple `key = value` text file
	- ## Hyperlinks, [[tmux]], and opening local paths in nvim
		- Context: question filed [[2026_03_22]] — want “click a file path in the terminal → open in nvim” alongside URL-style clicking
		- **Ghostty supports OSC 8 hyperlinks** (clickable regions emitted by programs). Linked text is visually distinct (e.g. dotted underline, hover underline)
			- On **macOS**, **⌘-click** opens the link via the platform; on **Linux**, **Ctrl-click** is the usual pattern
			- **`copy_url_to_clipboard`** can copy the target from regex-detected URLs or OSC 8 hyperlinks
		- **URLs vs file paths**: `https://…` style links are the common case. A bare path in compiler output is **not** automatically clickable unless something wraps it in OSC 8 (or you rely on URL-shaped text Ghostty already recognizes — plain relative paths usually are not)
		- **`file://`**: if a tool emits OSC 8 with `file:///…`, Ghostty still delegates to the **OS default** for that path/type — often not nvim unless you change file associations or register a custom URL handler / wrapper scheme
		- **tmux stack**: use a recent **tmux** (about **3.4+**) and declare hyperlink capability (e.g. `hyperlinks` via `terminal-features`) so OSC 8 sequences survive inside panes; Ghostty remains the emulator that actually handles the click
		- **Reality check for “always nvim”**: not a first-class “tmux feature”; you need **emitters** (build tools, grep wrappers, test runners) that print OSC 8, plus **OS or app-level** routing if you want nvim instead of the default app — otherwise copy-link / yank-path workflows or editor-native navigation (e.g. quickfix, LSP) stay the reliable path