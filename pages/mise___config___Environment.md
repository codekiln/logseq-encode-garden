alias:: [[mise Config Environments]]

- # [mise Config Environments](https://mise.jdx.dev/configuration/environments.html)
	- ## [[My Notes]]
		- it's possible to separate the behavior of mise between [[Env/dev]] and [[Env/prod]] using [[mise/Config/mise.toml/local]] `mise.*.local.toml` files.
	- ## Details of [[mise/Config/mise.toml/local]] -  [[mise/Docs/Configuration/Environments]]
		- To enable, either set the `-E,--env` option or [[mise/EnvVar/MISE_ENV]] environment variable to an environment like `development` or `production`. mise will then look for a `mise.{MISE_ENV}.toml` file in the current directory, parent directories and the `MISE_CONFIG_DIR` directory.
			- > mise will also look for "local" files like `mise.local.toml` and `mise.{MISE_ENV}.local.toml` in the current directory and parent directories. These are intended to not be committed to version control. (Add `mise.local.toml` and `mise.*.local.toml` to your `.gitignore` file.)
		- the precedence of these files (higher first):
			- `mise.{MISE_ENV}.local.toml`
			- `mise.local.toml`
			- `mise.{MISE_ENV}.toml`
			- `mise.toml`
		- > If  [[mise/EnvVar/MISE_OVERRIDE_CONFIG_FILENAMES]]  is set, that will be used instead of all of this.
		- You can also use paths like `mise/config.{MISE_ENV}.toml` or `.config/mise.{MISE_ENV}.toml` Those rules follow the order in [Configuration](https://mise.jdx.dev/configuration.html).
		- Use  [[mise/config]] (`mise config`) to see which files are being used.
		- **Multiple environments can be specified**, e.g. [[mise/EnvVar/MISE_ENV]]=ci,test with the last one taking precedence.
	- ## Details from [[mise/Docs/About/Tips and Tricks]]
		- [[mise/set]]
			- Instead of manually editing `mise.toml` to add env vars, you can use [`mise set`](https://mise.jdx.dev/cli/set.html) instead:
			- ```sh
			  mise set NODE_ENV=production
			  ```
		-