logseq-entity:: [[Logseq/Entity/Question]]
- # What does "New remote project" do in the [[Codex]] desktop app, and does it need a host I already have running?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Remote connections](https://learn.chatgpt.com/docs/remote-connections.md)
			- **Short answer:** Yes. "New remote project" connects the ChatGPT desktop app to a **project folder on an existing SSH-reachable machine** — a devbox, an EC2 instance, a home server, anything you already have SSH access to. Codex does not provision or spin up a host for you; it only auto-discovers hosts already defined in your local `~/.ssh/config`.
			- The remote host must already have the `codex` CLI installed and on `PATH` for the login shell the SSH connection uses, since the app starts a remote Codex app server over SSH using that shell.
			- Setup order: add a concrete `Host` alias to `~/.ssh/config` (pattern-only entries are ignored), confirm `ssh <alias>` works from the machine running the desktop app, then in **Settings > Connections** add/enable that SSH host and pick a remote project folder.
			- This is distinct from the mobile **Remote** feature, which pairs a phone with an already-running desktop app host (Mac/Windows) via QR code; SSH remote projects are a separate way to point the desktop app itself at a folder on another machine's filesystem and shell.
			- Security note from the docs: keep the remote host under normal SSH hygiene (trusted keys, least-privilege accounts, no unauthenticated public listeners), and don't expose the remote Codex app-server transport directly on a shared or public network — use a VPN or mesh network instead if you need off-network access.
