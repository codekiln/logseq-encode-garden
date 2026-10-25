logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Fmit slot 256 capture
	- [Download the slot 256 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___256%20Fmit___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 256 over USB on October 25, 2026 with `mise run microfreak:download --slot 256`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `3c985ffc5b3f28e288244d31a83afa2f4d0ef32ef9f99b1da3d91e8978deb252`.
