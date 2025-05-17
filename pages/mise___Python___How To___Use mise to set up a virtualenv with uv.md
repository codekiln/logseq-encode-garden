tags:: [[Diataxis/How To]]

- # How to configure a project [[mise/Config/mise.toml]] with the ability to manage a python virtualenv with [[uv]]
	- ## Goal
		- Enable any contributor to `cd` into the project and have a ready-to-use Python virtual environment created and activated automatically via **uv**, with the Python version pinned in `mise.toml`.
	- ## Preconditions
		- `mise` ≥ 2024.9.5 installed and activated in your shell (`eval "$(mise activate zsh)"`).
		- `uv` installed through mise (`mise use -g uv@latest`).
		- Desired Python version (e.g. `mise use -g python@3.12`) available.
	- ## Procedure
		- ### 1. Scaffold the config
			- Create or edit `mise.toml` at the project root:
			~~~toml
			min_version = "2024.9.5"

			[tools]              # pin tool versions
			python = "3.12"
			uv     = "latest"
			~~~
		- ### 2. Turn on automatic virtualenv creation
			- Add an **env** table that instructs mise to manage a `.venv` folder with uv and to seed it with `pip`:
			~~~toml
			[env]
			_.python.venv = { path = ".venv", create = true, uv_create_args = ["--seed"] }
			~~~
			- `create = true` lets mise build the venv the first time you enter the directory ([Automatic virtualenv activation](https://mise.jdx.dev/lang/python.html#automatic-virtualenv-activation)).  
			- `uv_create_args = ["--seed"]` installs *pip*, *setuptools* and *wheel*, because uv venvs omit them by default ([mise & uv](https://mise.jdx.dev/lang/python.html#mise--uv)).
		- ### 3. (Optional) Re-use uv-managed venvs
			- If the project was initialised with `uv init .` and you want mise to honour the existing venv, enable:
			~~~toml
			[settings]
			python.uv_venv_auto = true
			~~~
			- See the [uv cookbook section](https://mise.jdx.dev/mise-cookbook/python.html#mise--uv) for details.
		- ### 4. Add an install task
			- Provide a convenience task for installing dependencies:
			~~~toml
			[tasks.install]
			description = "Install Python deps with uv"
			run = "uv pip install -r requirements.txt"
			~~~
			- Run it with `mise run install` (alias `mise i` if configured).
		- ### 5. Verify the setup
			- Open a **new** shell, `cd` into the project and check:
				- `which python` → `./.venv/bin/python`
				- `python -V` shows the pinned version.
				- `echo $VIRTUAL_ENV` prints the `.venv` path.
	- ## Troubleshooting
		- **uv not found** – ensure `mise use -g uv@latest` and `mise install` were run.
		- **Global python being used** – delete any failed `.venv` and re-run `mise install`, confirming `create = true` is present.
		- **pip missing** – include `--seed` in `uv_create_args`, or install via `uv pip install pip setuptools wheel`.
		- **Conflicts with pyenv** – disable `.python-version` handling or remove pyenv from your shell (see [Configuration → settings](https://mise.jdx.dev/configuration.html#settings)).
	- ## References
		- [Python tool guide](https://mise.jdx.dev/lang/python.html)
		- [Configuration file reference](https://mise.jdx.dev/configuration.html)
		- [Mise + Python Cookbook](https://mise.jdx.dev/mise-cookbook/python.html)
