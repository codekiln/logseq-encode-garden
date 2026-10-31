logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Solitude slot 51 capture
	- [Download the slot 51 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___051%20Solitude___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 51 over USB on October 25, 2026 with `mise run microfreak:download --slot 51`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `088b4989bd34c0ad78a09fbc9139cd305ddf3399389480139130b79277273ee2`.
