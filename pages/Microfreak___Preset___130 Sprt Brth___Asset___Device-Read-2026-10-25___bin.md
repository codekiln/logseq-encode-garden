logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Sprt Brth slot 130 capture
	- [Download the slot 130 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___130%20Sprt%20Brth___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 130 over USB on October 25, 2026 with `mise run microfreak:download --slot 130`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `bc2653331cc2c567f41c54999dce4956ec48452155bd5921dbd33a1c1a364f92`.
