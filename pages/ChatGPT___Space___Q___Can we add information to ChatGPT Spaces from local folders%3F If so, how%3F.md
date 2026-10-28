logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[ChatGPT/Page]]

- # Can we add information to [[ChatGPT/Space]]s from local folders? If so, how?
	- ## [[AI Answer]]
		- **Short answer:** Not as a folder. Space takes uploaded files and files from connected apps; neither OpenAI article on Space mentions uploading, syncing, or linking a folder on your computer. You can get a local folder's contents into a Space by uploading its files or by having ChatGPT write them onto a page.
		- [[Answer/Official]] from [Getting started with Space in ChatGPT](https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt) and [ChatGPT Space](https://learn.chatgpt.com/docs/space)
			- Space holds pages, uploaded files, and folders. Those folders are Space's own organizing folders, not folders on disk.
			- Files reach a page in two ways. An uploaded file follows the page's permissions. A file in a connected service, such as Google Drive, keeps that service's permissions, and a link to it does not let page readers open it.
			- The documented way to fill a page from material you have is to open a conversation, attach the files, and ask ChatGPT to create or update a page from them.
		- Ways to get a local folder in
			- **Upload the files.** Select the files inside the folder and attach them to a page or to a chat that creates the page. A third-party page, [fast.io on upload limits](https://fast.io/resources/chatgpt-file-upload-limit/), reports no folder upload in ChatGPT and a cap of 80 files every 3 hours; neither claim is confirmed by OpenAI.
			- **Sync the folder to a connected service.** Put the folder in Google Drive or another service ChatGPT connects to, then link or cite those files from a page. Edits on disk reach Space only through the sync, and readers need access in the source service.
			- **Use a desktop local project as the bridge.** A local project in the [[ChatGPT/App/Desktop]] gives its chats read and write access to folders on your computer, per [Projects and chats](https://learn.chatgpt.com/docs/projects). Ask a chat in that project to read the folder and write a page into a named space. Neither article says a local-project chat can create Space pages, so this route is untested.
		- Not verified
			- Whether a chat in a local project can write into Space.
			- Whether Space's upload dialog accepts a whole folder in the desktop app. Check it by dragging a folder onto a page.
