tags:: [[Terminal/Emulator]]
created-by:: [[Person/George Nachman]]
date-created:: [[2011]]
see-also:: [[Terminal/Comparison]]

- [iTerm2](https://iterm2.com/) is a macOS terminal emulator and replacement for Terminal.app
	- The dominant terminal on macOS for many years, known for its deep macOS integration and extensive feature set
	- Forked from the original iTerm (2002) by Fabian Kaiser; rewritten and greatly expanded by [[Person/George Nachman]]
	- ## Platform
		- macOS only — no Linux or Windows support
	- ## Language
		- Objective-C with some Swift; built on macOS native frameworks (AppKit)
	- ## Image Protocol
		- Invented the [[iTerm2/Image/Protocol]] (also called "inline images protocol"), which many other terminals have since adopted
		- See [[iTerm2/Image/Protocol]] for implementation details
	- ## Nix
		- Available in nixpkgs as `pkgs.iterm2`
		- No `programs.iterm2` home-manager module — macOS-only, so configuration is handled via nix-darwin or by managing the `com.googlecode.iterm2` plist directly
		- Settings can be exported/imported via a `.itermocol` profile file and committed to a dotfiles repo
	- ## Notable Features
		- Shell integration (marks, command history, recent directories)
		- Split panes, tabs, window arrangements
		- tmux integration mode (`tmux -CC`)
		- Inline image display via [[iTerm2/Image/Protocol]]
		- Trigger-based automation
