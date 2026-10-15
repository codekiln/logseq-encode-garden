logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Code/Plugin/Skills-Directory Plugin]], [[Codex/Plugin/Q/Is a Codex skills-only plugin the same idea as a Claude Code skills-directory plugin?]]
- # Does registering a local [[Codex/Plugin]] copy it into a home-directory cache?
	- ## [[AI Answer]]
		- **Yes, installation copies it.** Registering a marketplace tells Codex where to find a catalog; installing a plugin creates the copy used at runtime. This distinction applies even when the catalog points to a local checkout.
		- [[Answer/Official]] from [Package your plugin — How local marketplaces work](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work), checked October 15, 2026: installed plugins live under `~/.codex/plugins/cache/<marketplace>/<plugin>/<version>/`; local plugins use `local` as the cache directory's version segment. The runtime reads that installed copy.
		- ### What happens after a source edit?
			- Edit the checkout named by the marketplace entry. Treat the cache as generated installation output.
			- The [Codex cache-refresh implementation](https://github.com/openai/codex/blob/main/codex-rs/core-plugins/src/loader.rs#L639-L668) has both version-conditional refresh and forced reinstall paths. Version-conditional refresh skips installation when the active version matches the source version. A saved file alone therefore does not guarantee that every refresh path copies the change.
			- The authoring documentation recommends restarting the desktop app after source changes. If the old behavior remains, bump the package version and reinstall through the plugin browser, then start a new chat. Verify the changed skill or tool behavior in that chat.
			- `codex plugin marketplace upgrade` refreshes configured Git marketplace snapshots. It is distinct from installing a plugin payload. The installed CLI, `codex-cli 0.162.1`, exposes installation as `codex plugin add <plugin>@<marketplace>`.
		- ### Can a repo still enable its own plugin?
			- Yes. A repo marketplace plus a trusted project configuration can enable a local-marketplace plugin; configured plugins can be installed or refreshed during marketplace refresh. This still uses the cache. See [[Codex/Plugin/Q/Is a Codex skills-only plugin the same idea as a Claude Code skills-directory plugin?]].
		- ### How does this compare with Claude?
			- A Claude marketplace installation also uses a cache. A [[Claude/Code/Plugin/Skills-Directory Plugin]] loads from its source directory; its `@skills-dir` origin identifies that discovery mechanism. [Claude plugin loading reference](https://code.claude.com/docs/en/plugins/loading#find-where-a-plugin-came-from).
			- For editing a Codex skill in place, use a plain [[Codex/Skill]] under `.agents/skills/<skill-name>/SKILL.md`. Codex supports symlinked skill directories and detects skill changes. [Build skills — local discovery](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
