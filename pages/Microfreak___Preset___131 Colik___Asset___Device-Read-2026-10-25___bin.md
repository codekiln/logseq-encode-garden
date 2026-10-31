logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Colik slot 131 capture
	- [Download the slot 131 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___131%20Colik___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 131 over USB on October 25, 2026 with `mise run microfreak:download --slot 131`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4bf67deb65d16df386a37577373fb6cc80d022ff340a8aad5f3f368be63da216`.
