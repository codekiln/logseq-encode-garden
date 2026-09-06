- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]] [[LazyVim/Keyshort/UI]]
	- **Toggle Diagnostics** [[Card]]
		- Shortcut: `<leader>ud`
		- Description: Turns [[LSP]] diagnostics on or off for the session. My config disables diagnostics globally on `VeryLazy`, so this is the switch that turns them on when I actually want them.
	- **Toggle Word Wrap** [[Card]]
		- Shortcut: `<leader>uw`
		- Description: Toggles `wrap`. My `options.lua` sets `wrap` and `linebreak` on by default, so this turns wrapping *off*.
	- **Toggle Line Numbers** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:48:56.342Z
	  card-last-score:: 1
		- Shortcut: `<leader>ul`
		- Description: Toggles the `number` column.
		- [[Mnemonic]]
			- TODO come up with mnemonic for `u`, which is used for things involving the line column.
			- `l` for ===l===ine number
	- **Toggle Relative Number** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:22:16.915Z
	  card-last-score:: 1
		- Shortcut: `<leader>uL`
			- [[Mnemonic]]
				- TODO come up with a mnemonic for `u` based on the pattern for `<leader>u`.
				- `L`: line number
				- possible mnemonic: unordered list
		- Description: Toggles `relativenumber`, which is what makes `10j` / `10k` counts readable off the gutter.
	- **Pick a Colorscheme with Live Preview** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:41:06.969Z
	  card-last-score:: 1
		- Shortcut: `<leader>uC`
		- Description: Opens the [[nvim/Plugin/snacks.nvim]] picker over installed colorschemes, previewing each as it is highlighted. My default is [[Catppuccin]] mocha.
		- [[My Notes]]
			- Wow, another banger of a keyshort. So useful!
	- **Toggle Dimming** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-08-16T04:00:00.000Z
	  card-last-reviewed:: 2026-08-15T08:48:11.004Z
	  card-last-score:: 1
		- Shortcut: `<leader>uD`
		- Description: Dims everything outside the current scope, focusing the block under the cursor.
	- [[My Note]]
		- All of these are `Snacks.toggle` mappings, so they show their on/off state in the [[which-key]] popup rather than a static label.
		- The whole `<leader>u` group is discoverable by pressing `<leader>u` and reading which-key.