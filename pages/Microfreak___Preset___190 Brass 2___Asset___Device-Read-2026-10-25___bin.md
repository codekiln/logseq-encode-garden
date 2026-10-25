logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Brass 2 slot 190 capture
	- [Download the slot 190 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___190%20Brass%202___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 190 over USB on October 25, 2026 with `mise run microfreak:download --slot 190`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `5097b842dd605a64a418ab6867e51af03446c905a383284ab51a207202e63fcd`.
