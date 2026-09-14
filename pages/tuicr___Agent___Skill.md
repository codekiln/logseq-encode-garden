tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[tuicr/Comment/Type]], [[tuicr]], [[tuicr/Q/In tuicr, is the --username on an agent comment tied to a GitHub or forge account, how does tuicr distinguish AI from human comments, and can a whole conversation happen offline before :submit?]]

- # [[tuicr]] [[Agent/Skills]]
	- ## Overview
		- The agent skill ([skills/tuicr/SKILL.md](https://github.com/agavra/tuicr/blob/main/skills/tuicr/SKILL.md) in [agavra/tuicr](https://github.com/agavra/tuicr)) is a packaged Claude/agent-tool skill that lets a coding agent talk to `tuicr review` — the non-interactive CLI side of tuicr — instead of the human-facing TUI.
		- Design line from the skill file itself: **"the TUI is where the human reviews code; the CLI is how the agent discovers active sessions, reads user comments, and, only when appropriate, adds agent-authored comments."**
		- Video coverage: ((6aa57707-6afe-46ec-bf96-766804d117dc)) in [[Person/Omer Hamerman/YouTube/26/07/The Holy Grail of Code Review TUIs]] — install via the packaged `pi-tuicr` skill rather than reinventing it; inline agent comments beat a generic AI summary.
	- ## Context
		- Two distinct workflows the skill is designed to pick between, before doing anything:
			- **User-led review of agent-generated changes** — the agent only *reads* the human's comments (`tuicr review comments`), polling on demand; it must not add its own comments and must never write comments that impersonate the user.
			- **Agent review of an AI-generated patch** — the agent inspects the diff itself and *adds* findings with `tuicr review add`, tagged with an explicit `--username` so they're visually distinguishable from the human's, only after the user approves writing them in.
		- If the workflow is ambiguous, the skill's instructions say to ask the user rather than guess.
	- ## Key Principles
		- **Session-scoped, not repo-scoped.** Every read/write targets one persisted review session (a local worktree/commit-range session or a PR session), resolved by slug via `tuicr review list`.
		- **Pull, not push.** There is no event stream from tuicr to the agent — comments are read by polling `tuicr review comments` on demand (roughly every 30s while actively waiting), not pushed to the agent as they're typed.
		- **Comments before submit are just session-file rows.** Both a human's and an agent's comments live as local draft entries in the same session JSON until a human runs `:submit` in the TUI; nothing reaches the forge (GitHub/GitLab/etc.) until then.
		- **Launching a pane vs. touching data are separate capabilities.** The skill can also *start* an interactive `tuicr` pane (via `tuicr-wrapper-{cmux,tmux,zellij,herdr}.sh`) for the human to review in, which is orthogonal to reading/adding comments through the CLI.
	- ## Mechanism
	  id:: 6aa7d15c-5c06-4684-8c13-e1018ecc3acf
		- **Adding a comment.** `tuicr review add --session <slug> --target-file ... --line ... --type issue --username "Codex" "..."` writes a local-draft comment (line, range, file, or review-level) into the session file; it shows up in the human's TUI (colorcoded, in the file tree) the next time they look, and in later `tuicr review comments` output with `lifecycle_state: local_draft` and the agent's `author`.
		- **Reading comments.** `tuicr review comments --session <slug>` returns every comment (human- or agent-authored) as JSON with `id`, `location`, `comment_type`, `author`, `lifecycle_state`, and `content` — this is the primary loop for the user-led workflow.
		- **No reply/thread primitive.** Comments are flat rows tied to a location, not a thread; adding a second comment at the same spot does not attach it to the first. For **remote** forge threads (GitHub/GitLab/Gitea/Bitbucket/Azure DevOps/Gerrit), tuicr fetches and displays existing comments but treats them as **read-only** for everyone, human or agent — the Gerrit docs state this explicitly ("existing comments are read-only in tuicr, as on every other forge").
		- **No submit path in the CLI.** `tuicr review` exposes `list`, `comments`, and `add` — nothing that pushes to a forge. `:submit` lives only in the interactive TUI and stays a human action.
		- **No fallback without a session.** Per the skill's own instructions, an agent should not silently review "locally only" when no *active* tuicr session exists — it should tell the user it's waiting, or start a new pane itself when a supported multiplexer (cmux/tmux/Zellij/Herdr) is available.
	- ## Examples
		- Agent polls `tuicr review comments` every ~30s while the human reviews in the TUI, then summarizes the human's `issue`/`suggestion` comments once `tuicr-summary:` reports `reviewed_count == file_count`.
		- Agent runs `tuicr review add --type suggestion --username "Codex" --target-file src/main.rs --line 42 "Consider handling the empty case."` after being asked to critique its own patch — the human then sees and can edit/delete that comment in the TUI before deciding to `:submit`.
	- ## Misconceptions (what it is **not**)
		- **Not a replacement for `:submit`.** The skill never pushes a review to a forge; a human still has to run `:submit` in the interactive TUI.
		- **Not real-time.** There's no push notification when a comment is added — the agent (or a human waiting on the agent) has to poll.
		- **Not a way to reply to existing forge comments.** Existing remote comments are read-only in tuicr regardless of who's asking; the skill can only add new, separate comments at the same location, never append to a thread.
		- **Not license to impersonate the user.** In the user-led workflow the agent's job is strictly read-only — the skill explicitly forbids adding or faking comments as if they were the user's.