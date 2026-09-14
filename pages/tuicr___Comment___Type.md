tags:: [[Diataxis/Concept]]
logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[tuicr/Config/comment_types]], [[tuicr/Agent/Skill]], [[tuicr]]

- # [[tuicr]] Comment Type
	- ## Overview
		- A **comment type** is [[tuicr]]'s built-in classification for a single review comment — a lightweight label (`note`, `suggestion`, `issue`, `praise`, `nit`, or any custom set you define) attached at the moment you write the comment, not after the fact.
		- It exists to make a terminal review read like a real code review at a glance: a reviewer or an agent skimming the diff (or the exported Markdown) can tell "blocking issue" from "optional nit" from "just praise" without reading every comment body.
	- ## Context
		- The video ((6aa57707-e737-4321-9b40-aaac81aaba45)) frames this as the differentiator over **hunk**, a diff-only TUI: hunk leaves comments on code but has no classification or forge push; [[tuicr]] pairs typed comments with a real `:submit` to GitHub/GitLab/Gitea/Bitbucket/Azure DevOps/Gerrit.
		- Configuration lives on [[tuicr/Config/comment_types]] (the `comment_types` array in `config.toml`); this page is about what the feature **means and does**, not how to set it.
	- ## Key Principles
		- **Per-comment, not per-review.** Every individual comment carries its own type; a review is just the sum of its comments.
		- **Cycle, don't type out.** `Tab` / `Shift-Tab` cycle through the configured types (plus the always-available untyped `None`) while writing a comment — there is no free-text type field.
		- **Configurable set, sensible defaults.** The garden's example config ships `note`/question, `suggestion`, `issue`, `praise`, and `nit`; you can rename, recolor, redefine, or replace this set entirely, or unset it to disable typing altogether.
		- **Visible in three places.** The same type drives the TUI badge color, the `[TYPE]` prefix on export/submit, and the `Comment types:` legend — one source of truth, three renderings.
	- ## Mechanism
		- Press `c`/`C`/`v`/`V` to start a comment, then `Tab`/`Shift-Tab` to cycle its type before saving.
		- On `:submit` or export, `comment_type_prefix` (on by default) turns the type into a literal `[TYPE] ` prefix on the comment body sent to the forge — the forge itself has no native concept of comment type, so this is purely a text convention `tuicr` adds and later readers must recognize.
		- `tuicr review add --type <id>` (the agent-facing CLI path) validates `<id>` against the configured set but only **warns** on a mismatch; it still stores the comment and exits `0`.
	- ## Examples
		- Marking a genuinely blocking finding `issue` versus a purely optional cleanup `nit` lets a human or agent triage a large review by scanning badges/prefixes first.
		- A `praise` comment on a well-factored function shows up as `[PRAISE] ...` in the export the same way an `[ISSUE] ...` would, just carrying positive framing.
	- ## Misconceptions (what it is **not**)
		- **Not a forge-native field.** GitHub/GitLab/etc. don't store or render a "comment type" — it is only the `[TYPE] ` text prefix `tuicr` prepends; strip the prefix and the forge sees an ordinary comment.
		- **Not a gate.** An unrecognized `--type` value doesn't block the CLI or the review; it only prints a warning. Comment types don't affect whether a review can be approved or submitted.
		- **Not required.** With `comment_types` unset (or when a comment is left on the always-available `None`), the comment behaves exactly as before typed comments existed — no tag, no badge, no legend entry.
		- **Not a workflow/automation trigger.** Choosing `issue` vs `nit` doesn't change tuicr's own behavior (no auto-blocking, no routing) — it is purely a display and export convention for humans and agents to read.
