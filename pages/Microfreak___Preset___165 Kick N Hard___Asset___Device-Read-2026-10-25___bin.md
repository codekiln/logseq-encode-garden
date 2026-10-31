logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Kick N Hard slot 165 capture
	- [Download the slot 165 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___165%20Kick%20N%20Hard___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 165 over USB on October 25, 2026 with `mise run microfreak:download --slot 165`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `dd59860e132eb378eaa2db5ca357573fb3327f8755d21551d4532c65f45bda1e`.
