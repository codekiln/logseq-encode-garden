logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Sneaker slot 74 capture
	- [Download the slot 74 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___074%20Sneaker___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 74 over USB on October 25, 2026 with `mise run microfreak:download --slot 74`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `d71013dba20afa4bb94150d2f6d481ec483dcbd41aa68912d59b616757e90c2e`.
