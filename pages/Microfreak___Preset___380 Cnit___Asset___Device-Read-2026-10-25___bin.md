logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Cnit slot 380 capture
	- [Download the slot 380 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___380%20Cnit___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 380 over USB on October 25, 2026 with `mise run microfreak:download --slot 380`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `9ae23efaa3f74f933905261cf6ddb811f2cb7f8b05a8b7123fccf236413e1cc6`.
