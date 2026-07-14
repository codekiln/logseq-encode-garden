title:: Claude/Desktop/Code/Browser
see-also:: [[Claude/Desktop/Code]], [[Claude/Desktop]], [[Claude/Code]], [[Claude/Code/Skill]], [[Claude/Desktop/Connector]], [[MCP]]
date-created:: [[2026/07/06]]

- # [Browser pane in the Claude Desktop Code tab](https://code.claude.com/docs/en/desktop#browse-external-sites)
	- ## Overview
		- The **Browser pane** is a built-in, tabbed browser embedded in the **Code** tab of [[Claude/Desktop]], separate from the [[Claude/Desktop/Connector]]-based **Claude in Chrome** extension. Claude drives it with the same tools it uses to verify a local dev-server preview.
		- **Introduced:** Week 28 2026 (July 6–10, v2.1.202–v2.1.206) — "Claude Code on desktop gets a built-in browser, so Claude can pull up docs, designs, or any other site and interact with pages the same way it does with your local dev server previews."
		- **Open it:** **Cmd+Shift+B** (macOS) / **Ctrl+Shift+B** (Windows), or the **Views** menu. **Cmd+Shift+S** / **Ctrl+Shift+S** selects an element in the Browser.
		- **Turn it off / clear data:** toggles in **Settings → Claude Code**.
		- **Under the hood** these are [[MCP]] tools prefixed `mcp__Claude_Browser__*`; the Chrome extension is a separate surface prefixed `mcp__claude-in-chrome__*`.
	- ## What it can do
		- **Preview a running app** — Claude starts the dev server and opens it in the pane, for frontend and backend alike (test API endpoints, view server logs, iterate). Starts automatically after edits in most cases; you can also ask any time.
		- **Open project files** — click an HTML, PDF, image, or video path in the chat to render it in the pane.
		- **Browse external sites** — documentation, issue trackers, designs, any site, in tabs beside the running app.
		- **Interact** — navigate, click, type, fill forms, scroll, read page text and the accessibility tree, take screenshots, inspect console output and network requests, and run JS for debugging.
		- **Sessions** — sign in to sites in the pane (including popup flows like Google OAuth); **Persist sessions** (dropdown) keeps cookies and local storage across server restarts so you don't re-login during development.
	- ## Browser pane vs Claude in Chrome
		- The pane uses a **clean profile, separate from your personal browser, with none of your saved logins or history**. Use it for building and testing your app and for sites that don't need your identity.
		- Use the **Claude in Chrome** extension when you want Claude to **act as you in your logged-in sessions** — it shares your browser's login state.
		- Both use the same safety model; see [Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely).
		- | | Browser pane | Claude in Chrome |
		  |---|---|---|
		  | Profile | Clean, isolated | Your real Chrome |
		  | Saved logins / history | None | Yours, available immediately |
		  | Best for | Building, testing, unauthenticated sites | Acting as you on authenticated sites |
		  | Surfaces | Desktop Code tab only | CLI, Desktop, VS Code |
		  | Tool prefix | `mcp__Claude_Browser__*` | `mcp__claude-in-chrome__*` |
	- ## Steering Claude toward the pane (not Chrome)
		- **Default leans to the pane.** The harness prefers the in-app Browser and reaches for Claude in Chrome only when the task needs your logged-in sessions. So to stay in the pane, keep the task free of anything requiring your identity and don't mention Chrome.
		- **Name the surface** when it matters — "open the **in-app Browser** / **Browser pane**", "check `localhost:3000` in the app", versus "use **Claude in Chrome**". The two are distinct tool namespaces, so naming disambiguates.
		- **Implicit routing** — clicking an external link in the chat offers **Open in app** (pane) vs **Default browser**; **Cmd/Ctrl-click** goes straight to your system browser.
		- **Config bias** — define dev servers in `.claude/launch.json` so preview stays in the pane; if the **Claude in Chrome** connector is enabled and you'd rather use the pane, disable it under **Settings → Connectors** or just say which one to use.
	- ## Using it from a Skill or command
		- The Browser tools are ordinary [[MCP]] tools; a [[Claude/Code/Skill]] steers Claude to them **in prose** — tell it to use the **Browser pane** and, where useful, name the tools (`mcp__Claude_Browser__navigate`, `mcp__Claude_Browser__preview_start`, `mcp__Claude_Browser__read_page`, `mcp__Claude_Browser__computer`, `mcp__Claude_Browser__get_page_text`, `mcp__Claude_Browser__read_console_messages`, `mcp__Claude_Browser__read_network_requests`).
		- **Pre-approve the tools** (so the skill runs without prompts) with permission strings in `settings.json` `permissions.allow`, e.g. `mcp__Claude_Browser__navigate`, or a slash command's `allowed-tools`. `browserExternalPageTools: "disabled"` (managed setting) blocks Claude's tools on external pages org-wide.
		- **In this garden, author under `.rulesync/skills/` and run `rulesync generate`** — never hand-edit the compiled `.claude/skills/` output.
		- **Shape of a Browser skill:** `preview_start` (dev server from `.claude/launch.json`, or a URL) → `navigate` → `read_page` / `get_page_text` to inspect → `computer` to click/type/screenshot → `read_console_messages` / `read_network_requests` to debug. Use `javascript_tool` for inspection only, not to implement UI changes.
	- ## Configure preview servers
		- Claude auto-detects the dev server and writes `.claude/launch.json` at the session's root folder (JSON-with-comments). Edit it to change the command or port, or click **Edit configuration** in the server dropdown.
		- ~~~json
		  {
		    "version": "0.0.1",
		    "configurations": [
		      { "name": "my-app", "runtimeExecutable": "npm", "runtimeArgs": ["run", "dev"], "port": 3000 }
		    ]
		  }
		  ~~~
		- Multiple configurations run several servers from one project (e.g. frontend + API).
		- **Auto-verify** is on by default: after every edit Claude screenshots, checks for errors, and confirms the change works. Disable per-project with `"autoVerify": false` in `.claude/launch.json` or the server dropdown; preview tools still work on request.
	- ## Safety and admin
		- **External-site approval:** the first time Claude acts on a site, a card offers **Allow once** / **Always allow** / **Deny**; each site (and subdomain) is approved separately. Local dev servers and project files need no approval.
		- **Guardrails:** safety classifiers review write actions (click, type) in every mode; outside Auto/Bypass a domain-allowlist check runs before navigating. Even on approved sites Claude won't purchase, create accounts, or bypass CAPTCHAs without you.
		- **Org controls:** the pane honors the same [site allowlist/blocklist](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls) as the Chrome extension; admins can disable external-page tools via the `browserExternalPageTools` managed setting.
	- ## Sources
		- [Claude Desktop — Preview your app](https://code.claude.com/docs/en/desktop#preview-your-app) / [Browse external sites](https://code.claude.com/docs/en/desktop#browse-external-sites) / [Configure preview servers](https://code.claude.com/docs/en/desktop#configure-preview-servers)
		- [What's new — Week 28 (July 6–10 2026)](https://code.claude.com/docs/en/whats-new/2026-w28)
