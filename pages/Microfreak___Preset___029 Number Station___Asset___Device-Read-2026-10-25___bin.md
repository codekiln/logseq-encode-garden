logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Number Station slot 29 capture
	- [Download the slot 29 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___029%20Number%20Station___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 29 over USB on October 25, 2026 with `mise run microfreak:download --slot 29`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b2f53f47027c077151d3be14f137b4db3a687dc2aaad09ca206e0c5376527e9c`.
