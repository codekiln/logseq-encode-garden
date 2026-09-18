logseq-entity:: [[Logseq/Entity/Card]], [[Logseq/Entity/Keyshort]]

- ### 1. What [[Keyshort]] opens [[nvim/Plugin/mini.files]] at the directory of the current file, and 2. what [[Keyshort]] opens it at the current working directory? [[card]]
	- 1. `<leader>fm` — opens at the directory containing the file in the active buffer
	- 2. `<leader>fM` — opens at Neovim's current working directory (cwd); not the same root/cwd split as picker/explorer until customized ([[LV4AD/Ch/05 Plugin Basics]])
