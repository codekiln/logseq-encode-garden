alias:: [[mise File Tasks]]

- # [Mise File Tasks](https://mise.jdx.dev/tasks/file-tasks.html)
	- Mise file tasks are [[Shell/Script]]s placed in directories relative to each config scope’s `config_root` (the directory containing that scope’s [[mise/Config/mise.toml]] or [[mise/Config/Global]] file). For global config at `~/.config/mise/config.toml`, `~/.config/mise/tasks/` is discovered via the default `.config/mise/tasks` entry—see [[mise/Q/If I place an executable file task in ~/.config/mise/tasks/myscript, will mise run myscript work without extra configuration?]].
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