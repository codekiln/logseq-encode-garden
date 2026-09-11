logseq-entity:: [[Logseq/Entity/Question]]

- # If I comment on a PR and exit [[tuicr]] without running `:submit`, is the comment still there next time I open the PR?
	- ## [[AI Answer]]
		- **Short answer:** yes — comments are written to disk immediately when saved, not held only in memory until `:submit`.
		- Each review session (including its `review_comments`, file comments, and line comments) is a `ReviewSession` struct persisted as JSON under the platform data dir at `tuicr/reviews/sessions/<hash>.json`, indexed by a manifest at `tuicr/reviews/index.json` (`src/persistence/storage.rs`).
		- `save_comment()` in `src/app/comments.rs` adds/edits the comment on `self.session`, then unconditionally calls `self.save_current_session_merging_external()` — this is an autosave that happens right after every comment add or edit, well before `:submit`.
		- `save_current_session_merging_external()` (`src/app/session.rs`) calls `storage::save_session_by_identity`, which writes the merged session to its JSON file on disk (merging any concurrent external changes to the same session file first).
		- New comments start life in `CommentLifecycleState::LocalDraft` (`src/model/comment.rs`) — this state only becomes `PushedDraft`/`Submitted` once `:submit` pushes them to GitHub. `LocalDraft` comments are still fully persisted locally; the lifecycle state governs whether they're locked/editable, not whether they're saved.
		- So exiting without `:submit` loses nothing: reopening the same PR reloads the session file from disk (`load_pr_session`) and the draft comment is still there, still editable, still unsubmitted.
		- Source: local clone `github.com/agavra/tuicr` at commit `2e8475c` (`src/app/comments.rs`, `src/app/session.rs`, `src/persistence/storage.rs`, `src/model/comment.rs`).
