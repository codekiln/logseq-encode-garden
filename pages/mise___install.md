# [mise install](https://mise.jdx.dev/cli/install.html)
	- **Usage**: `mise install [FLAGS] [TOOL@VERSION]…`
	- **Aliases**: `i`
	- ## [[mise]] questions
		- ### Where does [[mise/install]] `mise install TOOL@VERSION` place the installed [[mise/Tool]]? [[card]]
			- It installs `TOOL@VERSION` to `~/.local/share/mise/installs/<PLUGIN>/<VERSION>`
			- #### [[Example]]
				- In a directory with `mise.toml`:
				- ```toml
				  [tools]
				  node = 20
				  ```
				- then after running `mise install`, `~/.local/share/mise/installs/node/20` contains node version 20.
		-