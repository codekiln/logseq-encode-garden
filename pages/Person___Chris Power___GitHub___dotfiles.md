tags:: [[dotfiles]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Chris Power]]
date-created:: [[2024/02/02]]
via:: https://github.com/typecraft-dev/dotfiles

- # [typecraft-dev/dotfiles](https://github.com/typecraft-dev/dotfiles)
	- Public [[dotfiles]] for [[Person/Chris Power]] (typecraft), tracking the [[Linux]] desktop and [[nvim]] setups demonstrated on their channel. No README and no license file; the directory layout is the documentation.
	- Written in [[Lua]] (the [[nvim]] config dominates the repo by volume).
	- [[GitHub/Star]]: 1433 (checked 2026-08-04); 267 forks — an unusually high fork-to-star ratio, consistent with an audience cloning along with video tutorials rather than depending on it as a library.
	- ## Layout
		- Each top-level directory is a GNU Stow package whose contents mirror `$HOME`, so `nvim/.config/nvim/` symlinks to `~/.config/nvim/`. Stowing selects configs per machine instead of applying one monolithic tree, which is the lighter-weight alternative to the templated [[dotfile/Manager]]s ([[chezmoi]] and friends) used elsewhere in this garden.
		- Two parallel [[Linux]] desktop stacks live side by side: Wayland (Hyprland with hypridle/hyprlock/hyprpaper, waybar, wofi) and X11 (i3, picom, polybar, rofi, `.Xresources`). Useful as a diff between the two ecosystems for the same person's taste.
		- Three terminals are configured — [[Ghostty]], [[Alacritty]], and [[kitty]] — alongside [[starship]], [[zsh]] (`zshrc/.zshrc`), and [[tmux]].
		- Catppuccin Mocha is applied consistently across Alacritty, rofi, waybar, hypr, and [[nvim]]; see [[Catppuccin]].
	- ## [[nvim]]
		- [[lazy.nvim]] bootstrapped in `init.lua`, with one file per plugin under `lua/plugins/` and options factored into `lua/vim-options.lua`. The plugin-per-file split is the trait worth borrowing: each plugin's spec is independently readable and removable.
		- [nvim/.config/nvim/lua/plugins](https://github.com/typecraft-dev/dotfiles/tree/master/nvim/.config/nvim/lua/plugins) — Avante and Copilot for AI assistance, oil.nvim for file editing, snacks.nvim, treesitter, none-ls, plus Rails and vim-test for a Ruby workflow.
	- ## [[tmux]]
		- [[tmux/Config]] [tmux/.config/tmux/tmux.conf](https://github.com/typecraft-dev/dotfiles/blob/master/tmux/.config/tmux/tmux.conf)
		- Uses tpm for plugins and vim-tmux-navigator for unified pane/split motions with [[nvim]].
