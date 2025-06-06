tags:: [[Diataxis/Explanation]]
alias:: [[mise/Shim/Explanation]]

- # What Is a **Shim** in [[mise]]?
	- ## Overview
		- A *shim* is a tiny executable that masquerades as the tool you want to run (e.g. `node`, `prettier`). Each shim is a **symlink to the `mise` binary** that intercepts your shell call, figures out which version of the tool should run, loads mise's environment, and then delegates execution. See [Shims in the mise docs](https://mise.jdx.dev/dev-tools/shims.html).
	- ## Context
		- `mise activate` rewrites `PATH` on every prompt; this is great for interactive shells but unavailable to non-interactive environments like CI, IDEs, or scripts. Shims offer a **static directory of stand-ins** that works even when the shell cannot evaluate `mise activate`. See [Shims vs PATH activation](https://mise.jdx.dev/dev-tools/shims.html#shims-vs-path).
		- By default, shims live in `~/.local/share/mise/shims`. Adding this directory to `PATH` (or using `mise activate --shims`) makes every installed tool appear globally available. See [mise activate --shims](https://mise.jdx.dev/cli/activate.html#shims).
	- ## Key Principles
		- **One shim per binary** – every `bin` file provided by a tool gets its own shim at install time.
		- **Environment on demand** – env-vars from `mise.toml` load *only when a shim runs*; they are not present for unrelated commands. See [Shims: Environment](https://mise.jdx.dev/dev-tools/shims.html).
		- **Reshim after changes** – installing via managers that mise cannot detect (e.g. `yarn`, `pnpm`) may require a manual `mise reshim` to regenerate the shim set. See [`mise reshim` command](https://mise.jdx.dev/cli/#mise-reshim).
	- ## Mechanism
		- **Creation** – `mise install` (or any tool install) drops binaries, then writes matching shims; `mise reshim` can recreate them later. See [Shims: Creation](https://mise.jdx.dev/dev-tools/shims.html).
		- **Resolution flow**
			- 1. You run `node`.
			- 2. Shell finds `~/.local/share/mise/shims/node`.
			- 3. Shim runs `mise`, which selects the correct `node` version for the current directory and executes it.
			- 4. Subsequent child processes inherit the full PATH so they *don't* trigger mise again.
		- **Symlink anatomy**
			- ~~~sh
			  ls -l ~/.local/share/mise/shims/node
			  # ~/.local/share/mise/shims/node -> ~/.local/bin/mise
			~~~
	- ## Examples
		- **Listing versions via a shim path**
			- ~~~sh
			  ~/.local/share/mise/shims/node -v   # v20.0.0
			  ~/.local/share/mise/shims/prettier -v  # 3.1.0
			~~~
		- **Force-update shims after a global `npm i -g`**
			- ~~~sh
			  mise reshim           # recreates all shims
			~~~
			- See [`mise reshim` documentation](https://mise.jdx.dev/cli/#mise-reshim).
	- ## Misconceptions
		- **"Shims give me every mise feature."** Not quite: hooks, some env-vars, and `which` accuracy are limited under shims. See [Shims: Limitations](https://mise.jdx.dev/dev-tools/shims.html#shims-vs-path).
		- **"`which node` shows the real binary."** It shows the shim; use `mise which node` to see the resolved path. See [FAQ: which node](https://mise.jdx.dev/faq.html#mise-isnt-working-when-calling-from-tmux-or-another-shell-initialization-script).
		- **"Shims always outperform `mise activate`."** Both pay a small cost—`activate` on each prompt, shim on each invocation; impact depends on workflow. See [Shims: Performance](https://mise.jdx.dev/dev-tools/shims.html#performance).
	- ## Related
		- [Shims vs PATH activation](https://mise.jdx.dev/dev-tools/shims.html#shims-vs-path) – trade-offs and limitations
		- [`mise reshim` command](https://mise.jdx.dev/cli/#mise-reshim) – manual shim regeneration
		- [`mise activate --shims`](https://mise.jdx.dev/cli/activate.html#shims) – add shim dir to `PATH` automatically