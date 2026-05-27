logseq-entity:: [[Logseq/Entity/CLI/Command]]

- # [mise install](https://mise.jdx.dev/cli/install.html)
	- **Usage**: `mise install [FLAGS] [TOOL@VERSION]…`
	- **Aliases**: `i`
	- ## [[mise]] questions
		- ### Where does [[mise/install]] `mise install TOOL@VERSION` place the installed [[mise/Tool]]? [[card]]
		  card-last-interval:: 3.69
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2026-05-19T03:04:46.085Z
		  card-last-reviewed:: 2026-05-15T11:04:46.086Z
		  card-last-score:: 3
			- It installs `TOOL@VERSION` to `~/.local/share/mise/installs/<PLUGIN>/<VERSION>`
			- #### [[Example]]
				- In a directory with `mise.toml`:
				- ```toml
				  [tools]
				  node = 20
				  ```
				- then after running `mise install`, `~/.local/share/mise/installs/node/20` contains node version 20.
				- By default, it will be in the current directory, otherwise it will be in the global mise config.
		-