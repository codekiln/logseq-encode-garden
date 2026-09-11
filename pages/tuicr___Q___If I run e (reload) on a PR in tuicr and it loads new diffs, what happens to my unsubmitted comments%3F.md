logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tuicr/Q/If I comment on a PR and exit without running submit, is the comment still there next time I open the PR?]]

- # If I run `:e` (reload) on a PR in [[tuicr]] and it loads new diffs, what happens to my unsubmitted comments?
	- ## [[AI Answer]]
		- **Short answer:** it depends on whether the PR's head SHA actually changed. Same head → all unsubmitted comments are untouched. New head (new commits pushed) → review-level drafts always carry over; file/line drafts only carry over for files whose content didn't change.
		- `:e` and `:reload` both map to `CommandKind::Reload` → `reload_review()` (`src/handler.rs`). For a PR session this calls `spawn_pr_reload()` / `finish_pr_reload()` (`src/app/pr.rs`).
		- **Same head SHA (no new commits):** the "no new commits" branch just calls `self.session.add_diff_file(file)` per file, which only refreshes content hashes and prunes stale reviewed-hunk keys (`ReviewSession::add_diff_file` / `add_file` in `src/model/review.rs`). It never touches `review_comments`, `file_comments`, or `line_comments` — all unsubmitted comments survive as-is.
		- **Head SHA changed (new commits landed):** `opened_pr_with_new_head_session()` (`src/app/session.rs`) runs:
			- Autosaves the current session to disk first, so nothing is ever lost from disk even in this branch.
			- Loads (or creates) the session keyed to the *new* head SHA.
			- If creating fresh, `reviewed_state_carried_forward()` carries forward unlocked (`LocalDraft`, i.e. unsubmitted) **review-level** comments unconditionally.
			- **File-level and line-level** unsubmitted comments carry forward only when `file_review_carried_forward()` finds the file's `content_hash` unchanged between old and new head; if the file's content changed, that file's draft comments are dropped from the new active session view (old line numbers may no longer line up).
			- Dropped file/line drafts aren't destroyed outright — they still exist in the old head's on-disk session JSON (`tuicr/reviews/sessions/<hash>.json`) since that session was autosaved before switching; they're just no longer part of the active review for the new head.
		- Source: local clone `github.com/agavra/tuicr` at commit `2e8475c` (`src/handler.rs`, `src/app/pr.rs`, `src/app/session.rs`, `src/model/review.rs`).
