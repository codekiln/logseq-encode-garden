logseq-entity:: [[Logseq/Entity/Key]]
alias:: [[Key/Shift (S-)]], [[Key/Shift (⇧)]]
- # Shift (⇧)
	- Modifier key that selects a key's alternate form — uppercase for letters, the upper symbol for punctuation; written `S-` in Vim-style key notation, so `<S-l>` is `L`.
	- ## Larger Context
		- ### Origin
			- Inherited from the mechanical typewriter, where the key physically shifted the carriage (or the typebasket) so a second glyph on the same typebar struck the page. The name outlived the mechanism.
		- ### Notation
			- | Notation  | Meaning                                                  |
			  |-----------|----------------------------------------------------------|
			  | `⇧`       | Shift key symbol (U+21E7)                                |
			  | `S-`      | Shift modifier prefix in [[vim]] / [[nvim]] key notation |
			  | `<S-l>`   | Shift+l — identical to typing capital `L`                |
			  | `<S-Tab>` | Shift+Tab, a key with no capital form of its own         |
		- ### In Vim key notation
			- For a plain letter, `<S-x>` and the capital letter are the same keystroke: a mapping on `<S-l>` fires when `L` is pressed, and `:map` will often display it as `L`. Config authors write the `S-` form when they want the modifier to be visible next to sibling `<C-…>` and `<M-…>` mappings.
			- `S-` is load-bearing for keys that have no shifted glyph — `<S-Tab>`, `<S-Enter>`, `<S-Left>`, `<S-F1>` — and terminals only deliver those when they support extended key encoding.
			- `:help key-notation` lists the full set of `<…>` names and modifier prefixes.
		- ### Related modifier keys
			- **[[Key/Control]]** — the `Ctrl` modifier, written `C-`.
			- **[[Key/Meta]]** — maps to `Alt`/`Option` in terminals, written `M-`.
			- **[[Key/Mac/Command]]** — the macOS `⌘` modifier; not visible to terminal applications.
