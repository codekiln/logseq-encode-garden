logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[tmux/Keyshort/Pane/Resize Pane]], [[tmux/oh-my-tmux]]
via:: [[tmux/Keyshort/Pane/Resize Pane]]

- # Why doesn't prefix Alt-Left or Alt-Right resize the inner horizontal split in a nested [[tmux]] layout (outer top-bottom split and lower left-right split), while Alt-Up or Alt-Down still move the outer boundary?
	- ## Answer
		- [[AI/Response]]
			- **Short answer:** The [[tmux/Keyshort/Pane/Resize Pane]] bindings are still calling **`resize-pane`** on the **active** pane. In a **nested** layout they only move the **immediate** vertical border between the **two bottom panes**. If that border **cannot move**—most often because the **other** bottom pane is already at **tmux’s minimum width**—the command **no-ops**, which looks like “resize doesn’t work.” **Alt-Up / Alt-Down** still move the **outer** (full-width) **horizontal** divider, where there is usually **more slack** in **rows** than you have spare **columns** in the bottom row, so those resizes are more likely to succeed.
			- ### How tmux applies `resize-pane`
			  collapsed:: true
				- **`resize-pane -L` / `-R` / `-U` / `-D`** nudges the **edge** of the **current** pane in that direction **against its sibling** along that axis, **inside the layout “cell”** that already contains the pane ([tmux(1) — `resize-pane`](https://man7.org/linux/man-pages/man1/tmux.1.html)).
				- The maintainer describes this as resizing **up to the limit of the cell that contains** the active pane; **`resize-pane` does not recursively shrink or grow panes outside that cell** the way **dragging borders with the mouse** sometimes can in awkward layouts ([tmux issue #1774](https://github.com/tmux/tmux/issues/1774), [issue #4381](https://github.com/tmux/tmux/issues/4381)).
			- ### Why the inner left/right split often “won’t budge”
			  collapsed:: true
				- **Minimum pane size:** tmux enforces a **minimum width and height** for panes (on the order of a **few cells**; see discussion around **`PANE_MINIMUM`** in [tmux issue #1480](https://github.com/tmux/tmux/issues/1480)). If **bottom-left** is already **as narrow as allowed**, you **cannot** steal more columns for **bottom-right**, so **both** horizontal nudges can appear dead until you **first** give slack (e.g. widen the left pane with the **opposite** horizontal resize, or resize from the **other** pane).
				- **Asymmetric slack:** After a **top/bottom** split, the **bottom row** may be **short in height** but still **wide**; the limiting factor for **horizontal** resize is **columns shared with the sibling**, not the whole window. **Vertical** resize of the outer split uses **full window width** and **many rows**, so it **succeeds more often** even in the same session.
			- ### Things to verify
			  collapsed:: true
				- Run [[tmux/list-keys]] (pipe through **`rg resize`** if you like) and confirm **prefix + M-Left / M-Right** are bound to **`resize-pane -L` / `-R`** as expected for [[tmux/oh-my-tmux]].
				- Check pane widths with **`tmux display-message -p '#{pane_width}'`** after **`select-pane -L`** / **`-R`** to see whether the **sibling** is **pinned at a tiny width** (minimum-size panes block further horizontal steals).
				- If you need **deeper** layout changes than one border, use **`resize-pane -t <target>`** on specific panes, **`select-layout`**, or **mouse** dragging ([Super User — adjusting split sizes](https://superuser.com/questions/863295/adjusting-screen-split-pane-sizes-in-tmux)).
			- ### Sources
			  collapsed:: true
				- [tmux(1) — `resize-pane`](https://man7.org/linux/man-pages/man1/tmux.1.html)
				- [tmux/tmux #1774 — resize-pane does not adjust all splits](https://github.com/tmux/tmux/issues/1774)
				- [tmux/tmux #4381 — edge case resizing / nested grids](https://github.com/tmux/tmux/issues/4381)
				- [tmux/tmux #1480 — minimum pane size behavior](https://github.com/tmux/tmux/issues/1480)
				- [Super User — Adjusting screen split pane sizes in tmux](https://superuser.com/questions/863295/adjusting-screen-split-pane-sizes-in-tmux)