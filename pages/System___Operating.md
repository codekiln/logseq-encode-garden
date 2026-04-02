logseq-entity:: [[Logseq/Entity/concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Operating System]], [[OS]]

- # Operating system
	- ## Overview
		- An **operating system** (OS) is the **primary system software** on a general-purpose computer: it **controls and shares hardware**, **isolates programs from one another**, and **offers stable services** so applications do not talk to the machine’s raw details on their own.
		- In practice the OS is the layer that turns a pile of circuits (CPU, RAM, disks, networks, keyboards, GPUs, …) into something you can **boot**, **log into**, and **run many programs on** without each program reimplementing drivers, memory rules, and scheduling.
	- ## Context
		- **Below** the OS sit **firmware** and **boot loaders** (e.g. UEFI) that start the machine; **above** it sit **libraries**, **runtimes**, and **applications** (browsers, editors, games) that request resources through OS **interfaces** rather than by poking hardware directly.
		- Consumer-facing names (Windows, macOS, Ubuntu, Android, iOS) usually denote a **whole product stack**—often a **kernel**, **drivers**, **system daemons**, **windowing or UI shell**, and bundled utilities—while “the OS” in a narrow technical sense often centers on the **kernel** plus the **system call** boundary.
		- Closely related ideas you may see in notes: **[[Nix]]** (a way to describe and build software artifacts and environments; often used *with* an OS rather than replacing the OS itself), **containers** and **virtual machines** (ways to package or virtualize workloads *on top of* an OS).
	- ## Key principles
		- **Abstraction** — Presents files, sockets, processes, and permissions instead of raw disk sectors or CPU modes.
		- **Multiplexing** — Runs many processes **concurrently** (or with the illusion of concurrency) by **scheduling** CPU time and **virtualizing** memory.
		- **Protection** — Enforces **privilege levels** (kernel vs user space) so buggy or malicious user code cannot freely read every other program’s memory or reprogram devices.
		- **Persistence and naming** — Organizes durable data via **file systems** and mount points; mediates **I/O** to disks and networks.
		- **Extensibility via drivers** — Device-specific logic lives in **drivers** loaded into the kernel or attached as services so the same syscall API can support new hardware over time.
	- ## Mechanism
		- Programs ask the OS for work through **system calls** (open a file, allocate memory, spawn a process, send network packets). The **kernel** validates requests, updates kernel data structures, and performs privileged operations.
		- The scheduler decides **which runnable thread** gets CPU time and for how long; the **virtual memory** subsystem maps each process to its own address space using the MMU, backed by RAM and swap or paging files.
		- Interrupts and **DMA** let devices signal the CPU asynchronously; the OS handles interrupts in kernel mode and may wake blocked processes when I/O completes.
	- ## Examples
		- **Desktop and server**: Windows, **macOS**, GNU/Linux distributions, **BSD** family systems—different kernels and ecosystems, same broad role.
		- **Mobile and embedded**: iOS, Android (Linux kernel + userspace stack), RTOS-class systems on small devices where **real-time** or **minimal footprint** constraints dominate.
	- ## Misconceptions
		- “The OS is just the **desktop** or **window manager**” — **Too narrow**; the GUI is often one component among many. You can run a machine with no graphical shell and still have a full OS.
		- “**Linux** is an OS” — **Often shorthand**: Linux usually names the **kernel**; what people install is a **distribution** that bundles the kernel with userland tools, init, libraries, and often a desktop.
		- “Apps run **on** the hardware directly for speed” — **Mostly false** on protected systems: even performance-critical code still goes through the OS for allocation, I/O, and GPU APIs unless you are in firmware or bare-metal contexts.
