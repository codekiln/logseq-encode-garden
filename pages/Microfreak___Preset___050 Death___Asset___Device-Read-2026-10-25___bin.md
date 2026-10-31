logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Death slot 50 capture
	- [Download the slot 50 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___050%20Death___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 50 over USB on October 25, 2026 with `mise run microfreak:download --slot 50`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `617b8e5338bfc76dbdfa68348a01a55042881bf136279b07f0e248f60909d1d9`.
