logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Munks slot 320 capture
	- [Download the slot 320 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___320%20Munks___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 320 over USB on October 25, 2026 with `mise run microfreak:download --slot 320`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `cc9e45d071526498b17357c57caffe9904595895b970c9cae98804c159afa81f`.
