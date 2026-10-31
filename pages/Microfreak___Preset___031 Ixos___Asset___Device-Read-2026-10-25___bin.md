logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Ixos slot 31 capture
	- [Download the slot 31 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___031%20Ixos___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 31 over USB on October 25, 2026 with `mise run microfreak:download --slot 31`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `d90ab86eddeea7ad611f8e6401ea942d5d320abe9352c94d2eca4227f5b9f09b`.
