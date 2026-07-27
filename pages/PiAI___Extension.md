logseq-entity:: [[Logseq/Entity/Concept]]
see-also:: [[PiAI]], [[jiti]]

- # Pi Extension System
	- ## Overview
		- [[PiAI]] has no plugin API in the usual sense; it has an **extension** system, and extensions are the mechanism by which nearly every optional behavior in the agent is expressed. The project describes itself as a "self extensible coding agent", and the extension surface is what that phrase cashes out to.
		- An extension is a [[TypeScript]] module that default-exports `(pi: ExtensionAPI) => void | Promise<void>`. The host loads it in-process with [[jiti]], the factory registers contributions and subscribes to lifecycle events, and the return values of those event handlers can mutate, veto, or short-circuit what the agent does next.
		- Source lives in `packages/coding-agent/src/core/extensions/`, where three files carry the whole system: `types.ts` (the public contract), `loader.ts` (discovery and import), and `runner.ts` (the host that dispatches events and resolves conflicts).
	- ## Vocabulary
		- **Extension** — the unit of behavior. What most hosts would call a plugin.
		- **Package** — the unit of distribution. One package may ship many extensions plus skills, prompt templates, and themes.
		- **`ExtensionAPI`**, conventionally bound to `pi` — the registration object handed to the factory once, at load time.
		- **`ExtensionContext`**, conventionally bound to `ctx` — the runtime object handed to every event handler on every invocation.
		- **Contribution** — anything registered: a tool, command, shortcut, flag, renderer, or model provider.
		- **Event** — both notification and hook. There is no separate hook concept; what distinguishes an interception point from an observation point is only whether the host reads the handler's return value.
	- ## Sub-pages
		- [[PiAI/Extension/Architecture]] — discovery, dispatch, isolation, conflict resolution, persistence.
		- [[PiAI/Extension/Philosophy]] — the design commitments and the tensions they create.
		- [[PiAI/Extension/Ref]] — the API surface.
		- [[PiAI/Extension/Plan Mode]] — a bundled extension that replaces the agent's operating mode.
		- [[PiAI/Extension/Pi Review]] — an externally distributed extension.
	- ## Why it is unusual
		- Most plugin systems abstract over the host's internals. Pi's events are named call sites in the agent loop, the provider transport, and the session-tree machinery, so the extension surface is a projection of the internal architecture rather than a layer above it.
		- The consequence is that an extension can do almost anything the host can, including overriding built-in tools, rewriting the outgoing provider payload, and filtering the message history before every model call. Features that other agents ship as core — plan mode, sandboxing, permission gates, custom compaction — exist here as extensions.
