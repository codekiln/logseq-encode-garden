logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Jeff Dickey]]
date-created:: [[2026/08]]
tags:: [[CLI/Tool]], [[Rust]]
alias:: mbx, mr-boxington

- # [Mr Boxington](https://mr-boxington.jdx.dev/)
	- Repository: [jdx/mr-boxington](https://github.com/jdx/mr-boxington) ([[Person/Jeff Dickey/GitHub/mr-boxington]]). [[GitHub/Star]]: 652 (checked [[2026-11-01 Sun]]).
	- A shared cache for [[cargo]] builds, run as the `mbx` command. Cargo still resolves dependencies, plans builds, and runs tools; `mbx` restores matching compiler outputs from one shared store and compiles the rest. No daemon or cache server is needed for local use. [^1]
	- Equivalent compilations share cache keys when checkout paths differ, so building one git worktree warms the next.
	- The store has a disk budget. Managed `target/` directories are collected when their checkout disappears, goes unused, or exceeds its budget. `mbx gc --dry-run` previews a collection.
	- Independent Cargo commands share CPU and memory permits and deduplicate identical compilations in flight.
	- CI can reuse the cache through the [[GitHub/Action]] cache, a compatible cache server, or an S3-compatible bucket. [jdx/mr-boxington-action](https://github.com/jdx/mr-boxington-action) sets it up. Pull request builds only read from a cache server or bucket; writes come from pushes to protected branches.
	- Install with [[mise]] (`mise use --global --tool-option mr_boxington=true rust mr-boxington`), or with `cargo install mbx --locked` followed by `mbx setup`.
	- Builds on ideas from sccache and kache; kache directly inspired its design.
	- Licensed under MIT.
	- Written in [[Rust]].
- ## Setup with [[mise]]
	- Set the `mr_boxington` option on the `rust` tool and add `mr-boxington` as its own tool. Cargo then runs through `mbx` under `mise exec`, mise tasks, activated shells and mise's shims, with no `mbx setup` step. [^2]
		- ```toml
		  [tools]
		  rust = { version = "latest", mr_boxington = true }
		  mr-boxington = "latest"
		  ```
	- Calling a toolchain's `cargo` directly, such as `~/.cargo/bin/cargo`, skips `mbx`. Check with `command -v cargo`. [^2]
	- My global mise config turns it on: [dotfiles#181](https://github.com/codekiln/dotfiles/issues/181).
- ## Typical commands
	- `mbx doctor` — check the setup
	- `mbx cache stats` — cache size and hits
	- `mbx gc --dry-run` — preview what garbage collection would remove
	- `mbx explain --last` — why the last build hit or missed
- ## Footnotes
	- [^1]: https://mr-boxington.jdx.dev/
	- [^2]: https://github.com/jdx/mise/blob/main/docs/lang/rust.md#share-cargo-builds-with-mr-boxington
