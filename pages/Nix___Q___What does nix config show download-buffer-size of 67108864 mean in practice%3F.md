logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
- # What does `nix config show download-buffer-size` reporting `67108864` mean in practice?
	- ## Answer
		- [[AI/Response]]
			- The number is **bytes**: `67108864` = **64 MiB** (64 × 2^20). That matches the **current default** for the Nix setting `download-buffer-size` documented in the Nix reference manual.
			- **Practical meaning:** Nix keeps an **in-memory buffer** between the `curl` side of a download and whatever **consumes** the bytes next (for example unpacking a tarball or writing store objects). The setting is the **maximum size** of that buffer—not a disk quota, not a “download cap,” and not the size of the thing you are fetching.
			- **When it matters:** If the network delivers data **faster** than the consumer processes it, the buffer fills. Nix then **backpressures** the download (you may see warnings like “download buffer is full”). A larger buffer gives more **slack** so fast downloads can stay ahead of slow consumers; a smaller one tends to produce that warning more often on very fast links or large paths, even though work usually continues.
			- **Sources**
				- [Nix manual — `download-buffer-size`](https://nix.dev/manual/nix/stable/command-ref/conf-file.html#conf-download-buffer-size)
				- [NixOS/nix PR #11171 — add setting and default buffer behavior](https://github.com/NixOS/nix/pull/11171)
