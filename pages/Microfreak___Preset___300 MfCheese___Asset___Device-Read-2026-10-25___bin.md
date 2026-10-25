logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # MfCheese slot 300 capture
	- [Download the slot 300 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___300%20MfCheese___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 300 over USB on October 25, 2026 with `mise run microfreak:download --slot 300`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `6055cba6b4a5e73cfb2587321a3eacd889b1e98506f903a415d22a7f0eccdeb9`.
