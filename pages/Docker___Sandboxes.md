alias:: [[Docker Sandboxes]], [[sbx]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Docker]]
see-also:: [[Person/Luis Cardoso/Blog/26/01/A field guide to sandboxes for AI]], [[Infralovers/Blog/26/02/Sandboxing Claude Code on macOS: What I Actually Found]]

- # [Docker Sandboxes](https://www.docker.com/products/docker-sandboxes/)
	- Release repository: [docker/sbx-releases](https://github.com/docker/sbx-releases) — releases only, no source listed there. [[GitHub/Star]]: 490 (checked 2026-11-02). Community kits live in [docker/sbx-kits-contrib](https://github.com/docker/sbx-kits-contrib).
	- Runs AI coding agents unattended in disposable microVMs, on your machine or on Docker-managed cloud infrastructure. Each sandbox has its own kernel and its own private [[Docker]] Engine, with scoped access to files, network, and secrets.
	- Controlled with the `sbx` CLI, for example `sbx run claude` or `sbx run codex`. `sbx move` shifts a sandbox between laptop and cloud.
	- Agents named on the product page: [[Claude/Code]], Codex, Cursor, Devin, Copilot CLI, and OpenCode.
	- Runs on macOS, Windows, and Linux. Local use is free; cloud sandboxes are billed by the second.
	- Related: [[LangSmith/Sandbox]] — a managed sandbox for agent code in LangSmith.
