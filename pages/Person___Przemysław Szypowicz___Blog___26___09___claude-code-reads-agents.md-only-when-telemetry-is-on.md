logseq-entity:: [[Logseq/Entity/Article/Blog]]
created-by:: [[Person/Przemysław Szypowicz]]
date-created:: [[2026-09-23 Wed]]

- # [Claude Code reads AGENTS.md only when telemetry is on](https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/)
	- ## Summary
		- [[Claude Code]] 2.1.277 announced [[AI/Coding/Agents.md]] support, but the loader ships as a built-in plugin gated on a remote feature flag. With telemetry or nonessential traffic disabled, a local `AGENTS.md` is skipped and nothing says so.
		- The author measured the behavior against [Issue #95690](https://github.com/anthropics/claude-code/issues/95690) and posted his results there before collecting them here.
	- ## Notes
		- ### Where the gate sits
			- The loader is a built-in plugin named `agents-md`. In the 2.1.280 bundle its `isOnByDefault` is `false`, and `isAvailable` asks a remote flag `tengu_agents_md_mod` with `false` as the fallback. A flag that cannot be fetched leaves the plugin unavailable and the local file unread.
		- ### What he measured
			- A directory holding only an `AGENTS.md` with a canary word, queried with `claude -p`. Each configuration needed two sessions, because the first only fetches the flag.
			- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` blocks the feature, as the issue reports.
			- `DISABLE_TELEMETRY=1` blocks it as well, so both had to be cleared.
			- Setting either variable to `0` does not re-enable it — any value counts as set.
			- An `env` block in a project's `.claude/settings.json` clearing both has no effect, so there is no per-repo override.
			- `claude --settings '{"env":{"DISABLE_TELEMETRY":"","CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC":""}}'` does work, from the second session on.
			- The same gate reaches third-party gateways, [[Claude/Code/Bedrock]] and Vertex, where the flag cannot resolve to `true` either.
		- ### The workaround
			- `CLAUDE.md` supports `@path` imports, which do not consult the flag. `echo '@AGENTS.md' > CLAUDE.md` loads the file with telemetry off, at the price of the extra file that `AGENTS.md` support was meant to remove.
		- ### The argument
			- A privacy setting should not switch off unrelated local behavior. Reading a file from the working directory needs no network, yet waits on a server-side switch.
			- The gate lands hardest on the people most likely to want `AGENTS.md`: anyone keeping one instruction file for several agents is usually deliberate about what each tool sends home, and teams on Bedrock, Vertex or a gateway often disable nonessential traffic by policy.
			- Silence is the sharpest complaint. Without a canary test and a string search through the binary, the symptom reads as a model ignoring instructions, and the time goes into prompts rather than the file that never arrived.
			- His asks: make a local file's loading independent of telemetry, or at minimum warn at startup when an `AGENTS.md` is present and skipped; and add a user-level `AGENTS.md` beside the user `CLAUDE.md`, as [[Codex]] has at `~/.codex/AGENTS.md`.
	- ## Links
		- [Issue #95690 — AGENTS.md not loaded when telemetry is disabled](https://github.com/anthropics/claude-code/issues/95690)
		- [[AI/Coding/Agents.md/Q/Does the AGENTS.md specification mention a global or home-directory-level AGENTS.md?]]
