tags:: [[CLI/Tool]], [[Diataxis/How To]]

- # How To Use Mise with Poetry
	- ## Goal
		- Set up a project where **Mise** pins the Python version *and* installs **Poetry**, while Poetry handles dependency locking and its own virtual-environment — all reproducibly and with one-command tasks.
	- ## Preconditions
		- **Mise is installed** (e.g., `curl https://mise.run | sh`) and activated in your shell:  
		  `echo 'eval "$(mise activate zsh)"' >> ~/.zshrc` then restart the shell.
		- The project root is writable and contains (or will contain) a `pyproject.toml` managed by Poetry.
	- ## Procedure
		- ### 1. Pin Python
			- Run `mise use python@3.12` (substitute your required version). This both **installs** the interpreter and writes it to `mise.toml` so every teammate gets the same Python.
		- ### 2. Install the latest Poetry via Mise
			- Execute `mise use poetry@latest`. Mise pulls the Poetry plugin automatically from the registry and records it in `mise.toml`.
		- ### 3. Tell Mise to create & re-use `.venv`
			- Add this snippet to `mise.toml` so the environment appears automatically: 
			  ~~~toml
			  [env]
			  _.python.venv = { path = ".venv", create = true }
			  ~~~
		- ### 4. Scaffold (or adopt) the Poetry project
			- New project? `poetry new my_project` inside the Mise shell to generate the standard layout and `pyproject.toml`.
		- ### 5. Encode common commands as Mise tasks
			- Append a `[tasks]` section so teammates can type `mise run setup` instead of remembering Poetry flags: 
			  ~~~toml
			  [tasks]
			  setup   = "poetry install"         # lock & install deps into .venv
			  poetry  = { run = "poetry {{@}}", desc = "Pass-through to Poetry" }
			  test    = { run = "poetry run pytest", sources = ["src/**/*", "tests/**/*"] }
			  ~~~
			- List tasks with `mise tasks`; run with `mise run <task>`.
		- ### 6. First-time install
			- Run `mise install` (downloads all declared tools), then `mise run setup`. Poetry now builds or updates `poetry.lock` inside the isolated `.venv`.
		- ### 7. Daily usage
			- Simply `cd` into the project; Mise injects the pinned Python & `.venv/bin` at every prompt, so `python`, `poetry`, and `pytest` “just work.”
	- ## Troubleshooting
		- **“poetry: command not found”** → ensure `poetry = "latest"` appears under `[tools]` and rerun `mise use poetry@latest`.
		- **Wrong interpreter active** → check with `mise ls python`; correct via `mise use python@<ver>`.
		- **Stale tool cache** → `mise cache clear` then `mise install` to refresh.
	- ## References
		- Mise *Getting Started* & *Install* guides
		- Mise registry (Poetry plugin)
		- Mise Python docs (virtualenv directive)
		- Poetry docs: *Introduction*, *Managing environments*, *Basic usage*
		- Mise tasks overview
		- Internal Mise notes & examples