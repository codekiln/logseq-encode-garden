logseq-entity:: [[Logseq/Entity/Question]]

- # How can I find a more complete list of the default [[Keyshort]]s for [[tmux]] from the CLI? [[card]]
  card-last-interval:: 5.4
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-06-28T18:44:45.128Z
  card-last-reviewed:: 2026-06-23T09:44:45.129Z
  card-last-score:: 5
	- ## [[My Answer]]
		- use `C-b ?` to see some of the
			- This list **doesn’t** show any of the **custom** keybindings you create
		- to see **all** keyshorts, use [[tmux/list-keys]]
			- My favorite way - at the CLI, pipe list-keys into [[bat]]
				- `tmux list-keys | bat`
			- For interactive browsing, pipe through [[fzf]] with a [[bat]] preview
				- `tmux list-keys | fzf --preview 'echo {} | bat -l sh -p --color=always'`
				- [[fzf/--preview]] runs a command on each candidate and shows output in a side pane
				- [[bat/--language]] (`-l sh`) forces shell syntax highlighting
				- [[bat/--style]] (`-p`) removes UI chrome (no header, line numbers, or borders)
				- [[bat/--color]] (`--color=always`) keeps syntax colors even in a subprocess (bat strips them when stdout is not a TTY)
			- inside of tmux
				- open the [[tmux/Command/Prompt]]  with [[tmux/Prefix]] `:`
					- enter `list-keys`
					- hit `Enter` to get out
		- [[My Notes]]
			- at first I was confused by this suggestion, because there's a lot of noise from long commands, but really they are there.
	- ## [[AI Answer]]
		- **Short answer:** the full list lives in `tmux list-keys`, which dumps **every** key table (~267 bindings on a default 3.6a). `C-b ?` only shows one table.
		- **What `C-b ?` actually shows:** `prefix ?` runs `list-keys -N`, which prints the **prefix** key table only (bindings reached *after* the prefix). On tmux 3.6 every prefix binding carries a note, so `?` already shows all ~87 of them — it is complete *for the prefix table*.
		- **Why it still feels incomplete:** `-N` omits the other key tables entirely. `root` (mouse events and `-n` chords), `copy-mode`, and `copy-mode-vi` carry **no** notes, so nothing from them ever appears in `C-b ?`. That hides ~180 bindings — e.g. `bind-key -T copy-mode-vi v send-keys -X rectangle-toggle`.
		- **Commands that show everything:**
			- `tmux list-keys` — every binding across **all** tables, printed as `bind-key` lines exactly as in a `.tmux.conf`. Verbose by design; that density *is* the completeness.
			- `tmux list-keys -T prefix` — just the prefix table (the same set `C-b ?` shows).
			- `tmux list-keys -T copy-mode-vi` — copy-mode bindings for vi keys (use `copy-mode` for emacs keys).
			- `tmux list-keys -T root` — prefixless bindings (mouse, and chords bound with `-n`).
			- `tmux list-keys -N` — only noted bindings; on 3.6 this equals the prefix table.
		- **Gotcha — table names:** the tables are `prefix`, `root`, `copy-mode`, and `copy-mode-vi`. There is **no** `C-b` table, so `tmux list-keys -T C-b` errors with `table C-b doesn't exist`. The prefix key (`C-b`) is *printed* on each line, but the table itself is named `prefix`.
		- **Interactive per-key lookup:** `prefix /` prompts you to press a key, then shows that binding (it is bound to `command-prompt -k -p key { list-keys -1N "%%" }`).
		- **Offline manual:** `man tmux` only works when the man page is on `MANPATH`. A mise-managed tmux ships **no** man dir under its install, so `man tmux` returns `No manual entry for tmux`. Read it online at [man.openbsd.org/tmux.1](https://man.openbsd.org/tmux.1), or point `man` straight at the file (`man /path/to/tmux.1.gz`).
		- **Grep for one binding:** `tmux list-keys | grep split-window` finds which keys run a command (across all tables); add `-T prefix` to scope the search to one table.