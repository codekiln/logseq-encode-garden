logseq-entity:: [[Logseq/Entity/CLI/Command]]

- # [mise install](https://mise.jdx.dev/cli/install.html)
	- **Usage**: `mise install [FLAGS] [TOOL@VERSION]…`
	- **Aliases**: `i`
	- ## [[mise]] questions
		- ### Where does [[mise/install]] `mise install TOOL@VERSION` place the installed [[mise/Tool]]? [[card]]
		  card-last-interval:: 4
		  card-repeats:: 2
		  card-ease-factor:: 2.46
		  card-next-schedule:: 2026-06-28T06:00:45.109Z
		  card-last-reviewed:: 2026-06-24T06:00:45.109Z
		  card-last-score:: 5
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