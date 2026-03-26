tags:: [[Programming]], [[Diataxis/Explanation]]
alias:: [[CoW]]
see-also:: [[Programming/Concept/Heap]], [[Programming/Concept/Stack]]
- # Copy on Write Conceptual Overview
	- ## Overview
		- **Copy-on-write** (often abbreviated **CoW**) is an optimization and correctness pattern: multiple readers (or a parent and child) **share** a single physical copy of data until someone tries to **modify** it; only then is a **private duplicate** created so the update does not disturb other observers.
		- It is used across **operating systems** (shared memory, `fork`, memory-mapped files), **filesystems and databases** (snapshots, deduplicated blocks), and **data structures in application code** (persistent collections, cheap "copies" of large buffers).
	- ## Context
		- **Problem**: Eager duplication of large or many objects is expensive in time and space; some workflows (cloning a process, branching a snapshot, returning a "copy" from an API) appear to need a full duplicate even when most copies are never written.
		- **Idea**: Treat **read-mostly sharing** as the fast path. Pay the cost of a real copy **only when a write happens** (and only for the parts that are actually written, when the design allows partial sharing).
		- **Why it matters**: CoW is a bridge between **logical independence** ("each side has its own view") and **physical efficiency** (one set of pages or blocks on disk until divergence).
	- ## Key Principles
		- **Sharing first**: Start with a single underlying representation and multiple handles, references, or virtual mappings that refer to it.
		- **Lazy duplication**: On **write**, if the target is still shared, allocate new storage, copy the minimal necessary region, then apply the write to the private copy.
		- **Reference tracking**: Implementations use **reference counts**, **generation tags**, or **kernel page tables** to know when a write must split a shared resource.
		- **Not the same as "lazy" in general**: CoW is specifically **defer copying until a write**; other lazy strategies may defer computation or I/O for different reasons.
	- ## Mechanism
		- **OS virtual memory (illustrative)**: After `fork()`, parent and child often map the same physical pages read-only. The first write to such a page triggers a **page fault**; the kernel copies the page, remaps the writer's address space to the new physical page, and retries the write—classic **CoW at page granularity**.
		- **Filesystems / volumes**: Snapshots may reference the same extents as the live dataset; when a block is rewritten, the filesystem allocates a new block for the write (or for the branch that diverged) so older snapshots stay intact.
		- **In-process structures**: A string or array type might keep a **shared buffer** with a refcount; `mutate` or COW `clone` either increments the count (cheap) or duplicates the buffer on first exclusive write.
		- **Persistent / functional data structures**: New versions of a tree might **reuse** unmodified subtrees and only allocate new nodes along the path from root to the changed leaf (structural sharing); updating often behaves like CoW at the node level.
	- ## Examples
		- **Unix `fork`**: Child appears to duplicate the address space; many systems implement that logical copy with CoW pages until one process modifies memory.
		- **ZFS-style snapshots**: Historical snapshot data remains stable while the live dataset moves forward; diverging writes consume new space instead of rewriting history in place.
		- **Swift arrays / some C++ `std::string` histories / Rust `Arc` patterns**: Library types combine **shared ownership** with rules that duplicate underlying storage when uniqueness is required for mutation (exact APIs vary by language).
		- ### Pseudocode: logical CoW buffer (illustrative)
			- ~~~
			  // After "copy", both refer to shared storage until either writes.
			  cow_copy(src):
			      return Handle(shared=src.shared, refcount++)
			  write(handle, index, value):
			      if handle.refcount > 1:
			          handle.storage = duplicate(handle.shared)
			          handle.refcount = 1   // now unique
			      handle.storage[index] = value
			  ~~~
	- ## Misconceptions
		- **CoW eliminates the cost of copying** → **False** for writers. It avoids upfront duplication; writers still pay (latency, space) when the copy finally happens, sometimes at an **unpredictable** moment (e.g. page fault).
		- **CoW is always faster** → **Context-dependent**. Reference counting, fault handling, and fragmentation can add overhead; read-heavy workloads benefit most.
		- **CoW means "no copies exist"** → **False**. After writes, **multiple versions** of data coexist; memory or disk use can grow with how much diverges.
		- **CoW by itself fixes races** → **False**. You still need proper **synchronization**; CoW affects **when** storage diverges, not atomicity of higher-level operations.
