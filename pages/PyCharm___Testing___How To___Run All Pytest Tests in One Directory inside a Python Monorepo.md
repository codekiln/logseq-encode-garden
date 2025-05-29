tags:: [[PyCharm]], [[Diataxis/How To]]

- # How To Run All [[Pytest]] Tests in One Directory inside a [[Python]] [[Monorepo]] with [[PyCharm]]
	- ## Goal
		- Run and debug *only* the tests in a chosen sub-directory of a large monorepo, regardless of how many other packages (and their tests) exist.
	- ## Preconditions
		- PyCharm 2023.3 or newer (Community or Professional)
		- Monorepo already opened as the **project root** in PyCharm
		- A working Python [[Py/Virtualenv]] interpreter (virtualenv, Poetry, or Conda) set for the project
		- `pytest` installed in that interpreter
		- Directory structure like:
			- ```
			  monorepo/
			  ├─ apps/
			  │  └─ app_a/
			  │     └─ tests/      ← focus_dir
			  ├─ libs/
			  │  └─ lib_x/
			  │     └─ tests/
			  └─ pyproject.toml    (or setup.cfg / requirements.txt)
			  ```
	- ## Procedure
		- ### 1. Mark Source Roots with [[PyCharm/Tool/Project/Right Click/Mark Directory As/Sources Root]]
			- In the **Project** tool-window, right-click every top-level *package* (e.g. `apps/app_a`, `libs/lib_x`) → **Mark Directory As ▶ Sources Root**.
			- PyCharm then adds those folders to `PYTHONPATH` so imports inside tests resolve correctly.
		- ### 2. Tell PyCharm to Use *pytest* with [[PyCharm/Settings/Tools/Python Integrated Tools/Testing]] 
		  1. **Settings ▶ Tools ▶ Python Integrated Tools**  
		  2. *Testing* → Default test-runner **pytest**.  
		  3. Apply/OK.
		- ### 3. Create a [[PyCharm/Run Configuration]] for the Directory
		  1. Top-right toolbar → **Add Configuration…**  
		  2. **+** → **Python tests ▶ pytest**.  
		  3. Name: `tests-app_a`.  
		  4. **Target** → choose *Folder* and select `apps/app_a/tests`.  
		  5. **Working directory** → set to the **monorepo root** (crucial so relative imports & `pytest.ini` are found).  
		  6. *(Optional)* **Additional args**:
			- `-vv -s` for verbose output
			- `--maxfail=1` to stop after first failure  
			  7. Pick the same interpreter used by the project.  
			  8. Apply → Run 🟢.
		- ### 4. (Optional) Save as a Template
			- Back in **Run/Debug Configurations**, right-click the new entry → **Save Configuration as Template**.
			- Now you can duplicate it for other directories in seconds.
		- ### 5. Verify Discovery
			- After running once, the **Run** tool-window’s **Test Tree** should list only tests from `apps/app_a/tests`.
			- Green ▶ / Red ⨯ icons reflect pytest results; double-click any node to jump to code.
	- ## Troubleshooting
		- **ImportError: module not found**
			- Check that every package’s *root* is marked as **Sources Root** (step 1) and that your run config’s *Working directory* is the repo root.
		- **“No tests were found”**
			- Pytest’s discovery rules need files named `test_*.py` or `*_test.py`. Confirm naming; if you use a custom pattern, add `-k "pattern"` in **Additional args**.
		- **Tests from other packages still run**
			- Make sure the run config’s *Target* is **Folder**, not **Script path** or **Parametrized tests**.
			- Remove any `--rootdir` override in **Additional args** that might expand discovery.
		- **Multiple virtualenvs**
			- Each run config can point to a different interpreter. Pick the venv that has the dependencies for the target package.
	- ## References
		- [PyCharm Docs — Run pytest tests](https://www.jetbrains.com/help/pycharm/pytest.html)