logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Buzzsaw slot 72 capture
	- [Download the slot 72 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___072%20Buzzsaw___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 72 over USB on October 25, 2026 with `mise run microfreak:download --slot 72`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `3ff4078425e701ac095e3c479caf4e96bdb28c9a7a63a11193fe8ec2c5d069c7`.
