logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Notobeat slot 115 capture
	- [Download the slot 115 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___115%20Notobeat___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 115 over USB on October 25, 2026 with `mise run microfreak:download --slot 115`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `1cbf5f155d094c58b9120adc75065d6e4d61544fe9b53fd16c3090397d43b811`.
