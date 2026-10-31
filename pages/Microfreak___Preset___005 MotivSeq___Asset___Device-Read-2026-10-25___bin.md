logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # MotivSeq slot 5 capture
	- [Download the slot 5 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___005%20MotivSeq___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 5 over USB on October 25, 2026 with `mise run microfreak:download --slot 5`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `dac9a9cf6946b22c516b3db5b18be1ad869f6c375b7fa7999d258ca66f980d04`.
