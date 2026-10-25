logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Chip Thunder slot 136 capture
	- [Download the slot 136 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___136%20Chip%20Thunder___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 136 over USB on October 25, 2026 with `mise run microfreak:download --slot 136`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `fec270a520652b9ac69203308d28d7d3cf5122dfd3b351d821146ea1072c1c99`.
