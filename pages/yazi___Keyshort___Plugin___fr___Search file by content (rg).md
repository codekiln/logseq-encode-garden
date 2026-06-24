- [[Keyshort]] [[yazi]] [[yazi/Keyshort]] [[yazi/Keyshort/Plugin/fr]]
	- **Search file by content with rg (fr.yazi)** [[Keyshort/User]] #card
	  card-last-interval:: 3.81
	  card-repeats:: 2
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-06-28T02:33:36.520Z
	  card-last-reviewed:: 2026-06-24T07:33:36.520Z
	  card-last-score:: 3
		- Shortcut: `F` then `r` (two-key sequence, uppercase `F`)
		- Context: **User-defined** binding — *not* a yazi default. Set in my `~/.config/yazi/keymap.toml` (managed via [[chezmoi]] dotfiles) as an `[mgr]`-layer `prepend_keymap` running `plugin fr rg`. Uppercase `F` is the leader so the default `f` = `filter --smart` stays intact. Provided by the [[yazi/Plugin/fr.yazi]] plugin; requires [[rg]], [[fzf]], and [[bat]].
		- Description: Opens [[fzf]] over [[rg]] content matches with [[bat]]-powered syntax-highlighted previews. Navigate with arrow keys or `Ctrl-J/K`; selecting a result opens yazi at that file.