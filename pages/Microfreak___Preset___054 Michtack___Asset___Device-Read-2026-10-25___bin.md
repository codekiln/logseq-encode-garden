logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Michtack slot 54 capture
	- [Download the slot 54 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___054%20Michtack___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 54 over USB on October 25, 2026 with `mise run microfreak:download --slot 54`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `7a5a2d979e0be2c6c35f9fd4d02a7922cda626df9bc5b1044a886f8a5045aa2c`.
