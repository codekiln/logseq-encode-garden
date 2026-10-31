logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Poisoned 0scs slot 291 capture
	- [Download the slot 291 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___291%20Poisoned%200scs___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 291 over USB on October 25, 2026 with `mise run microfreak:download --slot 291`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `bbc91862cd9c10fcfe0e2640d6a03e34af9ea02ba4f53ad889604edb67f2df1a`.
