logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[nvim/Plugin/snacks.nvim/Picker]]

- # How do I see more of a long filename in the [[nvim/Plugin/snacks.nvim/Explorer]] sidebar (`<leader>e`)?
	- ## [[AI Answer]]
		- Short answer: the sidebar window is only 40 columns wide by default, and the `Explorer` picker shows filenames only (no path) with no ellipsis — long names simply get cut off at the window edge. Widen the sidebar layout in your [[nvim/Plugin/snacks.nvim]] `opts`.
		- Add this to the `snacks.nvim` plugin spec (e.g. `lua/plugins/snacks.lua`):
			- ~~~lua
			  return {
			    "folke/snacks.nvim",
			    opts = {
			      picker = {
			        sources = {
			          explorer = {
			            layout = { layout = { width = 60 } },
			          },
			        },
			      },
			    },
			  }
			  ~~~
		- This overrides only the `explorer` source's copy of the `sidebar` layout preset (`width = 40` by default). To widen every picker that uses the `sidebar` layout preset (not just Explorer), override the preset itself instead: `opts.picker.layouts.sidebar.layout.width = 60`.
		- Confirmed by reading the plugin source directly (no official width-tuning doc page): `lua/snacks/picker/config/sources.lua` sets `M.explorer.layout = { preset = "sidebar", preview = false }` and `formatters.file = { filename_only = true }`; `lua/snacks/picker/config/layouts.lua` sets `M.sidebar.layout.width = 40`. The filename formatter (`lua/snacks/picker/format.lua`, `M.filename`) does not truncate or ellipsize when `filename_only` is set — the neovim window itself clips anything past its width.
