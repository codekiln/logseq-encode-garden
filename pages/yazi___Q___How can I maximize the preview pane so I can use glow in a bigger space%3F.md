logseq-entity:: [[Logseq/Entity/Question]]
via:: [[2026-03-28 Sat]]
see-also:: [[Glow/Q/How do I use Glow as a default pager for markdown documents when I'm in a terminal?]]

- # How can I maximize the preview pane in [[yazi]] so I can use [[glow]] in a bigger space?
	- ## My Notes
		- [[2026-05-05 Tue]]
			- Goal: from Yazi, open the highlighted file in [[glow]] as a pager using the full terminal, then return to Yazi. The Answer below spells out the minimal config; the trick is Yazi’s **blocking** shell, not the preview column width.
			  id:: 69f9caa9-3b60-4ca5-bde0-56a39cbf7416
	- ## Answer
		- [[AI/Response]]
			- **Simplest way — glow in a blocking shell:** Assign a shortcut that means: run a command on the file under the cursor, give it the full terminal, and do not show Yazi again until that command exits. In Yazi you do that with the `shell` action plus the `--block` flag. The placeholder `%h` becomes the hovered file’s path. Use `glow -p` so glow runs as a pager (long files scroll inside glow). Docs: [shell](https://yazi-rs.github.io/docs/configuration/keymap/#mgr.shell).
			  id:: 69cd1d52-53db-483d-bb20-dbd4a2a91a62
			- **1.** Open (or create) your Yazi keymap file: `~/.config/yazi/keymap.toml`.
			- **2.** Add a binding whose `run` value is `shell 'glow -p %h' --block`. Use `prepend_keymap` in `keymap.toml` so you add one shortcut without wiping defaults. Example chord `g` then `l` — pick different keys if yours are taken:
			- ~~~
			  [[mgr.prepend_keymap]]
			  on   = [ "g", "l" ]
			  run  = "shell 'glow -p %h' --block"
			  desc = "Glow pager for hovered file (full terminal)"
			  ~~~
			- **3.** Restart Yazi. Point at a markdown file, press the shortcut, read in glow, quit glow (often `q`). You should return to Yazi.
			- **If you do not want pager behavior:** keep the same `shell '…' --block` pattern but swap in `glow %h` instead of `glow -p %h`.
			- **Optional — bigger preview column only:** The narrow preview panel on the right is separate from this full-terminal trick. To widen only that panel (still not full-screen), edit `~/.config/yazi/yazi.toml`, section `[mgr]`, key `ratio`, three numbers meaning parent column, file list, preview — e.g. `[0, 1, 3]` hides the parent column and gives preview more room ([ratio](https://yazi-rs.github.io/docs/configuration/yazi/#mgrratio)). That is optional; it does not replace `shell … --block` for full-terminal glow.
			- **Preview pane images/PDFs:** In `yazi.toml`, `[preview] max_width` and `max_height` affect image/PDF thumbnails in the side preview; after edits run `yazi --clear-cache`.
			- **Glow pager settings:** See [[Glow/Q/How do I use Glow as a default pager for markdown documents when I'm in a terminal?]] for `glow -p`, `pager:`, and related options.