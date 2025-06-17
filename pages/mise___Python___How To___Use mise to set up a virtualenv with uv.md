tags:: [[Diataxis/How To]]

- # How to configure a project [[mise/Config/mise.toml]] with the ability to manage a python virtualenv with [[uv]]
	- ## Goal
		- Use a project-local `mise.toml` to pin and install Python (via `uv`) and automatically create/activate a virtualenv, while keeping Python dependencies in `pyproject.toml`.
	- ## Preconditions
		- You have `mise` ≥ 2025.5.6 installed globally.
		- A Git repository with a [[pyproject.toml]] defining your Python project's metadata and dependencies.
		- You want all Mise configuration in `mise.toml`, not in `pyproject.toml`.
	- ## Procedure
		- ### 1. Create and commit `mise.toml`
			- At your project root, add a file named `mise.toml`:
			  ~~~toml
			  [env]
			  # Use the project name derived from the current directory
			  PROJECT_NAME = "{{ config_root | basename }}"
			  
			  # Automatic virtualenv activation
			  _.python.venv = { path = ".venv", create = true }
			  
			  [tools]
			  # Python version (via pyenv, as a fallback to .python-version)
			  python = "{{ get_env(name='PYTHON_VERSION', default='3.13') }}"
			  uv = "latest"
			  ruff = "latest"
			  
			  [tasks.install-deps]
			  description = "Install all basic dependencies"
			  alias = "id"
			  run = "uv sync --all-extras"
			  
			  [tasks.install-deps-dev]
			  description = "Install only dev dependencies"
			  alias = "idd"
			  run = "uv sync --extras dev"
			  
			  [tasks.install-deps-all]
			  description = "Install all dependencies (including dev dependencies)"
			  alias = "ida"
			  run = "uv sync --all-extras"
			  
			  [tasks.add-deps]
			  description = "Add new dependencies using uv"
			  alias = "ad"
			  run = "uv pip install $@"
			  
			  [tasks.test]
			  description = "Run tests"
			  run = "pytest tests/"
			  
			  [tasks.lint]
			  description = "Lint the code"
			  run = "ruff check ."
			  
			  [tasks.format]
			  description = "Format the code"
			  run = "ruff format ."
			  
			  [tasks.info]
			  description = "Print project information"
			  run = '''
			  echo "Project: $PROJECT_NAME"
			  echo "Virtual Environment: $VIRTUAL_ENV"
			  '''
			  ~~~
			- Use `mise.local.toml` for machine-specific overrides and add it to `.gitignore`.
		- ### 2. Install and pin tools
			- In your shell, run `mise install`.
		- ### 3. Define tasks for Python dependency management
			- The `mise.toml` above defines several useful tasks:
				- `mise run install-deps` (or `mise run id`): Install all basic dependencies
				- `mise run install-deps-dev` (or `mise run idd`): Install only dev dependencies
				- `mise run install-deps-all` (or `mise run ida`): Install all dependencies
				- `mise run add-deps <package>` (or `mise run ad <package>`): Add new dependencies
				- `mise run test`: Run tests
				- `mise run lint`: Lint the code
				- `mise run format`: Format the code
				- `mise run info`: Show project information
		- ### 4. Keep Python dependencies in `pyproject.toml`
			- In `pyproject.toml`, list your dependencies under `[project]`:
			  ~~~toml
			  [project]
			  dependencies = [
			    "requests>=2.30",
			    "numpy>=1.25"
			  ]
			  ~~~
			- Do not add Mise commands here—Mise reads only `mise.toml`.
		- ### 5. Ignore artifacts
			- Add to `.gitignore`:
			  ~~~gitignore
			  .mise/
			  .venv/
			  mise.local.toml
			  ~~~
		- ### 6. First-time setup for contributors
		  1. `git clone <repo> && cd <repo>`
		  2. Ensure `mise activate zsh` (or your shell) is in your shell RC.
		  3. Run `mise install` to install pinned tools.
		  4. Run `mise run install-deps` to create and populate the venv with basic dependencies.
		  5. (Optional) Run `mise run install-deps-dev` if you need development dependencies.
		- ### 7. Register the venv with VS Code
			- Open VS Code Command Palette (`⇧⌘P` / `Ctrl+Shift+P`) and run **Python: Select Interpreter**.
			- Choose the interpreter at `./.venv/bin/python`.
			- (Optional) Add a workspace setting in `.vscode/settings.json`:
			  ~~~json
			  {
			    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
			  }
			  ~~~
			- VS Code will now use the project's venv for linting, debugging, and IntelliSense.
	- ## Troubleshooting
		- **Mise didn't pick up `mise.toml`**  
		  Run `mise config ls` to confirm which config files are active.
		- **Python version mismatch**  
		  Ensure you ran `mise use --project python@3.13`; check with `python --version`.
		- **VS Code can't find the interpreter**  
		  Make sure you pointed to the correct `.venv/bin/python` path and reload the window.
	- ## References
		- Walkthrough: [Configure a project-local mise.toml](https://mise.jdx.dev/walkthrough.html)
		- Python tool guide: [Automatic virtualenv activation](https://mise.jdx.dev/lang/python.html#automatic-virtualenv-activation)
		- Mise + Python Cookbook: [Using mise with uv](https://mise.jdx.dev/mise-cookbook/python.html#mise--uv)