logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[LangChain]]

- # [LangSmith Sandboxes](https://docs.langchain.com/langsmith/sandboxes)
	- Managed, isolated environments in [[LangSmith]] where agents run arbitrary code and work with a filesystem without touching the infrastructure the agent is deployed on.
	- Generally available in the GCP US, EU and APAC regions and in AWS US.
	- Used from the `langsmith[sandbox]` Python SDK or the `langsmith` TypeScript SDK (`SandboxClient`), or from the [Sandbox CLI](https://docs.langchain.com/langsmith/sandbox-cli).
	- [[LangSmith/Deep Agents]] can use a sandbox as its backend, which adds the `execute` tool alongside the filesystem tools ([Sandboxes as agent backends](https://docs.langchain.com/oss/python/deepagents/sandboxes)). The same backend interface also accepts third-party providers such as Daytona, E2B, Modal, Runloop and Vercel.
	- ## Features
		- [Auth proxy](https://docs.langchain.com/langsmith/sandbox-auth-proxy) — a proxy sidecar injects credentials from workspace secrets into matching outbound requests, so secrets never live in the sandbox
			- also controls egress: HTTP and HTTPS to any host by default, all other raw TCP blocked unless an allow list opens a host and port
		- [Snapshots](https://docs.langchain.com/langsmith/sandbox-snapshots) — reusable filesystem images, built from a Docker image or captured from a running sandbox, used to boot new sandboxes
		- [Mounts](https://docs.langchain.com/langsmith/sandbox-mounts) — attach S3 buckets, GCS buckets and public Git repositories to the sandbox filesystem
		- [Service URLs](https://docs.langchain.com/langsmith/sandbox-service-urls) — authenticated URLs to HTTP services running inside a sandbox
		- [Permissions](https://docs.langchain.com/langsmith/sandbox-permissions) — which workspace members can interact with a sandbox after it is created
