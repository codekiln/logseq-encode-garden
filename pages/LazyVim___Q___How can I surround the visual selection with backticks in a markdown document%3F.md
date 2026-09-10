logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[vim/Q/Can I visually select a block of text and quickly surround it with quotes, backticks, etc?]]

- # How can I surround the visual selection with backticks in a [[LazyVim]] markdown document?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Enable the `mini-surround` coding extra (`:LazyExtras`), then in Visual mode select the text and press `gsa` followed by the backtick key.
			- ## Enabling the extra
				- [[LazyVim]] does not bundle `mini.surround` in its core plugins; it ships as an opt-in extra at `lua/lazyvim/plugins/extras/coding/mini-surround.lua`, built on [nvim-mini/mini.surround](https://github.com/nvim-mini/mini.surround).
				- Enable it via `:LazyExtras`, selecting `coding.mini-surround`, or by adding `{ import = "lazyvim.plugins.extras.coding.mini-surround" }` to the `lazy.nvim` setup spec.
			- ## Visual-mode workflow
				- 1. Enter Visual mode (`v`, `V`, or `Ctrl-v`) and select the target text.
				- 2. Press `gsa` (LazyVim's default `add` mapping — vanilla `mini.surround` instead maps this to `sa`).
				- 3. Type the delimiter character, `` ` ``, to wrap the selection: `` `text` ``.
			- ## Other default mappings from the extra
				- `gsd` — delete a surrounding.
				- `gsr` — replace a surrounding.
				- `gsf` / `gsF` — find the surrounding to the right / left.
				- `gsh` — highlight a surrounding.
				- These sit under the `gs` ("surround") which-key group that [[LazyVim]] registers even before the extra is enabled.
			- [[Answer/Official]] from [`mini.surround` add mapping source](https://raw.githubusercontent.com/LazyVim/LazyVim/main/lua/lazyvim/plugins/extras/coding/mini-surround.lua): `add = "gsa", -- Add surrounding in Normal and Visual modes`.
