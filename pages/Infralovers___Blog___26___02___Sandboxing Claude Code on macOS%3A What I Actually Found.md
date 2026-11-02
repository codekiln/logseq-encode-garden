date-created:: [[2026-02-15]]
created-by:: [[Person/Edmund Haselwanter]], [[Infralovers]]
see-also:: [[Docker/Sandboxes]], [[Person/Luis Cardoso/Blog/26/01/A field guide to sandboxes for AI]]

- # [Sandboxing Claude Code on macOS: What I Actually Found](https://www.infralovers.com/blog/2026-02-15-sandboxing-claude-code-macos/)
	- Ben Eisenbraun (HMS) shared it at the Harvard Software Development CoP AI-Assisted Coding tiger team meeting on [[2026-11-02]], after Artie Barrett's talk on [[Docker/Sandboxes]].
	- Written by [[Person/Edmund Haselwanter]] as his team moved [[Claude/Code]] from interactive use to agents that run in the background. Permission prompts assume someone is watching, and background agents have no one to click Allow.
- ## Level 1: Claude Code's built-in `/sandbox`
	- It uses Anthropic's open-source sandbox runtime: Seatbelt (`sandbox-exec`) on macOS and bubblewrap on Linux. Writes are limited to the working directory, and network traffic goes through an allowlisting proxy.
	- Anthropic reports about 84% fewer permission prompts with it on. Apple marks `sandbox-exec` as deprecated, which leaves its future uncertain.
	- It's enough for iterative pair programming.
- ## Level 2: where `/sandbox` stops
	- Docker commands end up in `excludedCommands`, which defeats the sandbox.
	- MCP servers can't be allowlisted precisely enough, browser automation is limited, and background agents can't answer prompts.
	- He estimates it covers about 40% of his team's workflows.
- ## Level 3: run the agent inside a VM
	- **[[Docker/Sandboxes]]:** a microVM per sandbox, each with its own kernel and Docker daemon. The workspace syncs both ways, network goes through a proxy with domain allow and deny lists, and Claude runs with `--dangerously-skip-permissions`. In February 2026 this needed Docker Desktop 4.58+, which is free only for organizations with fewer than 250 employees and under $10M in revenue. Its downsides were growing disk use and some effort to manage credentials.
		- At the 2026-11-02 tiger team meeting, Artie Barrett said Docker has since split sandboxes out into a separate `sbx` tool that is free to use locally.
	- **Lima and Colima:** open source, a CNCF project. Lima runs Claude inside one VM. Colima wraps Lima to give a Docker Desktop-like experience on the host, which is a different use.
	- **[[OrbStack]]:** very fast, with a 2-second boot, less RAM than Docker Desktop, and near-native file performance. But its Linux machines share one kernel, file sharing is bidirectional and can't be turned off, and it is closed source. He thinks it's fine for trusted work but not strong enough to sandbox an agent with permissions skipped.
	- **Tart (Cirrus Labs):** has the most security-minded defaults, with no mounts and a packet filter (Softnet) that allows only listed networks. It suits CI and is too much friction for interactive work.
- ## Where the real risks are
	- Mostly in what you share into the sandbox. Read access matters more than write access: if the agent can read `~/.ssh` and reach the network, your keys are gone.
	- Network access is the second risk. Docker Sandboxes filters by domain and Tart filters packets. With Lima and OrbStack you configure iptables yourself.
	- He gives CVE-2025-9074 as an example. It exposed Docker Desktop's Engine API to containers without authentication.
- ## His conclusion
	- The VM boundary is the security boundary. Containers, devcontainers and Seatbelt profiles add defense in depth but are not a different tier.
	- Use `/sandbox` for a pair programmer. Use a VM for agents that need Docker, MCP and network access.
