logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-03-28 Sat]]
see-also:: [[Glow/Q/How do I use Glow as a default pager for markdown documents when I'm in a terminal?]]

- # How can I maximize the preview pane in [[yazi]] so I can use [[glow]] in a bigger space?
	- ## Answer
		- [[AI/Response]]
			- **Widen the preview column:** in `~/.config/yazi/yazi.toml`, **`[mgr] ratio`** is a three-number array **`[parent, current, preview]`** that splits horizontal space between the parent directory, current directory, and preview (see [yazi.toml | Yazi — mgr.ratio](https://yazi-rs.github.io/docs/configuration/yazi/#mgrratio)). Example: **`[0, 1, 3]`** hides the parent pane (`0`) and gives the preview column **3 / (1+3)** of what remains; tune the numbers to taste (at least one part must be non-zero).
			- **Larger image/PDF tiles in preview:** the preview area also honors **`[preview] max_width`** and **`[preview] max_height`** (run **`yazi --clear-cache`** after changes).
			- **Full terminal with [[glow]]:** the in-ui preview column is still a slice of the terminal. For a **full-screen** Markdown read with **glow**, run a **blocking shell** on the hovered file, e.g. bind **`shell 'glow -p %h' --block`** (adjust flags; **`%h`** is the hovered path per [keymap — shell](https://yazi-rs.github.io/docs/configuration/keymap/#mgrshell)). That temporarily puts Yazi on a secondary screen and hands the whole terminal to glow until you quit glow.
			- **Paging inside glow:** see **`glow -p`** / config `pager:` on the see-also page for this graph.
	- ## My Notes
		- *placeholder*
