logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[OpenAI]]
date-created:: [[2026]]
see-also:: [[OpenAI/Dev/Day/26]], [[ChatGPT/Plugin/Extension]]

- # [ChatGPT Sites](https://learn.chatgpt.com/docs/sites)
	- A feature of ChatGPT that builds, hosts, and shares a website or small web app from a conversation. The user describes the site in chat and ChatGPT generates it and publishes it at a URL.
	- Launched 2026-07-09 on paid plans except Free and Go. It reached the UK, EEA, and Switzerland on 2026-07-20, per [Stacktree](https://stacktr.ee/chatgpt-sites-custom-domain).
	- Every deployment URL is a production URL; there is no staging environment, per [PlayCode](https://playcode.io/blog/chatgpt-sites-explained).
	- ## Data and connections
		- The official [Data and connections guide](https://learn.chatgpt.com/docs/sites/data-and-connections) recommends [[Cloudflare/D1]] for durable, structured site data such as saved records, user progress, or scores.
		- The guide recommends [[Cloudflare/R2]] for uploaded files such as images, documents, audio, and video. When uploaded files need searchable metadata, store metadata in D1 and file contents in R2.
		- Avoid persistent storage for temporary presentation choices, such as a selected theme or a dismissed banner; use it for product data a hosted site should remember.
		- Public sites can offer optional Sign in with ChatGPT. Authorization decisions belong in server-side code; the guide documents authenticated email and optional full-name request headers.
		- Workspace-private sites can use plugins to load connected-app data under each visitor's own connection and permissions. Sharing a site does not share the author's connected accounts.
	- Viewing is public or limited to signed-in invited users. There is no passcode option.
	- Questions
		- [[ChatGPT/Sites/Q/Can ChatGPT Sites be served from a custom domain?]]
		- [[ChatGPT/Sites/Q/To what extent is it possible, either using Claude artifacts or using ChatGPT sites, to have a database that backs the site?]]
