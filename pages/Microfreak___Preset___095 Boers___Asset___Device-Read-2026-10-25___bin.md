logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Boers slot 95 capture
	- [Download the slot 95 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___095%20Boers___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 95 over USB on October 25, 2026 with `mise run microfreak:download --slot 95`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `617aeb51f6f306b0526aa3c0c1d8b4ec9dce78ebb4d7c469189c4c61f38de480`.
