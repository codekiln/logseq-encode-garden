logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Low Battery slot 306 capture
	- [Download the slot 306 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___306%20Low%20Battery___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 306 over USB on October 25, 2026 with `mise run microfreak:download --slot 306`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `533263179fa2f3ce89961e7f66050d9eef9bf10a1c7f12b9f4d8c04fd0483ccb`.
