see-also:: [[My/AI/Rule/Markdown/Single Line Paragraphs]], [[My/Pref/Writing/Use Plain language]]

- When AI drafts a [[Slack]] post, a [[JIRA]] comment, a [[GitHub]] comment or an email for me to send, the draft is plain markdown: paragraphs, bullets, links, and a fenced code block where code is the point. I have AI write these in a markdown document so that I can copy them out and paste them where they are going.
- The paste is why the shape matters. Out of [[Obsidian]] I copy the rendered page and paste it into Jira as rich text, and I paste the raw markdown into Slack, which reads its own simplified markdown. A block quote costs me an edit on both trips: in Jira it arrives as a quote of my own words, and in Slack I strip the `>` off every line by hand. [[Logseq/Bug/Cannot Copy Block with Block Quote of Numbered List]] is the same trouble inside Logseq.
- A block quote belongs in a draft when I am quoting someone else in the message I am about to send — a line from the ticket I am answering, something a colleague wrote, terminal output I want set apart. There the `>` carries the meaning, and I want it.
- When a line in a draft needs to stand out, bold it, give it its own bullet, or make it a heading.
	- [[Example]]
		- Avoid, my own words inside a block quote in a draft Jira comment:
			- > Deployed to dev at 0930 and the syllabus builder returned assets for every course.
		- Prefer:
			- Deployed to dev at 0930 and the syllabus builder returned assets for every course.
		- Keep the quote when the words are someone else's and I am answering them:
			- The ticket asks:
			- > can we hold this until the release goes out?
			- Yes, it will wait for the fix version.
