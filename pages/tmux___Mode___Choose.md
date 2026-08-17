see-also:: [[tmux/Mode]]

- Choose mode replaces a pane with an interactive interface for selecting an item.
- tmux has three choose-mode interfaces:
	- [[tmux/Command/choose-tree]] enters [[tmux/Mode/Tree]] for sessions, windows, and panes. `choose-session` and `choose-window` are aliases for `choose-tree -s` and `choose-tree -w`.
	- `choose-client` enters client mode for attached clients.
	- `choose-buffer` enters buffer mode for paste buffers.
- The interfaces share navigation, search, filtering, sorting, tagging, previews, help, and exit controls. The available actions and displayed hierarchy depend on the item being chosen.
