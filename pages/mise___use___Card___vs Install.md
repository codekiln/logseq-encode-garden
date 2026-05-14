logseq-entity:: [[Logseq/Entity/Card]]

- # What's the difference between [[mise/use]] and [[mise/install]]? [[card]]
	- `mise install` does **one** thing:
		- Installs a tool version to `~/.local/share/mise/installs/<PLUGIN>/<VERSION>`
	- `mise use` does **two** things:
		- call `mise install`
		- add the [[mise/Tool]] version to [[mise/Config/mise.toml]]