logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Dandi slot 276 capture
	- [Download the slot 276 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___276%20Dandi___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 276 over USB on October 25, 2026 with `mise run microfreak:download --slot 276`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `7f839b5c1a71ae1f5c88012f6c8107688bd37af5c9a6688388a492f842109379`.
