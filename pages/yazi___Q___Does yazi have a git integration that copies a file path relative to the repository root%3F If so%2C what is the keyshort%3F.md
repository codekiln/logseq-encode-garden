logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[yazi/Keyshort]]

- # Does [[yazi]] have a [[git]] integration that copies a file path relative to the repository root? If so, what is the keyshort?
	- ## Answer
		- [[AI/Response]]
			- **No — not as a built-in “git integration.”** Stock [[yazi]] does **not** define a `copy` variant that is **relative to `git rev-parse --show-toplevel`**. The manager **`copy`** action only supports **`path`** (the file’s URL, i.e. the usual absolute filesystem path), **`dirname`**, **`filename`**, and **`name_without_ext`**, plus optional **`--separator`** (`unix` vs platform default) — there is no **`git_root`** (or similar) option in the documented action ([keymap — mgr.copy](https://yazi-rs.github.io/docs/configuration/keymap/#mgr.copy)).
			- **Default path-copy keybindings** (preset chord **`c`** then second key; “`c` ⇒ `c`” means press **`c`**, then **`c`** again): **`c` ⇒ `c`** copies the **file path**; **`c` ⇒ `d`** parent **directory** path; **`c` ⇒ `f`** **filename**; **`c` ⇒ `n`** filename **without extension** ([Quick Start — Copy paths](https://yazi-rs.github.io/docs/quick-start)). Those are the shipped shortcuts for clipboard path operations; none of them is “relative to repo root.”
			- **Practical workaround:** bind **`shell`** to run a one-liner that computes a path relative to the repo root (e.g. `realpath` / `git rev-parse` / `python -c …`) and pipes to **`pbcopy`** on macOS or **`wl-copy`** / **`xclip`** on Linux, or use a **community plugin** if you want a maintained implementation (search the [Yazi resources / plugin ecosystem](https://yazi-rs.github.io/docs/resources) for “git” / “relative path” plugins).
	- ## My Notes
		- Took the `shell` workaround above, in the [[chezmoi]] dotfiles: [[yazi/Keyshort/Copy GitHub markdown link]] binds `c` then `g`, calling [[git/Alias/md-url]].
		- Went one step past a repo-root-relative *path* to a repo-root-relative **GitHub link**, since pasting into this garden is what I actually wanted the path for. The link text is the repo-root path prefixed with the repo name, so a link pasted here still says which repo it came from.
		- The chord slots into yazi's own preset `c` copy family rather than being a new leader — `cc`/`cC`/`cd`/`cD`/`cf`/`cn` are the six that ship, and `cg`/`cG` were free.
		- Two details the answer above doesn't mention, both confirmed in the [[yazi]] source: `copy` acts on `selected_or_hovered_files()` and joins with newlines, so multi-selection already yields one line per file and a custom binding should match that; and file-path substitution in `shell` uses `%`-tokens (`%s` selected-or-hovered, `%h` hovered), not `$@`.
		- Still missing, and not solvable in yazi: a **line-anchored** permalink (`#L12-L30`). Yazi has no cursor inside a file, so that wants an editor binding.
