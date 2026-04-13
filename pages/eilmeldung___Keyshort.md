- [[Keyshort]] [[eilmeldung]] [[eilmeldung/Keyshort]]
	- Source: [eilmeldung keybindings](https://github.com/christo-auer/eilmeldung/blob/main/docs/keybindings.md)
	- **Toggle zen mode** #card
	  card-last-interval:: 4
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2026-04-16T08:21:11.861Z
	  card-last-reviewed:: 2026-04-12T08:21:11.861Z
	  card-last-score:: 3
		- Shortcut: `z`
		- Context: Reading / article view
		- Description: Toggle distraction-free mode, hiding all panels except the article content.
	- Opening links in articles with hints
		- Source: [Opening links in articles with hints](https://github.com/christo-auer/eilmeldung/blob/main/docs/keybindings.md#opening-links-in-articles-with-hints)
		- **Open a hinted article link in the browser** #card
		  card-last-interval:: -1
		  card-repeats:: 1
		  card-ease-factor:: 2.5
		  card-next-schedule:: 2026-04-13T04:00:00.000Z
		  card-last-reviewed:: 2026-04-12T08:22:31.460Z
		  card-last-score:: 1
			- Shortcut: `; ;`
			- Context: Article content with visible link hints
			- Description: Opens the hinted link in the web browser after you enter the hint code.
			- [[My Note]]
				- hints here are little pop-ups with a two character activation code like `A E`
		- **Share the URL for a hinted article link** #card
		  card-last-interval:: -1
		  card-repeats:: 1
		  card-ease-factor:: 2.5
		  card-next-schedule:: 2026-04-13T04:00:00.000Z
		  card-last-reviewed:: 2026-04-12T08:47:34.456Z
		  card-last-score:: 1
			- Shortcut: `; s`
			- Context: Article content with visible link hints
			- Description: Shares the hinted link URL by first choosing a share target and then entering the hint code.
			- [[My Note]]
				- `;` is the `hint` leader. in eilmeldung, `hints` are pop-ups like `A E` that appear next to links
				- `; s` is memorable because you take the hint next to the link and you ==s==hare it.
				- the only thing is that what this really means is: put it in the [[Clipboard]] it's about copy paste.
		- **Copy the URL for a hinted article link** #card
			- Shortcut: `; y`
			- Context: Article content with visible link hints
			- Description: Copies the hinted link URL to the clipboard after you enter the hint code.