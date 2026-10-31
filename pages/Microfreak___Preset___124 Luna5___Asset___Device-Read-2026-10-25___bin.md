logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Luna5 slot 124 capture
	- [Download the slot 124 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___124%20Luna5___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 124 over USB on October 25, 2026 with `mise run microfreak:download --slot 124`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `ae4ce1c12b428fb4be77c2f937b70e5224c0008a2db8966818de1c1d2b0015e2`.
