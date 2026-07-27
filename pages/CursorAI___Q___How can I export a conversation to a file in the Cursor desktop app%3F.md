logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[CursorAI/CLI/Q/Does Cursor CLI have some kind of way to export the text of a session to a file?]], [[Claude/Code/How To/Export Conversation to File]]

- # How can I export a conversation to a file in the [[CursorAI]] desktop app, the way [[Claude/Code]] has `/export`?
	- ## [[AI Answer]]
		- **Short answer:** In [[CursorAI]] 3.x's Agents Window, right-click the conversation and choose **Copy ▸ Copy Transcript**, then paste into a `.md`. That is the closest match to `/export`. To have Cursor write the file itself, ask the agent, e.g. `save this conversation to notes.md`.
		- **Copy ▸ Copy Transcript** puts the whole conversation on the clipboard; paste it into a new file.
		- **Share** makes a read-only link for teammates and works only on Teams and Enterprise plans. It is a link rather than a saved file. See [Shared transcripts](https://cursor.com/help/ai-features/shared-transcripts).
		- **Bulk export** uses community tools that read Cursor's local chat storage: [cursor-chat-export](https://github.com/somogyijanos/cursor-chat-export), [cursor-history](https://github.com/S2thend/cursor-history), and [Cursor Chat Bulk Export](https://open-vsx.org/extension/AnasAbbasCode/cursor-chat-bulk-export).
		- Sources:
			- [Shared transcripts](https://cursor.com/help/ai-features/shared-transcripts) (Cursor Docs)
			- [Cursor 3.0 — New Interface](https://cursor.com/changelog/3-0) (changelog)
