alias:: [[tmux Session Picker]]
see-also:: [[tmux/Mode/Tree]], [[tmux/Command/choose-tree]]

- # Tmux Session Picker
	- The session picker is [[tmux/Mode/Tree]] as opened by [[tmux/Prefix]] `s`, which runs `choose-tree -Zs`. Sessions begin collapsed and may be selected directly or expanded to reach their windows and panes.
	- [Choosing sessions, windows and panes](https://github.com/tmux/tmux/wiki/Getting-Started#choosing-sessions-windows-and-panes) in [[tmux/Docs/Getting Started/Using tmux interactively]]
	- ![The tmux session picker after C-b s](https://github.com/tmux/tmux/wiki/images/tmux_choose_tree1.png)
	- {{embed [[tmux/session/Picker/Window Expanded]]}}
	- `O` ([[Key/Shift]] + [[Key/O]]) changes the [[tmux/session/Picker/Order]] of the items
	- `C-h` ([[Key/Control]] + [[Key/H]]) opens the [[tmux/session/Picker/Help]]
