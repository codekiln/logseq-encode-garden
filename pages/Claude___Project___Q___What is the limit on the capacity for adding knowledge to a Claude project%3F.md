logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Project/Explanation/How the GitHub integration feeds project knowledge]]

- # What is the limit on the capacity for adding knowledge to a Claude project?
	- Prompted by adding two folders from GitHub to a project in Claude Enterprise and seeing 62% of capacity used.
	- ## [[AI Answer]]
		- **Short answer:** Anthropic publishes no fixed size, file count or token figure for project knowledge. The capacity meter is measured against the model's context window, and on paid plans (Pro, Max, Team, Enterprise) Claude switches the project to retrieval (RAG) mode as knowledge nears that limit, which expands capacity "up to 10x".
		- [[Answer/Official]] from [Retrieval augmented generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects).
			- RAG activates automatically when a project approaches or exceeds the context window limit, and a visual indicator shows the project is RAG-enabled.
			- The article gives no percentage at which RAG starts, no file limit, and says nothing about GitHub sources or Enterprise-specific behavior.
			- If knowledge later drops below the threshold, Claude can convert the project back to context-based processing.
			- In RAG mode Claude retrieves relevant passages with a project knowledge search tool instead of reading every file in each chat.
		- **What the other official pages add**
			- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) repeats that RAG expands capacity on paid plans, and gives no meter explanation, file size limit, file count, or behavior at 100%.
			- [Use the GitHub integration](https://support.claude.com/en/articles/10167454-use-the-github-integration) says multiple repositories can be added but must fit in Claude's context window, and advises selecting only the files central to the task. It describes only files on one branch, with no commit history or PRs.
		- **Reading the 62%**
			- Two folders reaching 62% fits the docs' picture: GitHub content is copied in as text, so a source tree spends context quickly. The percentage is a measure of what you selected, not of the repository's size.
			- Whether the meter keeps climbing, caps at 100%, or stops once RAG engages is not documented. Whether GitHub-sourced files are indexed for RAG the same way as uploaded files is also not documented.
		- **Design implications**
			- Narrow the file selection with the "Configure files" icon rather than adding whole folders.
			- Prefer several focused projects over one project holding every repository, since each project has its own capacity.
			- Treat a RAG-enabled project as search over your files, not full reading. Behavior that depends on Claude seeing every file, such as whole-repo review, needs the files to fit without RAG.
		- **Unverified:** the exact context window the meter uses for an Enterprise org, the point at which RAG starts, and the rules above for GitHub files. Testing them means adding a third folder and watching the indicator, which I have not done.
