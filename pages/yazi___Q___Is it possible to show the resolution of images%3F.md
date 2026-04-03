logseq-entity:: [[Logseq/Entity/question]]
via:: [[2026-04-02 Thu]]

- # Is it possible to show the resolution of images in [[yazi]]?
	- ## Answer
		- [[AI/Response]]
			- **Yes.** Pixel dimensions appear in the **spot** (file-information) UI, not in the main file list or the preview thumbnail alone.
			- **How:** Press **`spot`** on the hovered file (default **`Tab`** in the preset keymap). For `image/*` files, Yazi’s built-in **`image`** spotter reads metadata via `ya.image_info` and shows a **Size** row as **`WxH`** (width × height in pixels), plus **Format** and **Color** (color type / space). See the shipped [`image.lua` spotter](https://github.com/sxyazi/yazi/blob/shipped/yazi-plugin/preset/plugins/image.lua) (`M:spot_base`).
			- **Docs context:** Yazi’s terminology describes the **`spot`** layer as using spotters to show type-specific metadata, including **dimensions** (and color space) for images ([Terminology | Yazi](https://yazi-rs.github.io/docs/term/)). Default **`[plugin] spotters`** route `image/*` to the `image` spotter ([preset `yazi-default.toml`](https://github.com/sxyazi/yazi/blob/shipped/yazi-config/preset/yazi-default.toml)).
			- **Not the same as:** **`[mgr] linemode`** — built-in line modes are **`none`**, **`size`** (file byte size), **`mtime`**, **`btime`**, **`permissions`**, **`owner`**; there is no built-in linemode for image pixel dimensions ([yazi.toml | Yazi — mgr.linemode](https://yazi-rs.github.io/docs/configuration/yazi/#mgrlinemode)). **`[preview] max_width` / `max_height`** only cap preview rendering, not a labeled “resolution” readout ([Image preview sizing](https://yazi-rs.github.io/docs/image-preview/)).
			- **HEIC / AVIF / JXL / SVG:** those MIME types use the **`magick`** or **`svg`** spotters in the default table; if resolution is missing for a format, check Yazi version and optional **ImageMagick** support per [Installation | Yazi](https://yazi-rs.github.io/docs/installation/).
	- ## My Notes
		- *placeholder*
	- ## Related
		- [[yazi/Plugin/spotter]]
		- [[yazi/Q/How can I view file modification times?]] — **`spot`** and **`linemode`** contrast
