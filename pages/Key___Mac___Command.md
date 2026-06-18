logseq-entity:: [[Logseq/Entity/Key]]
alias:: [[Key/Mac/Command (⌘)]], [[Key/Command]], [[Key/Control]]

- # Command (⌘)
	- macOS-exclusive modifier key; the primary action key for most Mac keyboard shortcuts, equivalent to `Ctrl` on Windows and Linux.
	- ## Larger Context
		- ### Origin
			- Introduced by Apple in 1984 with the original Macintosh. The ⌘ symbol (the "Place of Interest" sign, U+2318) was chosen by Susan Kare. Steve Jobs wanted to avoid overloading the Apple logo, so a new symbol was picked from a Scandinavian road sign.
		- ### macOS role
			- `⌘` is the primary modifier for app-level shortcuts: `⌘C` (copy), `⌘V` (paste), `⌘Z` (undo), `⌘Q` (quit), `⌘Tab` (app switcher).
			- Most cross-platform apps document their shortcuts as `Ctrl` on Windows/Linux and `⌘` on macOS — they are functionally equivalent in that context.
		- ### Cross-platform equivalence
			- In terminal emulators and CLI tools, `⌘` is **not** forwarded to the shell. Cross-platform shortcuts that use `Ctrl` on other platforms use `⌘` only at the macOS GUI layer.
			- When a tool says "use `Ctrl+C` to copy" on Windows, the Mac equivalent is `⌘C` — the `[[Key/Control]]` alias captures this convention.
		- ### Notation
			- | Notation | Meaning |
			  |----------|---------|
			  | `⌘` | Command key symbol |
			  | `Cmd` | Common text abbreviation |
			  | `Meta` / `M-` | **Not** the same — see [[Key/Meta]] |
		- ### Related keys
			- **[[Key/Meta]]** — distinct key; maps to `Option/Alt` in terminals, not to Command.
			- **[[Key/Mac/Option]]** — the `⌥` modifier; maps to [[Key/Meta]] / [[Key/Alt]] in terminals.
			- **[[Key/Control]]** — `Ctrl` modifier; cross-platform equivalent of Command in GUI shortcuts.
