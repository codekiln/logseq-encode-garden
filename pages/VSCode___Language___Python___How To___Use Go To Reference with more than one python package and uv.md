# How to use [[VSCode/Command/Go To/References]] in a project with more than one package that's using [[uv]]
	- ## Problem Context
		- [[Poetry]] has dedicated support for installing packages in editable mode with `develop = true` in [[Py/pyproject.toml]]; see also [[Poetry/Concept/Disadvantages of Pip vs Poetry]]
			- of course, [[uv]] doesn't support poetry's non-standard syntax
				- When using `uv` with a python project that has more than one `pyproject.toml` in [[VSCode/Python]], one must instrument calling `uv pip install -e path/to/package` for each package
	- ## Observed behavior
		- Sometimes [[VSCode/Extension/Pylance]] doesn't find or display all references in response to [[VSCode/Command/Go To/References]] when the references are in different package contexts