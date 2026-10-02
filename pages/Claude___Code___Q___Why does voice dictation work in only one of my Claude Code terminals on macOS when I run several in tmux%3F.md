logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[AI/Voice/to/Text]]

- # Why does voice dictation work in only one of my [[Claude/Code]] terminals on macOS when I run several in [[tmux]]?
	- Observed 2026-10-02: with Claude Code open in two terminal windows, voice works only in the most recently started one. Using voice in the newer one makes the older one fail with `No audio detected from microphone. Check that the correct input device is selected and that Claude Code has microphone access.`
	- ## [[AI Answer]]
		- **Short answer:** No report involving tmux turned up. The nearest match is a macOS bug in which voice dies in every session that was running before Claude Code replaced its own binary. That fits "only the newest session works" and has nothing to do with the terminal. It is not confirmed as your cause.
		- **Closest match:** [Issue #94687](https://github.com/anthropics/claude-code/issues/94687) (open, filed 2026-09-16), macOS 26.5.1 on Apple Silicon in Terminal.app
			- The same error appears in several parallel sessions, and only a fresh session fixes it. Toggling `/voice`, `/voice tap`, `/voice hold` or changing the input device does not.
			- Root cause from the unified log: a session's auto-updater reinstalls the package and replaces `claude.exe`. Every session started before the swap keeps running the deleted old image. On its next recording, `coreaudiod` asks `tccd.system` for that PID's microphone right, gets an empty reply, and denies input. The addon then receives silence and Claude Code reports "No audio detected".
			- A commenter adds that a stale session can re-trigger a reinstall of a version that is already on disk, which kills voice in a brand new session as well.
			- **Workaround from the issue:** set `"env": { "DISABLE_AUTOUPDATER": "1" }` in `~/.claude/settings.json`, update manually, then restart sessions.
		- **Other reports with the same error text** (none mention tmux)
			- [#38054](https://github.com/anthropics/claude-code/issues/38054) (closed as a duplicate) — works in some sessions and not others inside one VS Code window on macOS. A new session usually fixes it.
			- [#78169](https://github.com/anthropics/claude-code/issues/78169) — a session stays broken after its input device is invalidated mid-session, for example by closing the lid on Apple Silicon.
			- [#52845](https://github.com/anthropics/claude-code/issues/52845) — voice stops working after a long session.
			- [#34459](https://github.com/anthropics/claude-code/issues/34459) — hold-space stops responding in Warp on an Intel Mac; toggling `/voice` off and on fixes it.
		- **How this compares with your case**
			- Your symptom is order-dependent: the newest session wins and the older one breaks the moment the newer one records. #94687 explains older sessions failing, but not a failure triggered by using voice in the newer one. If both of your sessions started after the last update, #94687 does not apply.
			- Possible cause to check: whether two sessions can hold the microphone at once. No issue or documentation says either way.
		- **To narrow it down**
			- Run `claude --version` in both sessions. If they differ, or `~/.claude/.last-update-result.json` is newer than the older session, suspect #94687.
			- Test the same two-session pattern outside tmux, in two Terminal.app tabs. If it still fails, tmux is not the cause. As far as I can tell, `audio-capture.node` talks to CoreAudio directly, so tmux is unlikely to matter.
			- Disable the auto-updater and retry with two freshly started sessions.
		- Docs: [Voice dictation](https://code.claude.com/docs/en/voice-dictation)
