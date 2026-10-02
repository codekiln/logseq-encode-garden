logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tuicr/Wishlist]]

- # In [[tuicr]], how can I reply to a PR comment?
	- ## [[AI Answer]]
		- **Short answer:** tuicr cannot reply to an existing PR comment thread. Remote threads are read-only. The closest substitute is a new comment on the same line, which `:submit` posts as a separate thread, not a reply.
		- **What the source says**
			- Remote threads render inline as read-only rows. The code comment on `RemoteThreadLine` says the cursor "cannot edit or reply to these in v1" (`src/app/mod.rs`).
			- The module that fetches forge comments states the design: remote comments are source-of-truth-on-remote, and tuicr never mutates, replies to, or persists them (`src/forge/remote_comments.rs`). Its `in_reply_to` field exists only to group fetched replies under their parent for display.
			- `docs/GERRIT.md` lists it as a known limitation: "Replying to a thread. Existing comments are read-only in tuicr, as on every other forge."
		- **Workarounds**
			- Reply on the forge's web UI, then press `e` to reload the PR in tuicr.
			- Add a new line comment on the same line in tuicr and run `:submit`. The comment lands on that line as part of the review, next to the existing thread. It is unverified whether GitHub attaches it to the thread; the code never sets a parent comment id.
			- Use the review-level comment, which becomes the review summary, to address the thread in prose.
		- **Related**
			- `:comments all`, `:comments unresolved` and `:comments hide` control which remote threads show (`docs/KEYBINDINGS.md`).
			- Upstream feature idea: replying in place. Not in [[tuicr/Wishlist]] yet.
		- Source: local clone `github.com/agavra/tuicr` at commit `1eb979f`, installed 0.27.0. Not tested against a live PR.
