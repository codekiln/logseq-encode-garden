logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/Backend/npm]], [[mise/search]], [[Aube]]

- # What's the most idiomatic way to search for an npm dependency in [[mise]], assuming I'm using [[Aube]] as my [[mise/Backend/npm]] backend?
- ## Answer
	- [[AI/Response]]
		- **Short answer:** use `npm search <term>` for discovery, then `mise use npm:<package>` (or `mise use -g npm:<package>`) once you know the package name.
		- **Why not `mise search`:** `mise search` searches the mise registry of tool shorthands, not arbitrary npm packages.
		- **Why not `aube search`:** Aube treats `search` as an out-of-scope registry helper and points you to the npm command instead.
		- **What the backend changes:** `npm.package_manager = "aube"` changes how the `npm:` backend installs packages; package discovery is still outside `mise search`.
		- **Practical flow:** run `npm search eslint` (or search on npmjs.com), then install the package you want with `mise use npm:eslint` or `mise use -g npm:eslint`.
		- [mise search](https://mise.jdx.dev/cli/search.html)
		- [mise npm backend](https://mise.jdx.dev/dev-tools/backends/npm.html)
		- [aube README](https://raw.githubusercontent.com/endevco/aube/main/README.md)
		- [npm search](https://docs.npmjs.com/cli/v7/commands/npm-search/)
