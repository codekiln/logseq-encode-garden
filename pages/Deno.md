logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Ryan Dahl]]
date-created:: [[2018]]

- # [Deno](https://deno.com/)
	- A "secure-by-default" [[Runtime]] for [[JavaScript]], [[TypeScript]], and WebAssembly. It is a [[Rust]] program that embeds the V8 engine, ships as a single executable, and includes its own tooling for formatting, linting, testing, and bundling.
	- [Source repository](https://github.com/denoland/deno) — [[GitHub/Star]] count: 107,367 as of [[2026-06-28 Sun]].
	- ## Design
		- "Secure by default" — explicit permission flags gate file, network, and environment access.
		- First-class [[TypeScript]] — runs `.ts` directly with no separate build step.
		- Built-in tooling — `deno fmt`, `deno lint`, `deno test`, `deno compile`, and a task runner driven by `deno.json`.
		- Web-standard APIs (fetch, Web Crypto, etc.) over Node-specific ones, with [[Node.js]] and [[npm]] compatibility layers.
	- ## Implementation
		- Deno is mostly a [[Rust]] program. The code you write runs inside V8, but the runtime around it is written in Rust: the scheduler, permission system, module loader, filesystem and network access, process management, the [[Node.js]] compatibility layer, the command-line interface, and much of the Web API.
		- Approximate share of the source by language: Rust ~62%, [[TypeScript]] ~26%, [[JavaScript]] ~11%, C ~1%. These shares change as the project evolves — earlier versions kept more of the runtime in TypeScript and have since rewritten the performance-sensitive parts in Rust.
		- Async work is scheduled on the [[Tokio]] runtime.
		- `deno_core` is the lower-level [[Rust/crate]] that embeds V8 in Rust; Deno is built on top of it.
		- One of the better-known production [[Rust]] applications, alongside tools like [[ripgrep]], [[fd]], and [[Cargo]].
		- How a program flows through the layers:
			- The TypeScript or JavaScript you write
			- runs inside the V8 engine,
			- which calls into the Rust runtime (permissions, networking, filesystem, subprocesses, Web APIs, module loader, Node compatibility, CLI),
			- which talks to the operating system.
	- ## Ecosystem
		- [[JSR]] — the Deno-first package registry (jsr.io).
		- [[Deno Deploy]] — hosted edge runtime, with Deno KV for storage.
		- Fresh — Deno's first-party web framework.
		- Compared with [[Node.js]] and [[Bun]] as a JS/TS runtime.
	- ## Notes
		- Created by [[Person/Ryan Dahl]], who also created [[Node.js]]; first released in 2018, with v1.0 in May 2020.
		- Can be managed per-project with [[mise]] (`mise use -g deno`) rather than a true global install.
		- [[Deno/Q/Under what circumstances would I need or want deno installed globally on my machine?]]