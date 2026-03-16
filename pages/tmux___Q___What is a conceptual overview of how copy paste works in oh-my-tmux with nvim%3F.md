- # What is a conceptual overview of how copy paste works in [[tmux/oh-my-tmux]] with [[nvim]]?
	- ## Answer
		- [[AI/Response]]
			- ### The Three Clipboard Layers
				- At its core, copy-paste in this stack involves three independent clipboard systems that must cooperate:
					- **tmux's internal buffer** — a paste buffer private to the tmux server process
					- **nvim's registers** — in-process yank storage, including the special `+` (system clipboard) and `*` (primary selection) registers
					- **the OS system clipboard** — macOS Pasteboard (`pbcopy`/`pbpaste`) or X11/Wayland clipboard
				- Getting text from A to B means understanding which layer it lands in and how (or whether) the layers are bridged.
			- ### tmux's Internal Buffer
				- Enter copy mode with `Prefix+[` (oh-my-tmux default; some configs use `Prefix+Escape`)
				- oh-my-tmux enables vi-style bindings in copy mode: `v` to begin selection, `y` to yank
				- Yanked text goes into tmux's paste buffer — **shared across all windows and sessions of the same tmux server**
				- Paste anywhere in the same server with `Prefix+]`
				- This means tmux-buffer copy/paste works transparently across sessions and windows without touching the OS clipboard at all
			- ### oh-my-tmux Clipboard Bridge
				- oh-my-tmux auto-detects the OS and wires `y` in copy mode to also send the selection to the system clipboard:
					- macOS: pipes through `pbcopy`
					- Linux: uses `xclip`, `xsel`, or `wl-copy` depending on what's available
				- Controlled in `.tmux.conf.local` via settings like `set -g @copy_use_prefix on`
				- After this bridge is active, yanking in tmux copy mode simultaneously fills both the tmux buffer **and** the OS clipboard
				- On macOS inside Terminal.app or iTerm2, this just works. Inside SSH or nested tmux, you may need `reattach-to-user-namespace` (older macOS) or proper `$TERM` / `$TMUX` detection
			- ### nvim's Clipboard Register
				- By default, nvim yanks (`y`, `dd`, etc.) go to nvim's unnamed register — **not** the OS clipboard
				- To yank explicitly to the system clipboard from nvim: `"+y` (or `"*y` for primary selection)
				- To make all nvim yanks go to the system clipboard automatically, add to your nvim config:
					- ~~~lua
					  vim.opt.clipboard = "unnamedplus"
					  ~~~
					- or in vimscript: `set clipboard=unnamedplus`
				- With `unnamedplus` set, `y` in nvim = `"+y` — text lands in both nvim's register and the OS clipboard
			- ### Practical Scenarios
				- #### Copy in nvim → paste in another tmux window or session
					- If `clipboard=unnamedplus` is set in nvim: yank normally, then `Prefix+]` will **not** work (that's the tmux buffer, not OS clipboard)
					- Better path: switch to the target window, enter nvim (or another shell), and paste with `Cmd+V` (macOS) or `Ctrl+Shift+V` (Linux terminal)
					- Alternative: explicitly yank to tmux buffer from nvim using a shell command: `:!echo -n "text" | tmux load-buffer -` (awkward)
					- Cleanest solution: with `clipboard=unnamedplus` on and oh-my-tmux's clipboard bridge active, **both** the OS clipboard and tmux buffer stay in sync — `Prefix+]` works anywhere in the server after a tmux-mode yank
				- #### Copy in tmux copy mode → paste in browser
					- Must go through the OS clipboard — the tmux buffer is invisible to the browser
					- With oh-my-tmux's clipboard bridge active: yank with `y` in copy mode → OS clipboard is filled → `Cmd+V` / `Ctrl+V` in browser works
					- If the bridge is not active, use mouse-select + `Cmd+C` (macOS) to copy directly via the terminal emulator
				- #### Copy in nvim → paste in browser
					- Yank to `+` register in nvim: `"+y` or use `clipboard=unnamedplus`
					- `Cmd+V` in browser works immediately
				- #### Copy from browser → paste in nvim
					- `Cmd+C` in browser fills OS clipboard
					- In nvim normal mode: `"+p` to paste from system clipboard
					- With `clipboard=unnamedplus`: plain `p` works
					- In tmux copy mode is not involved here at all
			- ### Summary Mental Model
				- | Goal | Mechanism |
				  |------|-----------|
				  | tmux window → tmux window/session | `Prefix+[` yank → `Prefix+]` paste |
				  | tmux → browser | oh-my-tmux clipboard bridge → OS clipboard → `Cmd+V` |
				  | nvim → browser | `"+y` in nvim (or `clipboard=unnamedplus`) → `Cmd+V` |
				  | nvim → other tmux window | OS clipboard (via `clipboard=unnamedplus`) → `Cmd+V` or `"+p` in destination |
				  | browser → nvim | `Cmd+C` browser → `"+p` in nvim (or `p` with `clipboard=unnamedplus`) |
			- ### Recommended Setup for Smooth Interop
				- In nvim config: `vim.opt.clipboard = "unnamedplus"` — makes nvim always use OS clipboard
				- Verify oh-my-tmux clipboard bridge is working: yank something in copy mode, then `pbpaste` (macOS) in a shell — should print it
				- With both in place, you effectively have one unified clipboard: yank anywhere, paste anywhere
			- ### Sources
				- [oh-my-tmux README — copy/paste section](https://github.com/gpakosz/.tmux)
				- [Neovim clipboard documentation](https://neovim.io/doc/user/provider.html#clipboard)
				- [tmux man page — buffers](https://man7.org/linux/man-pages/man1/tmux.1.html)
