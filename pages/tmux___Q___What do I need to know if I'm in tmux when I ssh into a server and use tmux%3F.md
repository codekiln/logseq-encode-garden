logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Q/Why doesn't prefix Alt-Left or Alt-Right resize the inner horizontal split in a nested tmux layout (outer top-bottom split and lower left-right split), while Alt-Up or Alt-Down still move the outer boundary?]]

- # What do I need to know if I'm in [[tmux]] when I [[SSH]] into a server and use [[tmux]]?
	- ## [[AI Answer]]
		- **Short answer:** The outer [[tmux]] intercepts your prefix key before it reaches the inner [[tmux]]. Press the prefix **twice** to send it to the inner session. Also watch for `TERM` terminfo mismatches on the remote.
		- ### Prefix key collision
			- Both outer (local) and inner (remote) [[tmux]] listen on the same prefix (`Ctrl+b` by default).
			- Pressing `Ctrl+b <key>` acts on the **outer** session.
			- To send a command to the **inner** session, press the prefix **twice**: `Ctrl+b Ctrl+b <key>`.
				- Examples:
					- `Ctrl+b Ctrl+b c` — new window in the inner session
					- `Ctrl+b Ctrl+b d` — detach from the inner session (leaves SSH open)
					- `Ctrl+b Ctrl+b [` — enter copy mode in the inner session
		- ### `TERM` terminfo mismatch
			- Inside [[tmux]], `TERM` is set to `tmux-256color` (or `screen-256color`). Remote servers often lack that terminfo entry, causing display artifacts or errors.
			- Quick fix — set `TERM` to a widely available value before SSHing:
				- ~~~
				  TERM=xterm-256color ssh user@host
				  ~~~
			- Or in `~/.ssh/config`:
				- ~~~
				  Host myserver
				      SendEnv TERM
				  ~~~
				- (requires `AcceptEnv TERM` on the server's `sshd_config`)
			- Permanent fix — install the tmux terminfo on the remote once:
				- ~~~
				  infocmp tmux-256color | ssh user@host -- tic -x -
				  ~~~
		- ### Double status bar
			- Both sessions show their own status bar. You get two stacked bars at the bottom while nested. This is normal and harmless; just visually noisy.
		- ### Using a different prefix for the inner session
			- A common convention: configure the remote `~/.tmux.conf` to use a different prefix (e.g. `Ctrl+a`) so the two sessions are unambiguous.
				- ~~~
				  # on the remote server's ~/.tmux.conf
				  set-option -g prefix C-a
				  bind-key C-a send-prefix
				  ~~~
		- ### The `$TMUX` environment variable
			- Inside any tmux session, `$TMUX` is set. The SSH connection starts a fresh environment on the remote, so `$TMUX` does **not** propagate to the remote server's shell. Remote tmux starts cleanly regardless.
		- ### Sources
			- [tmux FAQ — Nesting](https://github.com/tmux/tmux/wiki/FAQ#how-do-i-use-a-different-prefix-key)
			- [Super User — How to use tmux when logged into a remote server that also uses tmux](https://superuser.com/questions/249659/how-to-use-tmux-when-logged-into-a-remote-server-that-also-uses-tmux)
