logseq-entity:: [[Logseq/Entity/Question]], [[Logseq/Entity/Card]]

- # What is a tabpage in [[vim]]? [[card]]
  card-last-interval:: 5.4
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-06-28T18:54:59.355Z
  card-last-reviewed:: 2026-06-23T09:54:59.356Z
  card-last-score:: 5
	- ## [[Answer/Official]] from [`:help tabpage`](https://vimhelp.org/tabpage.html)
		- ### Short answer
			- A **tabpage** is vim's highest-level workspace container — it holds one or more **windows**, which are viewports onto **buffers**.
		- ### Three-level hierarchy
			- **Tabpage** — a full-screen workspace; each tabpage has its own window layout
				- **Window** — a viewport onto a buffer; created via `:split` / `:vsplit` within a tabpage
					- **Buffer** — the in-memory text of a file; persists even when no window is showing it
		- ### When to use tabs
			- tabpages let you maintain separate window layouts for distinct tasks (e.g., editing one module vs. reviewing another) without disrupting either layout when switching.
		- ### Key commands and keys
			- `:tabnew` / `:tabe[dit] {file}` — open a new tabpage (optionally loading a file)
			- `:tabc[lose]` — close the current tabpage
			- `:tabs` — list all tabpages and their windows
			- `:tabm[ove] {N}` — move current tabpage to position N (0-indexed)
			- `gt` — go to the next tabpage
			- `gT` — go to the previous tabpage
			- `{N}gt` — jump to tabpage N (1-indexed)
		- [vim help: tabpage](https://vimhelp.org/tabpage.html)