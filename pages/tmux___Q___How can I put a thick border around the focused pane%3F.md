# How can I put a thick border around the focused pane in [[tmux]]?
	- It's difficult to figure out which pane has focus.
	- ## Answer
		- Use the `pane-border-lines` option set to `heavy`:
			- ~~~
			  set -g pane-border-lines heavy
			  ~~~
		- This uses thick UTF-8 box-drawing characters for all pane borders.
		- To make the **active pane** stand out even more, combine with `pane-active-border-style`:
			- ~~~
			  set -g pane-border-lines heavy
			  set -g pane-active-border-style fg=green
			  set -g pane-border-style fg=colour238
			  ~~~
		- ### Available `pane-border-lines` values
			- `single` - single lines using ACS or UTF-8 characters (default)
			- `double` - double lines using UTF-8 characters
			- `heavy` - heavy/thick lines using UTF-8 characters
			- `simple` - simple ASCII characters
			- `number` - displays the pane number
			- `spaces` - space characters (no visible border)
		- ### Additional options for indicating the active pane
			- `pane-border-indicators` can highlight the active pane in different ways:
				- `off` - no special indication
				- `colour` - color only half the border in 2-pane windows
				- `arrows` - display arrow markers pointing to active pane
				- `both` - use both color and arrows
			- Example:
				- ~~~
				  set -g pane-border-indicators arrows
				  ~~~
		- ### Requirements
			- `heavy` and `double` border styles require UTF-8 support in your terminal
			- If UTF-8 is not supported, tmux falls back to standard ACS line drawing
	- ## Going Further: Making Focus Impossible to Miss
		- Heavy borders alone are still pretty subtle, especially in dense multi-pane layouts. Thick lines alone don't change enough visual contrast.
		- For **"impossible to miss" focus**, stack multiple signals:
			- border weight
			- strong color contrast
			- background fill change
			- title/status cue
			- optionally dim *inactive* panes instead of highlighting the active one
		- That last trick (dim others) is dramatically more legible.
		- ### Tier 1 — Strong border + high-contrast color
			- Much louder than basic `fg=green`:
				- ~~~
				  set -g pane-border-lines heavy
				  
				  # inactive = dark gray
				  set -g pane-border-style fg=colour238
				  
				  # active = neon
				  set -g pane-active-border-style fg=colour46,bold
				  ~~~
			- Bright green (`colour46`) or yellow (`colour226`) pops much harder than `green`.
		- ### Tier 2 — Fill the entire active pane background (huge improvement)
			- This is the first *actually obvious* solution.
			- Change the **pane background**, not just the border:
				- ~~~
				  # dim inactive panes
				  set -g window-style fg=colour245,bg=colour234
				  
				  # brighten active pane
				  set -g window-active-style fg=colour255,bg=colour236
				  ~~~
			- Effect:
				- everything else looks muted
				- active pane looks "lit"
			- This is far more perceptible than borders alone.
			- Most people who try this never go back.
		- ### Tier 3 — Add explicit focus markers (arrows)
			- Adds directional cues:
				- ~~~
				  set -g pane-border-indicators both
				  ~~~
			- Gives arrows + color hint on the border edges.
			- Helpful when panes are small.
		- ### Tier 4 — Big "FOCUS" tag in the border (very obvious)
			- tmux lets you show text in the active border:
				- ~~~
				  set -g pane-border-format "#{?pane_active,#[bold fg=black bg=colour46] ACTIVE #[default], }"
				  ~~~
			- You literally get `ACTIVE` on the focused pane's border. Zero ambiguity.
		- ### Tier 5 — Extreme (best for dense layouts)
			- Combine dimming + bright border + title:
				- ~~~
				  set -g pane-border-lines heavy
				  set -g pane-border-style fg=colour238
				  set -g pane-active-border-style fg=colour226,bold
				  
				  set -g window-style fg=colour245,bg=colour234
				  set -g window-active-style fg=colour255,bg=colour236
				  
				  set -g pane-border-indicators both
				  
				  set -g pane-border-format "#{?pane_active,#[bold fg=black bg=colour226] ● ACTIVE #[default], }"
				  ~~~
			- This gives you:
				- dim others
				- bright yellow border
				- arrows
				- literal "● ACTIVE" label
			- It's almost impossible to lose track of focus.
		- ### Bonus: focus flash when switching panes
			- A quick flash on selection for nice UX:
				- ~~~
				  bind -n C-h select-pane -L \; display-message "◀"
				  bind -n C-j select-pane -D \; display-message "▼"
				  bind -n C-k select-pane -U \; display-message "▲"
				  bind -n C-l select-pane -R \; display-message "▶"
				  ~~~
			- Small directional feedback helps muscle memory.
		- ### Practical recommendation
			- For dense layouts (lots of panes, codespaces, tmux nested in browser): start with **Tier 2 + Tier 5 combo** (dim inactive + bright border + label).
			- Borders alone just don't carry enough signal.
			- That combo makes the active pane visually dominant without being garish.
	- ## My Notes
		- Add to `~/.tmux.conf` and reload with `tmux source-file ~/.tmux.conf`
		- Or test live with `prefix + :` then type the set command
	- ## Related
		- [[tmux/setw]]