logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]
see-also:: [[tmux/Q/What expands every item in tree mode, and why does Cmd-plus resize the Ghostty font instead?]]

- # Is it possible to quickly increase or decrease the [[Ghostty]] font size with a keyboard shortcut? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** Yes — [[Ghostty]] ships with default font-size keybindings that work without any configuration.
			- **macOS defaults (`super` = ⌘):**
				- `Cmd+=` → `increase_font_size:1`
				- `Cmd+-` → `decrease_font_size:1`
				- `Cmd+0` → `reset_font_size`
			- **Linux/GTK defaults (`ctrl`):**
				- `Ctrl++` → `increase_font_size:1`
				- `Ctrl+-` → `decrease_font_size:1`
				- `Ctrl+0` → `reset_font_size`
			- **Custom step size:** The actions accept an integer argument for how many points to adjust per press. Example custom binding:
				- `keybind = super+shift+period=increase_font_size:2`
			- **Cost of the default:** `super++` and `super+=` are handled by [[Ghostty]] itself and never reach the program running in the terminal, so `⌘+` cannot serve as a shortcut inside [[tmux]] — see [[tmux/Q/What expands every item in tree mode, and why does Cmd-plus resize the Ghostty font instead?]]
			- **Sources:** [Keybind reference](https://ghostty.org/docs/config/keybind/reference); [Configuration reference](https://ghostty.org/docs/config/reference)
