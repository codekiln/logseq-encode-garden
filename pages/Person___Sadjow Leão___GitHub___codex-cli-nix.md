created-by:: [[Person/Sadjow Leão]]
- # [sadjow/codex-cli-nix](https://github.com/sadjow/codex-cli-nix)
	- Repository: [sadjow/codex-cli-nix](https://github.com/sadjow/codex-cli-nix)
	- Created by: [[Person/Sadjow Leão]]
	- Created: 2025-09-04
	- GitHub status on 2026-03-12: 59 stars, 14 forks, 0 open issues
	- **Nix flake for OpenAI Codex CLI with a native Rust binary default, hourly updates, and multi-platform caching.**
	- It packages [[OpenAI/Codex/CLI]] for Nix users who want declarative installs, quick release pickup, and a native binary that avoids a Node.js dependency by default.
	- ## Why It Exists
		- Gives Nix users near-immediate access to new [[OpenAI/Codex/CLI]] releases
		- Avoids the fragility of `npm install -g @openai/codex` when switching Node.js versions across projects
		- Provides a focused flake with binary caching and a dedicated update workflow
	- ## Packaging Model
		- Default package is a native Rust binary exposed as `codex`
		- Alternative package `codex-node` bundles Node.js 22 LTS for users who want the npm-style runtime
		- Pre-built binaries are intended for Linux and macOS on both x86_64 and ARM64
		- The flake can be used directly with `nix run`, installed with `nix profile install`, or consumed from a flake input in NixOS or Home Manager
	- ## Versioning and Updates
		- GitHub Actions checks hourly for new Codex releases
		- The project emphasizes getting new releases packaged within about an hour
		- Cachix support is included so users can download pre-built artifacts instead of compiling locally
	- ## Trust Model
		- The default package uses pre-built Rust binaries from OpenAI's GitHub releases
		- The alternative Node.js package uses the npm distribution of `@openai/codex`
		- Reproducibility depends on the flake revision and pinned hashes in the packaging
		- Trust still extends to the maintainer account, the automation workflow, OpenAI upstream release artifacts, and optionally the project's Cachix cache
	- ## Useful Commands
		- Try the native binary:
			- ~~~bash
			  nix run github:sadjow/codex-cli-nix
			  ~~~
		- Try the Node.js variant:
			- ~~~bash
			  nix run github:sadjow/codex-cli-nix#codex-node
			  ~~~
		- Install to profile:
			- ~~~bash
			  nix profile install github:sadjow/codex-cli-nix
			  ~~~
		- Add the Cachix cache:
			- ~~~bash
			  cachix use codex-cli
			  ~~~
	- ## Comparison Notes
		- Compared with `npm install -g @openai/codex`, this flake is more stable across Node.js version switching and easier to manage declaratively
		- Compared with raw source builds, this repo emphasizes pre-built multi-platform binaries and quick installation
		- It is a close parallel to [[Person/Sadjow Leão/GitHub/claude-code-nix]], but targeted at [[OpenAI/Codex/CLI]] instead of [[Claude Code]]
	- ## Links
		- README: [README.md](https://github.com/sadjow/codex-cli-nix/blob/main/README.md)
		- Issues: [GitHub Issues](https://github.com/sadjow/codex-cli-nix/issues)
		- Actions: [GitHub Actions](https://github.com/sadjow/codex-cli-nix/actions)
