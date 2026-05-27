logseq-entity:: [[Logseq/Entity/question]]

- # How do I clear the installed [[mise/Tool]]s? [[card]]
	- ## [[My Answer]]
		- [[mise/cache/clear]], optionally specifying the tools.
		- [[mise/cache/prune]] removes items not accessed in 30 days.
	- ## [[Answer from AI]]
		- **Short answer:** run [[mise/cache/clear]] to delete mise cache files. Pass one or more tool names to limit scope, e.g. `mise cache clear node python`. Alias: `mise cache c`.
		- **See the cache location:** [[mise/cache]] with no subcommand, or [[mise/cache/path]], prints the directory (on macOS often `~/Library/Caches/mise`; Linux often `~/.cache/mise`).
		- **Lighter cleanup:** [[mise/cache/prune]] removes cache entries not accessed in 30 days (override with `MISE_CACHE_PRUNE_AGE`). Use when you want to reclaim space without wiping everything.
		- **After a full clear:** reinstall tools that mise still lists in config, e.g. `mise install`, if versions were removed from disk along with cache data.
		- **Caveat:** some backends (notably `http:`) symlink installs into the cache; clearing cache can leave dangling installs until you reinstall those tools.