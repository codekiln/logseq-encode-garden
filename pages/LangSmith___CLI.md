logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[LangChain]]
date-created:: [[2026-03-02 Mon]]

- # [LangSmith CLI](https://docs.langchain.com/langsmith/langsmith-cli)
	- Source repository: [langchain-ai/langsmith-cli](https://github.com/langchain-ai/langsmith-cli). [[GitHub/Star]]: 70 (checked 2026-08-03).
	- Agent-first command-line tool for querying and managing [[LangSmith]] resources: tracing projects, traces, runs, threads, datasets, examples, evaluators, experiments, sandboxes, and Hub repos.
	- Written in [[Go]]. The recommended macOS/Linux installer is `curl -fsSL https://cli.langsmith.com/install.sh | sh`; it is also available through Homebrew (`langchain-ai/tap/langsmith-cli`), Scoop, GitHub Releases, and `go install github.com/langchain-ai/langsmith-cli/cmd/langsmith@latest`. It upgrades itself with `langsmith self-update`.
	- Outputs human-readable tables by default; `--format json` supports scripts and agents, and `-o <path>` writes output to a file.
	- Authenticates through browser-based [[OAuth]] (`langsmith auth login`) or `LANGSMITH_API_KEY`; OAuth is available for LangSmith Cloud and configured self-hosted deployments. Profiles and OAuth tokens are stored in `~/.langsmith/config.json`.
	- `langsmith api` is a `gh api`-style authenticated wrapper over the raw LangSmith REST API, including `langsmith api ls` / `langsmith api info` for browsing the OpenAPI spec — an escape hatch for anything the typed commands don't cover.
	- `langsmith trace setup claude` / `langsmith trace setup codex` writes [[Claude/Code]] and [[Codex]] config so a coding agent's own prompts, responses, and tool calls are traced to a LangSmith project.
	- `langsmith hub` pushes and pulls versioned agent and skill repos, the CLI surface over the SDK's `push_skill` / `pull_skill` / `push_agent` / `pull_agent` methods.
	- Global installation declaration: [codekiln/dotfiles mise config](https://github.com/codekiln/dotfiles/blob/main/chezmoi/dot_config/mise/config.toml).
