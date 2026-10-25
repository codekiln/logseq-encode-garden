logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # WubbliDub slot 255 capture
	- [Download the slot 255 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___255%20WubbliDub___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 255 over USB on October 25, 2026 with `mise run microfreak:download --slot 255`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `302e65a713850fceae27fb8252ff5a17f0b180a50c91aa952c6148565b90cebe`.
