tags:: [[mise/Commands]]

- # [mise cache prune](https://mise.jdx.dev/cli/cache/prune.html)
	- **Usage**: `mise cache prune [-v --verbose…] [--dry-run] [PLUGIN]…`
	- **Aliases**: `p`
	- **Source code**: [`src/cli/cache/prune.rs`](https://github.com/jdx/mise/blob/main/src/cli/cache/prune.rs)
	- Removes stale mise cache files. By default, deletes entries not accessed in 30 days; override with `MISE_CACHE_PRUNE_AGE`. Optional `[PLUGIN]…` limits pruning to named tools.
