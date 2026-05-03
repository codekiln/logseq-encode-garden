logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[vim/Q/How can I check whether vim or neovim will yank to the unnamedplus (system) clipboard?]]
via:: [[2026-05-01 Fri]]

- # What is **`:Noice`** in [[vim]] or [[nvim]]?
	- ## Answer
		- [[AI/Response]]
			- **`:Noice` is not part of stock [[vim]] or stock [[nvim]].** It is a **user-defined Ex command** registered by the third-party plugin **[noice.nvim](https://github.com/folke/noice.nvim)** (by Folke Lemaitre). If the plugin is not loaded, **`:Noice`** is **unknown**.
			- **What the plugin does:** **noice.nvim** replaces or augments Neovim’s UI for **messages**, the **cmdline**, and the **popupmenu** (see plugin readme and **`:help noice.nvim`** after install). **`:Noice`** is the **entry command** into that UI and its subcommands.
			- **Common subcommands** (from upstream docs): **`:Noice`** or **`:Noice history`** — message history; **`:Noice last`** — last message; **`:Noice dismiss`** — close visible noice views; **`:Noice disable`** / **`:Noice enable`** — toggle the plugin; **`:Noice errors`** — errors view; **`:Noice telescope`** / **`:Noice fzf`** / **`:Noice pick`** — pickers over history; **`:Noice stats`** — debug stats. Long forms like **`:NoiceHistory`** may also exist depending on version.
			- **[[vim]] vs [[nvim]]:** Classic **Vim** does not ship **`:Noice`**; you would only see it in **Neovim** (or a distribution) where **noice.nvim** is installed. Unrelated “noice” strings in other tools are not this command.
			- [noice.nvim repository](https://github.com/folke/noice.nvim)
			- [noice.nvim generated help (`doc/noice.nvim.txt`)](https://raw.githubusercontent.com/folke/noice.nvim/main/doc/noice.nvim.txt)
