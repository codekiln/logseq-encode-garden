tags:: [[Diataxis/How To]]

- # How to configure a project [[mise/Config/mise.toml]] with the ability to manage a python virtualenv with [[uv]]
	- ## Goal
		- Use a project-local `mise.toml` to pin and install Python (via `uv`) and automatically create/activate a virtualenv, while keeping Python dependencies in `pyproject.toml`.
	- ## Preconditions
		- You have `mise` ≥ 2025.5.6 installed globally.
		- A Git repository with a `pyproject.toml` defining your Python project’s metadata and dependencies.
		- You want all Mise configuration in `mise.toml`, not in `pyproject.toml`.
	- ## Procedure
		- ### 1. Create and commit `mise.toml`
			- At your project root, add a file named `mise.toml`:
			  ~~~toml
			  # pin tool versions
			  [tools]
			  python = "3.13"
			  uv     = "latest"
			  ~~~
			- Use `mise.local.toml` for machine-specific overrides and add it to `.gitignore`.
		- ### 2. Install and pin tools
			- In your shell, run `mise install`.
		- ### 3. Define a task to install Python dependencies
			- Still in `mise.toml`, add under `[tasks]`:
			  ~~~toml
			  [tasks]
			  install = "uv install && pip install --upgrade pip && pip install ."
			  ~~~
			- Now `mise run install` will create or activate the venv and install your package along with its dependencies.
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
		  4. Run `mise run install` to create and populate the venv.
		- ### 7. Register the venv with VS Code
			- Open VS Code Command Palette (`⇧⌘P` / `Ctrl+Shift+P`) and run **Python: Select Interpreter**.
			- Choose the interpreter at `./.venv/bin/python`.
			- (Optional) Add a workspace setting in `.vscode/settings.json`:
			  ~~~json
			  {
			    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
			  }
			  ~~~
			- VS Code will now use the project’s venv for linting, debugging, and IntelliSense.
	- ## Troubleshooting
		- **Mise didn’t pick up `mise.toml`**  
		  Run `mise config ls` to confirm which config files are active.
		- **Python version mismatch**  
		  Ensure you ran `mise use --project python@3.13`; check with `python --version`.
		- **VS Code can’t find the interpreter**  
		  Make sure you pointed to the correct `.venv/bin/python` path and reload the window.
	- ## References
		- Walkthrough: [Configure a project-local mise.toml](https://mise.jdx.dev/walkthrough.html)
		- Python tool guide: [Automatic virtualenv activation](https://mise.jdx.dev/lang/python.html#automatic-virtualenv-activation)
		- Mise + Python Cookbook: [Using mise with uv](https://mise.jdx.dev/mise-cookbook/python.html#mise--uv)