see-also:: [[tmux/Option/mode-keys]], [[tmux/Mode]]

- Enter with `Prefix [` or the `copy-mode` command.
- Replaces pane content with the scrollback history for navigation, search, and text selection.
- Key bindings controlled by [[tmux/Option/mode-keys]] (`vi` or `emacs`); uses key table `copy-mode-vi` or `copy-mode`.
- Exit with `q` (vi) or `C-c` / `C-g` (emacs).
- [[tmux/Mode/View]] is the same interface entered automatically when a command like `list-keys` produces output from a key binding.
