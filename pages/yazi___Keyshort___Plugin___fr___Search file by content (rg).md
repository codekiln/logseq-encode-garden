- [[Keyshort]] [[yazi]] [[yazi/Keyshort]] [[yazi/Keyshort/Plugin/fr]]
	- **Search file by content with rg (fr.yazi)** [[Keyshort/User]] #card
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-06-19T04:00:00.000Z
	  card-last-reviewed:: 2026-06-18T06:46:56.519Z
	  card-last-score:: 1
		- Shortcut: `F` then `r` (two-key sequence, uppercase `F`)
		- Context: **User-defined** binding — *not* a yazi default. Set in my `~/.config/yazi/keymap.toml` (managed via [[chezmoi]] dotfiles) as an `[mgr]`-layer `prepend_keymap` running `plugin fr rg`. Uppercase `F` is the leader so the default `f` = `filter --smart` stays intact. Provided by the [[yazi/Plugin/fr.yazi]] plugin; requires [[rg]], [[fzf]], and [[bat]].
		- Description: Opens [[fzf]] over [[rg]] content matches with [[bat]]-powered syntax-highlighted previews. Navigate with arrow keys or `Ctrl-J/K`; selecting a result opens yazi at that file.