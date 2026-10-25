logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Square Bass slot 201 capture
	- [Download the slot 201 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___201%20Square%20Bass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 201 over USB on October 25, 2026 with `mise run microfreak:download --slot 201`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `bc03745408c4a1409751105674423ce3a99cc7769d4ff99eeb163b4b5d66a985`.
