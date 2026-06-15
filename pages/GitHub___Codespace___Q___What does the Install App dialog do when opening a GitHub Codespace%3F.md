logseq-entity:: [[Logseq/Entity/Question]]

- # What does the Install App dialog do when opening a GitHub Codespace?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- [[Answer/Official]] from [GitHub Codespaces – VS Code Docs](https://code.visualstudio.com/docs/remote/codespaces)
			- **Short answer:** It is the browser's [[PWA]] (Progressive Web App) install prompt. Clicking **Install** opens the Codespace in a standalone app window outside the browser, which fixes keyboard-shortcut conflicts that occur when the editor runs inside a browser tab.
			- When a Codespace loads in the browser at a `*.github.dev` URL, the site ships a web-app manifest that tells the browser it is installable. The browser surfaces an **Install app** dialog (the exact dialog varies by browser — Chrome, Edge, etc.).
			- **What installing does:**
				- Opens the Codespace in a dedicated standalone window with no browser chrome (tabs, address bar).
				- Resolves keybinding conflicts: browser-level shortcuts (e.g. `Ctrl+W`, `Ctrl+N`) no longer intercept VS Code shortcuts.
				- The VS Code docs explicitly recommend installing as a PWA as the workaround for a class of keyboard-shortcut limitations in browser-based Codespaces.
			- **Scope is per-Codespace:** each Codespace gets a unique subdomain (e.g. `special-fortnight-gx5xp7956h9794.github.dev`), so a PWA install applies only to that specific instance.
			- **You can skip it** (click Cancel) and continue using the Codespace normally in the browser tab — functionality is identical, minus the keybinding improvements.
