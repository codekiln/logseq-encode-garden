- [[Keyshort]] [[LazyVim]] [[LazyVim/Keyshort]] [[LazyVim/Keyshort/LSP]]
	- **Go to Definition** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:51:56.887Z
	  card-last-score:: 1
		- Shortcut: `gd`
			- [[Mnemonic]]
				- **go** to **definition**
				- ===g==o to ===d===efinition
		- Description: Jumps to where the symbol under the cursor is defined. Provided by the attached [[LSP]] (e.g. [[Pyright]]/[[basedpyright]] for [[Python]]).
	- **Go to Declaration** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:56:24.147Z
	  card-last-score:: 1
		- Shortcut: `gD`
		- Description: Jumps to the symbol's declaration.
		- [[Mnemonic]]
			- **Go** to **Declaration**
			- ==g==o to ==D==eclaration
			- different from go to definition (lowercase `d`) because declaration is the implementation, the current context, just like how many of the LazyVim keyshorts use shift to be the modifier for "current directory" rather than "repository." The declaration, that is, the implementation, is "local," while the definition or interface is "global."
	- **Go to Implementation** [[Card]]
		- Shortcut: `gI`
		- Description: Jumps to the symbol's implementation.
	- **Go to References** [[Card]]
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:57:39.942Z
	  card-last-score:: 1
		- Shortcut: `gr`
			- **go** to **references**
			- ==g==o to ==r==eferences
		- Description: Lists references to the symbol under the cursor.
	- **Go to Type Definition** [[Card]]
	  id:: 6a97e367-f650-4e5f-89c8-a036a9b0eae0
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-07T04:00:00.000Z
	  card-last-reviewed:: 2026-09-06T10:30:04.389Z
	  card-last-score:: 1
		- Shortcut: `gy`
		- Description: Jumps to the definition of the symbol's *type* rather than the symbol itself — on a variable, that means the class or interface it is an instance of. LazyVim's description spells the [[Mnemonic]] out as "Goto T[y]pe Definition".
		- [[My Note]]
			- I remember that one is for going to the type Declaration, and one is for going to the type Definition. I think Declaration is for the interface, and Definition is for the implementation. I think it's either `gd` or `gD`. Whoops, I guess I was wrong. It's `gy`.
	- **Hover Documentation** [[Card]]
		- Shortcut: `K`
		- Description: Shows hover documentation for the symbol under the cursor.
	- **Step Between References in the Buffer** [[Card]]
	  id:: 6a97e367-a510-42f6-b0c6-e40ccc1e9e01
	  card-last-interval:: -1
	  card-repeats:: 1
	  card-ease-factor:: 2.5
	  card-next-schedule:: 2026-09-11T04:00:00.000Z
	  card-last-reviewed:: 2026-09-10T10:07:37.748Z
	  card-last-score:: 1
		- Shortcut: `]]` next, `[[` previous
		- Description: Cycles through the other occurrences of the symbol under the cursor, in place, without opening a picker. Backed by [[nvim/Plugin/snacks.nvim/Words]] over the LSP's document highlights, so it needs a server advertising [[documentHighlight]].
		- [[nvim/Plugin/snacks.nvim/Words]] Test Setup
			- ~~~bash
			  cd /tmp && mkdir -p snacks-words-test && cd snacks-words-test
			  cat > sample.py <<'EOF'
			  def greet(name):
			      return f"hello {name}"

			  greet("world")
			  greet("logseq")
			  EOF
			  nvim sample.py
			  ~~~
			- Inside `nvim`, put the cursor on `greet` and confirm the other two occurrences highlight automatically, then press `]]` / `[[` to cycle between them. Run `:LspInfo` first if nothing highlights — [[pyright]] or [[basedpyright]] must be attached for `documentHighlight` to work.
	- **Rename Symbol** [[Card]]
		- Shortcut: `<leader>cr`
		- Description: Renames the symbol under the cursor across the project.
	- **Inspect Attached Language Servers** [[Card]]
		- Shortcut: `<leader>cl`
		- Description: Opens a picker over LSP configuration and attached clients. `:LspInfo` still works and is now an alias for `:checkhealth vim.lsp`.
	- [[My Note]]
		- These keymaps are [[LSP]]-dependent — `gd` only resolves when a language server is attached. If `gd` does nothing:
			- 1. Check attached clients with `:LspInfo`.
			- 2. Confirm the server is installed via `:Mason` (e.g. `pyright` or `basedpyright`).
			- 3. Open Neovim from the project root (`nvim .`) so the LSP starts — a single file outside a project may not attach one.
			- 4. Verify the symbol actually has a definition the LSP can resolve.
			- 5. Deeper diagnosis: `:checkhealth vim.lsp`.
		- For an outline instead of a jump, `<leader>cs` opens document symbols in [[nvim/Plugin/trouble.nvim]] — see [[LazyVim/Keyshort/Code Action]]. `<leader>ss` belongs to the Telescope and fzf-lua extras and is not mapped here.
		- `<C-o>` returns from any of these jumps — see [[vim/Keyshort/Jump/Back and Forward]].