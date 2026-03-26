tags:: [[Idea]]
date-created:: [[2026-03-25 Wed]]

- # Weekly review via rulesync: agent chat history, patterns, session names
	- ## Sketch
		- Define **`[[rulesync]]`** rules (or commands / skills) for a **weekly review** that spans **[[Agentic Engineering Tools]]** — e.g. [[Claude Code]], [[CursorAI]] and [[CursorAI/CLI]], [[CodexCLI]], and any similar CLIs — instead of a one-off ritual that lives in a single vendor’s UI.
	- ## What it could do
		- Walk **chat or session history** for each tool (storage paths and formats differ by product; likely needs per-tool adapters or a phased v1).
		- **Notice patterns**: recurring friction, prompts that worked, blind spots, tool limits, “land the plane” gaps.
		- **Surface** findings somewhere durable (journal entry, garden page, `[[Beads]]` note — pick the habit).
		- Optionally **rename** conversations or sessions to **short, idiomatic titles** so scrolling history stays legible — where the host app exposes renames or on-disk names can be edited safely.
	- ## Constraints
		- **Privacy and secrets**: transcripts are sensitive; keep the workflow **local-first**, explicit about scope, and **redaction-aware** before anything is summarized or shared.
		- **Portability**: the interesting part is the *review protocol* in `.rulesync`; concrete “how to read Cursor DB” etc. may sit in `references/` or tool-specific docs.
	- ## Related
		- [[rulesync]]
		- [[Agentic Engineering Tools]]
		- [[AI/Coding/Concept/Land the Plane]] — review could include whether sessions actually closed the loop (git push, `bd`, etc.)
