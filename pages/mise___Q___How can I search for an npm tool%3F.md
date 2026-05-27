logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/Backend/npm]], [[mise/search]], [[Aube]]

- # How can I search for an [[npm]]/ [[Aube]] [[mise/Tool]]? [[card]]
	- ## [[My Answer]]
		- Step 1 - [[npm/search/--searchlimit]] for discovery
			- `npm search --searchlimit 1 rulesync`
				- ```
				  rulesync
				  Unified AI rules management CLI tool that generates configuration files for various AI development tools
				  Version 8.21.0 published 2026-05-26 by GitHub Actions
				  Maintainers: dyoshikawa
				  Keywords: ai cli cline configuration copilot cursor development rules
				  https://npm.im/rulesync
				  ```
		- Step 2 (Optional) - [[npm/view]] for tool to confirm choice
			- `npm view rulesync`
				- ```
				  rulesync@8.21.0 | MIT | deps: 16 | versions: 253
				  Unified AI rules management CLI tool that generates configuration files for various AI development tools
				  https://github.com/dyoshikawa/rulesync#readme
				  
				  keywords: ai, cli, cline, configuration, copilot, cursor, development, rules
				  
				  bin: rulesync
				  
				  dist
				  .tarball: https://registry.npmjs.org/rulesync/-/rulesync-8.21.0.tgz
				  .shasum: 2f4c6890d1c963d756727331cf26c51f3904818d
				  .integrity: sha512-CesPQRnK+HZ3YvGFUq1pvVgxDwf4l/29PLoOKwA/5flneOvN4ccVEIsX6u6VBEfYKZnv59dxGAySbrYdwdy23Q==
				  .unpackedSize: 2.9 MB
				  
				  dependencies:
				  @modelcontextprotocol/sdk: 1.27.1, @octokit/request-error: 7.1.0, @octokit/rest: 22.0.1, @toon-format/toon: 2.1.0, @valibot/to-json-schema: 1.6.0, commander: 14.0.3, effect: 3.20.0, es-toolkit: 1.45.1, fastmcp: 3.34.0, globby: 16.1.1, gray-matter: 4.0.3, js-yaml: 4.1.1, jsonc-parser: 3.3.1, smol-toml: 1.6.1, sury: 10.0.4, zod: 4.3.6
				  
				  maintainers:
				  - dyoshikawa <dyoshikawa1993@gmail.com>
				  
				  dist-tags:
				  latest: 8.21.0
				  
				  published 23 hours ago by GitHub Actions <npm-oidc-no-reply@github.com>
				  
				  ```
		- Step 3 - [[mise/use/--global]] for the tool, prefixed by npm
			- `mise use -g npm:rulesync`
	- ## [[AI Answer]]
		- **Short answer:** use `npm search <term>` for discovery, then `mise use npm:<package>` (or `mise use -g npm:<package>`) once you know the package name.
		- **Why not `mise search`:** `mise search` searches the mise registry of tool shorthands, not arbitrary npm packages.
		- **Why not `aube search`:** Aube treats `search` as an out-of-scope registry helper and points you to the npm command instead.
		- **What the backend changes:** `npm.package_manager = "aube"` changes how the `npm:` backend installs packages; package discovery is still outside `mise search`.
		- **Practical flow:** run `npm search eslint` (or search on npmjs.com), then install the package you want with `mise use npm:eslint` or `mise use -g npm:eslint`.
		- [mise search](https://mise.jdx.dev/cli/search.html)
		- [mise npm backend](https://mise.jdx.dev/dev-tools/backends/npm.html)
		- [aube README](https://raw.githubusercontent.com/endevco/aube/main/README.md)
		- [npm search](https://docs.npmjs.com/cli/v7/commands/npm-search/)