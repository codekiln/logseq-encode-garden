logseq-entity:: [[Logseq/Entity/question]], [[Logseq/Entity/Card]] 
see-also:: [[mise]], [[mise/unuse]], [[mise/uninstall]], [[mise/cache/clear]], [[mise/Q/How do I remove a mise tool?]], [[mise/Q/How do I clear the installed mise tools?]]

- # What's the difference between [[mise/unuse]], [[mise/uninstall]], and [[mise/cache/clear]]? [[card]]
  card-last-interval:: -1
  card-repeats:: 1
  card-ease-factor:: 2.5
  card-next-schedule:: 2026-06-11T04:00:00.000Z
  card-last-reviewed:: 2026-06-10T07:49:17.536Z
  card-last-score:: 1
	- ## [[My Answer]]
		- | Command              | Primary effect           | Config `[tools]` | Installed binaries | Cache |
		  | -------------------- | ------------------------ | ---------------- | ------------------ | ----- |
		  | [[mise/unuse]]       | remove config and binary | ✓                | ✓                  | ✗     |
		  | [[mise/uninstall]]   | remove binary            | ✗                | ✓                  | ✗     |
		  | [[mise/cache/clear]] | remove build cache       | ✗                | ✗                  | ✓     |
		- Cache clear does **not** uninstall, but symlinked backends may need [[mise/install]] after a full clear.
			- TODO fix the other flashcard about how to uninstall all commands in mise
	- ## [[AI Answer]]
		- **Short answer:** they operate on three different layers. [[mise/unuse]] removes a tool from **config** and usually prunes the install too; [[mise/uninstall]] deletes **installed versions on disk** without touching config; [[mise/cache/clear]] wipes **mise's download/build cache** without editing config.
		- **[[mise/unuse]]** — removes `TOOL@VERSION` entries from `mise.toml` (or global / env-specific config with flags). Aliases: `mise rm`, `mise remove`. By default it **also prunes** the installed copy when no other config still references that version; pass `--no-prune` to drop the config line but keep the binary. This is the usual way to stop tracking a tool in a project or globally. [mise unuse](https://mise.jdx.dev/cli/unuse.html)
		- **[[mise/uninstall]]** — deletes installed version trees from disk only. Docs: “This only removes the installed version, it does not modify mise.toml.” After uninstall, `mise ls` can still show the tool from config until you run `mise install` again or remove it with [[mise/unuse]]. Use when you want to reclaim disk space but keep the pin in config, or before reinstalling a broken copy. [mise uninstall](https://mise.jdx.dev/cli/uninstall.html)
		- **[[mise/cache/clear]]** — deletes cache files (all plugins by default, or pass `node python` to scope). Alias: `mise cache c`. Does not edit config or directly run unuse/uninstall semantics. After a full clear you may need `mise install` for tools still listed in config; some backends symlink installs into the cache, so clearing cache can leave broken installs until reinstall. See [[mise/Q/How do I clear the installed mise tools?]] and [[mise/cache/prune]] for lighter cleanup. [mise cache clear](https://mise.jdx.dev/cli/cache/clear.html)
		- **Quick comparison**
			- **Config `[tools]`:** unuse ✓ · uninstall ✗ · cache clear ✗
			- **Installed tool binaries:** unuse ✓ (default prune) · uninstall ✓ · cache clear ✗ (may require reinstall after cache issues)
			- **Download/build cache:** unuse ✗ · uninstall ✗ · cache clear ✓
		- **Pick one:** stop using a tool in this config → `mise unuse`; keep config but drop binaries → `mise uninstall`; fix stale downloads or cache corruption → `mise cache clear`. See also [[mise/Q/How do I remove a mise tool?]].