logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Ridiance slot 356 capture
	- [Download the slot 356 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___356%20Ridiance___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 356 over USB on October 25, 2026 with `mise run microfreak:download --slot 356`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `846dfd47c90c101f49f92f8475423890be10ecb9c396acb8f654c778fdc4d4f3`.
