logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Zoxide]], [[fzf]]
via:: [[2026-04-01 Wed]]

- # In [[yazi]], how can I integrate [[zoxide]] and [[fzf]] beyond the **z** (fzf-only subtree) picker?
	- ## Answer
		- [[AI/Response]]
			- **Yes — Yazi already ships both.** The **z** key runs the built-in **fzf** plugin (fuzzy pick **files and directories under the current directory** or among selections). The **Z** key runs the built-in **zoxide** plugin, which opens **zoxide’s interactive UI**; that UI **uses fzf** as its picker, so you get the same kind of “zoxide + fzf” flow as in the shell, but scoped to Yazi’s navigation ([Builtins | Yazi — fzf.lua / zoxide.lua](https://yazi-rs.github.io/docs/plugins/builtins)).
			- **Requirements for Z:** install **zoxide** and **fzf**, and **initialize zoxide** for your shell so its database is populated and tools can use it (per [zoxide installation](https://github.com/ajeetdsouza/zoxide?tab=readme-ov-file#installation)). If **Z** does nothing or errors, check those dependencies first.
			- **Optional:** record directories in zoxide when Yazi **cd**s by enabling **`update_db`** in `~/.config/yazi/init.lua`: `require("zoxide"):setup { update_db = true }` ([Builtins | Yazi — zoxide.lua options](https://yazi-rs.github.io/docs/plugins/builtins)).
			- **If you want the shell’s exact widget** (e.g. your **zi** binding): run a **blocking shell** from Yazi (e.g. **`shell`** with **`--block`**) that executes your zoxide+fzf script, then return to Yazi — that hands the full terminal to fzf for one shot ([keymap — shell](https://yazi-rs.github.io/docs/configuration/keymap/#mgrshell)). Prefer the built-in **Z** when you only need to jump and stay inside Yazi.
	- ## My Notes
		- *placeholder*
