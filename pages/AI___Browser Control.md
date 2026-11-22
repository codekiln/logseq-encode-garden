tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[AI/Agent]], [[Browser/Headless]]

- # AI Browser Control
	- ## Overview
		- An [[AI/Agent]] operating a web browser on a person's behalf: opening pages, reading them, clicking, typing into forms and submitting them. The agent uses websites the way a person does, through their pages, rather than through an API the website offers.
	- ## Context
		- Most websites a person relies on, such as billers, banks and stores, offer no API an agent can call. Browser control lets an agent work with those sites anyway.
		- It also means the agent inherits whatever the browser session holds: sign-ins, saved cards on merchant accounts, and anything else that site lets a signed-in person do.
	- ## Key Principles
		- **Where the browser runs.** On a remote computer the vendor runs, or on the person's own computer. A remote browser can keep working while the person is away. A local browser can use the person's existing sign-ins, extensions and password manager.
		- **Who confirms.** Agents ask the person before a payment, purchase or other hard-to-reverse step, and hand the browser back when they get stuck on a sign-in or a challenge.
		- **What it can pay with.** Browser control alone can only use payment details a site already stores. Paying with a new card takes a separate payment feature such as [[ChatGPT/Wallet]].
	- ## Examples
		- [[ChatGPT/Cloud/Browser]] — a remote browser used by [[ChatGPT/Work]]
		- [[Claude/Desktop/Code/Browser]] — a browser pane inside the Claude Desktop Code tab; Claude in Chrome is a separate extension that drives the person's own Chrome
		- [[CursorAI/Feature/Browser Control]] — Cursor's agent driving a browser through an MCP server
		- [[Playwright/MCP]] — a general-purpose way to give any MCP-capable agent a browser
		- [[My/AI/Agent/Fleet/Browser]] — how my own agents choose between Claude in Chrome and Playwright
