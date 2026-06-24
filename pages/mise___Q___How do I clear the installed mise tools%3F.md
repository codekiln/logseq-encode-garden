logseq-entity:: [[Logseq/Entity/Question]]

- # How do I clear the installed [[mise/Tool]]s (either all of them, or the recently used ones) so you can reinstall them? [[card]]
  card-last-interval:: 3.95
  card-repeats:: 2
  card-ease-factor:: 2.36
  card-next-schedule:: 2026-06-28T04:44:10.251Z
  card-last-reviewed:: 2026-06-24T06:44:10.251Z
  card-last-score:: 3
	- ## [[My Answer]]
		- 1 - AFAIK there's **no** built-in way to bulk uninstall all mise tools. One could use [[mise/ls]] and pipe that to [[mise/uninstall]] somehow, perhaps.
			- 1.1 - I have a [[mise/Task/File]] defined in [[My/Dotfiles]] which can help remove tools that aren't globally installed (that is): `mise tool:missing:uninstall`; that could be used as a guide
				- ```
				  > mise tasks | grep tool
				  tool:missing:ls         List installed mise tools not referenced in any config
				  tool:missing:uninstall  Uninstall mise tools not referenced in any config
				  ```
		- ### [[My Note]]
			- [[mise/cache/clear]] clears the build cache for all tools or, if one has specified a single tool, it clears the build cache for just that tool. This does **not** uninstall the tool.
			- [[mise/cache/prune]] removes cache items not accessed in 30 days.
	- ## [[Answer from AI]]
	  collapsed:: true
		- **Short answer:** run [[mise/cache/clear]] to delete mise cache files. Pass one or more tool names to limit scope, e.g. `mise cache clear node python`. Alias: `mise cache c`.
		- **See the cache location:** [[mise/cache]] with no subcommand, or [[mise/cache/path]], prints the directory (on macOS often `~/Library/Caches/mise`; Linux often `~/.cache/mise`).
		- **Lighter cleanup:** [[mise/cache/prune]] removes cache entries not accessed in 30 days (override with `MISE_CACHE_PRUNE_AGE`). Use when you want to reclaim space without wiping everything.
		- **After a full clear:** reinstall tools that mise still lists in config, e.g. `mise install`, if versions were removed from disk along with cache data.
		- **Caveat:** some backends (notably `http:`) symlink installs into the cache; clearing cache can leave dangling installs until you reinstall those tools.