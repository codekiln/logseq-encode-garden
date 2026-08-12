logseq-entity:: [[Logseq/Entity/Question]]

- # What is the difference between the leader key and the local leader key in [[vim]]?
	- ## [[AI Answer]]
		- Short answer: `mapleader` sets `<Leader>`, the prefix for *global* mappings meant to work in every buffer; `maplocalleader` sets `<LocalLeader>`, a prefix intended for mappings that only make sense in a specific buffer or filetype (set by filetype plugins, e.g. Markdown or LaTeX ftplugins).
		- Both are plain string variables, not special key events. When a mapping's left-hand side contains `<Leader>` or `<LocalLeader>` (e.g. `nnoremap <Leader>x ...`), vim substitutes the current value of `mapleader`/`maplocalleader` **at the moment the mapping is defined** — changing the variable afterward does not retroactively change mappings already created with the old value.
		- The split exists so a filetype plugin can ship its own mappings without stepping on whatever the user picked as their global leader: the plugin author writes `<LocalLeader>` for filetype-specific commands, and the user's global `<Leader>` mappings stay untouched no matter what `<LocalLeader>` resolves to.
		- Both default to backslash (`\`) unless a config sets them.
		- In my [[LazyVim]] config: LazyVim sets `mapleader = " "` (Space); I additionally override `maplocalleader = " "` in `config/options.lua` (LazyVim otherwise leaves `maplocalleader` at vim's default of `\`). Practical effect: any filetype plugin's `<LocalLeader>` mapping shows up under `<Space>` for me too, instead of under `\` — one fewer prefix to remember, at the small cost that a global `<leader>x` and a filetype's `<localleader>x` could now collide in the same buffer since they share a prefix.
