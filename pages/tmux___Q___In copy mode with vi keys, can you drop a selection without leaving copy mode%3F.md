logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[tmux/Q/What is a conceptual overview of how copy paste works in oh-my-tmux with nvim?]], [[tmux/Q/Is there a way to do rectangular selection when using oh-my-tmux and tmux with vim visual selection mode?]]

- # In [[tmux]] copy mode with vi keys, can you drop a selection without leaving copy mode?
	- ## Answer
		- [[AI/Response]]
			- **Yes, tmux can do this** with the copy-mode command **`clear-selection`**, which removes the highlight **without** leaving copy mode, so your **scroll position stays put**.
			- ### Why `v` does not “toggle off” like Vim
				- In typical **[[tmux/oh-my-tmux]]**-style vi copy-mode tables, **`v` is bound to `begin-selection`**, not to “exit visual.” Pressing **`v` again usually starts or resets selection behavior rather than acting like Vim’s visual toggle—so your observation is expected.
				- **`C-v`** is often **`rectangle-toggle`** in the default vi table (orthogonal to “exit visual”).
			- ### Why **Escape** may kick you out entirely
				- Many configs (including common **oh-my-tmux** patterns) bind **`Escape` in `copy-mode-vi` to `cancel`**, which **exits copy mode**—the opposite of “only clear the selection.” That matches **`tmux list-keys -T copy-mode-vi`** on typical setups. Stock documentation sometimes describes **`Escape` as “clear selection”** in older tables or mixed emacs/vi docs; **trust `tmux list-keys -T copy-mode-vi` for your session**.
			- ### What to use instead
				- **Bind `clear-selection` to a key you can reach in copy mode**, for example **`C-g`** (mnemonic: cancel *selection*, not the whole mode):
				- ~~~text
				  bind-key -T copy-mode-vi C-g send-keys -X clear-selection
				  ~~~
				- Or make **`Escape` conditional** so it clears when something is selected and only cancels when there is no selection (pattern discussed in community answers and blog posts):
				- ~~~text
				  bind-key -T copy-mode-vi Escape if-shell -F "#{selection_present}" "send-keys -X clear-selection" "send-keys -X cancel"
				  ~~~
				- After adding bindings, reload config (**`tmux source-file ~/.tmux.conf`**) or restart tmux.
			- ### Verify your table
				- Run **`tmux list-keys -T copy-mode-vi`** and look for **`clear-selection`**; if nothing is bound, you need one of the binds above.
			- ### Sources
				- [tmux(1) — OpenBSD man page](https://man.openbsd.org/tmux.1) (copy-mode / `send-keys -X` commands)
				- [How to stop marking while in tmux copy-mode? (Unix & Linux SE)](https://unix.stackexchange.com/questions/537452/how-to-stop-marking-while-in-tmux-copy-mode)
				- [Selecting text in Tmux copy mode (Super User)](https://superuser.com/questions/196060/selecting-text-in-tmux-copy-mode) (historical key tables; cross-check with `list-keys`)
