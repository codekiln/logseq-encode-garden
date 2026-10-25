logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Kick A slot 142 capture
	- [Download the slot 142 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___142%20Kick%20A___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 142 over USB on October 25, 2026 with `mise run microfreak:download --slot 142`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `ba9b09efd1be4a10188a0a53933fcf28292422ad4926145c9f34c87ced8f2779`.
