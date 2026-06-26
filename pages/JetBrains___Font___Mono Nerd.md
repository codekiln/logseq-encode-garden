logseq-entity:: [[Logseq/Entity/Font]]
is-nerd-font:: true
see-also:: [[Font/Nerd Font]], [[Font/nerdfonts]]

- # [JetBrains Mono](https://www.jetbrains.com/lp/mono/) — Nerd Font variant
	- A monospaced programming typeface designed for developers, patched with [[Font/Nerd Font]] icon glyphs for terminal icon and glyph rendering.
	- ## Install
		- ~~~sh
		  brew install --cask font-jetbrains-mono-nerd-font
		  ~~~
	- ## Font-family strings
		- `JetBrains Mono` — base font-family string; works in terminals when the nerd font cask is installed.
		- `JetBrainsMonoNL Nerd Font` — explicit nerd font variant (NL = no ligatures).
		- `JetBrainsMonoNL Nerd Font Mono` — fixed-width glyph variant preferred by some terminal emulators.
	- ## Used in
		- [[Ghostty]], [[Kitty]], [[Alacritty]], and [[WezTerm]] reference this font in their Nix home-manager config examples.
	- ## Nerd Font
		- Patched by the [[Font/nerdfonts]] project; see [[Font/Nerd Font]] for glyph coverage and icon rendering background.
