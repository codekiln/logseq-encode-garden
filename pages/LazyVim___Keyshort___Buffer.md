- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]]
	- **List Open [[vim/Buffer]]s - 1. open buffers with snacks leader, 2. open buffers with shorter chord, 3. all buffers, even unlisted ones** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T11:10:22.896Z
	  card-last-score:: 1
		- Shortcut to open buffers in a [[nvim/Plugin/snacks.nvim/Picker]]:
			- 1. Open buffers with snacks `find` leader: `<leader>fb`
				- [[Mnemonic]]
					- **find** **buffer**
					- ==f==ind ==b==uffer
			- 2. Open buffers with short chord: `<leader>,`
				- [[Mnemonic]]
					- I don't really think this is going to need a mnemonic, as it's likely to be very frequently used, and it's so helpful and easy to type
			- 3. All buffers, even unlisted ones: `<leader>fB`
				- [[Mnemonic]]
					- this one is a big counterintuitive for me, since shift usually narrows the scope, rather than widens it (e.g. to current directory rather than root directory), but here, I think the way to remember it is that the shift key is the "alternate" that's expected to be not as frequently used and there are definitely fewer use cases for needing [[vim/Buffer/Unlisted]]
		- Description: Opens the [[nvim/Plugin/snacks.nvim]] picker over open buffers. `<leader>,` is the same thing on a shorter chord; `<leader>fB` widens it to all buffers including unlisted ones.
	- **Jump to a Buffer by Letter** [[Card]]
		- Shortcut: `<leader>bj`
		- Description: Labels every entry in the [[nvim/Plugin/bufferline.nvim]] strip with a letter and jumps to whichever one is typed. Constant effort however far away the buffer is, where `<S-h>` and `<S-l>` cost one press per buffer crossed.
	- **Next and Previous Buffer** [[Card]]
		- Shortcut: `<S-l>` next, `<S-h>` previous
		- Description: Steps through the buffer list. `S-` is [[Key/Shift]], so these are plain `H` and `L` — which normally jump to the top and bottom of the screen — rebound to buffer navigation.
	- **Next and Previous Buffer (bracket form)** [[Card]]
	  id:: 6a97e366-aefe-4855-926a-594760ca350e
	  card-last-interval:: 3.94
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-09-10T08:18:21.106Z
	  card-last-reviewed:: 2026-09-06T10:18:21.106Z
	  card-last-score:: 3
		- Shortcut: `]b` next, `[b` previous
		- Description: Same movement as `<S-l>` / `<S-h>`, in the `[`/`]` bracket-pair family shared with `]d`, `]q`, `]t`.
	- **Close Current Buffer** [[Card]]
	  card-last-interval:: 3.94
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-09-14T08:59:10.994Z
	  card-last-reviewed:: 2026-09-10T10:59:10.995Z
	  card-last-score:: 3
		- Shortcut: `<leader>bd`
		- Description: Deletes the buffer but keeps the window layout. `<leader>bD` deletes the buffer *and* its window; `<leader>bo` closes every other buffer.
	- [[My Note]]
		- Buffer order and the tab-like strip at the top come from [[nvim/Plugin/bufferline.nvim]]; `[B` / `]B` reorder buffers rather than navigate them.
		- Those chips look like tabs and are not: they render *buffers*, so `gt` and `gT` do nothing to them. Those keys move between tabpages, a separate container holding its own window layout — [[vim/Q/What is a tabpage in vim?]].