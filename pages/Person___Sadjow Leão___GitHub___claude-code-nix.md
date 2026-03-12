created-by:: [[Person/Sadjow Leão]]
- # [sadjow/claude-code-nix](https://github.com/sadjow/claude-code-nix)
	- Repository: [sadjow/claude-code-nix](https://github.com/sadjow/claude-code-nix)
	- Created by: [[Person/Sadjow Leão]]
	- Created: 2025-06-20
	- GitHub status on 2026-03-12: 251 stars, 17 forks, 0 open issues
	- **Always up-to-date Nix package for Claude Code with hourly updates, native binary default, and Node.js/Bun alternatives.**
	- It packages [[Claude Code]] for Nix users who want faster updates than upstream `nixpkgs`, plus explicit version pinning and rollback.
	- ## Why It Exists
		- Targets the gap between Anthropic's official installer and the slower update cadence of upstream `nixpkgs`
		- Keeps new [[Claude Code]] releases available within about an hour of upstream release
		- Gives Nix users a declarative install that does not disappear when switching Node.js versions with tools like `asdf` or `nvm`
	- ## Packaging Model
		- Default package is a native self-contained binary with no runtime dependency
		- Alternative packages are available for Node.js 22 LTS and Bun
		- The flake can be used directly with `nix run`, installed with `nix profile install`, or consumed through an overlay in NixOS or Home Manager
		- Cachix is supported for faster installs, but local builds are also supported for users who prefer stronger verification
	- ## Runtime Options
		- `claude-code`: native binary, exposed as `claude`
		- `claude-code-node`: Node.js runtime, exposed as `claude-node`
		- `claude-code-bun`: Bun runtime, exposed as `claude-bun`
	- ## Versioning and Updates
		- GitHub Actions checks for new [[Claude Code]] versions every hour
		- The repository supports both moving refs and immutable refs
		- Exact version tags such as `v2.1.71` and commit SHAs are the real reproducible pins
		- Major tags like `v2`, the `latest` tag, and the default branch intentionally move forward over time
	- ## Trust Model
		- The package fetches npm tarballs and native binaries with fixed hashes
		- `flake.lock` pins inputs for a given repo revision
		- The packaged binaries disable Claude's built-in auto-updater so updates flow through Nix instead
		- Trust still extends to the maintainer account, the auto-update GitHub Actions workflow, Anthropic's upstream artifacts, and optionally the project's Cachix cache
	- ## Useful Commands
		- Try it without installing:
			- ~~~bash
			  nix run github:sadjow/claude-code-nix
			  ~~~
		- Install to profile:
			- ~~~bash
			  nix profile install github:sadjow/claude-code-nix
			  ~~~
		- Pin an exact release:
			- ~~~bash
			  nix run github:sadjow/claude-code-nix?ref=v2.1.71
			  ~~~
		- Update installed flake packages:
			- ~~~bash
			  nix profile upgrade --all
			  ~~~
	- ## Comparison Notes
		- Compared with `npm install -g @anthropic-ai/claude-code`, this flake is more declarative and survives Node.js version switching
		- Compared with upstream `nixpkgs`, this repo optimizes for freshness, runtime choice, and a dedicated maintenance path
		- Compared with Anthropic's [official installer](https://claude.ai/install.sh), this flake adds Nix-native pinning, rollback, and configuration ergonomics
	- ## Links
		- README: [README.md](https://github.com/sadjow/claude-code-nix/blob/main/README.md)
		- Issues: [GitHub Issues](https://github.com/sadjow/claude-code-nix/issues)
		- Actions: [GitHub Actions](https://github.com/sadjow/claude-code-nix/actions)
