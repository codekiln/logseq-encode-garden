source:: https://nextkicklabs.substack.com/p/the-threat-model-for-agentic-ai-what
date-created:: [[2026/02/19]]
created-by:: [[Person/Fernando Lucktermberg]]
provider:: [[AI Maker]]
platform:: [[Substack]]
intake-status:: full
- # [The threat landscape for Agentic AI - What can actually go wrong](https://nextkicklabs.substack.com/p/the-threat-model-for-agentic-ai-what)
	- ## Intake
		- Captured from Readwise shared link and validated against the original Substack post.
		- Published: 2026-01-13.
	- ## TL;DR
		- The article maps the attack surface of Agentic AI systems and argues that risk compounds when LLMs move from "answering" to "acting."
		- It frames threats as a full-chain problem: adversarial inputs, poisoned tools, model-specific exploits, and weak authorization/observability.
		- The main recommendation is defense in depth: isolate execution, gate tool actions with least privilege, constrain prompts and outputs, and continuously monitor.
	- ## Core Thesis
		- The security model for agents must shift from prompt quality to system architecture.
		- Agent workflows create transitive trust chains across prompts, memory, tools, APIs, and runtime infrastructure.
		- Failures are often compositional: multiple small weaknesses combine into high-impact compromise.
	- ## Threat Model By Layer
		- 1. Input and Prompt Layer
			- Prompt injection can override task goals, exfiltrate secrets, or trigger unauthorized tool use.
			- Indirect injection through untrusted artifacts (docs, web pages, issue text, emails) is a key risk for autonomous loops.
			- Training-time or retrieval-time data poisoning can steer behavior toward attacker objectives.
		- 2. Tool and Integration Layer
			- Tool over-permissioning turns minor prompt mistakes into major action risks.
			- Malicious or compromised MCP servers and plugins can become privilege-escalation pivots.
			- Function-call argument tampering and weak validation can produce unsafe side effects.
		- 3. Model and Runtime Layer
			- Jailbreak and policy bypass patterns can unlock restricted actions in production contexts.
			- Runtime compromise risks include insecure containerization, poor network segmentation, and shared-secret exposure.
			- Memory leakage and context poisoning can persist attacker influence across sessions.
		- 4. Governance and Human Layer
			- Lack of strong approval gates for high-risk actions increases blast radius.
			- Weak auditability makes incident response and attribution difficult.
			- Teams often over-trust "assistant behavior" without explicit control-plane constraints.
	- ## Representative Attack Paths
		- Prompt injection in ingested content causes the agent to call privileged tools and leak secrets.
		- Poisoned knowledge sources alter retrieval context, nudging an agent toward unsafe decisions.
		- Compromised integration endpoints execute malicious actions under the agent's valid credentials.
		- Inadequate sandboxing enables lateral movement from agent runtime to broader infrastructure.
	- ## Defensive Controls Emphasized
		- Enforce least privilege per tool, per action, and per execution context.
		- Use explicit allowlists for tool invocation and strict schema validation for arguments/outputs.
		- Isolate agent runtimes with hardened containers/VMs and restrictive egress controls.
		- Add human approval checkpoints for destructive, sensitive, or high-cost operations.
		- Maintain high-fidelity logging/telemetry for prompts, tool calls, and state transitions.
		- Continuously red-team with agent-specific adversarial scenarios.
	- ## Practical Implementation Notes
		- Treat agents as semi-trusted orchestration components, not trusted principals.
		- Model "what can this workflow do if hijacked?" before shipping.
		- Security reviews should cover end-to-end chains, not isolated prompt snippets.
	- ## Why This Matters
		- Agentic systems collapse planning and execution into one loop, so weak guardrails can create fast, scalable failure modes.
		- The article positions agent security as an architectural and operational discipline, not a prompt-writing exercise.
	- ## Related
		- [[OpenClaw]]
		- [[AI/Security/Attack/Agentic/Tool Chain/Poisoning]]
		- [[MCP/Server/Attack/Root Problem]]
		- [[AI Fluency]]
