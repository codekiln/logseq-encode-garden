logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # PWM vox slot 316 capture
	- [Download the slot 316 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___316%20PWM%20vox___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 316 over USB on October 25, 2026 with `mise run microfreak:download --slot 316`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `cfe8cb726ad42fb6dfb7e769bfa61922bf6535d38b7d1976719e5a6589b98cba`.
