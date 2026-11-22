logseq-entity:: [[Logseq/Entity/Software/Feature]]

- # [ChatGPT desktop built-in browser](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)
	- A web browser inside [[ChatGPT/App/Desktop]] on macOS and Windows. The person and ChatGPT share one view of a website or local web app in a chat, and ChatGPT can click and type on the person's behalf.
	- ## Parts
		- **Own profile** — it keeps cookies, history and sign-ins apart from the person's regular browser. Settings > Browser manages that data and any profile import the device offers.
		- **Sign-in** — the person signs in directly on the website. OpenAI says to enter credentials in the browser, never in the chat.
		- **Passwords** — Settings > Passwords lists the passwords this browser has saved. See [[ChatGPT/App/Desktop/Browser/Password Manager]].
		- **Extensions** — Chrome extensions such as [[1Password]] can be installed in it.
		- **Admin policies** — organizations configure it with Chrome Enterprise policies delivered by MDM, Group Policy or a JSON file. OpenAI lists the 244 supported policies on its [desktop browser policies](https://learn.chatgpt.com/docs/enterprise/desktop-browser-policies) page.
	- ## Neighbors
		- [[ChatGPT/Cloud/Browser]] runs on a remote computer for [[ChatGPT/Work]] tasks and keeps none of the person's saved passwords.
		- The ChatGPT browser extension works inside the person's own Chrome profile, for tasks that need existing tabs, cookies or sign-ins.
	- ## Questions
		- [[ChatGPT/App/Desktop/Q/what is the expected, best-practices way I can use 1Password in the ChatGPT Desktop built-in browser safely without exposing my passwords to ChatGPT?]]
