logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[tmux/Keyshort/Pane/Zoom Pane]]

- # What does it mean to "zoom" a [[tmux]] pane, and how do you zoom out?
	- ## Answer
		- [[AI/Response]]
			- **What “zoom” means:** In [[tmux]], **zoom** is a **per-window layout toggle** on the **active pane**. The pane is marked **zoomed** and **temporarily expands to use the entire client area** for that window; **other panes in the same window stay in the layout but are not drawn** until you leave zoomed state. Under the hood this is the **`resize-pane -Z`** behavior exposed as the default binding **`prefix` + `z`** (see [tmux(1) — default key bindings](https://man.openbsd.org/tmux.1)).
			- **How to zoom out:** **Press the same key again** — **`prefix` + `z`** **toggles** zoom **on and off** for the current pane (same binding as zoom in). There is **not** a separate “zoom out” chord in the default table; it is **one toggle**.
			- **Naming note:** People coming from [[vim]] sometimes say **`<leader> z`**, but in tmux documentation and configs the chord is almost always written as **`<prefix> z`** where **`prefix`** is your **`prefix` key** (often **`Ctrl-b`** by default, or whatever you set with `set -g prefix`).
			- **Verify your session:** Run **`tmux list-keys`** and look for **`resize-pane -Z`** (or search for **`z`** in the **`prefix` table**) to confirm nothing in [[tmux/oh-my-tmux]] or `.tmux.conf` remapped it.
			- **How to tell you're zoomed**
				- **Visually:** The window shows **only one** pane edge-to-edge; you **do not** see split **borders between sibling panes** in that window (other panes still exist in the layout but are **not drawn**).
				- **`#{pane_zoomed}`:** In status/command **formats**, **`#{pane_zoomed}`** is **`1`** when that pane is zoomed, **`0`** otherwise. Quick check from the shell: **`tmux display-message -p '#{pane_zoomed}'`** → **`1`** means the **active** pane is zoomed.
				- **Optional status hint:** Add something like **`#{?pane_zoomed,[Z],}`** to **`status-left`** or **`status-right`** in `.tmux.conf` if you want a persistent on-screen flag (see **FORMATS** in [tmux(1)](https://man.openbsd.org/tmux.1)).
			- **Sources**
				- [tmux(1) — OpenBSD manual pages](https://man.openbsd.org/tmux.1) (default bindings: “`z` Toggle zoom state of the current pane.”; **FORMATS** / `pane_zoomed`)
