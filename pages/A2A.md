logseq-entity:: [[Logseq/Entity/Standard]]
see-also:: [[Agent Communication Protocol]]

- # [A2A](https://a2a-protocol.org/)
	- ## Overview
		- **Agent2Agent (A2A)** is an open protocol for communication and interoperability between opaque agentic applications: agents built on different frameworks, by different vendors, on separate servers, collaborate *as agents* without exposing their internal state, memory, or tools.
		- Created by [[Google]] and contributed as an open source project under the Linux Foundation; Apache 2.0 licensed. In August 2026 it was accepted as a Growth Stage project of the Linux Foundation-directed Agentic AI Foundation (AAIF), alongside [[MCP]], goose, and AGENTS.md. ([announcement](https://github.com/a2aproject/A2A/blob/main/docs/blog/posts/a2a-joins-aaif.md))
	- ## Normative links
		- [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/) — latest released spec version `1.0.0`; earlier versions `0.3.0`, `0.2.6`, `0.1.0`
		- [a2aproject/A2A](https://github.com/a2aproject/A2A) — spec repo; latest release [v1.0.1](https://github.com/a2aproject/A2A/releases/tag/v1.0.1) (2026-05-28), v1.0.0 released 2026-03-12
	- ## Scope
		- **Agent Card** — JSON metadata an A2A server publishes describing identity, capabilities, skills, service endpoint, and auth requirements; discovered at `/.well-known/agent-card.json`, via registries, or by direct configuration.
		- **Task** — the stateful unit of work with a defined lifecycle; **Message** — a turn with role `user` or `agent` made of **Parts** (text, file references, structured data); **Artifact** — a task output made of Parts.
		- Interaction modes: synchronous request/response, streaming over Server-Sent Events, and asynchronous push notifications to a client webhook for long-running tasks.
		- The spec is layered: a canonical data model (Protocol Buffer messages), abstract operations (send message, send streaming message, get / list / cancel task, get Agent Card), and protocol bindings for JSON-RPC 2.0, gRPC, and HTTP+JSON/REST, plus custom bindings.
	- ## Relationship to MCP
		- [[MCP]] connects an agent to tools and resources (vertical: deepens one agent); A2A connects agents to other agents across team or organization boundaries (horizontal). The two are designed as complements. ([A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/))
	- ## Implementations
		- Official SDKs for Python (`a2a-sdk`), Go, JavaScript, Java, .NET, and Rust, linked from the spec repo README.
		- [[LangSmith]] Agent Server exposes each assistant at `/a2a/{assistant_id}` (methods `message/send`, `message/stream`, `tasks/get`) and serves its Agent Card at `/.well-known/agent-card.json?assistant_id={assistant_id}`. ([A2A endpoint in Agent Server](https://docs.langchain.com/langsmith/server-a2a))
		- A LangSmith Deployment of a [[LangSmith/Deep Agents]] agent can expose it via MCP or A2A. ([Going to production](https://docs.langchain.com/oss/python/deepagents/going-to-production))
