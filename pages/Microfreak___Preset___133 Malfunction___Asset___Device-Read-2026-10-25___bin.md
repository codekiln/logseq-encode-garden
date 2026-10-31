logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Malfunction slot 133 capture
	- [Download the slot 133 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___133%20Malfunction___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 133 over USB on October 25, 2026 with `mise run microfreak:download --slot 133`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `e7c04bb80d8c0c297a6b31cb5838822b3c737416ba041837d6d0aaf93254a6f9`.
