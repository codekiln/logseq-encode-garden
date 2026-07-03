tags:: [[Diataxis/Explanation]]

- # How to handle Monorepos in Poetry vs uv
	- ## Overview
		- Managing **multiple inter-dependent Python packages in one repository** requires local editable installs for day-to-day work while still publishing clean wheels. Poetry and uv take different approaches but reach the same goal.
	- ## Context
		- *Poetry* popularised `pyproject.toml`-only workflows and gave first-class support for editable path deps.
		- *uv* (from Astral) replaces both *pip* and *virtualenv*, favouring a **single lock file** and a lightweight override table instead of editable paths in the core dependency list.
	- ## Key Principles
		- **Declarative dependency list** — every package declares real, version-bounded requirements (no local paths) so published wheels stay portable.
		- **Local override for dev** — a monorepo needs a way to tell the installer “use the sibling folder, editable” without leaking that info to PyPI.
		- **Single source of truth** — one lock file (uv) or one resolver invocation per project (Poetry) keeps CI deterministic.
	- ## Mechanism
		- ### Poetry
			- `pyproject.toml`
				- ~~~toml
				  [project]
				  name = "my-app"
				  dependencies = ["my-shared-lib>=0.1,<1"]
				  
				  [tool.poetry.dependencies]
				  my-shared-lib = { path = "../shared-lib", develop = true }
				  ~~~
			- `poetry install` reads the **path+develop** entry, installs editable, and records versions in *poetry.lock*.
		- ### uv
			- `pyproject.toml`
				- ~~~toml
				  [project]
				  name = "my-app"
				  dependencies = ["my-shared-lib>=0.1,<1"]
				  
				  [tool.uv.sources]
				  my-shared-lib = { path = "../shared-lib", editable = true }
				  ~~~
			- `uv lock --all-projects` writes one **uv.lock** at repo root.
			- `uv sync` respects the override; **`uv build --no-sources`** disables it so the wheel only lists `my-shared-lib>=0.1,<1`.
		- ### Workspace shorthand (uv ≥ 0.8)
			- ~~~toml
			  [tool.uv.sources]
			  my-shared-lib = { workspace = true }
			  ~~~
			- `workspace = true` tells uv to locate a sibling project with the same name automatically.
	- ## Examples
		- **Directory tree**
			- ~~~text
			  monorepo/
			  ├─ uv.lock
			  ├─ libs/
			  │  ├─ shared-lib/
			  │  │  └─ pyproject.toml
			  │  └─ my-app/
			  │     └─ pyproject.toml
			  └─ tests/
			  ~~~
		- **CI snippet**
			- ~~~bash
			  export UV_FROZEN=true   # fail if lock drifts
			  uv sync                 # install all packages editable
			  pytest -q
			  ~~~
	- ## Misconceptions
		- **“uv can’t do editable installs.”**  
		  It can — just not in the `[project.dependencies]` table; use `[tool.uv.sources]`.
		- **“Poetry can’t share one lock.”**  
		  True, each project has its own *poetry.lock*. uv’s unified lock is a design choice, not a limitation lift.
		- **“Overrides leak into published wheels.”**  
		  Both tools strip local paths automatically (`poetry build`, `uv build --no-sources`).
	- ## Related
		- [uv documentation – Path & workspace sources](https://docs.astral.sh/uv/#sources)
		- [Poetry documentation – Path dependencies](https://python-poetry.org/docs/dependency-specification/#path-dependencies)
		- [LangChain monorepo structure](https://github.com/langchain-ai/langchain/tree/master/libs)