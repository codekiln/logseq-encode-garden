logseq-entity:: [[Logseq/Entity/CLI/Command]]
tags:: [[mise/Commands]]

- # `mise tasks add` [mise command](https://mise.jdx.dev/cli/tasks/add.html)
	- **Usage**: `mise tasks add [FLAGS] <TASK> [-- RUN]…`
	- **Source code**: [`src/cli/tasks/add.rs`](https://github.com/jdx/mise/blob/main/src/cli/tasks/add.rs)
	- Create a new task
	- Adds a task to the local [[mise/Config/mise.toml]].
		- See [https://mise.en.dev/configuration.html#target-file-for-write-operations](https://mise.en.dev/configuration.html#target-file-for-write-operations)
	- ## Selected Flags
		- {{embed [[mise/tasks/add/file]]}}