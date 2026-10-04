logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[OpenAI]]
date-created:: [[2026]]
see-also:: [[OpenAI/Dev/Day/26]], [[ChatGPT/Plugin/Extension]]

- # [ChatGPT Sites](https://help.openai.com/en/articles/20001339-creating-and-using-chatgpt-sites)
	- A feature of ChatGPT that builds, hosts, and shares a website or small web app from a conversation. The user describes the site in chat and ChatGPT generates it and publishes it at a URL.
	- Launched 2026-07-09 on paid plans except Free and Go. It reached the UK, EEA, and Switzerland on 2026-07-20, per [Stacktree](https://stacktr.ee/chatgpt-sites-custom-domain).
	- Every deployment URL is a production URL; there is no staging environment, per [PlayCode](https://playcode.io/blog/chatgpt-sites-explained).
	- Runs on Cloudflare Workers with a D1 (SQLite) database; no Node.js servers, Postgres, WebSockets, or background jobs, per [PlayCode](https://playcode.io/blog/chatgpt-sites-explained).
	- Viewing is public or limited to signed-in invited users. There is no passcode option.
	- Questions
		- [[ChatGPT/Sites/Q/Can ChatGPT Sites be served from a custom domain?]]
