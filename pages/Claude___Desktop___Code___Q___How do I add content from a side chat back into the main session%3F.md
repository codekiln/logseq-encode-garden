tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/How do I add content from a side chat back into the main session?
see-also:: [[Claude/Desktop/Code/Q/What does the Side chat feature do?]]

- # How do I add content from a [[Claude/Desktop/Code]] side chat back into the main session?
	- ## [[AI Answer]]
		- **Short answer:** There's no built-in "merge" or "promote" button — a side chat is intentionally one-way (it can read the main thread, but nothing inside it writes back). If you want to keep something it produced, copy the relevant text yourself and paste it into the main session's prompt box, then close the side chat.
		- **Why there's no automatic merge:** The [official docs](https://code.claude.com/docs/en/desktop#ask-a-side-question-without-derailing-the-session) describe the feature as explicitly not adding anything back to the main conversation — that's the point of it (avoid steering the main session off course).
		- **Requests for a real merge-back exist but aren't shipped:** [Issue #10370 — "Chat Branching: Spawn side-chain conversations with selective merging back to main"](https://github.com/anthropics/claude-code/issues/10370) proposed `/merge-to-main` / `/merge "<summary>"` commands for exactly this workflow. It gathered supportive comments through early 2026 but was auto-closed for inactivity without being implemented, so manual copy-paste remains the only path today.
		- **Practical workaround:** Select and copy the useful part of the side chat's response, paste it into the main thread as your own message (optionally with a short "from the side chat:" framing), then close the side chat. This is the same "manual copy-paste" option the feature request itself lists as the current alternative.
