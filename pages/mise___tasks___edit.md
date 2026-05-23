tags:: [[mise/Commands]]

- # `mise tasks edit <task-name>` [mise command](https://mise.jdx.dev/cli/tasks/edit.html)
	- **Usage**: `mise tasks edit [-p --path] <TASK>`
	- **Source code**: [`src/cli/tasks/edit.rs`](https://github.com/jdx/mise/blob/main/src/cli/tasks/edit.rs)
	- Edit a task with $EDITOR
	- The task will be created as a standalone script if it does not already exist.