tags:: [[mise/Commands]]

- [mise en | mise-en-place](https://mise.jdx.dev/cli/en.html)
	- **Usage**: `mise en [-s --shell <SHELL>] [DIR]`
	- **Source code**: [`src/cli/en.rs`](https://github.com/jdx/mise/blob/main/src/cli/en.rs)
	- Starts a new shell with the mise environment built from the current configuration
	- This is an alternative to `mise activate` that allows you to explicitly start a mise session. It will have the tools and environment variables in the configs loaded. Note that changing directories will not update the mise environment.