logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Atlassian]]

- # [TWG](https://teamworkgraph.com/cli)
	- Command-line client for Atlassian's Teamwork Graph; the binary is `twg`. [Installation docs](https://developer.atlassian.com/cloud/twg-cli/getting-started/installation/).
	- Reads data across [[JIRA]], [[Confluence]], Bitbucket, and other Atlassian products from the terminal.
	- Built for AI coding agents as well as people; an alternative route to the data the [[Atlassian/MCP]] server exposes.
	- Authenticates with OAuth 2.1 through a browser sign-in; credentials persist in the TWG config directory.
	- Ships as a standalone binary (no Node.js or other runtime) for macOS arm64/x64, Linux x64, and Windows arm64/x64.
	- Install options
		- `bash <(curl -fsSL https://teamwork-graph.atlassian.com/cli/install)` on macOS and Linux; `TWG_VERSION` pins a release and `--install-dir` overrides the default `~/.local/bin`.
		- macOS `.pkg`, and PowerShell or MSI installers on Windows.
		- Raw binaries are published at `https://teamwork-graph.atlassian.com/cli/twg-<os>-<arch>-v<version>`, with a `SHA256SUMS-v<version>` file per release.
	- Agent skills ship in the binary and in a public repo: [[TWG/Agent/Skill]].
