logseq-entity:: [[Logseq/Entity/CLI/Command]]

- [tmux choose-tree](https://man.openbsd.org/tmux#choose-tree) [`-GhikNrswyZ`] [`-F` format] [`-f` filter] [`-K` key-format] [`-O` sort-order] [`-t` target-pane] [template]
	- Put a pane into [[tmux/Mode/Tree]], where a [[tmux/session]], [[tmux/Window]], or [[tmux/Pane]] may be chosen from a hierarchy.
	- `-s` starts with sessions collapsed; `-w` starts with windows collapsed; `-Z` zooms the pane; and `-y` disables confirmation prompts.
	- Given neither `-s` nor `-w`, every branch starts open down to the panes, so `choose-tree -Z` is the fully expanded picker.
	- The flags also bound how far expand-all goes. Under `-s` or `-w`, `M-+` never opens a window, so it reveals the windows after `-s` and changes nothing after `-w`; panes are reached one window at a time. Without either flag it restores the whole tree, panes included.
	- `-F` formats each item, `-K` formats shortcut keys, `-f` filters items, `-O` sets the initial [[tmux/session/Picker/Order]], and `-t` selects the pane that displays the tree.
	- The default template switches the client to the chosen target. A custom template receives the target through `%%` or `%1`.
	- [[tmux/Prefix]] `s` is bound to `choose-tree -Zs`; [[tmux/Prefix]] `w` is bound to `choose-tree -Zw`.
	- `choose-session` and `choose-window` are aliases for `choose-tree -s` and `choose-tree -w`.
	- Tree-mode controls are documented in [[tmux/session/Picker/Help]].
