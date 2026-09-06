- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]] [[LazyVim/Keyshort/Window]]
	- **Split Window Right (vertical)** [[Card]]
		- Shortcut: `<leader>|`
		- Description: LazyVim's alias for `<C-w>v`. The `|` glyph mirrors the resulting vertical divider.
	- **Split Window Below (horizontal) (1. Lazy-Vim specific, 2. Native Vim)** [[Card]]
	  id:: 6a97e367-de2b-44fb-8fbc-26f0f92a0f66
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:14:38.761Z
	  card-last-score:: 1
		- Description: LazyVim's alias for `<C-w>s`. The `-` glyph mirrors the resulting horizontal divider.
		- 1. Native LazyVim Shortcut: `<leader>-`
		-
	- **Move Focus Between Splits (lazyvim-specific keyshorts)** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:03:06.727Z
	  card-last-score:: 1
		- Shortcut: `<C-h>` `<C-j>` `<C-k>` `<C-l>`
		- Description: Jumps focus left/down/up/right without the `<C-w>` prefix. The vanilla `<C-w>h/j/k/l` still works and is what these remap to.
	- **Close Current Split with 1. LazyVim keyshort, 2.) vanilla vim** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:27:15.803Z
	  card-last-score:: 1
		- 1. LazyVim Shortcut: `<leader>wd`
			- [[Mnemonic]]: `w` is the split leader, and `d` is for ==d==elete.
		- 2. Vanilla Vim shortcut: `<C-w>c`
			- [[Mnemonic]]: `<C-w>` is the leader for all split items, and `c` is for ==c==lose.
		- Description: Closes the focused window, leaving the buffer loaded.
			- [[My Question]]: what does it really mean to close the focused window, leaving the buffer loaded, and why would I want to do that?
			  id:: 6a9d3f38-19d6-4ac5-92a2-946764075772
				- [[Hypothesis]] I suppose it probably means that I can list my nvim buffers and easily get back to it. I remember there's a set of keyboard shortcuts for navigating buffers in a stack, but I don't remember what they are.
	- **Resize Split** [[Card]]
		- Shortcut: `<C-Up>` `<C-Down>` `<C-Left>` `<C-Right>`
		- Description: Grows/shrinks the focused window by arrow direction. Vanilla equivalents: `<C-w>+` / `<C-w>-` / `<C-w><` / `<C-w>>`.
	- [[My Note]]
		- Holding `<C-w>` opens [[nvim/Plugin/which-key.nvim/Hydra Mode]], which keeps the window submenu live so a run of resizes and splits needs the prefix only once.