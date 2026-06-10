logseq-entity:: [[Logseq/Entity/Software/Plugin]]

- # [fr.yazi](https://github.com/lpnh/fr.yazi)
	- [[yazi]] plugin that pipes [[rg]] search results into [[fzf]] with [[bat]]-powered syntax-highlighted previews; also supports [[rga]] for archive and document search with previews.
	- **Stars:** 51 · **Language:** [[Lua]] (not [[Rust]])
	- Navigate matches with arrow keys or `Ctrl-J/K`; selecting a result opens yazi at that file.
	- **Chosen** for my dotfiles integration over two alternatives that do roughly the same thing (all wrap `rg`/`rga` + [[fzf]] for content search): [[yazi/Plugin/fazif.yazi]] (15★, Shell) and [[yazi/Plugin/yafg.yazi]] (12★, Lua). Picked fr.yazi for being the most-starred, [[Lua]]-native, with [[bat]]/[[rga]] previews and distinct rg vs rga modes.
	- Integrated via [[chezmoi]] + [[mise]]: declared in `~/.config/yazi/package.toml` (pinned), installed by a [[mise]] `postinstall` + `yazi:plugins` task, and bound in `~/.config/yazi/keymap.toml` — see [[yazi/Keyshort/Plugin/fr/Search file by content (rg)]] and [[yazi/Keyshort/Plugin/fr/Search file by content (rga)]].
