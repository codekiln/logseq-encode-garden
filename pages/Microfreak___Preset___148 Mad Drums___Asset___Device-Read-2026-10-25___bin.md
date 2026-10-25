logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Mad Drums slot 148 capture
	- [Download the slot 148 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___148%20Mad%20Drums___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 148 over USB on October 25, 2026 with `mise run microfreak:download --slot 148`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `63295f77a6107ea04eb1001c36ee9d7b9cc6e1dabd3a1757bff8b3a0907cf24e`.
