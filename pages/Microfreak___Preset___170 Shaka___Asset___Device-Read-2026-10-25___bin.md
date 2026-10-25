logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Shaka slot 170 capture
	- [Download the slot 170 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___170%20Shaka___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 170 over USB on October 25, 2026 with `mise run microfreak:download --slot 170`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `89a87d0f7a41b1ed4e2c2e101969b47f4ce15698c7ceecafb9d7614dbfe0c624`.
