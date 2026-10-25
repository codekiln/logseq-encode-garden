logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Canadian Bass slot 68 capture
	- [Download the slot 68 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___068%20Canadian%20Bass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 68 over USB on October 25, 2026 with `mise run microfreak:download --slot 68`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b68ab4f39418b3170791b6df3ee2197bed72a649c5aba19874465ffd681f0172`.
