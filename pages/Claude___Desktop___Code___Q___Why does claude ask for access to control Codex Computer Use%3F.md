tags:: [[Claude/Desktop]], [[Claude/Code]], [[Codex]], [[macOS]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/Why does claude ask for access to control Codex Computer Use?

- # Why does macOS say "claude" wants access to control "Codex Computer Use"?
	- ## The dialog
		- Seen on [[2026-10-30 Fri]] while several [[Claude/Desktop/Code]] sessions were running and the [[ChatGPT/App/Desktop]] was open.
		- Title: *"claude" wants access to control "Codex Computer Use"*. Body: allowing it gives access to documents and data in that app and lets claude act within it. Buttons: **Don't Allow** and **Allow**.
		- The line under it, *Claude Code needs to send Apple Events to open URLs and control applications you authorize*, is Claude Code's generic reason for Apple Events. It says nothing about this particular request.
	- ## [[AI Answer]]
		- **Short answer:** a Claude Code process sent macOS Apple Events to OpenAI's computer-use helper app, and macOS asks once for each pair of apps. Click **Don't Allow**. Claude Code never needs to control that app, and denying it breaks nothing.
		- **What "Codex Computer Use" is:** a helper app that the ChatGPT/Codex desktop app installs and launches for its own screen-control feature.
			- Path: `~/.codex/computer-use/Codex Computer Use.app`
			- Bundle id: `com.openai.sky.CUAService`
			- Process: `SkyComputerUseService`, started by the ChatGPT app, so it runs whenever ChatGPT is open.
		- **What "claude" is:** the `claude` binary of a Claude Code session started by [[Claude/Desktop]], at `~/Library/Application Support/Claude/claude-code/<version>/…/claude.app/Contents/MacOS/claude`. With several sessions open, the dialog doesn't say which one sent the events.
		- **Likely cause:** a session ran something that talks to running apps by name, such as an `osascript` script or a screen-control or app-listing tool, and the Codex helper was one of the apps it reached. The investigation on [[2026-10-30 Fri]] didn't find the exact command.
		- **Changing the answer later:** System Settings → Privacy & Security → Automation → claude → Codex Computer Use. To reset all Automation answers for claude and get asked again: `tccutil reset AppleEvents`. That resets every app, so check what else is listed first.
	- ## Finding the source next time
		- Check that the helper is running: `ps -axo pid,ppid,command | grep -i 'computer use'`. The parent pid is the ChatGPT app.
		- List the Claude Code sessions: `ps -axo pid,lstart,command | grep 'MacOS/claude '`.
		- Search the session transcripts under `~/.claude/projects/` for `osascript` or `tell application` near the time the dialog appeared.
