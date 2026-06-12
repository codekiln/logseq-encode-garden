logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]]

- # How can I find a more complete list of the default bindings for [[tmux]] from the CLI? [[card]]
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** `C-b ?` runs `list-keys -N`, which only displays bindings that carry a human-readable **note**. Bindings without notes (like `prefix %` → `split-window -h`) are silently omitted. Use `tmux list-keys` or `tmux list-keys -T prefix` from the shell to see every binding in a given key table.
			- **Why `C-b ?` is incomplete:**
				- `prefix ?` is bound to `list-keys -N`. The `-N` flag filters output to only bindings that were declared with an attached note string. Many built-in bindings were never given notes, so they are invisible in the `?` help screen.
				- Example: `bind-key -T prefix \% split-window -h -c "#{pane_current_path}"` has no note → absent from `C-b ?`.
			- **Commands that show all bindings:**
				- `tmux list-keys` — all bindings across **every** key table (prefix, root, copy-mode, copy-mode-vi, etc.) exactly as they would appear in a `.tmux.conf`.
				- `tmux list-keys -T prefix` — only the **prefix table** (bindings active after pressing the prefix key, i.e. `C-b`).
				- `tmux list-keys -T root` — bindings active **without** a prefix (mouse bindings, and any chord you bound with `-n`).
				- `tmux list-keys -T copy-mode` and `tmux list-keys -T copy-mode-vi` — copy-mode bindings for emacs or vi keys respectively.
				- `tmux list-keys -N` — the same subset `C-b ?` shows (only noted bindings), but formatted for the shell.
			- **Interactive per-key lookup:** `prefix /` prompts you to press a key and then shows the note for that binding (runs `list-keys -1N <key>`). Still limited to noted bindings.
			- **Canonical offline reference:** `man tmux` (section *DEFAULT KEY BINDINGS*) lists the shipped defaults including notes. On macOS you can also browse [man.openbsd.org/tmux.1](https://man.openbsd.org/tmux.1).
			- **Grep trick for a specific binding:**
				- `tmux list-keys | grep split-window` — find what keys trigger a command.
				- `tmux list-keys -T prefix | grep %` — confirm a specific key in the prefix table.
