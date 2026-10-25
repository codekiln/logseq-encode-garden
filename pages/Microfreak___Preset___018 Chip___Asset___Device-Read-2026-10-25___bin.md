logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Chip slot 18 capture
	- [Download the slot 18 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___018%20Chip___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 18 over USB on October 25, 2026 with `mise run microfreak:download --slot 18`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `85a7e4ac267a0777222962c34162b3c59ca62123b56056937dfba7f87df09220`.
