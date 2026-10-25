logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Hoss slot 42 capture
	- [Download the slot 42 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___042%20Hoss___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 42 over USB on October 25, 2026 with `mise run microfreak:download --slot 42`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `7a6794602f77c37dc23fce13663f7f15cd3971cf43d1e7680fc0bf86fa47da9e`.
