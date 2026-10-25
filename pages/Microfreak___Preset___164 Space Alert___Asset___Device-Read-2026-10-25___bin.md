logseq-entity:: [[Logseq/Entity/Asset/B2]]
- # Space Alert slot 164 capture
	- [Download the slot 164 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___164%20Space%20Alert___Asset___Device-Read-2026-10-25.bin)
	- Read from the connected MicroFreak's slot 164 over USB on October 25, 2026 with `mise run microfreak:download --slot 164`. The file is the preset header followed by the unmodified data packets the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). It is not a MIDI Control Center `.mbp` file. SHA-256: `ca1c840682e63e2a867e21de7a68cc9027cf57aeeab69b830288302f7295dfec`.
