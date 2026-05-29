logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[yazi/Q/In yazi, if I navigate to a directory, is there a way to exit yazi into that directory?]]

- # In [[yazi]], if I launched without the shell wrapper, can I still cd to the current directory when I exit?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **No direct mechanism.** The `--cwd-file` flag must be passed at launch time — there is no way to add it retroactively to a running yazi session. Without it, yazi never writes the cwd file, so the parent shell has no file to read.
			- **Workarounds from inside a running yazi session:**
				- - 1. **Open a subshell** — press `!` (default: open shell at current directory). This drops you into a new shell already in that directory. Yazi stays running in the background; type `exit` to return to yazi.
				- - 2. **Copy the path to clipboard** — if you have a copy-path keybinding configured (e.g. `yp` or similar), copy the current directory, exit yazi, then run `cd "$(pbpaste)"` (macOS) or `cd "$(wl-paste)"` (Wayland) to jump to it.
			- **Going forward:** always launch yazi via the `y` wrapper function (which passes `--cwd-file`) instead of calling `yazi` directly. See [[yazi/Q/In yazi, if I navigate to a directory, is there a way to exit yazi into that directory?]].
