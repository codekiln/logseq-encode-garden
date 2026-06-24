alias:: [[mise Environments]]

- # [Environments | mise-en-place](https://mise.jdx.dev/environments/)
	- ## What are two ways to set [[EnvVars]] with [[mise]]? [[card]]
	  card-last-interval:: 4.14
	  card-repeats:: 2
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-06-28T09:01:42.890Z
	  card-last-reviewed:: 2026-06-24T06:01:42.890Z
	  card-last-score:: 5
		- ### 1 - In [[mise/Config/mise.toml/env]]
			- ```toml
			  [env]
			  NODE_ENV = 'production'
			  ```
		- ### 2 - with [[mise/set]]
			- `mise set NODE_ENV=development`
	- ## What are two ways to _unset_ [[EnvVars]] with [[mise]]? [[card]]
	  card-last-interval:: 4.14
	  card-repeats:: 2
	  card-ease-factor:: 2.7
	  card-next-schedule:: 2026-06-28T09:01:57.138Z
	  card-last-reviewed:: 2026-06-24T06:01:57.138Z
	  card-last-score:: 5
		- ### 1 - In [[mise/Config/mise.toml/env]]
			- ```toml
			  [env]
			  NODE_ENV = false # unset a previously set NODE_ENV
			  ```
			- [[My Notes]]
				- *It's a bit [[Astonishing]] to me that we can unset environment variables with this technique*
				- See also [[TOML/Q/Is false a first-class primitive]].
		- ### 2 - with [[mise/unset]]
			- `mise unset NODE_ENV`
	- ## How do I view declared [[EnvVars]]? [[card]]
		- ### with [[mise/set]]
			- ```
			  mise set
			  # key       value        source
			  # NODE_ENV  development  mise.toml
			  ```
			- [[My Notes]]
				- *This is also a bit [[Astonishing]] to me; I would expect `mise list` or something similar*
	- ## What are the 4 ways that [[EnvVars]] declared in a [[mise/Config/mise.toml]] can be used/expressed in [[mise]]? [[card]]
	  card-last-score:: 1
	  card-repeats:: 1
	  card-next-schedule:: 2026-06-25T04:00:00.000Z
	  card-last-interval:: -1
	  card-ease-factor:: 2.5
	  card-last-reviewed:: 2026-06-24T06:14:56.958Z
		- ### 1 - in [[mise/exec]] with a shell command
			- ```sh
			  mise set MY_VAR=123
			  mise exec -- bash -c 'echo $MY_VAR'
			  # 123
			  ```
		- ### 2 - when invoking a [[mise/Tool]]
			- #### 2.1 via [[mise/exec]]
				- [[My Notes]] AFAIK it's not possible to make a tool-specific [[EnvVar]] unless one wraps it in a [[mise/Task]], (unfortunately, IMO)
				- ```sh
				  mise use node@26
				  mise set MY_VAR=123
				  cat mise.toml
				  # [tools]
				  # node = '24'
				  # [env]
				  # MY_VAR = '123'
				  mise exec -- node --eval 'console.log(process.env.MY_VAR)'
				  # 123
				  ```
			- #### 2.2 - in the shell, after [[mise/activate]]
				- As long as your [[zsh/.zshrc]], [[Bash/.bashrc]] etc has `eval "$(mise activate zsh)"` in it, any declared environment variables will be available
				- ```sh
				  $> cd /path/to/project
				  $> mise set NODE_ENV=production
				  $> cat mise.toml
				  # [env]
				  # NODE_ENV = 'production'
				  
				  $> echo $NODE_ENV
				  # production
				  ```
			- #### 2.3 - when using a [[mise/Shim]]'d version of a [[mise/Tool]]
				- If, instead of using `mise activate` in one's zshrc shell, one is using mise shims, whereby tools are symlinks that are configured to point to the executable that's been configured to have the mise environment, then the declared mise environment will be available to that binary
				- ```sh
				  mise set NODE_ENV=production
				  mise use node@26
				  # using the absolute path for the example
				  ~/.local/share/mise/shims/node --eval 'console.log(process.env.NODE_ENV)'
				  ```
		- ### 3 - in [[mise/tasks]], including per-task env-vars
			- you can modify environment variables just for a particular mise task.
			- Here's an example of a [[mise/Task/TOML]] version of this, but it's also possible in [[mise/Task/File]]
				- ```toml
				  [tasks.print]
				  run = "echo $MY_VAR"
				  env = { _.file = '/path/to/file.env', "MY_VAR" = "my variable" }
				  ```
		- ### 4 - after calling [[mise/en]] to activate just mise's declared environment vars
			- The `mise en` command is perhaps comparable to activating a [[Py/Virtualenv]]; subsequent commands make use of certain set environment variables.
			- ```sh
			  mise set FOO=bar
			  mise en
			  echo $FOO
			  # bar
			  ```