logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Invitation slot 8 capture
	- [Download the slot 8 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___008%20Invitation___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 8 over USB on October 25, 2026 with `mise run microfreak:download --slot 8`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `6c3b8545d9de3dd1a22c493c65f44734e20f6b0fdd0123d81165f2c96694b87f`.
