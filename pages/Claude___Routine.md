tags:: [[Claude/Code]], [[Diataxis/Explanation]], [[AI/Automation]]
alias:: [[Claude Routines]]
see-also:: [[Claude/Code]], [[Claude/Code/Subagent]], [[Claude/Code/Skill]]
title:: Claude/Routine

- # [Automate work with routines (Claude Code)](https://code.claude.com/docs/en/routines)
	- ## Overview
		- **Routines** are saved **Claude Code** configurations—prompt, repositories, cloud environment, and connectors—packaged to run **unattended** on **Anthropic-managed cloud infrastructure** (Claude Code on the web).
		- A routine is a **template for repeated agent work**: define what Claude should do once, then start runs on a **schedule**, via **HTTP API**, or from **GitHub** repository events.
		- Each successful trigger creates a **new cloud session** (with a session URL); runs do not require an open local terminal or laptop.
		- Product status (as of research preview, announced **2026-04-14**): behavior, limits, and API shapes may change; see [Trigger a routine via API](https://platform.claude.com/docs/en/api/claude-code/routines-fire) for the experimental `/fire` surface.
	- ## Context
		- Interactive Claude Code sessions excel when a human is in the loop—approving edits, steering prompts, and closing the laptop ends the work.
		- Routines move the **execution layer** to the cloud: the same agentic capabilities (shell, repo clone, MCP connectors, skills in the cloned repo) run **without permission prompts** and **without** waiting for a local session.
		- Typical fits: recurring hygiene (backlog grooming, doc drift), **event-driven** reactions (PR opened, release published), and **pipeline- or alert-driven** kicks (CI failure, monitoring webhook) where the caller passes context in the API body.
		- Management surfaces: [claude.ai/code/routines](https://claude.ai/code/routines) (web), **Desktop** app (Remote routine), CLI **`/schedule`** (schedules only; API and GitHub triggers are configured on the web).
		- Availability: **Pro, Max, Team, and Enterprise** plans with Claude Code on the web enabled; Team/Enterprise admins can disable routines org-wide.
	- ## Key principles
		- **Define once, trigger many ways**: one routine can combine **schedule**, **API**, and **GitHub** triggers; the same prompt and repo scope apply to every run.
		- **Self-contained prompts**: runs are autonomous—no approval UI—so the saved prompt must state goals, constraints, and what “done” looks like without relying on mid-run human input.
		- **Scope follows configuration**: what a routine can reach is bounded by selected **repositories** (and branch-push rules), the **cloud environment** (network, env vars, setup script), and **connectors** included on the routine—not by a separate permission mode.
		- **Account-scoped, not team-shared**: routines belong to the individual **claude.ai** account; commits and connector actions appear as that user. Teammates do not share routine definitions (as of research preview).
		- **Not the Claude Platform API**: API triggers use a **per-routine bearer token** (`sk-ant-oat01-...`) and path `/v1/claude_code/routines/.../fire`, billed against **Claude Code subscription** usage—not Console `x-api-key` Platform billing.
	- ## Mechanism
		- ### What is saved in a routine
			- **Instructions** (prompt), with a per-routine **model** choice applied on every run.
			- **Repositories**: one or more GitHub repos cloned each run; default branch unless the prompt says otherwise; changes usually on `claude/`-prefixed branches unless **Allow unrestricted branch pushes** is enabled per repo.
			- **Environment**: network access level (e.g. Default “Trusted” allowlist vs custom domains vs full), **environment variables** (secrets), and optional **setup script** (cached across runs).
			- **Connectors**: MCP integrations from the claude.ai account (not CLI-only `claude mcp add` local servers unless also added as cloud connectors or committed `.mcp.json` in the repo).
			- **Triggers**: zero or more of schedule, API, GitHub event (see below).
		- ### Trigger types
			- **Schedule**
				- Recurring presets (hourly, daily, weekdays, weekly) or **one-off** at a future timestamp; wall-clock times use the creator’s local zone.
				- CLI **`/schedule`** (and natural-language variants) creates and updates scheduled routines; custom cron via **`/schedule update`** (minimum interval one hour).
				- One-off scheduled runs **do not** count against the daily routine-run cap (they still consume normal subscription usage).
			- **API**
				- After saving a routine, add an **API** trigger in the web UI to obtain the **fire URL** and a **one-time-shown** bearer token.
				- `POST` to `https://api.anthropic.com/v1/claude_code/routines/{routine_id}/fire` with header `anthropic-beta: experimental-cc-routine-2026-04-01`; optional JSON body field **`text`** (up to 65,536 characters) prepended as run context (literal string, not parsed structured JSON).
				- Response returns `claude_code_session_id` and `claude_code_session_url`; the HTTP call returns when the session is **created**, not when work finishes.
				- **No idempotency**: retries create **multiple** sessions.
			- **GitHub (webhook-style)**
				- Requires the **Claude GitHub App** on the repo (`/web-setup` alone does **not** enable webhook delivery).
				- Supported event families (research preview): **pull request** (many actions) and **release**; optional filters (author, branches, labels, draft/merged, regex on title/body, etc.).
				- Each matching event → **one new session** (no session reuse across events); hourly caps may drop excess events during preview.
		- ### Run lifecycle
			- Trigger fires → cloud session starts → clone repos → run prompt with connectors/tools → user may open session URL to review transcript, open PR, or continue chat.
			- **Run now** on the routine detail page starts immediately regardless of schedule.
			- Green status in the run list means **no infrastructure error**, not guaranteed task success—outcomes live in the session transcript.
		- ### Usage and limits
			- Routine **starts** count toward a **per-account daily cap** (plan-dependent; shown at claude.ai/code/routines); session work also draws **Claude Code subscription** usage like interactive sessions.
			- Hitting limits yields `429` on API fire with `Retry-After`; orgs with usage credits may continue on metered overage.
	- ## Examples
		- **Nightly backlog grooming**: schedule trigger + issue-tracker connector; label, assign, Slack summary.
		- **Alert triage**: monitoring tool `POST`s to `/fire` with Sentry body in `text`; routine correlates commits and opens a draft fix PR.
		- **PR review checklist**: GitHub trigger on `pull_request.opened` with filters (e.g. non-draft, `main` base); inline comments for security/style.
		- **Post-deploy smoke check**: CD pipeline calls `/fire` after production deploy with deploy metadata in `text`.
		- **Cross-routine chaining**: routines cannot nest triggers directly; one routine may `POST` another routine’s `/fire` endpoint using that routine’s token.
	- ## Misconceptions
		- **“Routines are the same as `/loop` or local Desktop schedules.”**
			- **`/loop`** schedules work **inside an open CLI session** on the local machine. **Desktop → Local** scheduled tasks run on the **user’s machine**. **Routines** are **remote cloud** sessions at claude.ai.
		- **“`/schedule` configures API and GitHub triggers.”**
			- CLI **`/schedule`** handles **scheduled** routines only; API tokens and GitHub triggers are added in the **web** editor.
		- **“The fire endpoint uses my Anthropic API key.”**
			- It uses a **per-routine OAuth-style token** from the routines UI, not Console API keys; it is **not** in Anthropic SDKs.
		- **“One failed GitHub event retries into the same session.”**
			- Each event creates a **new** session; webhook retries from external systems can duplicate runs if they hit `/fire` or duplicate deliveries.
		- **“Green run status means the task succeeded.”**
			- It only indicates the session infrastructure started cleanly; verify results in the session transcript and any PRs/commits.
	- ## Contrasts (when to use what)
		- | Need | Prefer |
		  |------|--------|
		  | Local files, no cloud | Desktop Local schedule or interactive CLI |
		  | Recurring reminder inside current chat | `/loop` in an open CLI session |
		  | Unattended cloud agent on timer, webhook, or repo event | Routine (cloud) |
		  | CI on GitHub Actions with repo checkout | GitHub Actions + Claude Action, or routine `/fire` from the workflow |
	- ## Footnotes
		- [^1]: https://code.claude.com/docs/en/routines
		- [^2]: https://platform.claude.com/docs/en/api/claude-code/routines-fire
