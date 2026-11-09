logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[LazyVim/Q/In LazyVim, how can I traverse wiki links in an Obsidian knowledge garden?]]

- # What is [[vim]] mode in [[Obsidian]] and how can I start to use it?
	- ## [[AI Answer]]
		- **Short answer:** Vim mode is a built-in setting that gives the [[Obsidian]] editor modal [[vim]] key bindings (normal, insert, visual, and `:` Ex commands). Turn it on under **Settings → Editor → Vim key bindings**; no plugin is needed.
		- **What it is**
			- It's Obsidian's own emulation of vim inside the note editor, built on the CodeMirror vim layer. It isn't nvim: there's no `init.lua`, no vim plugins, and no startup file.
			- It covers motions, operators, text objects, registers, macros, marks, search, and a subset of Ex commands. Release [[Obsidian]] 1.15.0 (desktop, 2026-10-22) added `g?` (ROT13), `:put`, search patterns in `:` ranges such as `:/foo/,/bar/d`, vim-style regexes via `:set nopcre`, and `<A-…>` mappings on macOS, and fixed `gj`, `:sort`, and `;` `,` `>` `<` in visual mode — see the [v1.15.0 changelog](https://obsidian.md/changelog/2026-10-22-desktop-v1.15.0).
			- Earlier 2026 releases added the `:image` Ex command for working with a selected image ([v1.13.2](https://obsidian.md/changelog/2026-07-14-desktop-v1.13.2/)) and vim-key navigation in the Settings panel ([v1.13.4](https://obsidian.md/changelog/2026-07-30-desktop-v1.13.4/)).
		- **How to start**
			- 1. Open Settings (`Cmd+,`), go to **Editor**, and toggle **Vim key bindings** on.
			- 2. Open a note in editing view (not reading view). The cursor is now in normal mode: `i` to insert, `Esc` to return, `:` for commands.
			- 3. Try the editing you already use in [[LazyVim]]: `ciw`, `dap`, `.`, `gj`/`gk` on wrapped lines, `/` to search the note.
			- 4. Keep Obsidian's own hotkeys (`Cmd+P` command palette, `Cmd+O` quick switcher) for anything outside the current note; vim mode only drives the editor.
		- **Making it feel like home**
			- The built-in mode reads no config file. The community plugin [Vimrc Support](https://community.obsidian.md/plugins/obsidian-vimrc-support) loads `.obsidian.vimrc` from the vault root, so mappings such as `imap jj <Esc>` or `nmap j gj` persist. It can also map keys to Obsidian commands with `exmap` + `obcommand`.
			- Lighter or adjacent options: [Mini Vimrc](https://community.obsidian.md/plugins/mini-vimrc), [Vim Commands](https://community.obsidian.md/plugins/vim-commands) (multi-key sequences bound to any Obsidian command, outside the editor too), and [Vim Mode Per Device](https://www.obsidianstats.com/plugins/vim-mode-per-device) (on for desktop, off for phone).
		- ### Sources
			- [Obsidian 1.15.0 desktop changelog](https://obsidian.md/changelog/2026-10-22-desktop-v1.15.0)
			- [Activating/configuring vim in Obsidian — Obsidian Forum](https://forum.obsidian.md/t/activating-configuring-vim-in-obsidian/53707)
			- [Vimrc Support — Obsidian community plugin](https://community.obsidian.md/plugins/obsidian-vimrc-support)
