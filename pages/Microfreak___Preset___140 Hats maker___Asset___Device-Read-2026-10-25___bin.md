logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Hats maker slot 140 capture
	- [Download the slot 140 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___140%20Hats%20maker___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 140 over USB on October 25, 2026 with `mise run microfreak:download --slot 140`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `e5ef98181d77e266dd89065819f1baf6a8f9fddea5a0f224165ca2990c816ce8`.
