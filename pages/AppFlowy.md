tags:: [[PKM/Tool]]

- # [AppFlowy](https://appflowy.com/)
	- ## About
		- **Type:** Open-source Notion alternative
		- **Website:** https://appflowy.com/
		- **Description:** Open source alternative to Notion with multiple pricing plans
	- ## Features
		- **Pricing:** Several pricing plans available
		- **Free tier:** Self-hosted 1-seat option available
			- [[Help] Self Hosted Configuration : r/AppFlowy](https://www.reddit.com/r/AppFlowy/comments/1ooh9px/comment/nn8ppel/)
				- It sounds like it's a relatively restricted configuration:
				- > Update: Just seen the ridiculous rules on self hosting limits. No need to reply. Will look elsewhere. Welcome to drop recommendations though 😊
		- **Private local RAG:** Features include private local Retrieval-Augmented Generation
	- ## Tech Stack
		- [AppFlowy, an open source alternative to Notion, can now be self-hosted : r/selfhosted](https://www.reddit.com/r/selfhosted/comments/169l5sy/appflowy_an_open_source_alternative_to_notion_can/)
			- Built with
				- [[Rust]]
				- [[Flutter]]
				- [[Supabase]]
			- Apparently requires [[XWindow]] to be deployed in [[Docker]]?
				- got a lot of flack in the thread for that,
					- > It seems like they are using X11 to make Flutter work on embedded systems. But that still doesn't answer the question: why the h*** would you expose this in a docker container. The web interface doesn't need one... I'll give it a go and just remove that X11 all together
					- > I don’t think I’ve had an open port to X since the 1990s. It was a great idea that didn’t work that well even back then.
					  Most Linux machines are running Wayland now. Why on Earth would you develop an X application?
					- > It’s self-hosted but is using supabase as a backend. Yes you can self-host supabase too, but this is just cringe, same as the fact that there is no web UI but an X-based app you can use via docker.
					  How hard is it to create a simple webapp that works in the browser and on mobile (preferable with an app for login).
			- People give them a lot of flack for using [[Flutter]]
				-
	- ## Related
		- [[Personal Knowledge Management]]
		- [[App/Notion]]