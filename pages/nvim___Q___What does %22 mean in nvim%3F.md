- # What does `"` mean in [[nvim]]?
	- ## Answer
		- [[AI/Response]]
			- `"` is the **register prefix operator**. It tells nvim: "use this register for the next yank, delete, or put command."
			- ### Syntax
				- ~~~
				  "<register><operator>
				  ~~~
				- Examples:
					- `"ay` — yank into register `a`
					- `"ap` — paste from register `a`
					- `"+y` — yank into the `+` register (system clipboard)
					- `"+p` — paste from the `+` register (system clipboard)
					- `"0p` — paste from register `0` (most recent explicit yank)
			- ### What is a register?
				- A register is a named slot that holds text. nvim has many:
					- | Register | Name | Contents |
					  |----------|------|----------|
					  | `"` | unnamed | last yank or delete (default target) |
					  | `0` | yank | last explicit `y` yank (not deletes) |
					  | `1`–`9` | delete history | recent deletes, `1` = most recent |
					  | `a`–`z` | named | user-controlled; persist until overwritten |
					  | `A`–`Z` | named (append) | uppercase appends to the lowercase register |
					  | `+` | system clipboard | OS clipboard (`pbcopy`/`pbpaste` on macOS) |
					  | `*` | primary selection | X11 primary; same as `+` on macOS |
					  | `_` | black hole | discards text (write-only; like `/dev/null`) |
					  | `/` | search | last search pattern |
					  | `:` | command | last Ex command |
					  | `%` | filename | current buffer's filename (read-only) |
					  | `#` | alternate file | alternate buffer filename (read-only) |
					  | `.` | last insert | text inserted in last insert mode (read-only) |
			- ### The unnamed register `"`
				- When you type `"` followed by `"` (i.e., `""y` or `""p`), you're explicitly naming the **unnamed register**
				- But `"` by itself as a prefix just means "register selector" — the character that follows names which register to use
				- Every `y`, `d`, `c`, `x` goes to `"` (unnamed) by default unless you prefix a register name
			- ### Why `"0` matters
				- `d` (delete) overwrites the unnamed register `"`, so after a delete, your previous yank is gone from `"`
				- But explicit yanks (`y`) also always go to register `0`
				- So `"0p` always pastes your last **yank** regardless of intervening deletes — very useful
			- ### Inspecting registers
				- ~~~
				  :reg
				  ~~~
				- or to see a specific one:
					- ~~~
					  :reg a + 0
					  ~~~
			- ### Sources
				- [Neovim registers documentation](https://neovim.io/doc/user/change.html#registers)
