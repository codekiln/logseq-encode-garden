created-by:: [[Person/Farid Zakaria]]
date-created:: [[2026/06/01]]
logseq-entity:: [[Logseq/Entity/Article]]

- # [Every Byte Matters](https://fzakaria.com/2026/06/01/every-byte-matters)
	- Author: **[[Person/Farid Zakaria]]** - Source: [fzakaria.com](https://fzakaria.com/)
	- ## Summary
		- Explores how CPU cache line size (64 bytes) and memory hierarchy fundamentally affect performance even within the same algorithmic complexity class (e.g., a plain `O(N)` loop).
		- Data layout choice—Array of Structs (AoS) vs Struct of Arrays (SoA)—can yield up to 30x throughput difference for large structs in sequential access patterns.
		- For random-access patterns (hash maps, pointer chasing, trees), total working set size determines which cache level data fits in, making struct byte size a direct performance dial.
	- ## Notes
		- Cache line is 64 bytes: reading one byte pulls all 64 surrounding bytes into cache; the CPU pre-fetcher exploits temporal and spatial locality for sequential access.
		- Cache hierarchy on author's machine: L1d ~35 KiB/core (~560 lines, ~1–2 ns), L2 ~2 MiB/core-pair (~4–5 ns), L3 12 MiB shared (~10–15 ns), DRAM ~60–100 ns.
		- AoS: each cache line loads one full struct; iterating over a single field wastes the rest of the line.
		- SoA: each cache line loads 64 values of the same field, maximizing useful payload per fetch.
		- Random access defeats the pre-fetcher entirely; the whole collection must fit in cache to avoid stalls.
		- Working set staircase: 512 Monsters at 64 B → 32 KiB, fits L1d at ~3 ns; at 128 B → 64 KiB, already spills to L2 at ~11 ns.
		- Practical rule: keep tight control over struct size when random access is common; shrinking a struct can jump an entire cache tier.
