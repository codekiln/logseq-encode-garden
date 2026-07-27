logseq-entity:: [[Logseq/Entity/Software/Plugin]]
see-also:: [[PiAI/Extension]], [[PiAI/Extension/Architecture]]

- # [Plan Mode](https://github.com/earendil-works/pi/tree/main/packages/coding-agent/examples/extensions/plan-mode)
	- A bundled [[PiAI]] example extension providing read-only exploration in the style of [[Claude/Code]]'s plan mode: the agent may investigate but not modify, produces a numbered plan, and on confirmation switches to an execution mode with progress tracking.
	- Roughly 390 lines in `index.ts` plus a small `utils.ts`. Toggled by `/plan`, by `Ctrl+Alt+P`, or by the `--plan` flag.
	- Architecturally the most revealing example in the repository, because a mode is exactly the kind of feature most agents hardcode. Its existence as an extension is the strongest evidence that the seams described on [[PiAI/Extension/Architecture]] are real.
	- ## State is four variables in a closure
		- ~~~typescript
		  export default function planModeExtension(pi: ExtensionAPI): void {
		  	let planModeEnabled = false;
		  	let executionMode = false;
		  	let todoItems: TodoItem[] = [];
		  	let toolsBeforePlanMode: string[] | undefined;
		  	// registrations and pi.on(...) subscriptions close over these
		  }
		  ~~~
		- No class, no state manager, no dependency injection. The session log is the durable backing store, and the closure holds the working copy.
		- This is the idiomatic shape, and it scales: [[PiAI/Extension/Pi Review]] uses the same pattern at four times the size.
	- ## Nine subscriptions, each with one job
		- `registerFlag("plan")` starts the mode from the command line, `registerCommand("plan")` and `registerCommand("todos")` provide human entry points, and `registerShortcut` binds the same toggle to a key rather than hardcoding it.
		- `on("tool_call")` enforces the restriction, `on("context")` removes stale mode instructions from history, `on("before_agent_start")` injects the mode's instructions, `on("turn_end")` detects progress, `on("agent_end")` orchestrates the hand-off, and `on("session_start")` reconstructs state.
		- Restriction, instruction, hygiene, observation, and orchestration are five different hooks, and collapsing any pair of them would break the feature.
	- ## Restriction happens at two levels
		- The declarative level removes tools from the model's toolset entirely.
			- ~~~typescript
			  function enablePlanModeTools(): void {
			  	if (toolsBeforePlanMode === undefined) {
			  		toolsBeforePlanMode = pi.getActiveTools();
			  	}
			  	pi.setActiveTools(getPlanModeTools(toolsBeforePlanMode));
			  }
			  ~~~
			- Only `edit` and `write` are disabled. The filter subtracts from whatever was already active and then adds the plan-mode set, rather than replacing with a fixed list, so another extension's custom tools survive the switch.
			- The previous toolset is captured for exact restoration, and a separate set of managed tool names ensures restore does not clobber tools the mode never touched.
		- The imperative level vetoes anything that slips through.
			- ~~~typescript
			  pi.on("tool_call", async (event) => {
			  	if (!planModeEnabled || event.toolName !== "bash") return;
			  	const command = event.input.command as string;
			  	if (!isSafeCommand(command)) {
			  		return { block: true, reason: `Plan mode: command blocked (not allowlisted). ...` };
			  	}
			  });
			  ~~~
			- `bash` cannot simply be removed, since read-only exploration needs it, so it is allowlisted per invocation instead.
		- The general pattern: capability removal handles tools that can be taken away, and a runtime veto handles the general-purpose escape hatch that cannot. The veto carries a reason string back to the model so it can adapt rather than retry blindly.
	- ## Injected context is scrubbed when the mode ends
		- `before_agent_start` returns a message with `customType: "plan-mode-context"` and `display: false`, making it visible to the model, invisible in the transcript, and persisted in the session.
		- Because it persists, it would linger after the mode ends, so a `context` handler filters it out whenever plan mode is off. The filter also matches the literal `[PLAN MODE ACTIVE]` marker in user content, covering messages that lost their custom type.
		- A plugin API that permits context injection needs a matching retraction path. Injection-only APIs produce conversations that slowly fill with contradictory stale instructions.
	- ## Progress tracking uses prose as the protocol
		- The injected prompt asks the model to emit a `[DONE:n]` marker after finishing step *n*, and `turn_end` scans assistant text for those markers.
		- No tool call, no structured output, no schema — a marker in prose is the entire channel. Cheap and surprisingly robust, at the cost described below.
	- ## Orchestration in `agent_end`
		- When a plan is finished, numbered steps are extracted from the last assistant message and the user is offered a choice through `ctx.ui.select`: execute, stay in plan mode, or refine.
		- On execute, the extension flips modes, restores tools, and drives the next turn itself.
			- ~~~typescript
			  pi.sendMessage(planTodoListMessage, { deliverAs: "followUp" });
			  pi.sendMessage(
			  	{ customType: "plan-mode-execute", content: execMessage, display: true },
			  	{ triggerTurn: true, deliverAs: "followUp" },
			  );
			  ~~~
			- `triggerTurn: true` means an extension can start an agent turn; extensions are not confined to reacting.
			- The `plan-mode-execute` entry doubles as a marker in the session log, used later during state reconstruction.
		- On refine, `ctx.ui.editor` collects text and forwards it as a user message. The extension is mediating a multi-turn human workflow rather than filtering events.
	- ## State reconstruction and its sharp edge
		- `session_start` reads the last `plan-mode` custom entry to restore the four closure variables, which is straightforward.
		- Rebuilding *completion* state on resume is not, because `[DONE:n]` markers live in prose scattered through history.
			- ~~~typescript
			  // Only scan messages AFTER the last "plan-mode-execute" marker
			  let executeIndex = -1;
			  for (let i = entries.length - 1; i >= 0; i--) {
			  	if (entries[i].customType === "plan-mode-execute") { executeIndex = i; break; }
			  }
			  ~~~
			- Without that guard, resuming a session containing an earlier completed plan would mark the new plan's steps as done, an intermittent and confusing bug.
		- This is the honest cost of event-sourced extension state: replay requires a window, and the window needs its own marker in the log.
		- The extension also persists cleared state after completion, so a later resume does not restore a finished execution mode.
	- ## Ambient UI is keyed for cleanup
		- ~~~typescript
		  ctx.ui.setStatus("plan-mode", ctx.ui.theme.fg("warning", "⏸ plan"));
		  ctx.ui.setWidget("plan-todos", lines);
		  ~~~
		- Every ambient surface is keyed by a string the extension owns, and clearing is a matter of passing `undefined` for that key. Multiple extensions coexist in the footer without collision, and cleanup requires no handle bookkeeping.
		- Colors come from semantic theme names rather than literals, so the extension respects whatever theme the user has chosen.
