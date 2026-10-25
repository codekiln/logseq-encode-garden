logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Arame slot 107 capture
	- [Download the slot 107 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___107%20Arame___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 107 over USB on October 25, 2026 with `mise run microfreak:download --slot 107`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `f146982e75bf91714527cebe9f2e3344594f6393ceaf0b06dd37efcab921be7c`.
