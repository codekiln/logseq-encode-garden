- [[Keyshort]] [[vim]] [[vim/Keyshort]]
	- **Close the `gO` outline / table-of-contents UI (help in location list)** #card
	  card-last-score:: 5
	  card-repeats:: 2
	  card-next-schedule:: 2026-06-28T06:16:56.282Z
	  card-last-interval:: 4
	  card-ease-factor:: 2.8
	  card-last-reviewed:: 2026-06-24T06:16:56.282Z
		- **Direct close:** `:lclose` — closes the **location-list** window Neovim opens for the `gO` outline (`:lopen` under the hood). Prefer this when you only want rid of the outline split.
		- **If other splits are left over (e.g. `[No Name]`, empty area):** `:only` — keep **only** the current window; heavier than `:lclose` but good when layout is confusing.
		- **With focus inside the list split:** `:q` or `Ctrl-W c` — same idea as closing any window.
		- **See also**
			- `Ctrl-W w` — cycle windows; see where focus is after `gO` / `:lclose`.
			- `:buffers` / `:ls` — list buffers; useful when you suspect extra buffers, not only extra windows.
		- **Note:** In **Neovim**, `gO` in `help` uses the **location list** (not a special “outline buffer” type). Plain **Vim** may differ; if this card ever feels wrong there, split a **Neovim-only** keyshort page.