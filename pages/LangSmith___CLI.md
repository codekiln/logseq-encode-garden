logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[LangChain]]
date-created:: [[2026-03-02 Mon]]

- # [LangSmith CLI](https://docs.langchain.com/langsmith/langsmith-cli)
	- Source repository: [langchain-ai/langsmith-cli](https://github.com/langchain-ai/langsmith-cli). [[GitHub/Star]]: 70 (checked 2026-08-03).
	- Agent-first command-line tool for querying and managing [[LangSmith]] resources: tracing projects, traces, runs, threads, datasets, examples, evaluators, experiments, sandboxes, and Hub repos.
	- Written in [[Go]]. Ships as a single binary via `curl -fsSL https://cli.langsmith.com/install.sh | sh`, Homebrew (`langchain-ai/tap/langsmith-cli`), Scoop, GitHub Releases, or `go install`, and upgrades itself with `langsmith self-update`.
	- Outputs JSON by default so it pipes into scripts and agents; `--format pretty` renders human-readable tables and `-o <path>` writes to a file.
	- Authenticates by [[OAuth]] device flow (`langsmith auth login`, LangSmith Cloud only) or by `LANGSMITH_API_KEY`; tokens and workspaces are stored per profile in `~/.langsmith/config.json`.
	- `langsmith api` is a `gh api`-style authenticated wrapper over the raw LangSmith REST API, including `langsmith api ls` / `langsmith api info` for browsing the OpenAPI spec — an escape hatch for anything the typed commands don't cover.
	- `langsmith trace setup claude` / `langsmith trace setup codex` writes [[Claude/Code]] and [[Codex]] config so a coding agent's own prompts, responses, and tool calls are traced to a LangSmith project.
	- `langsmith hub` pushes and pulls versioned agent and skill repos, the CLI surface over the SDK's `push_skill` / `pull_skill` / `push_agent` / `pull_agent` methods.
