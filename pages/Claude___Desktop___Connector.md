title:: Claude/Desktop/Connector
see-also:: [[Claude/Desktop]], [[Claude/Desktop/Extension]], [[MCP]]
date-created:: [[2026/04/23]]

- # [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
	- ## Overview
		- **Connectors** let Claude access apps and services, retrieve data, and take actions within connected services. Claude inherits each person's permissions from the source system.
		- **Web (remote) connectors** work on Claude web, Cowork, [[Claude/Desktop]], Claude Mobile, and Claude Code (and via API [MCP Connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)).
		- **Desktop extensions** (local [[MCP]]) install via [[Claude/Desktop/Extension]] but their tools also appear under the chat **Connectors** menu once installed.
		- **Directory:** [Connectors Directory](https://claude.ai/connectors) — per-connector use cases, read/write capabilities, availability.
		- **When to use which:** [When to use desktop and web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)
	- ## Remote connectors vs desktop extensions
		- | Tool type | Install / connect | Surfaces |
		  |---|---|---|
		  | Cloud SaaS (Slack, Linear, Notion, GitHub, …) | **Customize > Connectors** or directory | Web, mobile, Cowork, Desktop, Code |
		  | Runs on your machine (files, localhost DB, desktop app) | **Settings > Extensions** (`.mcpb`) | Desktop, Code only |
		  | Custom MCP with public URL | Add **custom connector** (remote) | All surfaces |
		  | Custom MCP that runs locally | Desktop **extension** | Desktop, Code only |
		- **Plugins** can bundle remote MCP, local MCP, or both.
	- ## Browse and connect (remote)
		- **From chat:** **+** (or `/`) → **Connectors** → **Manage connectors** → **+** next to Connectors → browse by category.
		- **From settings:** [Customize > Connectors](https://claude.ai/customize/connectors) → **+** → pick connector → **Connect** / **Install** → authenticate.
		- **In conversation:** **+** → **Connectors** → toggle services on for that chat.
		- **Desktop app:** **Settings → Connectors** or **Manage connectors** from the prompt **Connectors** menu ([Claude Code Desktop docs](https://code.claude.com/docs/en/desktop)).
	- ## Tool access modes
		- **+** → **Connectors** → **Tool access** (or see [Manage Claude's tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)).
		- **Auto** (default) for most users; **On demand** when **10+** connectors are active.
	- ## Custom connectors (remote MCP)
		- **Customize > Connectors** → **+** → **Add custom connector** → name, URL, optional OAuth client ID/secret.
		- Server must be reachable from **Anthropic's cloud** (not only your LAN). Free plan: **one** custom connector.
		- Setup guide: [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
	- ## Team and Enterprise
		- Owners enable connectors at **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** before members can authenticate.
		- **Tool permissions** per connector: Always allow / Needs approval / Blocked (read vs write categories).
		- Connectors in **private projects** only; synced chats not shareable.
	- ## Notable connectors and local tools
		- ### Remote / directory examples
			- **Linear** — create and manage issues
			- **Slack** — send messages, search channels
			- **Google Drive** — search and read files (per account permissions)
			- **Claude in Chrome** — browser tasks from Desktop; configure under **Settings > Connectors** → **Claude in Chrome**; requires [Chrome Web Store extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn). See [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome).
		- ### Desktop extensions (install under [[Claude/Desktop/Extension]])
			- Local MCP packages from **Settings > Extensions > Browse extensions**; tools then show in chat **Connectors**. Common directory examples:
			- **Filesystem** — read/write access to directories you approve; find, read, write, and organize files without drag-and-drop.
			- **Control Chrome** — read the active tab, navigate, click, and extract content from the open browser (live, not cached); pairs with browser use cases on the machine.
			- **pdf-viewer** — open PDFs inline with annotation and text extraction without a separate viewer app.
			- Other frequently paired extensions (community writeups): **Desktop Commander** (shell/process workflows), **Filesystem Plus** (stricter path controls)—often combined with **Filesystem** for local agentic loops (write → run script → read output in one chat).
	- ## Security
		- Encrypted transfers; only data you can access in the source system.
		- Review permissions when connecting; disconnect unused services.
		- Custom connectors are **unverified** by Anthropic—trusted servers only.
	- ## Troubleshooting
		- Remote: stable network, active account, disconnect/reconnect at **Customize > Connectors**.
		- **Custom connector timeout:** server must be public-internet reachable from Anthropic cloud (firewall allowlist)—not the same as local extensions.
		- Local tools missing: confirm extension installed under **Settings > Extensions**; check **+** → **Connectors** toggles; restart Desktop; see [[Claude/Desktop/Extension]] troubleshooting.
