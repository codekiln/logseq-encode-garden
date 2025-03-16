# Disadvantages of [[uv]] with [[pip]] as compared to using [[Poetry]]
	- ## There's no easy way to use [[Py/pyproject.toml]] to do [[Py/Editable Install]]s with `uv pip` as there is with [[Poetry]]
	  id:: 67d6a7e5-3d9a-4b8e-97b1-975254980c95
		- In poetry, it's possible to have a python [[Monorepo]] with poetry by specifying editable installs. With `uv pip`, the recommended approach would be to specify `requirements-dev.txt` with `-e path/to/package` alongside `pyproject.toml`, which seems like a strange mixture of old and new package management techniques.
		- | Feature | Poetry (`poetry install`) | `pip` / `uv pip install` |
		  | ---- | ---- | ---- | ---- | ---- |
		  | Editable installs in `pyproject.toml` | ✅ `{path = "path/to/package", develop = true}` | ❌ Not supported |
		  | `-e` flag in `requirements.txt` | ❌ Not needed | ✅ `-e path/to/package` works |
		  | Installing local editable packages automatically | ✅ Done via `pyproject.toml` | ❌ Must be installed manually |
-