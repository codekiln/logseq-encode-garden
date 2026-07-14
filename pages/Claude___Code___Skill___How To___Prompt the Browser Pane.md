tags:: [[Diataxis/How To]]
title:: Claude/Code/Skill/How To/Prompt the Browser Pane
see-also:: [[Claude/Desktop/Code/Browser]], [[Claude/Code/Skill]], [[Claude/Desktop/Code]]

- # How To Prompt the Browser Pane in a Claude Code Skill
	- ## Overview
		- This guide shows how to write a [[Claude/Code/Skill]] that reliably drives the in-app **Browser pane** ([[Claude/Desktop/Code/Browser]]) rather than the **Claude in Chrome** extension.
		- Use it when a skill needs to preview a running app, open documentation, or interact with a web page from a clean, isolated browser profile.
	- ## Prerequisites
		- The **Browser pane**, available in the Claude Desktop **Code** tab (not the terminal CLI).
		- A skill you can edit — a `SKILL.md` in a named directory, invoked explicitly (`/skill-name`) or discovered automatically.
		- Knowing the two surfaces are distinct tool namespaces: the pane is `mcp__Claude_Browser__*`; the extension is `mcp__claude-in-chrome__*`.
	- ## Steps
		- ### 1. Name the surface in the skill body
			- Say **"Browser pane"** or **"in-app browser"** explicitly, and state that the skill should **not** use Claude in Chrome. Naming the surface disambiguates, because the two are separate tool namespaces.
			- If the skill only ever needs a clean profile, add a one-line rule such as: "Do all browsing in the in-app Browser pane; do not use Claude in Chrome."
		- ### 2. Call out the tools you expect
			- List the specific `mcp__Claude_Browser__*` tools the task needs so Claude reaches for them directly instead of guessing a surface.
			- ~~~text
			  Use the Browser pane tools: preview_start (dev server or URL),
			  navigate, read_page (accessibility tree), get_page_text,
			  computer (click/type/screenshot), form_input,
			  read_console_messages and read_network_requests (debugging).
			  ~~~
		- ### 3. Give the tool-use sequence
			- Describe the flow in the order the tools run, so the skill closes the loop instead of stopping at "navigate":
			- 1. `preview_start` — open a URL, or start the dev server the project defines.
			- 2. `navigate` — go to the target page.
			- 3. `read_page` / `get_page_text` — inspect structure and copy before acting.
			- 4. `computer` / `form_input` — click, type, screenshot, submit.
			- 5. `read_console_messages` / `read_network_requests` — verify and debug. Use `javascript_tool` for inspection only, never to implement UI changes.
		- ### 4. Pre-approve the tools so the skill runs uninterrupted
			- If you want the skill to run without per-tool prompts, allow the Browser tools in `settings.json`:
			- ~~~json
			  {
			    "permissions": {
			      "allow": [
			        "mcp__Claude_Browser__navigate",
			        "mcp__Claude_Browser__computer",
			        "mcp__Claude_Browser__read_page",
			        "mcp__Claude_Browser__preview_start"
			      ]
			    }
			  }
			  ~~~
			- For a slash-command skill, list the same strings in the command's `allowed-tools` frontmatter instead.
		- ### 5. Reserve Claude in Chrome for logged-in work
			- Keep tasks in the pane when they don't need your identity. If a step genuinely requires your existing sessions and cookies, that step belongs in **Claude in Chrome** — split it out rather than fighting the routing.
	- ## Troubleshooting
		- **Claude uses Claude in Chrome instead of the pane** — name the Browser pane explicitly in the skill, or disable the Claude in Chrome connector under **Settings → Connectors** while the skill runs.
		- **Permission prompts interrupt the run** — add the `mcp__Claude_Browser__*` strings to `permissions.allow` (step 4).
		- **Actions on an external site are blocked or keep prompting** — the first action on each site (and subdomain) shows an **Allow once / Always allow / Deny** card; safety classifiers can still prompt on write actions in any mode. Local previews and project files need no approval.
		- **The tools aren't available at all** — the Browser pane exists only in the Desktop Code tab; a terminal CLI session has no pane to drive.
