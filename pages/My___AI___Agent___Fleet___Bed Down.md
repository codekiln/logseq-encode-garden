tags:: [[Diataxis/How To]]
see-also:: [[My/AI/Agent/Fleet]], [[Chroma/Paper/25/07/Context Rot - Increasing Input Tokens Impacts LLM Performance]], [[Claude/Code/--resume]]

- # Fleet — Bed Down
	- Ending a [[Claude/Code]] context window on purpose and starting a fresh one in the same [[tmux/Pane]], so a long day does not accumulate into one enormous session. The [[My/AI/Agent/Fleet]] ceiling is **200k tokens**.
	- ## Why there is a ceiling at all
		- The measured shape of the problem: on [[2026/08/17]] the chiefs peaked at **358k–484k** tokens, and the [[herdr]] era reached **641k**. None of those sessions were told to stop.
		- Long sessions get worse rather than better. They hold conclusions that were true earlier in the day and re-derive things they already knew — the failure that [[Chroma/Paper/25/07/Context Rot - Increasing Input Tokens Impacts LLM Performance]] measures, arriving as confident staleness rather than as an error.
		- So three or four context windows in a day is the correct number, not a sign that something went wrong. Bed down at minimum after the first deliverable, in the early afternoon, and before closing for the day.
	- ## The cycle
		- `ctx-check <session-name>` → if the verdict is `BED-DOWN SOON` or `BED-DOWN NOW`, refresh the handoff doc → `bed-down <session-name> <handoff-doc>`.
	- ## `ctx-check`
		- Prints the session's live context size as a percentage of 200k, and a verdict: `OK`, `BED-DOWN SOON` at 85%, `BED-DOWN NOW` at 100%. `CTX_BUDGET` overrides the 200k.
			- ~~~sh
			  ctx-check hayward-2026-08-24
			  # hayward-2026-08-24: 63,624 tokens = 32% of 200,000  ->  OK
			  ~~~
		- **An agent cannot see its own context total**, which is the whole reason the script exists. It reads the number from the session's own transcript under `~/.claude/projects`, so asking costs no model tokens.
		- The size is the last usage record's `input_tokens` plus `cache_read_input_tokens` plus `cache_creation_input_tokens` — the whole input of the most recent request, which is the live context.
		- Matching is on the `agentName` field recorded by `claude -n`, **not on the working directory**. Several sessions can share a cwd, and on [[2026/08/17]] three did. A seat that never passed `-n` cannot be found this way.
	- ## `bed-down`
		- Writes over the current pane with a fresh `claude` that reads the handoff doc first:
			- ~~~sh
			  bed-down hayward-2026-08-24 tmp/hayward-handoff.md
			  ~~~
		- Implemented as `tmux respawn-pane -k -t "$TMUX_PANE"`, so it must be run from inside the pane being replaced; it exits rather than guessing when `TMUX_PANE` is unset.
		- **It refuses unless the handoff doc exists and was written in the last 15 minutes.** That guard is the point of the script: respawning without a current handoff destroys the only copy of what the session knew. Both refusals were tested against their failure cases before the script was used.
	- ## The handoff doc is not a summary of the day
		- It is what the next context window needs in order to keep working: what was in progress, what had been concluded and how it was checked, what had been ruled out, exact paths, and the next action.
		- Write it for someone with none of the author's context, because that is exactly who reads it.
		- A day's report doc and a handoff doc are different documents with different readers. The report says what happened; the handoff says what to do next.
	- ## Where the scripts live
		- Four of them, not two: `bed-down`, `ctx-check`, `wake-successor` and `viewer`. As of [[2026-08-24 Mon]] they sit in `bin/` beside the day's fleet conventions, under the `tmp/` tree, and there are **two byte-identical copies** — one in [[My/Dotfiles]] and one in the work knowledge vault. Use the copy in whichever repository the pane is working in, and note that **this garden holds neither**: a seat here that looks locally finds nothing and has to reach across.
			- **That is a staging location, not a home.** `tmp/` is gitignored in both repositories that carry the scripts, and the scripts are untracked in both, so every copy exists on this machine only and a fresh clone gets none of them. This garden is the exception that makes the pattern easy to misread — its own `tmp/` is tracked and published.
		- Where they land permanently is a [[My/Dotfiles]] question and goes through [[My/Pref/Dev/AI/OpenSpec]]; it is not settled here. Recording the path as though it were the answer is how a garden page rots.
		- `bed-down` reads a file's age with `stat -f %m`, which is the BSD form — it wants the GNU spelling to run on Linux.
