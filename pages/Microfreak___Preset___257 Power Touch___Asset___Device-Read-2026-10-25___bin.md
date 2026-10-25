logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Power Touch slot 257 capture
	- [Download the slot 257 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___257%20Power%20Touch___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 257 over USB on October 25, 2026 with `mise run microfreak:download --slot 257`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `0fa7bfb384956024ed46b0153891ad7763d09ccb104fe7033599e5ccfd881dd1`.
