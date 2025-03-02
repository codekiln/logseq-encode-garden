tags:: [[uv]], [[Py/pyproject.toml]], [[Package/Management]], [[Diataxis/How To]], [[CursorAI/Project Rule/diataxis-how-to.mdc/Created By]]

- # How To Add a Package to pyproject.toml with uv
	- ## Overview
		- This guide walks you through adding a package dependency to your Python project's pyproject.toml file using the uv tool.
		- It's for Python developers who are working on projects managed with uv and need to add new dependencies.
	- ## Prerequisites
		- [uv installed](https://github.com/astral-sh/uv) on your system
		- An existing Python project with a pyproject.toml file
		- Project directory structure initialized with `uv init` or containing a valid pyproject.toml
	- ## Steps
		- ### 1. Navigate to Your Project Directory
			- Open a terminal or command prompt
			- Change to your project's root directory where the pyproject.toml file is located
			- Example: `cd path/to/your/project`
		- ### 2. Add a Package Using the uv Command
		  id:: 67c45284-ca87-43f8-919b-8c8ed7cbed73
			- Run the `uv add` command followed by the package name
			- Basic syntax: `uv add <package-name>`
			- Example: `uv add ruff`
			- This will:
				- Create a virtual environment at .venv if one doesn't exist
				- Add the package to your project's dependencies in pyproject.toml
				- Install the package in your project's virtual environment
				- Update the uv.lock file with the exact resolved versions
		- ### 3. Specify a Version Constraint (Optional)
			- To add a specific version or version range, use the following syntax:
			- `uv add <package-name>@<version-constraint>`
			- Examples:
				- Exact version: `uv add ruff@0.5.4`
				- Version range: `uv add ruff@">=0.5.0,<0.6.0"`
				- Minimum version: `uv add ruff@">=0.5.0"`
		- ### 4. Add Multiple Packages (Optional)
			- You can add multiple packages in a single command by listing them
			- Example: `uv add ruff pytest black`
		- ### 5. Add Development Dependencies (Optional)
			- To add a package as a development dependency, use the `--dev` flag
			- Example: `uv add --dev pytest`
			- This adds the package to the `project.optional-dependencies.dev` section in pyproject.toml
		- ### 6. Verify the Package Was Added
			- Check your pyproject.toml file to confirm the dependency was added
			- The package should appear in the `dependencies` list under the `[project]` section
			- Example of updated pyproject.toml:
			  ```toml
			  [project]
			  name = "your-project"
			  version = "0.1.0"
			  description = "Your project description"
			  dependencies = [
			     "ruff>=0.5.0",
			  ]
			  ```
	- ## Using uv with #mise
		- ### Overview
			- [mise](https://mise.jdx.dev/) is a dev tool manager that can manage Python versions and tools like uv
			- Using mise with uv provides a seamless way to manage both Python versions and packages
		- ### Setting Up mise with uv
			- #### 1. Install mise
				- Install mise using the official installer: `curl https://mise.run | sh`
				- Activate mise in your shell: `eval "$(~/.local/bin/mise activate bash)"` (adjust for your shell)
			- #### 2. Configure Python with mise
				- Create a `.mise.toml` file in your project root:
				  ```toml
				  [tools]
				  python = "3.11"  # Or your preferred version
				  ```
				- Or use the command line: `mise use python@3.11`
			- #### 3. Install uv with mise
				- Add uv to your mise configuration:
				  ```toml
				  [tools]
				  python = "3.11"
				  
				  [tasks.install-uv]
				  description = "Install uv package manager"
				  run = "pip install uv"
				  ```
				- Run the task: `mise run install-uv`
			- #### 4. Create a Task for Adding Packages
				- Add a task to your `.mise.toml` for adding packages:
				  ```toml
				  [tasks.add-pkg]
				  description = "Add a package to pyproject.toml"
				  run = "uv add $@"
				  ```
				- Use it with: `mise run add-pkg ruff`
				- #### [[My Notes]] on this technique
					- *Why would one want to do this? Perhaps because #mise affords one the opportunity to set a common schema of tasks and reuse them across package managers. If one created similarly named tasks in each language that mise manages, then this `add-pkg` could be that interface.*
		- ### Benefits of Using mise with uv
			- Consistent Python versions across team members
			- Project-specific Python version management
			- Simplified workflow with mise tasks for common uv commands
			- Easier onboarding for new team members
		- ### Local Configuration
			- For personal preferences, use `.mise.local.toml` (add to .gitignore)
			- Example for personal uv configuration:
			  ```toml
			  [env]
			  UV_CACHE_DIR = "~/.cache/uv-custom"
			  
			  [tasks.my-add-pkg]
			  description = "Add a package with my preferred settings"
			  run = "uv add --dev $@"
			  ```
	- ## Troubleshooting
		- If you see `Error: No pyproject.toml found`: Make sure you're in the correct directory or initialize a project with `uv init`
		- If you see `Error: Package not found`: Check the package name for typos or verify it exists on PyPI
		- If installation fails with version conflicts: Try using a different version constraint or check compatibility with your other dependencies
		- If the virtual environment isn't created: Run `uv venv` to manually create it
		- If using mise and commands aren't found: Ensure mise is activated with `eval "$(mise activate)"`
		- If mise tasks aren't working: Check your `.mise.toml` syntax and try running with `MISE_DEBUG=1`
	- ## Related
		- [[uv/How To/Initialize a Project]]
		- [[uv/How To/Remove a Package]]
		- [[uv/How To/Update Dependencies]]
		- [[uv/Reference/pyproject.toml]]
		- [[mise/How To/Manage Python Projects]]