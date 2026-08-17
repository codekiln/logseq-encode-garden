logseq-entity:: [[Logseq/Entity/Question]]
- # What does "Create permanent [[git/worktree]]" do in [[Codex]]?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Worktrees](https://developers.openai.com/codex/app/worktrees)
			- **Short answer:** It creates a long-lived Git worktree for the selected repository and adds that worktree to the Codex sidebar as a separate project. Multiple chats can use the same permanent worktree, and Codex does not automatically delete it.
			- A worktree is another checkout of the repository: it has its own working files while sharing the repository's Git metadata. This lets work in that project proceed independently of the original checkout.
			- Ordinary Codex-managed worktrees are lightweight environments typically associated with one chat. Codex may delete them when their chat is archived or when it trims older managed worktrees.[^1] Permanent worktrees remain until they are removed explicitly, so they are useful when the checkout needs to be reused across chats or kept set up over time.
			- Each checkout can consume substantial disk space once it has its own dependencies and build caches. Git also permits a branch to be checked out in only one worktree at a time.
	- ## Footnotes
		- [^1]: https://learn.chatgpt.com/docs/environments/git-worktrees#worktree-cleanup
