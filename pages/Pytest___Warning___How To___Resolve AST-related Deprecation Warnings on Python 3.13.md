tags:: [[Diataxis/How To]]

- # Pytest AST-related Deprecation Warnings on [[Python 3.13]] [[Pytest/v/7/3]] and under
	- ## TL;DR
		- Running **pytest < 7.4** under **Python 3.13 (or 3.12)** triggers a flood of warnings like
		- ~~~
		  DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead
		  ~~~
		- because pytest's assertion-rewriter still used the legacy `ast.Str`/`ast.NameConstant` nodes.
		- Upgrade to **pytest ≥ 7.4.0** (or any 8.x release) to eliminate the warnings; those versions switch to the new `ast.Constant` API. ([Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b))
	- ## What you see
		- Example warning (truncated): `_pytest/assertion/rewrite.py:958: DeprecationWarning: ast.Str is deprecated…`
		- Where it comes from: pytest's assertion-rewriting pass instruments every `assert` in your code to produce richer failure messages.
		- If your project promotes warnings to errors (`-W error`, `python -X dev`, or `pytest --strict-config`) the test session may even fail.
	- ## Why it happens
		- Python 3.8 unified several constant node classes (`ast.Str`, `ast.Num`, `ast.NameConstant`, etc.) into a single `ast.Constant`. The old node types stayed around but became officially **deprecated**, and Python 3.13 now emits a `DeprecationWarning` each time they are referenced.
		- pytest versions prior to 7.4 rewrote `assert` statements by *constructing* those legacy nodes, so merely importing pytest on Python 3.13 raises the warnings.
	- ## How to fix it (root-cause, not suppression)
		- ### 1  Upgrade pytest
			- ~~~
			  # Poetry
			  poetry add --group dev "pytest>=7.4"
			  
			  # pip
			  python -m pip install -U "pytest>=7.4"
			  ~~~
			- *7.4.0* includes commit **9335a0b** ("Avoid ast deprecation warnings on Python 3.12").
			- This commit aliases the old names to `ast.Constant` at runtime, eliminating the warnings. ([Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b))
			- **Side-benefit:** Newer pytest releases bring many bug-fixes and features; upgrading is the canonical solution.
		- ### 2  Pinned-Python fallback (not recommended long-term)
			- Use Python ≤ 3.11 in the project's virtualenv until you're ready to update pytest.
			- This merely postpones the issue.
		- ### 3  Temporary warning filter (stop-gap only)
			- Add to *pyproject.toml* or *pytest.ini*:
			- ~~~
			  [tool.pytest.ini_options]
			  filterwarnings = [
			  "ignore::DeprecationWarning:_pytest.assertion.rewrite",
			  ]
			  ~~~
			- …but remember this **hides** the warning; it does not future-proof your code for Python 3.14, where the old nodes will disappear entirely.
	- ## References
		- [Python docs – Deprecated AST node types](https://docs.python.org/3.13/library/ast.html#ast.Str) (Pending removal in 3.14 section for `ast.Str`/`ast.NameConstant`)
		- [Assertion rewriting triggers DeprecationWarning](https://github.com/pytest-dev/pytest/issues/10977) (pytest issue #10977)
		- pytest commit **9335a0b** (part of 7.4.0) – fixes the problem. ([Avoid ast deprecation warnings on Python 3.12](https://github.com/pytest-dev/pytest/commit/9335a0b))