logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[AI Agent Harness]], [[AI Agent Harnesses]]
see-also:: [[AI/Agent]], [[AI/Agent/Framework]], [[AI/Agent/Skill]], [[GitHub/CoPilot/CLI]]

- # AI agent harness
	- ## Overview
		- An **agent harness** is the surrounding software that turns a raw [[AI/LLM]] into a working [[AI/Agent]]: the loop that sends prompts, parses responses, invokes tools, feeds results back, and decides when to stop.
		- The model supplies reasoning; the harness supplies **structure**—context assembly, tool-calling protocol, memory/state across turns, permissions, and the interface a human or system uses to drive the agent.
		- It matters because two agents built on the same underlying model can behave very differently depending on harness design: how it manages context, what tools it exposes, and how it recovers from errors.
	- ## Context
		- Harnesses range from thin (a single system prompt plus a tool-call loop) to elaborate (multi-agent orchestration, planning layers, sandboxed execution, persistent memory).
		- Coding-agent products—CLIs, IDE extensions, and hosted agents—are largely harness engineering: the same frontier models sit underneath, and much of the competitive difference is in the harness.
		- Related but distinct terms: an **[[AI/Agent/Framework]]** is a library for building harnesses (LangGraph, AutoGen, etc.); a **harness** is the resulting runtime that actually drives an agent's loop, whether built on a framework or from scratch.
	- ## Key Principles
		- **Context assembly** — deciding what history, files, and instructions get placed in the model's context window on each turn.
		- **Tool-calling protocol** — the schema and loop for letting the model request actions (shell, search, file edits) and receive results.
		- **State and memory** — how the harness persists progress, todos, or facts across turns or sessions, since the model itself is stateless between calls.
		- **Permissions and safety** — sandboxing, approval prompts, and scoping of what tools can do without human confirmation.
		- **Stopping conditions** — how the harness decides a task is done, needs user input, or should hand off to another agent.
	- ## Mechanism
		- On each turn, the harness builds a prompt from the running context, sends it to the model, and receives either a final answer or one or more tool calls.
		- Tool calls are executed by the harness (not the model), and their results are appended to the context for the next turn—this loop repeats until the harness decides to stop.
		- Around this core loop, most harnesses add scaffolding: system instructions, retrieved documentation, sub-agent delegation, and UI for streaming output to the user.
	- ## Examples
		- Terminal coding agents such as [[GitHub/CoPilot/CLI]] and [[Claude/Code]] are harnesses wrapped around frontier models, exposing shell, file-edit, and search tools.
		- IDE-integrated agents (e.g. [[CursorAI/Agent]]) ship harness improvements—like an "Agent Harness" upgrade—independently of switching the underlying model, since harness quality affects reliability as much as model choice.
		- Multi-agent setups, where a primary agent's harness can spawn and coordinate sub-agents, are an extension of the same pattern to multiple concurrent loops.
	- ## Misconceptions
		- A better model does not make the harness irrelevant—model progress and harness quality are separate levers, and weak harnesses bottleneck strong models.
		- A harness is not the same as a framework: a framework is a toolkit for building harnesses; the harness is the specific, running agent loop assembled (possibly using a framework).
