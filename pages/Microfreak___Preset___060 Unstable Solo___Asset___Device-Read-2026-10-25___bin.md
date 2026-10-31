logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Unstable Solo slot 60 capture
	- [Download the slot 60 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___060%20Unstable%20Solo___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 60 over USB on October 25, 2026 with `mise run microfreak:download --slot 60`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `cd210939f110ea128e4a8f933066c8f3d0dfd8c3c8672c85681735250385c5c1`.
