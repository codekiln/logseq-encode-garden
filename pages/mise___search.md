tags:: [[mise/Comm]]

- [mise search | mise-en-place](https://mise.jdx.dev/cli/search.html)
	- **Usage**: `mise search [FLAGS] [NAME]`
	- **Source code**: [`src/cli/search.rs`](https://github.com/jdx/mise/blob/main/src/cli/search.rs)
	- Search for tools in the registry
	- This command searches a tool in the registry.
	- By default, it will show all tools that fuzzy match the search term. For non-fuzzy matches, use the `--match-type` flag.