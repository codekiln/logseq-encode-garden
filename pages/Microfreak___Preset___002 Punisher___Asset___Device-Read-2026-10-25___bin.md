logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Punisher slot 2 capture
	- [Download the slot 2 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___002%20Punisher___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 2 over USB on October 25, 2026 with `mise run microfreak:download --slot 2`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `77b8b2dc4e0e0996d5461ec1f9acb1759a955c5fdd70fb9256c3ba3dc995154d`.
