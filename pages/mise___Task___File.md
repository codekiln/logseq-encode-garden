alias:: [[mise File Tasks]]

- # [Mise File Tasks](https://mise.jdx.dev/tasks/file-tasks.html)
	- Mise file tasks are [[Shell/Script]]s placed in directories relative to [[mise/Config/mise.toml]] such as
		- [[My Note]] it's not clear to me that this includes the root ~/.config/mise/tasks directory out of the box. I think that in a directory that has `mise.toml`, the subdirectories are valid, but I'm still not quite sure where the mise file tasks should be placed that are global. It is possible to [manually define task directories](https://mise.jdx.dev/tasks/task-configuration.html#task-config-includes) but I'd prefer to rely on convention over configuration where possible.
		- `mise-tasks/:task_name`
		- `.mise-tasks/:task_name`
		- `mise/tasks/:task_name`
		- `.mise/tasks/:task_name`
		- `.config/mise/tasks/:task_name`
	- They have `#MISE` directives in them which can be used to provide [[mise Task Arguments]]
		- ```sh
		  #!/usr/bin/env bash
		  #MISE description="Build the CLI"
		  cargo build
		  ```
	- {{embed [[mise/Task/File/Group]]}}
	-