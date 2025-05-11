alias:: [[mise/Docs/Dev Tools Overview]]

- # [Dev Tools | mise-en-place](https://mise.jdx.dev/dev-tools/)
	- ## [How it works](https://mise.jdx.dev/dev-tools/#how-it-works)
	  id:: 682090e2-b6c2-47ae-a404-d806aab03b3d
		- mise hooks into your shell (with `mise activate zsh`) and sets the `PATH` environment variable to point your shell to the correct runtime binaries. When you `cd` into a directory containing a `mise.toml`/`.tool-versions` file, mise will automatically set the appropriate tool versions in `PATH`.