logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # No Sleep slot 135 capture
	- [Download the slot 135 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___135%20No%20Sleep___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 135 over USB on October 25, 2026 with `mise run microfreak:download --slot 135`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `05b4a0f3b56f3c729ec253cdb679dc2dd4cbda1e249a07cfb7c3418fe5cf0ac7`.
