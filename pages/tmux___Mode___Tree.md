alias:: [[tmux Tree Mode]]
see-also:: [[tmux/Mode/Choose]], [[tmux/Command/choose-tree]], [[tmux/session/Picker]]

- # tmux Tree Mode
	- Tree mode is the hierarchical form of [[tmux/Mode/Choose]]. It replaces a pane with a tree of sessions, windows, and panes; each level may be expanded or collapsed.
	- ![C-b w opens the tmux tree with windows initially collapsed](https://github.com/tmux/tmux/wiki/images/tmux_choose_tree2.png)
	- ## Entering tree mode
		- [[tmux/Command/choose-tree]] enters tree mode directly.
		- [[tmux/Prefix]] `s` runs `choose-tree -Zs`, opening the [[tmux/session/Picker]] with sessions initially collapsed.
		- [[tmux/Prefix]] `w` runs `choose-tree -Zw`, opening the same mode with windows initially collapsed.
		- `choose-session` and `choose-window` are command aliases for `choose-tree -s` and `choose-tree -w`.
		- `-Z` zooms the pane while tree mode is open.
	- ## Working in tree mode
		- Navigate and expand the hierarchy, search or filter it, change its [[tmux/session/Picker/Order]], tag items, reorder or kill windows, mark a pane, and toggle the preview.
		- Press `Enter` to choose the selected item and `q` to return to the starting pane.
		- `F1` or `C-h` opens [[tmux/session/Picker/Help]].
		- `tree-mode-preview-format` and `tree-mode-preview-style` configure the preview indicator.
