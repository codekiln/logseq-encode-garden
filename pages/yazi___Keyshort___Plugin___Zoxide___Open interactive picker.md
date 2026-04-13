- [[Keyshort]] [[yazi]] [[yazi/Keyshort]] [[yazi/Keyshort/Plugin/Zoxide]]
	- **Jump with zoxide’s interactive picker (fzf-backed)** #card
	  card-last-interval:: 4.91
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-04-17T05:29:22.299Z
	  card-last-reviewed:: 2026-04-12T08:29:22.302Z
	  card-last-score:: 5
		- Shortcut: `Z` (uppercase)
		- Context: File list / manager pane (default keymap); built-in **zoxide** plugin
		- Description: Opens **zoxide’s interactive UI** to jump by frecency; that UI **uses fzf** as its picker (requires **zoxide** and **fzf** installed, and zoxide initialized so the DB is populated). Optional: `require("zoxide"):setup { update_db = true }` in `~/.config/yazi/init.lua` to record dirs on cd. See [Builtins | Yazi — zoxide.lua](https://yazi-rs.github.io/docs/plugins/builtins).