logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Night Organ slot 195 capture
	- [Download the slot 195 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___195%20Night%20Organ___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 195 over USB on October 25, 2026 with `mise run microfreak:download --slot 195`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `a9e309a9113a9dc6682cc01d9cc690464fa58133d4496199a664516e53aa4c9f`.
