logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[yazi/Keyshort]]

- # Does [[yazi]] have a [[git]] integration that copies a file path relative to the repository root? If so, what is the keyshort?
	- ## Answer
		- [[AI/Response]]
			- **No — not as a built-in “git integration.”** Stock [[yazi]] does **not** define a `copy` variant that is **relative to `git rev-parse --show-toplevel`**. The manager **`copy`** action only supports **`path`** (the file’s URL, i.e. the usual absolute filesystem path), **`dirname`**, **`filename`**, and **`name_without_ext`**, plus optional **`--separator`** (`unix` vs platform default) — there is no **`git_root`** (or similar) option in the documented action ([keymap — mgr.copy](https://yazi-rs.github.io/docs/configuration/keymap/#mgr.copy)).
			- **Default path-copy keybindings** (preset chord **`c`** then second key; “`c` ⇒ `c`” means press **`c`**, then **`c`** again): **`c` ⇒ `c`** copies the **file path**; **`c` ⇒ `d`** parent **directory** path; **`c` ⇒ `f`** **filename**; **`c` ⇒ `n`** filename **without extension** ([Quick Start — Copy paths](https://yazi-rs.github.io/docs/quick-start)). Those are the shipped shortcuts for clipboard path operations; none of them is “relative to repo root.”
			- **Practical workaround:** bind **`shell`** to run a one-liner that computes a path relative to the repo root (e.g. `realpath` / `git rev-parse` / `python -c …`) and pipes to **`pbcopy`** on macOS or **`wl-copy`** / **`xclip`** on Linux, or use a **community plugin** if you want a maintained implementation (search the [Yazi resources / plugin ecosystem](https://yazi-rs.github.io/docs/resources) for “git” / “relative path” plugins).
	- ## My Notes
		- *placeholder*
