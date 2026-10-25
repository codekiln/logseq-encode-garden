logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Guisky slot 90 capture
	- [Download the slot 90 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___090%20Guisky___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 90 over USB on October 25, 2026 with `mise run microfreak:download --slot 90`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `7eea64c26ee31ee4d46dd1eb1496cf2d9b187ced1e19b40dfea5af93a04077e7`.
