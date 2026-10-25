logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # PowerStab slot 56 capture
	- [Download the slot 56 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___056%20PowerStab___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 56 over USB on October 25, 2026 with `mise run microfreak:download --slot 56`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `4e6b6146a2f20cd133ed7317778e92bcb6fe2c81f84400a0a21b24b189940d2a`.
