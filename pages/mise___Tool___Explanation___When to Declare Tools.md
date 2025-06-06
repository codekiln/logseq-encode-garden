tags:: [[mise]], [[Diataxis/Explanation]]

- # When to Declare [[mise/Tool]]s
	- ## Overview
		- **`[tools]` pins a versioned binary and gives you a [[mise/Shim]]; tasks merely *use* whatever is already on `PATH`.**
		- [Mise can be used to install and run tools, launch tasks, and manage environment variables](https://mise.jdx.dev/getting-started.html#exec-and-run). Choosing where a command lives decides whether it is upgraded by `mise` or by the command's own update mechanism.
	- ## Context
		- New users often add every CLI to `[tools]`, then wonder why `npx prettier` or `pipx some-app` discovers a newer version than `prettier --version` run directly.
		- The clash is most visible with Node CLIs such as **Claude Code**: a shimmed `claude` froze at `0.2.115` while `npx @anthropic-ai/claude-code` updated to `1.0.11`.
	- ## Key Principles
		- **Pin runtimes & long-lived CLIs.** Anything you expect teammates or CI to call directly (`python`, `terraform`, `aws_okta_keyman`) belongs in `[tools]`. See [Dev Tools Overview](https://mise.jdx.dev/dev-tools/).
		- **On-demand wrappers stay in tasks.** Commands that bootstrap themselves each run (`npx`, `go run`, `cargo install --locked`) should be invoked inside the `run = "..."` line. See [Tasks Guide](https://mise.jdx.dev/tasks/).
		- **One source of truth.** A given binary should be provided *either* by a shim *or* by its own downloader—never both.
	- ## Mechanism
		- **Shims & activation.** When a tool lives in `[tools]`, `mise` installs it and places a shim earlier in `PATH`. Running `prettier` or `aws_okta_keyman` now hits that shim. See [How it works](https://mise.jdx.dev/dev-tools/#how-it-works).
		- **`exec` / `run`.** Tasks inherit the full "mise context" (all shims & env-vars) via [`mise run`](https://mise.jdx.dev/cli/run.html) or [`mise exec`](https://mise.jdx.dev/cli/exec.html).
		- Examples:
			- *Pinned CLI* – consistent, no auto-update:
				- ~~~toml
				  [tools]
				  "pipx:aws-okta-keyman" = "latest"   # shim = uvx aws_okta_keyman
				  [tasks.sts]
				  run = "uvx aws_okta_keyman"         # uses the shim
				  ~~~
			- *On-demand CLI* – always latest:
				- ~~~toml
				  [tasks.claude]
				  run = "npx @anthropic-ai/claude-code $@"
				  ~~~
			- The docs even show mixing backends:
				- ~~~sh
				  mise use -g cargo:ripgrep@14
				  mise use -g npm:prettier@3
				  ~~~
				  See [Getting Started: exec and run](https://mise.jdx.dev/getting-started.html#exec-and-run).
	- ## Examples
		- **Runtime**: `node = "lts"` → shimmed `node`; tasks can just say `node script.js`.
		- **Project tool**: `ruff = "latest"` ensures the same linter version everywhere.
		- **One-shot generator**: keep `cookiecutter` out of `[tools]` and call it via `npx` or `pipx run`.
	- ## Misconceptions
		- **"`npx` will respect my `[tools]` pin."** Not true; `npx` downloads a fresh copy into its own cache, bypassing shims. See [npx and mise](https://mise.jdx.dev/faq.html#how-does-mise-interact-with-npx).
		- **"`pipx:` entries auto-update on every run."** They install once; updates come from `mise up` or version bumps.
		- **"Tasks require the tool in `[tools]`.** Tasks can run any shell command; `[tools]` is only needed if that command expects the shim.
	- ## Related
		- [Dev Tools overview](https://mise.jdx.dev/dev-tools/) – how shims, plugins, and backends work
		- [Tasks guide](https://mise.jdx.dev/tasks/) – writing `run = "..."` blocks with `mise run` context
		- [Configuration reference](https://mise.jdx.dev/configuration.html) – complete `mise.toml` schema