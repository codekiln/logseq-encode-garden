entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Key/Short]]

- ## [[yazi]] [[Keyshort/User]] to search file by content with [[yazi/Plugin/fr.yazi]]** [[card]]
  card-last-score:: 5
  card-repeats:: 2
  card-next-schedule:: 2026-06-23T15:43:46.325Z
  card-last-interval:: 5.4
  card-ease-factor:: 2.6
  card-last-reviewed:: 2026-06-18T06:43:46.325Z
	- Shortcut: `F` then `a` (two-key sequence, uppercase `F`)
	- Context: **User-defined** binding — *not* a yazi default. Set in my `~/.config/yazi/keymap.toml` (managed via [[chezmoi]] dotfiles) as an `[mgr]`-layer `prepend_keymap` running `plugin fr rga`. Uppercase `F` is the leader so the default `f` = `filter --smart` stays intact. Provided by the [[yazi/Plugin/fr.yazi]] plugin; requires [[rga]] (ripgrep-all) in addition to [[fzf]].
	- Description: Like the `F` `r` (rg) mode, but searches *inside* PDFs, Office documents, and archives via [[rga]], with rga-powered previews. Navigate with arrow keys or `Ctrl-J/K`; selecting a result opens yazi at that file.