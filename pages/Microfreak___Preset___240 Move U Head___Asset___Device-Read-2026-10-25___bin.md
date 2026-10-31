logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Move U Head slot 240 capture
	- [Download the slot 240 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___240%20Move%20U%20Head___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 240 over USB on October 25, 2026 with `mise run microfreak:download --slot 240`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `202f01c043257c438c7c3ab917019772366f92bf4bf8061de966a41f0a63d92d`.
