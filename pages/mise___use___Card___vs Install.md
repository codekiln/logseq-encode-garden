logseq-entity:: [[Logseq/Entity/Card]]

- # What's the difference between [[mise/use]] and [[mise/install]]? [[card]]
  card-last-interval:: 4.28
  card-repeats:: 2
  card-ease-factor:: 2.7
  card-next-schedule:: 2026-06-28T12:20:03.190Z
  card-last-reviewed:: 2026-06-24T06:20:03.190Z
  card-last-score:: 5
	- `mise install` does **one** thing:
		- Installs a tool version to `~/.local/share/mise/installs/<PLUGIN>/<VERSION>`
	- `mise use` does **two** things:
		- call `mise install`
		- add the [[mise/Tool]] version to [[mise/Config/mise.toml]]