logseq-entity:: [[Logseq/Entity/Software/Feature]]
see-also:: [[Password Management]], [[Credential/Manage/ment]]

- # [ChatGPT desktop browser password manager](https://learn.chatgpt.com/docs/enterprise/desktop-browser-policies)
	- The password store of [[ChatGPT/App/Desktop/Browser]]. When the person signs in to a website in the built-in browser, the browser can save that username and password and fill it in next time. Settings > Passwords, under Integrations, lists what it has saved, with a search box and a Refresh button.
	- An empty list ("Saved passwords (0)") means the built-in browser has not saved any passwords. That is expected when sign-ins go through [[1Password]] or happen elsewhere.
	- ## What OpenAI documents
		- The [built-in browser help article](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app) says the browser supports "richer sign-in, autofill, password management, extensions, downloads, and navigation."
		- The [desktop browser policies](https://learn.chatgpt.com/docs/enterprise/desktop-browser-policies) page uses Chrome's policy names. Its example sets `PasswordManagerEnabled` to `false`, which "Prevents saving new passwords. Existing saved passwords are not deleted."
		- The same page lists `ImportSavedPasswords`, `PasswordLeakDetectionEnabled` and `PasswordManagerBlocklist` among the supported policies, so passwords can come in by profile import and the browser can check them against leaks.
		- As of 2026-11-22, OpenAI has no page about the Passwords settings pane itself.
	- ## What stays separate
		- Chrome's own saved passwords. The built-in browser has its own profile, so Chrome's passwords appear here only if the person imports them.
		- [[ChatGPT/Cloud/Browser]]. Its secure sign-in form sends credentials to the remote browser, and OpenAI says "ChatGPT does not store your username or passwords."
		- Passwords saved in ChatGPT Atlas, the retired Mac browser. OpenAI's [Atlas help](https://help.openai.com/en/articles/12628461-setting-up-the-atlas-browser) points those to a CSV export and Google Password Manager.
	- ## Open question
		- OpenAI does not say whether ChatGPT, while it controls the browser, can trigger autofill from this store. A report from [Runtime Wire](https://runtimewire.com/article/openai-chatgpt-desktop-browser-chrome-extensions) on 2026-09-18 says OpenAI states the agent cannot interact with extensions or their data, which covers 1Password but not this built-in store.
		- [[ChatGPT/App/Desktop/Q/what is the expected, best-practices way I can use 1Password in the ChatGPT Desktop built-in browser safely without exposing my passwords to ChatGPT?]] covers signing in with 1Password instead.
