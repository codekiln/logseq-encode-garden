logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Mood slot 64 capture
	- [Download the slot 64 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___064%20Mood___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 64 over USB on October 25, 2026 with `mise run microfreak:download --slot 64`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `548bcb24066fa763168e57b4c7b22c21c8cc5f9ac5779024d67270ce5a9bd047`.
