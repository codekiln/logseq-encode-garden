see-also:: [[PiAI/Extension]], [[PiAI/Extension/Architecture]], [[PiAI/Extension/Philosophy]]

- # Pi Extension API Reference
	- The API surface of [[PiAI]]'s extension system, for lookup rather than reading. Canonical source is `packages/coding-agent/src/core/extensions/types.ts`; canonical prose is `packages/coding-agent/docs/extensions.md`.
	- Accurate as of pi `0.82.x`. There is no API version field, and minor releases may break any of this.
	- ## Minimum viable extension
		- ~~~typescript
		  import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
		  export default function (pi: ExtensionAPI) {
		    pi.on("session_start", async (_event, ctx) => {
		      ctx.ui.notify("loaded", "info");
		    });
		  }
		  ~~~
		- The exported type is `ExtensionFactory = (pi: ExtensionAPI) => void | Promise<void>`.
		- Run with `pi -e ./my-extension.ts`. Place under `~/.pi/agent/extensions/` or `.pi/extensions/` for auto-discovery and `/reload` support.
	- ## Importable from an extension
		- `@earendil-works/pi-coding-agent` — `ExtensionAPI`, `ExtensionContext`, event types, `defineTool`, `withFileMutationQueue`, built-in tool constructors.
		- `typebox` — tool parameter schemas.
		- `@earendil-works/pi-ai` — provider and message types, and `StringEnum` for Google-compatible enums.
		- `@earendil-works/pi-tui` — components for custom rendering, and `Key` for shortcuts.
		- [[NodeJS]] built-ins, plus any npm dependency installed in a `package.json` beside or above the extension.
	- ## Events
		- Subscribe with `pi.on(name, handler)`, where the handler is `(event, ctx) => Result | void`, sync or async. Dispatch is sequential in load order; the result semantics are the operative part of the contract.
		- ### Startup and resources
			- `project_trust` — receives `{ cwd }`, returns `{ trusted: "yes" | "no" | "undecided", remember?: boolean }`. First decisive answer wins and suppresses the built-in prompt. Only user-scoped and CLI extensions participate, and `ctx` is a reduced trust context carrying `cwd`, `mode`, `hasUI`, and the four dialog helpers.
			- `resources_discover` — receives `{ cwd, reason }`, returns `{ skillPaths?, promptPaths?, themePaths? }`. Accumulated across all handlers.
		- ### Session
			- `session_start` — `{ reason, previousSessionFile? }` where reason is one of `startup`, `reload`, `new`, `resume`, `fork`. Observe. The place to rebuild state and start session-scoped resources.
			- `session_shutdown` — `{ reason, targetSessionFile? }`. Observe. Must be idempotent.
			- `session_info_changed` — `{ name? }`. Observe.
			- `session_before_switch` — `{ reason, targetSessionFile? }`, returns `{ cancel: true }`.
			- `session_before_fork` — `{ entryId, position }`, returns `{ cancel: true }`.
			- `session_before_compact` — `{ preparation, branchEntries, customInstructions, reason, willRetry, signal }`, returns `{ cancel: true }` or a replacement `{ compaction }`.
			- `session_compact` — `{ compactionEntry, fromExtension, reason, willRetry }`. Observe.
			- `session_before_tree` — `{ preparation, signal }`, returns `{ cancel: true }` or `{ summary }`.
			- `session_tree` — `{ newLeafId, oldLeafId, summaryEntry, fromExtension }`. Observe, and the usual partner to `session_start` for state rebuilds.
		- ### Prompt and agent
			- `input` — the user's raw input, returning `{ action: "continue" }`, `{ action: "transform", text, images? }`, or `{ action: "handled" }`. The last short-circuits everything downstream including skill and template expansion. Extension commands are checked before this fires.
			- `before_agent_start` — `{ prompt, images, systemPrompt, systemPromptOptions }`, returning `{ message?, systemPrompt? }`. The system prompt chains across handlers; injected messages accumulate. The options object exposes `customPrompt`, `selectedTools`, `toolSnippets`, `promptGuidelines`, `appendSystemPrompt`, `cwd`, `contextFiles`, and `skills`.
			- `agent_start` — observe.
			- `agent_end` — `{ messages }`. Observe. May be followed by an auto-retry, auto-compaction, or a queued follow-up.
			- `agent_settled` — observe. Fires only when the host will not continue on its own, which makes it the right hook for status integrations.
			- `turn_start` — `{ turnIndex, timestamp }`. Observe.
			- `turn_end` — `{ turnIndex, message, toolResults }`. Observe.
		- ### Messages
			- `message_start` — `{ message }`, for user, assistant, and tool-result messages. Observe.
			- `message_update` — `{ message, assistantMessageEvent }`, the streaming deltas. Observe.
			- `message_end` — `{ message }`, returning `{ message }` to replace it. The replacement must keep the same role. Chains.
		- ### Context and provider transport
			- `context` — `{ messages }`, a deep copy, returning `{ messages }`. Chains, so each handler sees the previous one's output. Fires before every model call.
			- `before_provider_headers` — `{ headers }`, mutated in place. A string value adds or overrides; `null` deletes. Fires once per request, and retries reuse the headers rather than re-firing.
			- `before_provider_request` — `{ payload }`, where any returned value replaces the payload. Chains. Can strip provider-level system instructions, which `ctx.getSystemPrompt()` will not reflect.
			- `after_provider_response` — status and headers, before the stream body is consumed. Observe.
		- ### Tools
			- `tool_call` — `{ toolName, input }`, returning `{ block: true, reason }` to veto. The `input` object is mutable in place, later handlers see mutations, and no re-validation occurs. A throw here blocks the tool.
			- `tool_result` — returns `{ content?, details?, isError?, usage? }`. Chains.
			- `tool_execution_start` — `{ toolCallId, toolName, args }`. Observe. In parallel tool mode these are emitted in assistant source order during preflight.
			- `tool_execution_update` — `{ toolCallId, toolName, args, partialResult }`. Observe. May interleave across tools.
			- `tool_execution_end` — `{ toolCallId, toolName, result, isError }`. Observe. Emitted in completion order.
			- `user_bash` — the user's `!command`. The first handler to return a result wins and short-circuits.
		- ### Model
			- `model_select` — observe.
			- `thinking_level_select` — observe. Also fires when a model change clamps the thinking level.
	- ## ExtensionAPI, the `pi` object
		- ### Contributions
			- `registerTool(tool)` — re-registering a built-in name overrides it.
			- `registerCommand(name, { description, handler, getArgumentCompletions? })`
			- `registerShortcut(key, { description?, handler })` — keys are built with helpers such as `Key.ctrlAlt("p")`.
			- `registerFlag(name, { description?, type, default? })` and `getFlag(name)`
			- `registerMessageRenderer(customType, renderer)` for model-visible custom messages.
			- `registerEntryRenderer(customType, renderer)` for TUI-only session entries.
			- `registerProvider(name, config)`, `registerProvider(provider)`, and `unregisterProvider(name)`. Registrations from an async factory are queued and flushed before `session_start`.
		- ### Session actions
			- `sendMessage(message, { triggerTurn?, deliverAs? })` where `deliverAs` is `steer`, `followUp`, or `nextTurn`.
			- `sendUserMessage(content, { deliverAs? })`
			- `appendEntry(customType, data?)` — the persistence primitive.
			- `setSessionName(name)`, `getSessionName()`, `setLabel(entryId, label?)`
			- `exec(command, args, options?)` returning a promise of the result.
			- `getActiveTools()`, `getAllTools()`, `setActiveTools(names)`, `getCommands()`
			- `setModel(model)`, `getThinkingLevel()`, `setThinkingLevel(level)`
			- `events` — an untyped inter-extension bus with `emit(channel, data)` and `on(channel, handler)`. No namespacing, and handler errors are logged and swallowed.
		- Skills, prompts, themes, and subagents are **not** registered through this API. They arrive through package discovery or the `resources_discover` event, which returns paths rather than objects.
	- ## ExtensionContext, the `ctx` in every handler
		- ~~~typescript
		  export interface ExtensionContext {
		  	ui: ExtensionUIContext;
		  	mode: ExtensionMode;          // "tui" | "rpc" | "json" | "print"
		  	hasUI: boolean;
		  	cwd: string;
		  	sessionManager: ReadonlySessionManager;
		  	modelRegistry: ModelRegistry;
		  	model: Model<any> | undefined;
		  	thinkingLevel?: ThinkingLevel;
		  	isIdle(): boolean;
		  	isProjectTrusted(): boolean;
		  	signal: AbortSignal | undefined;
		  	abort(): void;
		  	hasPendingMessages(): boolean;
		  	shutdown(): void;
		  	getContextUsage(): ContextUsage | undefined;
		  	compact(options?: CompactOptions): void;
		  	getSystemPrompt(): string;
		  }
		  ~~~
		- `ExtensionCommandContext` extends this for commands and shortcuts, adding `getSystemPromptOptions()`, `waitForIdle()`, `newSession()`, `fork()`, `navigateTree()`, `switchSession()`, and `reload()`.
		- The last five invalidate the current extension instance; a captured `pi` or `ctx` used afterward throws.
	- ## The `ctx.ui` surface
		- Dialogs: `select`, `confirm`, `input`, `notify`, `editor`. All accept an optional abort signal for auto-dismissal, and all require `hasUI`.
		- Ambient surfaces: `setStatus` for the footer, `setWidget` above or below the editor, plus `setFooter`, `setHeader`, `setTitle`, `setWorkingMessage`, `setWorkingIndicator`, `setWorkingVisible`, and `setHiddenThinkingLabel`. Each is keyed by a string the extension owns, and clearing means passing `undefined`.
		- Editor: `getEditorText`, `setEditorText`, `pasteToEditor`, `getEditorComponent`, `setEditorComponent`, `addAutocompleteProvider`.
		- Full control: `custom()` for a component with keyboard input, plus overlays. TUI mode only; returns `undefined` under RPC.
		- Theming: `theme.fg(color, text)` with semantic color names, plus `getAllThemes`, `getTheme`, `setTheme`.
		- Gate on `ctx.mode === "tui"` for `custom()` and component factories; gate on `ctx.hasUI` for dialogs and notifications.
	- ## Mode behavior
		- `tui` — interactive, `hasUI` true, everything available.
		- `rpc` — `hasUI` true, dialogs travel over a JSON protocol, and `custom()` returns `undefined`.
		- `json` — `hasUI` false, UI methods are no-ops.
		- `print` — `hasUI` false; extensions run but cannot prompt.
	- ## Tool definition notes
		- Parameters are TypeBox schemas. `promptSnippet` adds a one-line entry to the system prompt's tool list, and omitting it leaves the tool out of that section entirely.
		- `promptGuidelines` adds bullets to the system prompt's guidelines section while the tool is active. Bullets are appended flat with no grouping, so each must name its own tool.
		- `terminate: true` makes a tool end the run, which is the pattern for structured final output.
		- `executionMode: "sequential"` opts out of parallel execution.
		- Tools that mutate files must wrap the entire read-modify-write window in `withFileMutationQueue(absolutePath, fn)`, or a parallel built-in edit can silently clobber the change. Pass a resolved absolute path rather than the raw argument.
		- `renderCall` and `renderResult` control presentation without changing behavior.
		- Errors are signaled by throwing; the throw is caught and returned to the model with `isError: true`.
		- Some models prefix path arguments with `@`. Built-in tools strip it, and custom tools should too.
	- ## Distribution
		- ~~~json
		  {
		    "name": "my-package",
		    "keywords": ["pi-package", "pi-extension"],
		    "peerDependencies": { "@earendil-works/pi-coding-agent": "*" },
		    "pi": { "extensions": ["./index.ts"], "skills": ["./skills"] }
		  }
		  ~~~
		- Install with `pi install npm:@foo/bar@1.0.0`, `pi install git:github.com/user/repo@v1`, or a local path. Adding `-l` writes to project settings instead of user settings.
		- Manage with `pi list`, `pi remove`, `pi update --extensions`, and `pi config`, which enables or disables individual resources and switches between global and project scope with Tab.
		- Try without installing using `pi -e <source>`.
		- Git refs are pinned; `pi update` reconciles a clone to the declared ref but does not advance it. Moving requires installing the new ref explicitly.
		- Without a `pi` manifest, convention directories apply: `extensions/` for `.ts` and `.js`, `skills/` for recursive `SKILL.md` folders plus top-level `.md`, `prompts/` for `.md`, and `themes/` for `.json`.
	- ## Settings keys
		- `extensions` — an array of local file or directory paths.
		- `packages` — an array of strings, or of objects carrying a `source` plus per-type filter globs supporting `!` exclude, `+` force-include, and `-` force-exclude.
		- `npmCommand` — a wrapper command for npm lookups and installs, useful with version managers.
		- `defaultProjectTrust` — controls whether an unknown project prompts, trusts, or declines.
		- User settings live at `~/.pi/agent/settings.json` and project settings at `.pi/settings.json`. The project entry wins on collision unless it sets `autoload: false`, in which case it applies as a delta over the user entry.
	- ## Error handling summary
		- A load error is recorded, that extension is skipped, and the others load.
		- A handler error is logged; dispatch and the agent both continue.
		- A `tool_call` error blocks the tool, failing safe.
		- A tool `execute` error is returned to the model as `isError: true`.
		- There are no handler timeouts and no auto-disable.
