tags:: [[Diataxis/How To]]

- # How To Keep ChatGPT Links in Your Browser (macOS)
	- ## Goal
		- Ensure links to `chatgpt.com` open in your default web browser instead of launching the ChatGPT desktop app.
	- ## Preconditions
		- macOS 13 or later with the ChatGPT desktop app installed.
		- Terminal access with an admin account (for Options 3 & 4).
	- ## Procedure
		- ### 0. Toggle Off the Built-In Setting (==recommended==)
			- Open **ChatGPT → Settings → App** and disable **Open ChatGPT Links in Desktop App** (the switch turns gray).  
			  macOS will now route every `chatgpt.com` link to your browser.
		- ### 1. Quick Work-Around (per-link, must be in browser already)
			- This only works if you are in a browser when you click on the link.
			- **Control-click** the link in Safari ➜ choose **Open Link in New Tab**.  
			  This bypasses the Universal Link and keeps you in the browser ([Michael Tsai blog](https://mjtsai.com/blog/2022/04/19/disabling-universal-links/)).
		- ### 2. Remove the Desktop App (simple and dumb)
			- Drag **ChatGPT.app** from `/Applications` to the Trash and empty it.  
			  With no matching app, macOS falls back to the website for every ChatGPT link.
		- ### 3. Unregister ChatGPT’s Universal-Link Association (flakey)
			- Run **once** in Terminal:
			  ~~~bash
			  /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -u -f /Applications/ChatGPT.app
			  ~~~
			- This removes the app’s `applinks:chatgpt.com` entry.  
			  Source: *Ask Different* answer describing `lsregister -u` for URL-scheme cleanup  [here](https://apple.stackexchange.com/questions/143147/how-to-remove-removed-apps-os-x-url-schemes-from-system)
			- **Caveat :** Launching or updating the ChatGPT app re-registers the link; repeat the command when needed.
		- ### 4. Use a Browser-Picker Utility (persistent, reversible, paid 💰) - [[Velja]]
			- Install **Velja** (<https://sindresorhus.com/velja>).
			- In **Velja › Rules**:
			  1. Add **URL Matcher** → `chatgpt.com/*`
			  2. Set **Open In** → your preferred browser.
			- Velja intercepts the Universal Link and forces it into the browser every time.
	- ## Troubleshooting
		- **Link still opens the app after Option 3**
			- The app re-registered itself. Re-run the `lsregister -u` command or move to Option 4.
		- **Velja shows a prompt each click**
			- In **Velja › Advanced** disable **“Show prompt unless a rule matches.”**
		- **You rely on the ⌥ Space desktop shortcut**
			- Keep the app installed and use Option 4; Velja only overrides links, not the global hot-key.
	- ## References
		- Michael Tsai, “Disabling Universal Links,” 19 Apr 2022.
		- *Ask Different*: “How to remove removed apps OS X URL schemes from system?” (explains `lsregister -u`).
		- Velja — Powerful browser picker for macOS.