logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Paralex slot 155 capture
	- [Download the slot 155 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___155%20Paralex___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 155 over USB on October 25, 2026 with `mise run microfreak:download --slot 155`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `793beca4ddde1283ff351a34bdab3b09725ac963ef1b2a4faa3b93892a6f7437`.
