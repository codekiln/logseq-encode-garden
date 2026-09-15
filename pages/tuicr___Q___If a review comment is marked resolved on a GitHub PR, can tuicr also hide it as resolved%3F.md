logseq-entity:: [[Logseq/Entity/Question]]

- # If a review comment is marked resolved on a [[GitHub]] PR, can [[tuicr]] also hide it as resolved?
	- ## [[AI Answer]]
		- **Short answer:** yes — `:comments unresolved` is the **default** remote-comment mode and already hides threads GitHub reports as resolved; you don't need a separate action to hide them.
		- tuicr exposes three remote-comment visibility modes via the `:comments` command:
			- `:comments unresolved` — show unresolved remote comments (PR mode, default).
			- `:comments all` — show every remote comment, including resolved and outdated ones.
			- `:comments hide` — hide remote comments entirely in PR mode.
		- The resolved/unresolved state itself comes from the forge (GitHub, GitLab, Gerrit, etc.), not from tuicr — tuicr just filters on whatever the API reports. Resolving a thread on GitHub.com (or the equivalent action on another forge) is what changes the state; tuicr reflects it once it has fetched the threads for the current head commit.
		- **Caveat on Gitea specifically:** `:comments unresolved` still hides resolved threads there, but Gitea's API doesn't expose whether a force-push made a thread outdated, so tuicr shows every existing thread as current regardless.
		- To pick up a resolution made after you opened the PR in tuicr, reload (`:e` / `:reload`, keyshort `e`): a same-head reload keeps the session but doesn't always refetch remote threads, while a reload that detects a new head commit re-fetches PR threads for that head.
		- **No per-comment minimize/expand toggle:** resolved status controls visibility (via `:comments` mode) and styling only. Under `:comments all`, a resolved thread still renders fully expanded — dimmed and carrying a `resolved` badge — rather than folding to a single collapsed line; there's no fold/unfold action for an individual thread keyed on its resolved state. tuicr does have a separate collapse mechanic for *marking a hunk as read* ([[tuicr/Q/In tuicr, how can I mark a hunk as read, rather than a whole file?]]), but that's independent of GitHub's comment-resolved status.
		- Source: [KEYBINDINGS.md on GitHub](https://github.com/agavra/tuicr/blob/main/docs/KEYBINDINGS.md) ("`:comments unresolved`" / "`:comments all`" rows) and [GITEA.md on GitHub](https://github.com/agavra/tuicr/blob/main/docs/GITEA.md) ("Outdated threads are not marked" limitation); confirmed by reading `src/handler.rs` (`reload_review`), `src/app/pr.rs` (`reload_pull_request_with_backend`), and `src/ui/comment_panel.rs` (`format_remote_thread_lines`, the resolved-badge/muted-palette rendering with no fold state) in the local `agavra/tuicr` clone.
