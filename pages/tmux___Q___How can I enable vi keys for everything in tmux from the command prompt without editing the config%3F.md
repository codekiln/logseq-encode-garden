logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]
see-also:: [[tmux/Command/Prompt/Q/Will the TMux Command prompt use Vim or Emacs keys?]]

- # How can I enable [[vim]] keys for everything in [[tmux]] from the [[tmux/Command/Prompt]] without editing the config? [[card]]
  card-last-interval:: 5.4
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-06-29T14:56:11.352Z
  card-last-reviewed:: 2026-06-24T05:56:11.352Z
  card-last-score:: 5
	- [[tmux/Command/Prompt]] (`Prefix :`)
		- `set -g mode-keys vi`
			- sets vi controls in [[tmux/Option/mode-keys]] (scrolling, search, text selection)
		- `set -g status-keys vi`
			- sets vi controls in [[tmux/Option/status-keys]] ([[tmux/Command/Prompt]], rename prompt, search prompts)
		- these are runtime-only; it will be gone again after `tmux kill-server`
	- ## [[AI Answer]]
	  collapsed:: true
		- **Short answer:** Press `Prefix :` and run `set -g mode-keys vi`, then repeat for `set -g status-keys vi`. Two commands, done. Changes are runtime-only—they vanish after `tmux kill-server`.
		- ### The two options
			- [[tmux/Option/mode-keys]] — controls [[tmux/Mode/Copy]], scrolling, search, and text selection. Default is `emacs`.
			- [[tmux/Option/status-keys]] — controls the [[tmux/Command/Prompt]] (`Prefix :`, rename prompts, search prompts). Default is `emacs` unless `$VISUAL` or `$EDITOR` contains `vi`.
		- ### Steps at the command prompt
			- 1. `Prefix :` → type `set -g mode-keys vi` → Enter
			- 2. `Prefix :` → type `set -g status-keys vi` → Enter
			- Both options accept `vi` or `emacs`. The `-g` flag applies the change globally (all sessions on the current server) without writing to any file.
		- ### From the shell (outside tmux)
			- ~~~sh
			  tmux set -g mode-keys vi && tmux set -g status-keys vi
			  ~~~
			- Useful when you want to script it or apply it before attaching.
		- ### Persistence caveat
			- These commands change the **running tmux server**; they do not touch `~/.tmux.conf`. The settings disappear when the server stops (`tmux kill-server` or system reboot). To make them permanent, add the same two `set -g` lines to your config and reload with `Prefix r` (or `tmux source-file ~/.tmux.conf`).