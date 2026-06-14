logseq-entity:: [[Logseq/Entity/Question]]

- # How do I clear the installed [[mise/Tool]]s (either all of them, or the recently used ones) so you can reinstall them? [[card]]
  card-last-interval:: -1
  card-repeats:: 1
  card-ease-factor:: 2.5
  card-next-schedule:: 2026-06-11T04:00:00.000Z
  card-last-reviewed:: 2026-06-10T07:41:44.377Z
  card-last-score:: 1
	- ## [[My Answer]]
		- [[mise/cache/clear]], optionally specifying the tools.
		- [[mise/cache/prune]] removes items not accessed in 30 days.
	- ## [[Answer from AI]]
		- **Short answer:** run [[mise/cache/clear]] to delete mise cache files. Pass one or more tool names to limit scope, e.g. `mise cache clear node python`. Alias: `mise cache c`.
		- **See the cache location:** [[mise/cache]] with no subcommand, or [[mise/cache/path]], prints the directory (on macOS often `~/Library/Caches/mise`; Linux often `~/.cache/mise`).
		- **Lighter cleanup:** [[mise/cache/prune]] removes cache entries not accessed in 30 days (override with `MISE_CACHE_PRUNE_AGE`). Use when you want to reclaim space without wiping everything.
		- **After a full clear:** reinstall tools that mise still lists in config, e.g. `mise install`, if versions were removed from disk along with cache data.
		- **Caveat:** some backends (notably `http:`) symlink installs into the cache; clearing cache can leave dangling installs until you reinstall those tools.