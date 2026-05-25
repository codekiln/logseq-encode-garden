# [OpenSpec Getting Started Docs](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md)
	- There are two main ways to use openspec.
		- "Default quick path" aka "core profile"
			- `/opsx:propose ──► /opsx:apply ──► /opsx:sync ──► /opsx:archive`
		- "Expanded path" aka "custom workflow selection"
			- `/opsx:new ──► /opsx:ff or /opsx:continue ──► /opsx:apply ──► /opsx:verify ──► /opsx:archive`
	- It seems like they call these "profiles" because [[OpenSpec/config/profile]] is supposed to let you configure them.
	- It's also confusing because not all [[Agentic Coding Tool]]s support [[Slash Command]]s; for example, [[Codex/CLI]] does not. So what are we to do in Codex?
	-