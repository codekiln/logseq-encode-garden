logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Stillbass slot 234 capture
	- [Download the slot 234 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___234%20Stillbass___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 234 over USB on October 25, 2026 with `mise run microfreak:download --slot 234`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `13a60d90fdd3a2c79997378027e5a21e2ff3524a37aefbdee82c7ca0018b6e1e`.
