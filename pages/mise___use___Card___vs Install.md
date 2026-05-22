logseq-entity:: [[Logseq/Entity/Card]]

- # What's the difference between [[mise/use]] and [[mise/install]]? [[card]]
  card-last-interval:: 5.4
  card-repeats:: 1
  card-ease-factor:: 2.6
  card-next-schedule:: 2026-05-27T17:17:00.530Z
  card-last-reviewed:: 2026-05-22T08:17:00.531Z
  card-last-score:: 5
	- `mise install` does **one** thing:
		- Installs a tool version to `~/.local/share/mise/installs/<PLUGIN>/<VERSION>`
	- `mise use` does **two** things:
		- call `mise install`
		- add the [[mise/Tool]] version to [[mise/Config/mise.toml]]