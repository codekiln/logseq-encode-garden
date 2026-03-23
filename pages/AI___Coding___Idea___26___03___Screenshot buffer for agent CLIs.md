tags:: [[Idea]]
date-created:: [[2026-03-23 Mon]]

- # Screenshot buffer for agent CLIs (wish) — friction with [[CursorAI/CLI]] vs [[Claude Code]]
	- Personal friction: getting screenshots into **cursor-agent** is **much harder** than in [[Claude Code]], and it’s **frustrating** in daily use
	- In [[Claude Code]], **Ctrl+V** in the interface **pastes the image** and the session can see it — low ceremony
	- In **Cursor Agent** / [[CursorAI/CLI]], the practical path observed so far is **`@` plus an absolute filesystem path** to the image; the agent does not get the screenshot from a simple paste the same way
	- Using a path that contains **`~`** (home shorthand) **breaks the flow** — expansion or resolution does not behave like a normal shell path in that context, so you end up needing a fully expanded absolute path
	- Cross-tool wish: something like **Vim-style buffers** but for **recent screenshots** — a small **clipboard-of-files** or **named slots** (e.g. `@screenshot:0`) that **Codex**, **Copilot CLI**, **Cursor CLI**, and similar agents could all address without the user hand-copying `/Users/...` every time
	- Broader product angle: **standardize “last capture”** or **workspace temp attachment** semantics across coding agents so multimodal input isn’t tied to one vendor’s paste implementation
