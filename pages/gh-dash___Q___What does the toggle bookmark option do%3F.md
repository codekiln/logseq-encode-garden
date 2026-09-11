logseq-entity:: [[Logseq/Entity/Question]]

- # In [[gh-dash]], what does the toggle bookmark option do?
	- ## [[AI Answer]]
		- **Short answer:** `Toggle Bookmark` (key `b`) is a **Notifications-view-only** feature — it is not on the PR page. It flags/unflags a notification so it persists across "mark all as read" and unread filters, letting you keep a notification visible until you deliberately deal with it.
		- ### Where it lives
			- Defined as `NotificationKeys.ToggleBookmark` (`internal/tui/keys/notificationKeys.go`), bound to `b`, help text `"toggle bookmark"`.
			- Wired only in `internal/tui/components/notificationssection/notificationssection.go`; the PR section has no such binding.
			- A dedicated test (`TestFullHelpForPRViewDoesNotIncludeNotificationKeys` in `internal/tui/keys/keys_test.go`) asserts `"toggle bookmark"` must **not** appear in the PR view's help — so seeing it on a PR page would indicate a config/version mismatch rather than intended behavior.
		- ### What it does under the hood
			- Backed by a `NotificationIDStore` singleton (`internal/data/bookmarks.go`) persisted to `bookmarks.json` under `$XDG_STATE_HOME/gh-dash` (or `~/.local/state/gh-dash`).
			- `ToggleBookmark(id)` flips membership of the notification's ID in that store; `IsBookmarked` / `GetBookmarkedIds` read it back.
			- The notifications section's default (unread) filter sets `IncludeBookmarked: true`, so bookmarked notifications keep showing even once marked read; explicit read/unread filters turn that auto-include off.
		- [[Answer/Official]] source is the [dlvhdr/gh-dash](https://github.com/dlvhdr/gh-dash) source itself (no public docs page found for this key at the time of writing); local clone: `$(ghq root)/github.com/dlvhdr/gh-dash`.