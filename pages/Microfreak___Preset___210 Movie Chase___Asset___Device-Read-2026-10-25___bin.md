logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Movie Chase slot 210 capture
	- [Download the slot 210 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___210%20Movie%20Chase___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 210 over USB on October 25, 2026 with `mise run microfreak:download --slot 210`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `1f73ca7f4491fa9ef2241fbb14e6f45846794727f2325b259620133ee03755de`.
