alias:: [[mise Environments]]

- # [Environments | mise-en-place](https://mise.jdx.dev/environments/)
	- ## What are two ways to set [[EnvVars]] with [[mise]]? [[card]]
	  card-last-interval:: 5.4
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-05-20T20:03:53.140Z
	  card-last-reviewed:: 2026-05-15T11:03:53.140Z
	  card-last-score:: 5
		- ### 1 - In [[mise/Config/mise.toml/env]]
			- ```toml
			  [env]
			  NODE_ENV = 'production'
			  ```
		- ### 2 - with [[mise/set]]
			- `mise set NODE_ENV=development`
	- ## What are two ways to _unset_ [[EnvVars]] with [[mise]]? [[card]]
	  card-last-interval:: 5.4
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2026-05-20T20:05:17.785Z
	  card-last-reviewed:: 2026-05-15T11:05:17.786Z
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
	- ## What are the 6 places that [[EnvVars]] can be used in [[mise]]? [[card]]
		- ### 1 - [[mise/exec]]
			- ```sh
			  mise set MY_VAR=123
			  mise exec -- bash -c 'echo $MY_VAR'
			  # 123
			  ```
		- ### 2 - in [[mise/Tool]] (invoked via mise exec, after mise activate, or via mise shims)
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
		- ### 3 - [[mise/activate]]
			- As long as your [[zsh/.zshrc]], [[Bash/.bashrc]] etc has `eval "$(mise activate zsh)"` in it, any declared environment variables will be available
			- ```sh
			  cd /path/to/project
			  mise set NODE_ENV=production
			  cat mise.toml
			  # [env]
			  # NODE_ENV = 'production'
			  
			  echo $NODE_ENV
			  # production
			  ```
		- ### 4 - [[mise/Shim]]
			- If, instead of using `mise activate` in one's zshrc shell, one is using mise shims, whereby tools are symlinks that are configured to point to the executable that's been configured to have the mise environment, then the declared mise environment will be available to that binary
			- ```sh
			  mise set NODE_ENV=production
			  mise use node@26
			  # using the absolute path for the example
			  ~/.local/share/mise/shims/node --eval 'console.log(process.env.NODE_ENV)'
			  ```
		- ### 5 - [[mise/en]]
			- The `mise en` command is perhaps comparable to activating a [[Py/Virtualenv]]; subsequent commands make use of certain set environment variables.
			- ```sh
			  mise set FOO=bar
			  mise en
			  echo $FOO
			  # bar
			  ```
		- ### 6 - [[mise/Tasks]]
			- you can modify environment variables just for a particular mise task
			- ```toml
			  [tasks.print]
			  run = "echo $MY_VAR"
			  env = { _.file = '/path/to/file.env', "MY_VAR" = "my variable" }
			  ```