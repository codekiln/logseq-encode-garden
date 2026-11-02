date-created:: [[2026-01-05]]
created-by:: [[Person/Luis Cardoso]]
see-also:: [[Docker/Sandboxes]], [[Infralovers/Blog/26/02/Sandboxing Claude Code on macOS: What I Actually Found]]

- # [A field guide to sandboxes for AI](https://www.luiscardoso.dev/blog/sandboxes-for-ai)
	- Ben Eisenbraun (HMS) shared it at the Harvard Software Development CoP AI-Assisted Coding tiger team meeting on [[2026-11-02]], after Artie Barrett's talk on [[Docker/Sandboxes]].
	- A long explainer on what "sandbox" means when an AI agent runs code. Once an agent can run a program, it can also leak secrets, send private code somewhere, move into internal networks or burn compute, even if it never escapes.
- ## The four things people call a sandbox
	- **Container:** shares the host kernel. A bug in a kernel path the code can reach can affect the host.
	- **MicroVM:** runs its own guest kernel behind hardware virtualization. The host deals with the VM, not with the workload's Linux syscalls.
	- **gVisor:** a userspace kernel (the Sentry) answers the workload's syscalls before they reach the host kernel.
	- **WebAssembly / V8 isolates:** no syscall interface at all. The code can only call the host operations the embedder exposes.
- ## Three questions to ask of any sandbox
	- **Boundary:** what is shared between this code and the host?
	- **Policy:** what can the code touch: files, network, devices, syscalls, quotas?
	- **Lifecycle:** what survives between runs? A fresh run each time, a long-lived workspace, or snapshot/restore?
	- A tight policy inside a weak boundary is still a weak sandbox.
- ## Why containers fall short for untrusted code
	- Many escapes are self-inflicted: `--privileged`, a mounted Docker socket, writable `/sys`, broad capabilities such as `CAP_SYS_ADMIN`, or joining the host's namespaces.
	- Even a well-configured container still shares the kernel. Dirty COW, Dirty Pipe and the runC overwrite bug are past examples.
	- Many agent sandbox failures are policy leaks, not kernel escapes. An agent that can read the repo and reach the network can leak the repo. One that can read `~/.aws` can leak credentials.
	- Seccomp, AppArmor/SELinux, dropped capabilities and rootless containers tighten policy. None of them changes the boundary.
- ## Choosing a sandbox
	- Work through four questions: threat model, compatibility, lifecycle, and what you can operate.
	- His defaults:
		- MicroVMs (Firecracker or cloud-hypervisor) for multi-tenant agents, or for any code you don't fully trust that needs a shell and package managers.
		- gVisor when its compatibility limits are acceptable.
		- Hardened containers for trusted internal automation.
		- Wasm or isolates for tools that only need a few specific operations.
	- Single-tenant doesn't mean trusted. Classify code by what an adversary can influence, which includes prompt injection and compromised dependencies.
	- The minimum policy before he would call it a sandbox:
		- Outbound network denied by default, with an allowlist or a policy proxy.
		- No long-lived credentials. Use short-lived, scoped tokens.
		- File access limited to the workspace.
		- Limits on CPU, memory, disk, time and process count.
		- Logs of the process tree and network traffic.
	- An appendix covers the local OS sandboxes: macOS Seatbelt, Linux Landlock with seccomp, and Windows AppContainer.
