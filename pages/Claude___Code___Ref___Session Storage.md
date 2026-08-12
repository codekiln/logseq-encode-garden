tags:: [[Diataxis/Reference]]
see-also:: [[Claude/Code/Session/ID]], [[Claude/Code/--resume]], [[Claude/Code/--continue]], [[Claude/Code/Q/If I rename a CLI session with /rename, can I resume it in Claude Desktop's Code tab?]]

- # Claude Code CLI Session Storage
	- ## Overview
		- Where the [[Claude/Code]] CLI keeps conversation state on disk. Everything lives under `~/.claude`, split across two stores with different jobs: a registry of *running* sessions keyed by process id, and an append-only transcript per session keyed by session id.
		- Observed on Claude Code `2.1.226`. None of these paths or record shapes are part of the documented interface; they change between releases.
	- ## Layout
		- | Path                                               | Holds                                         |
		  | -------------------------------------------------- | --------------------------------------------- |
		  | `~/.claude/sessions/<pid>.json`                    | Live registry — one file per running process  |
		  | `~/.claude/projects/<cwd-slug>/<session-id>.jsonl` | Conversation transcript  |
		  | `~/.claude/projects/<cwd-slug>/<session-id>/`      | Spilled tool output for that session          |
		  | `~/.claude/projects/<cwd-slug>/memory/`            | Memory files scoped to that working directory |
		  | `~/.claude/history.jsonl`                          | Submitted prompts, across all projects        |
		  | `~/.claude/file-history/<session-id>/`             | Versioned copies of files a session edited    |
		  | `~/.claude/tasks/<session-id>/`                    | Task records, one JSON file per task          |
		  | `~/.claude/shell-snapshots/`                       | Captured shell environments                   |
	- ## Live session registry
		- `~/.claude/sessions/<pid>.json` — one JSON object per running process, the filename being the OS process id.
		- Fields: `pid`, `sessionId`, `cwd`, `startedAt`, `procStart`, `version`, `peerProtocol`, `kind`, `entrypoint`, `tmux`, `messagingSocketPath`, `name`, `nameSource`, `status`, `updatedAt`, `statusUpdatedAt`.
		- Observed values: `kind` `interactive`; `entrypoint` `cli` or `claude-desktop`; `status` `idle` or `busy`; `nameSource` `derived` for an auto-generated name (absent when the name was set explicitly).
		- The `status` fields plus `messagingSocketPath` make this a presence and discovery table for live processes — what backs cross-session listing, messaging, and the status indicator.
		- Process ids are reused after a process exits, so the registry cannot address past sessions and is not what resume reads.
	- ## Transcript
		- `~/.claude/projects/<cwd-slug>/<session-id>.jsonl` is the record of a conversation. The directory name is the session's working directory with `/` and `.` replaced by `-`; the filename is the session id, a uuid — see [[Claude/Code/Session/ID]].
		- Siblings in the same project directory: `<session-id>/tool-results/*.txt` for tool output too large to inline, and `memory/` for the project's memory files.
		- One JSON object per line, appended in order. Every record carries `type` and `sessionId`. Conversation records use type `user` and `assistant`; the rest carry session metadata — observed types include `mode`, `last-prompt`, `attachment`, `file-history-snapshot`, `queue-operation`, and `system`.
		- ### Name and title records
			- | `type`         | Payload key   | Holds                                          |
			  | -------------- | ------------- | ---------------------------------------------- |
			  | `ai-title`     | `aiTitle`     | Display title generated from the conversation  |
			  | `custom-title` | `customTitle` | Display title set with `/rename`               |
			  | `agent-name`   | `agentName`   | Addressable handle for cross-session messaging |
			- Each is a standalone record whose only keys are `type`, `sessionId`, and its payload key — no nesting inside a message.
			- The log is append-only, so a name change appends a fresh record rather than rewriting a header. A transcript therefore accumulates many such records over a session and the last one wins, which is why a mid-session rename appears in the resume picker with no other file touched. A name set explicitly can appear as both a `custom-title` and an `agent-name` record carrying the same string.
			- The name-to-session binding lives inside the transcript, so it travels with the file rather than with a process or an index. That `--resume` resolves names from these records is not documented; it is consistent with the binding sitting in the same files a resume listing must enumerate.
	- ## Prompt history
		- `~/.claude/history.jsonl` — one record per submitted prompt, with keys `display`, `project`, `timestamp`, `pastedContents`. It backs prompt recall in the input line. It is not a conversation transcript: it holds no assistant output and no session id.
	- ## Session-keyed side stores
		- `~/.claude/file-history/<session-id>/<content-hash>@v<n>` — successive versions of each file a session edited.
		- `~/.claude/tasks/<session-id>/<n>.json` — one file per task, numbered in creation order.
		- `~/.claude/shell-snapshots/` — captured shell state, named by shell, epoch milliseconds, and a random suffix; not keyed by session.