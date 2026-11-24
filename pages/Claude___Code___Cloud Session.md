logseq-entity:: [[Logseq/Entity/Software/Feature]]

- # [Cloud session](https://code.claude.com/docs/en/claude-code-on-the-web)
	- A [[Claude/Code]] session that runs on cloud infrastructure, by default an isolated VM that Anthropic manages. It keeps running after the laptop closes, and it can be checked on or steered from any device.
	- Start one from the browser at [claude.ai/code](https://claude.ai/code), which Anthropic also calls Claude Code on the web, from the Code tab in the Claude mobile app, from the Desktop app, or from the terminal with `claude --cloud "<task>"`. `claude --teleport` pulls a cloud session into the terminal.
	- Each session clones the repository from GitHub and runs in a cloud environment, the saved configuration for network access, environment variables, network secrets and the setup script. Network access is limited by default. GitHub credentials and network secrets stay outside the VM, and a proxy attaches them to matching requests.
	- Auto-fix watches a pull request and pushes fixes for failing CI checks and clear review comments.
	- A project has Claude start and track many cloud sessions, called threads, from one conversation. Projects are in public beta.
	- ## In [[AI/ES/26/11 Code/YouTube/Rethinking Claude Code Best Practices]]
		- [[Person/Lydia Hallie]] recommends cloud sessions for sessions that run for hours unattended. A local sandbox covers only shell commands, while Claude's file tools, MCP servers and hooks still run on your machine. A cloud session gets its own machine with a fresh copy of the repo, so `.env`, SSH keys and the GitHub token aren't there to leak. [9:10](https://www.youtube.com/watch?v=vlfCjWuv4es&t=550s)
		- Keep auto mode on and commit deny rules to the repo, because the machine is disposable but pushed commits and messages sent through connectors are not. [10:26](https://www.youtube.com/watch?v=vlfCjWuv4es&t=626s)
		- To get started: give Claude a task bigger than usual, make sure CI catches what you care about, configure the environment's network access, secrets and setup script, and start in the cloud. [17:02](https://www.youtube.com/watch?v=vlfCjWuv4es&t=1022s)
