tags:: [[Question]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Bevy]], [[Game/Video/Engine]], [[Rust]]

- # What are the main [[Game/Video/Engine]]s for [[Rust]]?
	- ## Answer
		- [[My Notes]]
			- [Game Engines | Are we game yet.rs?](https://arewegameyet.rs/ecosystem/engines/)
				-
		- [[AI/Response]]
			- **Short answer:** The main native [[Rust]] options today are [[Bevy]] (largest ecosystem), Fyrox (editor + 3D), Macroquad (minimal 2D), and ggez (comfortable 2D). None is a full Unity/Unreal analogue; pick by dimension (2D vs 3D), tooling (code-only vs editor), and tolerance for API churn.
			- [[Bevy]] — data-driven ECS engine for 2D and 3D; largest community, plugin ecosystem, and learning resources; still pre-1.0 with frequent breaking releases (~every 3 months). [bevyengine/bevy on GitHub](https://github.com/bevyengine/bevy) · [bevy.org](https://bevy.org)
			- **Fyrox** (formerly rg3d) — feature-rich 2D/3D engine with a built-in scene editor; closest to a traditional engine-with-tooling stack in pure Rust. [FyroxEngine/Fyrox on GitHub](https://github.com/FyroxEngine/Fyrox)
			- **Macroquad** — small cross-platform 2D-first framework (raylib-inspired); low friction for prototypes and game jams. [not-fl3/macroquad on GitHub](https://github.com/not-fl3/macroquad)
			- **ggez** — mature lightweight 2D framework with comfortable defaults; smaller scope than Bevy, less architectural ceremony than ECS. [ggez/ggez on GitHub](https://github.com/ggez-rs/ggez)
			- **Also on the radar:** Comfy (minimal, macroquad/ggez-like ergonomics), Piston (older modular ecosystem), Amethyst (archived — historical reference only). Hybrid path: run Rust gameplay against Godot via [godot-rust/gdext](https://github.com/godot-rust/gdext) bindings rather than a Rust-native renderer.
			- **How to choose (rule of thumb):** ambitious multi-system 2D/3D game → Bevy; need a visual editor for 3D → Fyrox; quick 2D prototype → Macroquad; stable simple 2D → ggez; already committed to Godot → Godot + Rust bindings.
			- [5 Rust game engines to consider for your next project (LogRocket)](https://blog.logrocket.com/5-rust-game-engines-consider-next-project/)