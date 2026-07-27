logseq-entity:: [[Logseq/Entity/Software/Plugin]]
created-by:: [[Earendil]]
see-also:: [[PiAI/Extension]], [[PiAI/Extension/Plan Mode]]

- # [pi-review](https://github.com/earendil-works/pi-review)
	- A code review extension for [[PiAI]], distributed as its own repository and npm package rather than bundled with the agent. `/review` picks a target — pull request, uncommitted changes, branch, commit, or folder — optionally opens a fresh session branch, and drives the agent through a review rubric; `/end-review` returns with an optional summary or fix pass.
	- A single `review.ts` of roughly 1600 lines. Interesting less for its hook usage than for what it shows about distribution and workflow ownership; the complement to [[PiAI/Extension/Plan Mode]], which is bundled and hook-heavy.
	- ## The distribution contract is four lines
		- ~~~json
		  {
		    "keywords": ["pi-package", "pi-extension"],
		    "peerDependencies": {
		      "@earendil-works/pi-coding-agent": "*",
		      "@earendil-works/pi-ai": "*",
		      "@earendil-works/pi-tui": "*"
		    },
		    "pi": { "extensions": ["./review.ts"] }
		  }
		  ~~~
		- Installed with `pi install git:github.com/earendil-works/pi-review`, or tried without installing via `pi -e`.
		- Zero runtime dependencies: everything needed is either a host peer dependency or a binary shelled out to.
		- The wildcard peer-dependency range matters. Host libraries must not be bundled, because [[jiti]] aliases those imports to the host's own copies; bundling would produce two incompatible copies of the type system at runtime.
		- The `pi-package` keyword is what surfaces it in the public package gallery. Discovery is a keyword convention rather than a registry.
	- ## It ships source, not a build
		- The published artifact is the [[TypeScript]] source, compiled on load by [[jiti]]. There is no `dist/`, no build step, and no source maps to keep synchronized.
		- The security consequence matters more than the convenience one: since the source *is* the distribution, "review before you install" is actually feasible, which is the mitigation the trust model on [[PiAI/Extension/Philosophy]] depends on.
	- ## Shelling out is the integration strategy
		- Git and GitHub access is entirely `pi.exec("git", ...)` and `pi.exec("gh", ...)`. There is no git library and no GitHub API client.
		- The extension composes tools the user already has and is already authenticated to, which makes credential storage, auth flows, and API versioning someone else's problem. A good `exec` primitive absorbs a large amount of would-be API surface.
	- ## It owns the session tree, not just the conversation
		- A review runs on its own branch of the session, so the review conversation does not pollute the working one.
			- ~~~typescript
			  if (useFreshSession) {
			  	let originId = ctx.sessionManager.getLeafId() ?? undefined;
			  	if (!originId) {
			  		pi.appendEntry(REVIEW_ANCHOR_TYPE, { createdAt: new Date().toISOString() });
			  		originId = ctx.sessionManager.getLeafId() ?? undefined;
			  	}
			  	// navigate to the first user message, label the branch "code-review"
			  	setReviewWidget(ctx, true);
			  	pi.appendEntry(REVIEW_STATE_TYPE, { active: true, originId: lockedOriginId });
			  }
			  ~~~
			- Note the anchor trick: when there is no leaf to return to, an entry is appended purely to create one. The persistence primitive doubles as an addressing primitive.
		- Three custom entry types carry all durable state, and both `session_start` and `session_tree` re-apply them — the same reducer pattern as [[PiAI/Extension/Plan Mode]].
		- `/end-review` navigates back with a summary, so the working conversation gains the review's conclusion without its transcript.
		- Where a host has branchable history, a plugin can use branching as scoping. That is considerably cleaner than a plugin trying to hide its own messages.
	- ## The rubric is a prompt, and the prompt is the product
		- The review flow assembles a full prompt from a rubric constant plus the target description plus user guidelines, then calls `pi.sendUserMessage`. Custom instructions persist through appended entries so they survive across sessions.
		- Most of the 1600 lines are terminal UI and git plumbing. The agent-facing logic is a prompt template and a single message send.
		- This generalizes: for an agent host, a large share of extensions are prompt packaging plus UI plus shell integration, and only a minority need deep hooks. Registering a command, executing a subprocess, sending a message, and appending an entry carry most of the real-world weight.
	- ## Sibling repositories, for contrast
		- **pi-review-loop** — the same problem in the opposite shape: a modular `src/` tree, a file watcher, and a native web window with a Monaco diff viewer rather than a terminal UI. Feedback is inserted into the editor instead of auto-sent. Evidence that the extension surface does not constrain an extension's own UI technology.
		- **pi-tutorial** — an onboarding walkthrough, notable for detecting its own `/reload` through a global symbol plus a shutdown timestamp, and for kicking itself off with a message that triggers a turn. Still on the older `@mariozechner/pi-*` peer-dependency names, which the host's import aliases keep working.
		- **pi-chat** — bridges Discord and Telegram into a sandboxed session, and is the heaviest known extension: multi-process worker orchestration under tmux, a per-channel micro-VM, overrides of the built-in file and shell tools that delegate to the host's own exported tool constructors, encrypted secret exchange, and a `tool_call` gate limiting remote turns. It marks the upper bound of what the API permits.
