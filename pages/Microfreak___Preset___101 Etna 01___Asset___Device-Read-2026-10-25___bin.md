logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Etna 01 slot 101 capture
	- [Download the slot 101 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___101%20Etna%2001___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 101 over USB on October 25, 2026 with `mise run microfreak:download --slot 101`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `69b6d07aa9285558c421848b3ab7d3e37dba9614d2e5e0ad6c57fb8c30ded59d`.
