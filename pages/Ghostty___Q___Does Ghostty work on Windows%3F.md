logseq-entity:: [[Logseq/Entity/Question]]
- # Does [[Ghostty]] work on Windows?
	- ## [[AI Answer]]
		- **Short answer:** No official native Windows build as of mid-2026 — [[Ghostty]] officially targets macOS and Linux only — but community ports exist and official groundwork is underway.
		- **Official status:** The core `libghostty` library already supports Windows as a build target, and that work is what the small Ghostty team is currently building toward, but there is no official native Windows application release yet.
		- **Community alternatives (unofficial, third-party):**
			- [Winghostty](https://winghostty.com/) — native Windows terminal built on Ghostty's terminal core, with tabs, splits, session restoration, and signed x64/ARM64 releases
			- [ghostty-windows](https://github.com/InsipidPoint/ghostty-windows) — community port using Win32 API, OpenGL rendering, and ConPTY, with no WSL required
		- **Sources:** [Windows support q&a (Discussion #12290)](https://github.com/ghostty-org/ghostty/discussions/12290); [Windows Support (Discussion #2563)](https://github.com/ghostty-org/ghostty/discussions/2563)
