logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # D-Funk slot 88 capture
	- [Download the slot 88 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___088%20D-Funk___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 88 over USB on October 25, 2026 with `mise run microfreak:download --slot 88`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `08cbd590edc62f8c0c680384cca90e97118ff9830303b2dccee8a881ac19b9bc`.
