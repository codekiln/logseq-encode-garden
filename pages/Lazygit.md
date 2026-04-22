tags:: [[CLI/Tool]], [[TUI]]
created-by:: [[Person/Jesse Duffield]]
see-also:: [[Lazydocker]]

- [Lazygit](https://github.com/jesseduffield/lazygit) is a delightful alternative to something like the GitHub Desktop application, and it runs inside the terminal.
	- You can run it directly, by going to any directory managed by git and running `lazygit`. Or you can run it inside Neovim where it can be started with `Space G G`.
	- You hop between the different panes using `Tab`. In the Files pane, you select files for staging using `Space`, and then you can create a new commit using `c`. You can see all the commands available using `?`.
	- **Open selected file from commit history in editor** #card
	  card-last-interval:: 4
	  card-repeats:: 2
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-04-26T08:39:39.702Z
	  card-last-reviewed:: 2026-04-22T08:39:39.702Z
	  card-last-score:: 5
		- Shortcut: `e`
		- Context: In the commit history patch view, select a file and press `e` to open it in `$VISUAL` or `$EDITOR` (for example, `vim`).
- Installation