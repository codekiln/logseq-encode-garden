logseq-entity:: [[Logseq/Entity/Question]]

- # Is there a way to fuzzy find through the directories that are open in my [[tmux/Pane]]s?
	- ## [[AI Answer]]
		- **Short answer:** yes — tmux exposes each pane's working directory as the `pane_current_path` format variable, so you can list every pane across all sessions and windows and pipe it through [[fzf]], then jump straight to the match.
		- Native command, no plugin required:
			- ~~~bash
			  tmux list-panes -a -F "#{session_name}:#{window_index}.#{pane_index} #{pane_current_path}" | fzf
			  ~~~
			- Parse the selected line and run `tmux switch-client -t <session> \; select-window -t <window> \; select-pane -t <pane>` to land on it. A worked version of this script (also matching on window name, pane title, and current command, not just the path) is in [tmux and fzf: fuzzy tmux session/window/pane switcher](https://eioki.eu/2021/01/12/tmux-and-fzf-fuzzy-tmux-session-window-pane-switcher).
		- **Ready-made plugin:** [tmux-fuzzywuzzy](https://github.com/cfoust/tmux-fuzzywuzzy) fuzzy-searches sessions/windows/panes with a live preview. Install via [[tmux/Plugin/Manager]]:
			- ~~~
			  set -g @plugin 'cfoust/tmux-fuzzywuzzy'
			  set -g @fuzzy-wuzzy "b"
			  ~~~
			- Then trigger it with `prefix + b` (or whichever key you bind).
		- This is the pane-directory-scoped sibling of the `ff` file-fuzzy-finder already noted on [[fzf]] — same underlying idea, applied to `pane_current_path` instead of a directory tree.
