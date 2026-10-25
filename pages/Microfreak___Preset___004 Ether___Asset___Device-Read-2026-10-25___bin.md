logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Ether slot 4 capture
	- [Download the slot 4 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___004%20Ether___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 4 over USB on October 25, 2026 with `mise run microfreak:download --slot 4`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `b5c4c87698cc579bc6b25671c3585ddf4b674f48a35fdeee0c556da0ea5a59a0`.
