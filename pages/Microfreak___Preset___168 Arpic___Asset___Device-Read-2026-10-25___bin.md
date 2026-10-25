logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Arpic slot 168 capture
	- [Download the slot 168 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___168%20Arpic___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 168 over USB on October 25, 2026 with `mise run microfreak:download --slot 168`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `19a48aa478c76e2ea613d184e70f6f19ad0d86699893d74094290abb2a96f91d`.
